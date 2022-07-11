from django.db import models
from django.apps import apps
from django.contrib.auth import get_user_model


# GET Authenticated user model.
# -----------------------------
Authenticated_manager = get_user_model()

# To get the model from the other app
# ------------------------------------
# product_model = apps.get_model("C_app", "InventoryModel")


class InventoryModel(models.Model):
    active_manager = models.ForeignKey(
        Authenticated_manager,
        on_delete=models.CASCADE,
        verbose_name="auth_manager",
        related_name="manager_data",
        blank=True,
        null=True,
    )
    product_name = models.CharField(
        max_length=1000,
        blank=False,
        null=False,
    )
    product_discription = models.CharField(
        max_length=1500,
        blank=False,
        null=False,
    )
    product_price = models.IntegerField(
        default=0,
        null=False,
        blank=False,
    )
    record_date_edited = models.DateTimeField(
        auto_now=True,
    )
    record_date = models.DateTimeField(
        auto_now_add=True,
    )
    style_image = models.ImageField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return "{manager} added product: {name} on {date}".format(manager=self.active_manager.username, name=self.product_price, date=self.record_date)


class OrderModel(models.Model):
    product_ordered = models.ForeignKey(
        InventoryModel,
        on_delete=models.CASCADE,
        verbose_name="product_info",
        related_name="ordered_product_data",
        blank=True,
        null=True,
    )
    material_quality = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    outfit_name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    material_color = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    length = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    waist = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    laps = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    knees = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    ankles = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    style_image = models.ImageField(
        null=False,
        blank=False,
    )
    wrist_measurment = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    lower_arm_measurment = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    upper_arm_measurment = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    sleeve_length_measurment = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    tummy_measurment = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    chest_measurment = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    shoulder_measurment = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    neck_measurment = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    sleeve_type = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    button_type = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    order_remark = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    order_quantity = models.IntegerField(
        blank=False,
        null=False,
        default=0,
    )
    order_status = models.CharField(
        max_length=1000,
        blank=False,
        null=False,
    )
    order_total_amount = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    customer_name = models.CharField(
        max_length=1000,
        blank=False,
        null=False,
    )
    customer_phone = models.CharField(
        help_text='Customer phone number',
        max_length=20,
        blank=False,
        null=False,
    )
    customer_email = models.EmailField(
        max_length=1000,
        blank=False,
        null=False,
    )
    customer_state = models.CharField(
        max_length=1000,
        blank=False,
        null=False,
    )
    customer_address = models.CharField(
        max_length=1000,
        blank=False,
        null=False,
    )
    deliver_date = models.DateTimeField(
        default=0,
    )
    date_ordered = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return "{quantity}x {product} ordered on {date}".format(quantity=self.order_quantity, product=self.product_name, date=self.date_ordered)


class DeliverySettings(models.Model):
    active_manager = models.ForeignKey(
        Authenticated_manager,
        on_delete=models.CASCADE,
        verbose_name="auth_manager",
        related_name="delivery_manager",
        blank=True,
        null=True,
    )
    state = models.CharField(
        max_length=1500,
        blank=False,
        null=False,
    )
    delivery_rate = models.IntegerField(
        default=0,
        null=False,
        blank=False,
    )
    # order_status = models.CharField(
    #     max_length=1000,
    #     null=False,
    #     blank=False,
    # )
    # customer_address = models.CharField(
    #     max_length=1000,
    #     null=False,
    #     blank=False,
    # )
    record_date_edited = models.DateTimeField(
        null=True,
        blank=True,
        auto_now=True,
    )
    record_date = models.DateTimeField(
        null=True,
        blank=True,
        auto_now_add=True,
    )

    def __str__(self):
        return "{state} state delivery rate: {delivery_rate} by: {manager} added on {date}".format(state=self.state, delivery_rate=self.delivery_rate, manager=self.active_manager, date=self.record_date)


class ProductImageModel(models.Model):
    product_ordered = models.ForeignKey(
        InventoryModel,
        on_delete=models.CASCADE,
        verbose_name="product_info",
        related_name="product_data",
        blank=True,
        null=True,
    )
    product_image = models.ImageField()
