from . import forms
from . import models

from pprint import pprint
from django.apps import apps
from django.utils import timezone
from os.path import join as join_path
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from django.views.generic.base import View as custom_view


# GET Current date and time.
# ---------------------------
Todays_Date = timezone.now()
Todays_Date = Todays_Date.strftime("%Y")

# GET Authenticated user model.
# -----------------------------
Authenticated_manager = get_user_model()

# SET admin acess title.
# -----------------------
panel_name = "Prime Access"


class PrimeAccessView(custom_view):
    template_name = join_path("dashboard", "prime-access.html")

    def get(self, request):
        context = {
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        context = {
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
        }

        return render(request, self.template_name, context=context)


class AllProductsView(custom_view):
    template_name = join_path("dashboard", "all-products.html")

    def get(self, request, category):
        context = {
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
        }

        return render(request, self.template_name, context=context)

    def post(self, request, category):
        context = {
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
        }

        return render(request, self.template_name, context=context)


class AddProductsView(custom_view):
    template_name = join_path("dashboard", "add-products.html")

    def get(self, request):
        context = {
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        context = {
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
        }

        return render(request, self.template_name, context=context)


class AllOrdersView(custom_view):
    template_name = join_path("dashboard", "all-orders.html")

    def get(self, request, category):
        context = {
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
        }

        return render(request, self.template_name, context=context)

    def post(self, request, category):
        context = {
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
        }

        return render(request, self.template_name, context=context)


class DeliverySettings(custom_view):
    action = "create"
    template_name = join_path("dashboard", "delivery-settings.html")

    def get(self, request):
        form_class = forms.DeliverySettngsForm()
        delivery_record = models.DeliverySettings.objects.all()

        context = {
            "form": form_class,
            "action": self.action,
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
            "delivery_record": reversed(delivery_record),
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        form_class = forms.DeliverySettngsForm(request.POST)
        delivery_record = models.DeliverySettings.objects.all()

        context = {
            "form": form_class,
            "action": self.action,
            "panel_name": panel_name,
            "Todays_Date": Todays_Date,
            "delivery_record": reversed(delivery_record),
        }

        if form_class.is_valid():
            form_class.save(commit=False)
            form_class.active_manager = request.user
            form_class.save()
            return redirect(reverse('DeliverySettingsView'))

        return render(request, self.template_name, context=context)


class ModifyDeliverySettings(custom_view):
    action = "update"
    template_name = join_path("dashboard", "delivery-settings.html")

    def get(self, request, action, instance):

        if action == "delete":
            models.DeliverySettings.objects.get(pk=instance).delete()
            return redirect(reverse("DeliverySettingsView"))
        elif action == "update":
            all_delivery_record = models.DeliverySettings.objects.all()
            delivery_record = models.DeliverySettings.objects.get(
                pk=instance)
            # delivery_record_render = {
            #     "state": delivery_record.values("state")[0]["state"],
            #     "delivery_rate": delivery_record.values("delivery_rate")[0]["delivery_rate"],
            # }
            form_class = forms.DeliverySettngsForm(instance=delivery_record)

            context = {
                "form": form_class,
                "action": self.action,
                "panel_name": panel_name,
                "Todays_Date": Todays_Date,
                "delivery_record": all_delivery_record,
                # "delivery_record": reversed(instance_date),
            }

        return render(request, self.template_name, context=context)

    def post(self, request, action, instance):
        if action == "update":
            all_delivery_record = models.DeliverySettings.objects.all()
            delivery_record = models.DeliverySettings.objects.get(
                pk=instance)
            # delivery_record_render = {
            #     "state": delivery_record.values("state")[0]["state"],
            #     "delivery_rate": delivery_record.values("delivery_rate")[0]["delivery_rate"],
            # }
            form_class = forms.DeliverySettngsForm(
                data=request.POST, instance=delivery_record)

            context = {
                "form": form_class,
                "action": self.action,
                "panel_name": panel_name,
                "Todays_Date": Todays_Date,
                "delivery_record": all_delivery_record,
                # "delivery_record": reversed(instance_date),
            }

            if form_class.is_valid():
                # form_class.save(commit=False)
                # form_class.active_manager = request.user
                form_class.save()
                return redirect(reverse("DeliverySettingsView"))

        return render(request, self.template_name, context=context)
        # new_instance = instance_data.update(
        #     state=request.POST["state"],
        #     delivery_rate=request.POST["delivery-rate"]
        # )
        # new_instance.save()