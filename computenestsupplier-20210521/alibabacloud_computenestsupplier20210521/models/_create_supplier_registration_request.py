# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateSupplierRegistrationRequest(DaraModel):
    def __init__(
        self,
        contact_email: str = None,
        contact_number: str = None,
        contact_person: str = None,
        contact_person_title: str = None,
        enable_reseller_mode: bool = None,
        product_annual_revenue: str = None,
        product_business: str = None,
        product_delivery_types: List[str] = None,
        product_publish_time: str = None,
        product_sell_types: List[str] = None,
        region_id: str = None,
        resell_business_desc: str = None,
        suggestion: str = None,
        supplier_desc: str = None,
        supplier_logo: str = None,
        supplier_name: str = None,
        supplier_name_en: str = None,
        supplier_url: str = None,
    ):
        # The email address of the contact person.
        # 
        # This parameter is required.
        self.contact_email = contact_email
        # The phone number of the contact person.
        # 
        # This parameter is required.
        self.contact_number = contact_number
        # The contact person.
        # 
        # This parameter is required.
        self.contact_person = contact_person
        # The title of the contact person.
        # 
        # This parameter is required.
        self.contact_person_title = contact_person_title
        # Specifies whether to enable distribution.
        self.enable_reseller_mode = enable_reseller_mode
        # The annual revenue of the product.
        self.product_annual_revenue = product_annual_revenue
        # The industry of the service provider\\"s product.
        self.product_business = product_business
        # The delivery methods of the service provider\\"s product. Valid values:
        # 
        # - SaaS
        # 
        # - License
        # 
        # - API
        # 
        # - DesktopSoftware
        # 
        # - Others
        # 
        # This parameter is required.
        self.product_delivery_types = product_delivery_types
        # The launch date of the product.
        self.product_publish_time = product_publish_time
        # The sales models of the service provider\\"s product. Valid values:
        # 
        # - Direct: Direct sales
        # 
        # - Channel: Channel sales
        # 
        # This parameter is required.
        self.product_sell_types = product_sell_types
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The description of the distribution business.
        self.resell_business_desc = resell_business_desc
        # The suggestions from the service provider.
        self.suggestion = suggestion
        # The description of the service provider.
        # 
        # This parameter is required.
        self.supplier_desc = supplier_desc
        # The icon of the service provider.
        self.supplier_logo = supplier_logo
        # The name of the service provider.
        # 
        # This parameter is required.
        self.supplier_name = supplier_name
        # The English name of the service provider.
        # 
        # This parameter is required.
        self.supplier_name_en = supplier_name_en
        # The supplier\\"s address.
        # 
        # This parameter is required.
        self.supplier_url = supplier_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email

        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number

        if self.contact_person is not None:
            result['ContactPerson'] = self.contact_person

        if self.contact_person_title is not None:
            result['ContactPersonTitle'] = self.contact_person_title

        if self.enable_reseller_mode is not None:
            result['EnableResellerMode'] = self.enable_reseller_mode

        if self.product_annual_revenue is not None:
            result['ProductAnnualRevenue'] = self.product_annual_revenue

        if self.product_business is not None:
            result['ProductBusiness'] = self.product_business

        if self.product_delivery_types is not None:
            result['ProductDeliveryTypes'] = self.product_delivery_types

        if self.product_publish_time is not None:
            result['ProductPublishTime'] = self.product_publish_time

        if self.product_sell_types is not None:
            result['ProductSellTypes'] = self.product_sell_types

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resell_business_desc is not None:
            result['ResellBusinessDesc'] = self.resell_business_desc

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.supplier_desc is not None:
            result['SupplierDesc'] = self.supplier_desc

        if self.supplier_logo is not None:
            result['SupplierLogo'] = self.supplier_logo

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        if self.supplier_name_en is not None:
            result['SupplierNameEn'] = self.supplier_name_en

        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')

        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')

        if m.get('ContactPerson') is not None:
            self.contact_person = m.get('ContactPerson')

        if m.get('ContactPersonTitle') is not None:
            self.contact_person_title = m.get('ContactPersonTitle')

        if m.get('EnableResellerMode') is not None:
            self.enable_reseller_mode = m.get('EnableResellerMode')

        if m.get('ProductAnnualRevenue') is not None:
            self.product_annual_revenue = m.get('ProductAnnualRevenue')

        if m.get('ProductBusiness') is not None:
            self.product_business = m.get('ProductBusiness')

        if m.get('ProductDeliveryTypes') is not None:
            self.product_delivery_types = m.get('ProductDeliveryTypes')

        if m.get('ProductPublishTime') is not None:
            self.product_publish_time = m.get('ProductPublishTime')

        if m.get('ProductSellTypes') is not None:
            self.product_sell_types = m.get('ProductSellTypes')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResellBusinessDesc') is not None:
            self.resell_business_desc = m.get('ResellBusinessDesc')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('SupplierDesc') is not None:
            self.supplier_desc = m.get('SupplierDesc')

        if m.get('SupplierLogo') is not None:
            self.supplier_logo = m.get('SupplierLogo')

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        if m.get('SupplierNameEn') is not None:
            self.supplier_name_en = m.get('SupplierNameEn')

        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')

        return self

