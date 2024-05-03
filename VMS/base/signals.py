from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import VendorModel


def generate_vendor_code(name):
  initials = ''.join([x[0] for x in name.split(' ') ])

  vendor_no = VendorModel.vendors +1 

  format_vendor_no = f'{vendor_no:03d}'

  code = f'{initials}{format_vendor_no}' 

  return code

@receiver(pre_save,sender = VendorModel)
def GenerateVendorCode(sender, instance, **kwargs):
    print("Signal handler triggered")
    instance.vendor_code = generate_vendor_code(instance.name)


