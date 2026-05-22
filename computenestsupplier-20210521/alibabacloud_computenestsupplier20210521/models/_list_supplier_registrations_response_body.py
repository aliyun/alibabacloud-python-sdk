# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListSupplierRegistrationsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        supplier_registrations: List[main_models.ListSupplierRegistrationsResponseBodySupplierRegistrations] = None,
        total_count: int = None,
    ):
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The supplier registrations
        self.supplier_registrations = supplier_registrations
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.supplier_registrations:
            for v1 in self.supplier_registrations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SupplierRegistrations'] = []
        if self.supplier_registrations is not None:
            for k1 in self.supplier_registrations:
                result['SupplierRegistrations'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.supplier_registrations = []
        if m.get('SupplierRegistrations') is not None:
            for k1 in m.get('SupplierRegistrations'):
                temp_model = main_models.ListSupplierRegistrationsResponseBodySupplierRegistrations()
                self.supplier_registrations.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSupplierRegistrationsResponseBodySupplierRegistrations(DaraModel):
    def __init__(
        self,
        comment: str = None,
        contact_email: str = None,
        contact_number: str = None,
        contact_person: str = None,
        contact_person_title: str = None,
        enable_reseller_mode: bool = None,
        product_annual_revenue: str = None,
        product_business: str = None,
        product_delivery_types: str = None,
        product_publish_time: str = None,
        product_sell_types: str = None,
        registration_id: str = None,
        resell_business_desc: str = None,
        status: str = None,
        submit_time: str = None,
        supplier_desc: str = None,
        supplier_logo: str = None,
        supplier_name: str = None,
        supplier_name_en: str = None,
        supplier_uid: str = None,
        supplier_url: str = None,
    ):
        # The comment of this registration.
        self.comment = comment
        # Contact email
        self.contact_email = contact_email
        # Contact number
        self.contact_number = contact_number
        # Contact person
        self.contact_person = contact_person
        # Contact person tiltle.
        self.contact_person_title = contact_person_title
        # Whether to enable the resell mode.
        self.enable_reseller_mode = enable_reseller_mode
        # Annual product revenue
        self.product_annual_revenue = product_annual_revenue
        # The business of product.
        self.product_business = product_business
        # Product delivery type，Valid values:
        # 
        # SaaS
        # License
        # API
        # DesktopSoftware
        # Others
        self.product_delivery_types = product_delivery_types
        # The publish time of product.
        self.product_publish_time = product_publish_time
        # Product sell type, Valid values:
        # 
        # - Direct
        # - Channel
        self.product_sell_types = product_sell_types
        # The registration ID.
        self.registration_id = registration_id
        # The description of resell business.
        self.resell_business_desc = resell_business_desc
        # The deployment state of the registration. Valid values:
        # 
        # - Submitted
        # - Approved
        # - Rejected
        self.status = status
        # The submit time of this registration.
        self.submit_time = submit_time
        # The description of service provider.
        self.supplier_desc = supplier_desc
        # The Logo of service provider.
        self.supplier_logo = supplier_logo
        # The name of the service provider.
        self.supplier_name = supplier_name
        # The english name of the service provider.
        self.supplier_name_en = supplier_name_en
        # The Alibaba Cloud account ID of the service provider.
        self.supplier_uid = supplier_uid
        # The URL of the service provider.
        self.supplier_url = supplier_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

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

        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id

        if self.resell_business_desc is not None:
            result['ResellBusinessDesc'] = self.resell_business_desc

        if self.status is not None:
            result['Status'] = self.status

        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time

        if self.supplier_desc is not None:
            result['SupplierDesc'] = self.supplier_desc

        if self.supplier_logo is not None:
            result['SupplierLogo'] = self.supplier_logo

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        if self.supplier_name_en is not None:
            result['SupplierNameEn'] = self.supplier_name_en

        if self.supplier_uid is not None:
            result['SupplierUid'] = self.supplier_uid

        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

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

        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')

        if m.get('ResellBusinessDesc') is not None:
            self.resell_business_desc = m.get('ResellBusinessDesc')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        if m.get('SupplierDesc') is not None:
            self.supplier_desc = m.get('SupplierDesc')

        if m.get('SupplierLogo') is not None:
            self.supplier_logo = m.get('SupplierLogo')

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        if m.get('SupplierNameEn') is not None:
            self.supplier_name_en = m.get('SupplierNameEn')

        if m.get('SupplierUid') is not None:
            self.supplier_uid = m.get('SupplierUid')

        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')

        return self

