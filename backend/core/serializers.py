from rest_framework import serializers, generics
from .models import *
from datetime import datetime
from django.db import transaction

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["gl_account"]


class PriceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceType
        fields = "__all__"

    def to_representation(self, instance):
        return str(instance)


class EditPriceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceType
        fields = ["name"]

    def to_internal_value(self, data):
        if isinstance(data, dict) and "name" in data:
            name = data["name"]
            try:
                # Retrieve the existing PriceType instance from the database based on the provided name
                return PriceType.objects.get(name=name)
            except PriceType.DoesNotExist:
                raise serializers.ValidationError(f"PriceType '{name}' does not exist.")
        return super().to_internal_value(data)

    def to_representation(self, instance):
        return str(instance)


class DiscountSerializer(serializers.ModelSerializer):
    price_type = serializers.CharField()

    class Meta:
        model = Discount
        fields = ["price_type", "discount", "description"]


# Because DiscountSerializer doesn't work with EditEventSerializer, declaring a new one


class EditDiscountSerializer(serializers.ModelSerializer):
    price_type = EditPriceTypeSerializer()

    class Meta:
        model = Discount
        fields = ["price_type", "discount", "description"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "location_name"]


class PriceLayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceLayer
        fields = "__all__"

    def to_representation(self, instance):
        return str(instance)


class AccountLayerSerializer(serializers.ModelSerializer):
    price_layer = PriceLayerSerializer()
    gl_account = AccountSerializer()

    class Meta:
        model = AccountLayer
        fields = ["gl_account", "price_layer"]


class EditAccountLayerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    price_layer = PriceLayerSerializer()
    account_data = AccountSerializer(source="gl_account")
    print("EditAccount here...")
    print(id)

    class Meta:
        model = AccountLayer
        fields = ["id", "account_data", "price_layer"]


class PriceLayerPriceSerializer(serializers.ModelSerializer):
    price_type = PriceTypeSerializer()
    price_layer = PriceLayerSerializer()

    class Meta:
        model = PriceLayerPrice
        fields = ["price_type", "price_layer", "price"]


class EditPriceLayerPriceSerializer(serializers.ModelSerializer):
    price_type = EditPriceTypeSerializer()
    price_layer = PriceLayerSerializer()

    class Meta:
        model = PriceLayerPrice
        fields = ["price_type", "price_layer", "price"]


class PriceSerializer(serializers.ModelSerializer):
    price_type = serializers.StringRelatedField()

    class Meta:
        model = Price
        fields = [
            "price_type",
            "price_1",
            "price_2",
            "price_3",
            "price_4",
            "price_5",
            "price_6",
        ]


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ["time_range", "capacity", "held"]


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ["id", "facility_name"]


class DateTimeSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(read_only=True)
    event_date = serializers.DateField()
    event_time = serializers.TimeField()
    event_end_time = serializers.TimeField()
    door_open = serializers.TimeField()
    door_close = serializers.TimeField()
    sell_date = serializers.DateTimeField()
    stop_date = serializers.DateTimeField()
    early_closure_time = serializers.TimeField()

    def to_representation(self, instance):
        # Convert datetime object to a string in the format 'YYYY-MM-DD'
        event_date = instance.event_date.strftime("%Y-%m-%d")
        event_time = instance.event_time.strftime("%H:%M")
        event_end_time = instance.event_end_time.strftime("%H:%M")
        door_open = instance.door_open.strftime("%H:%M")
        door_close = instance.door_close.strftime("%H:%M")
        sell_date = instance.sell_date.strftime("%Y-%m-%d %H:%M")
        stop_date = instance.stop_date.strftime("%Y-%m-%d %H:%M")
        early_closure_time = instance.early_closure_time.strftime("%H:%M")

        return {
            "event": instance.event.id,
            "event_date": event_date,
            "event_time": event_time,
            "event_end_time": event_end_time,
            "door_open": door_open,
            "door_close": door_close,
            "sell_date": sell_date,
            "stop_date": stop_date,
            "early_closure_time": early_closure_time,
        }

    class Meta:
        model = DateTime
        fields = [
            "event",
            "event_date",
            "event_time",
            "event_end_time",
            "door_open",
            "door_close",
            "sell_date",
            "stop_date",
            "early_closure_time",
        ]


class EventSerializer(serializers.ModelSerializer):
    timeslot_set = TimeSlotSerializer(many=True, read_only=True)
    date_time = DateTimeSerializer()
    price_layer_price = PriceLayerPriceSerializer(many=True, read_only=True)
    account = AccountLayerSerializer(many=True, read_only=True)
    discount = DiscountSerializer(many=True, read_only=True)
    prices = PriceSerializer(many=True)
    facility = FacilitySerializer()
    location = LocationSerializer()
    price_type = PriceTypeSerializer(many=True, read_only=True)
    price_layer = PriceLayerSerializer(many=True, read_only=True)

    class Meta:
        model = Event

        fields = [
            "id",
            "name",
            "description",
            "capacity",
            "held",
            "entrance",
            "gr_required",
            "early_closure",
            "csi_needed",
            "csi_mandatory",
            "csi_notes",
            "facility",
            "location",
            "date_time",
            "timeslot_set",
            "price_type",
            "price_layer",
            "price_layer_price",
            "status",
            "website_link",
            "websales_link",
            "discount",
            "additional_notes",
            "prices",
            "price_layer_price",
            "account",
        ]

    def create(self, validated_data):
        date_data = validated_data.pop("date_time")
        event = Event.objects.create(**validated_data)
        # The event must be created first since the foreign key lives on the DateTime model. We need an event to insert.
        DateTime.objects.create(event=event, **date_data)

        return event


class AddEventSerializer(serializers.ModelSerializer):
    facility = serializers.PrimaryKeyRelatedField(queryset=Facility.objects.all())
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())
    date_time = DateTimeSerializer()
    timeslot_set = TimeSlotSerializer(many=True, write_only=True)
    price_layer_price = serializers.ListSerializer(
        child=serializers.DictField(), write_only=True
    )
    account = AccountLayerSerializer(many=True)
    discount = DiscountSerializer(many=True)

    class Meta:
        model = Event
        fields = [
            "name",
            "description",
            "capacity",
            "held",
            "entrance",
            "gr_required",
            "early_closure",
            "csi_needed",
            "csi_mandatory",
            "csi_notes",
            "facility",
            "location",
            "date_time",
            "timeslot_set",
            "price_layer_price",
            "account",
            "discount",
        ]

    def create(self, validated_data):
        timeslot_data = validated_data.pop("timeslot_set")
        date_data = validated_data.pop("date_time")
        price_layer_price_data = validated_data.pop("price_layer_price")
        account_layer_data = validated_data.pop("account")
        discount_data = validated_data.pop(
            "discount", []
        )  # remove the 'discount' field
        event = Event.objects.create(**validated_data)

        with transaction.atomic():
            #event = Event.objects.create(**validated_data)

            # Create TimeSlot instances
            for timeslot in timeslot_data:
                TimeSlot.objects.create(event=event, **timeslot)

            DateTime.objects.create(event=event, **date_data)

            # Create PriceLayerPrice instances
            price_layer_prices = []
            for price_layer_price in price_layer_price_data:
                price_layer_name = price_layer_price["price_layer"]["name"]
                price_type_name = price_layer_price["price_type"]["name"]

                try:
                    price_layer = PriceLayer.objects.get(name=price_layer_name)
                except PriceLayer.DoesNotExist:
                    raise serializers.ValidationError(
                        f"PriceLayer '{price_layer_name}' does not exist."
                    )

                # Check if PriceType already exists
                try:
                    price_type = PriceType.objects.get(name=price_type_name)
                except PriceType.DoesNotExist:
                    # Create a new PriceType if it doesn't exist
                    price_type = PriceType.objects.create(name=price_type_name)

                price_layer_price_instance = PriceLayerPrice.objects.create(
                    event=event,
                    price=price_layer_price["price"],
                    price_layer=price_layer,
                    price_type=price_type,
                )
                price_layer_prices.append(price_layer_price_instance)

            event.price_layer_price.set(price_layer_prices)

            # Create AccountLayer instances
            for account_layer in account_layer_data:

                account_data = account_layer["gl_account"]
                price_layer_data = account_layer["price_layer"]
                price_layer_name = price_layer_data["name"]

                account, created = Account.objects.get_or_create(
                    gl_account=account_data["gl_account"]
                )

                try:
                    price_layer = PriceLayer.objects.get(name=price_layer_name)
                except PriceLayer.DoesNotExist:
                    raise serializers.ValidationError(
                        f"PriceLayer '{price_layer_name}' does not exist."
                    )

                account_layer_instance = AccountLayer.objects.create(
                    gl_account=account, price_layer=price_layer, event=event
                )
                #account_layer_instance.event.add(event)

                print('here...')
                print(account_layer)

            # now that you have an Event, you can add the related Discounts

            for discount in discount_data:
                price_type_name = discount["price_type"]

                try:
                    price_type = PriceType.objects.get(name=price_type_name)
                except PriceType.DoesNotExist:
                    raise serializers.ValidationError(
                        f"PriceType '{price_type_name}' does not exist."
                    )

                Discount.objects.create(
                    event=event,
                    price_type=price_type,
                    discount=discount["discount"],
                    description=discount["description"],
                )
            return event

        return event


class EditEventSerializer(serializers.ModelSerializer):
    timeslot_set = TimeSlotSerializer(many=True)
    date_time = DateTimeSerializer()
    price_layer_price = EditPriceLayerPriceSerializer(many=True)
    # price_layer_price = serializers.ListSerializer(child=serializers.DictField())
    discount = EditDiscountSerializer(many=True)
    account = EditAccountLayerSerializer(many=True)
    price_type = EditPriceTypeSerializer(many=True, read_only=True)
    price_layer = PriceLayerSerializer(many=True, read_only=True)
    location = serializers.CharField(source="location.location_name")
    facility = serializers.CharField(source="facility.facility_name")

    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "description",
            "capacity",
            "held",
            "entrance",
            "gr_required",
            "early_closure",
            "csi_needed",
            "csi_mandatory",
            "csi_notes",
            "location",
            "date_time",
            "timeslot_set",
            "price_type",
            "price_layer",
            "status",
            "website_link",
            "websales_link",
            "facility",
            "discount",
            "additional_notes",
            "account",
            "price_layer_price",
        ]  #'account_layer_set']

    def create(self, validated_data):
        date_data = validated_data.pop("date_time")
        event = Event.objects.create(**validated_data)
        # The event must be created first since the foreign key lives on the DateTime model. We need an event to insert.
        DateTime.objects.create(event=event, **date_data)
        return event

    def get_date_time(self, obj):
        return {"event_date": obj.date_time.strftime("%Y-%m-%d %H:%M:%S")}

    def update(self, instance, validated_data):
        print("right here...")
        print(validated_data)
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.capacity = validated_data.get("capacity", instance.capacity)
        instance.held = validated_data.get("held", instance.held)
        instance.entrance = validated_data.get("entrance", instance.entrance)
        instance.gr_required = validated_data.get("gr_required", instance.gr_required)
        instance.early_closure = validated_data.get(
            "early_closure", instance.early_closure
        )
        instance.csi_needed = validated_data.get("csi_needed", instance.csi_needed)
        instance.csi_mandatory = validated_data.get(
            "csi_mandatory", instance.csi_mandatory
        )
        instance.csi_notes = validated_data.get("csi_notes", instance.csi_notes)
        instance.additional_notes = validated_data.get(
            "additional_notes", instance.additional_notes
        )
        instance.website_link = validated_data.get(
            "website_link", instance.website_link
        )
        instance.websales_link = validated_data.get(
            "websales_link", instance.websales_link
        )
        # instance.date_time = validated_data.get('date_time', instance.date_time)
        location_name = validated_data.get("location", {}).get("location_name")

        if location_name:
            location, _ = Location.objects.get_or_create(location_name=location_name)
            instance.location = location
        facility_name = validated_data.get("facility", {}).get("facility_name")
        if facility_name:
            facility, _ = Facility.objects.get_or_create(facility_name=facility_name)
            instance.facility = facility
        instance.save()

        # Update the DateTime model
        date_time_data = validated_data.get("date_time")
        if date_time_data:
            date_time_fields = [
                "event_date",
                "event_time",
                "event_end_time",
                "sell_date",
                "stop_date",
                "door_open",
                "door_close",
                "early_closure_time",
            ]
            for field_name in date_time_fields:
                field_value = date_time_data.get(field_name)
                if field_value is not None:
                    setattr(instance.date_time, field_name, field_value)
            instance.date_time.save()

        # Update the PriceLayer, PriceType, and PriceLayerPrice models
        price_layer_price_set_data = validated_data.get("price_layer_price")
        if price_layer_price_set_data:
            for price_layer_price_data in price_layer_price_set_data:
                price_type_name = price_layer_price_data["price_type"].name
                price_layer_name = price_layer_price_data["price_layer"]["name"]
                try:
                    # Try to get an existing PriceType object with the same name
                    price_type = PriceType.objects.get(name=price_type_name)
                except PriceType.DoesNotExist:
                    # If no existing object was found, create a new one
                    price_type = PriceType(name=price_type_name)
                    price_type.save()

                try:
                    # Try to get an existing PriceLayer object with the same name
                    price_layer = PriceLayer.objects.get(name=price_layer_name)
                except PriceLayer.DoesNotExist:
                    # If no existing object was found, create a new one
                    price_layer = PriceLayer(name=price_layer_name)
                    price_layer.save()

                try:
                    # Try to get an existing PriceLayerPrice object with the same price_type and price_layer
                    price_layer_price = instance.price_layer_price.get(
                        price_type=price_type, price_layer=price_layer
                    )
                except PriceLayerPrice.DoesNotExist:
                    # If no existing object was found, create a new one
                    price_layer_price = PriceLayerPrice(
                        event=instance, price_type=price_type, price_layer=price_layer
                    )

                # Update the price field of the PriceLayerPrice object
                if price_layer_price_data["price"] > 0:
                    price_layer_price.price = price_layer_price_data["price"]
                    price_layer_price.save()
                elif price_layer_price.id:
                    price_layer_price.delete()

        discount_data = validated_data.get("discount")
        if discount_data:
            for discount in discount_data:
                price_type_name = discount.get("price_type")
                # price_type_name = price_type_data.get('name')
                # price_type_name = price_type_data['price_type'].name
                try:
                    # Try to get an existing PriceType object with the same name
                    price_type = PriceType.objects.get(name=price_type_name)
                except PriceType.DoesNotExist:
                    # If no existing object was found, raise a validation error
                    raise serializers.ValidationError(
                        {"price_type": ["Invalid price type."]}
                    )

                try:
                    # Try to get an existing Discount object with the same price_type
                    discount_obj = instance.discount.get(price_type=price_type)
                except Discount.DoesNotExist:
                    # If no existing object was found, create a new one
                    discount_obj = Discount(event=instance, price_type=price_type)

                # Update the discount and description fields of the Discount object
                discount_obj.discount = discount["discount"]
                discount_obj.description = discount["description"]
                discount_obj.save()

        # Update the AccountLayer model
        account_layer_set_data = validated_data.get("account", [])
        created_account_layers = []

        if account_layer_set_data:
            for account_layer_data in account_layer_set_data:
                account_layer_id = account_layer_data.get(
                    "id"
                )  # Get the ID of the AccountLayer
                account_data = account_layer_data.get("gl_account")
                price_layer_data = account_layer_data.get("price_layer")
                print("here...")
                print(account_layer_id)
                print(account_data)
                print(price_layer_data)

                if account_data and price_layer_data:
                    gl_account = account_data.get("gl_account")
                    price_layer_name = price_layer_data.get("name")

                    if gl_account and price_layer_name:
                        try:
                            account, created_account = Account.objects.get_or_create(
                                gl_account=gl_account
                            )
                            # Update other fields of account here, if needed

                        except Account.DoesNotExist:
                            raise serializers.ValidationError(
                                f"Account with gl_account '{gl_account}' does not exist."
                            )

                        try:
                            price_layer, created_price_layer = PriceLayer.objects.get_or_create(
                                name=price_layer_name
                            )

                            if account_layer_id:  # Check if ID is present
                                try:
                                    # Try to update an existing AccountLayer object based on the ID
                                    account_layer = AccountLayer.objects.get(
                                        id=account_layer_id, event=instance
                                    )
                                except AccountLayer.DoesNotExist:
                                    raise serializers.ValidationError(
                                        f"AccountLayer with id '{account_layer_id}' does not exist."
                                    )
                            else:
                                # Create a new AccountLayer object
                                account_layer = AccountLayer(event=instance, gl_account=account)

                            # Update the AccountLayer object's fields
                            account_layer.gl_account = account
                            account_layer.price_layer = price_layer

                            # Save the updates
                            account_layer.save()

                        except PriceLayer.DoesNotExist:
                            raise serializers.ValidationError(
                                f"PriceLayer with name '{price_layer_name}' does not exist."
                            )

        instance.save()
        return instance


class SimpleDateTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateTime
        fields = ["event", "event_date"]


class SimpleEventSerializer(serializers.ModelSerializer):
    date_time = SimpleDateTimeSerializer()

    class Meta:
        model = Event
        fields = ["id", "name", "date_time", "status"]
