from django.db import models
from django.utils.translation import gettext_lazy as _


class VendorModel(models.Model):

  name = models.CharField(_("Vendor's Name"), max_length=50)
  contact_details = models.TextField(_("Contact Details"))
  address = models.TextField(_("Address"))
  vendor_code = models.CharField(_("Vendor Code"), max_length=50,unique = True)
  on_time_delivery_rate = models.FloatField(_("On-time Delivery Rate"),null=True,blank=True)
  quality_rating_avg = models.FloatField(_("Quantity Rating Average"),null=True,blank=True)
  average_response_time = models.FloatField(_("Average Response Time"),null=True,blank=True)
  fulfillment_rate = models.FloatField(_("Fulfillment Rate"),null=True,blank=True)

  vendors = 0

  def save(self,*args, **kwargs):
        if self.pk is None:
            VendorModel.vendors += 1
        super().save(*args, **kwargs)
    