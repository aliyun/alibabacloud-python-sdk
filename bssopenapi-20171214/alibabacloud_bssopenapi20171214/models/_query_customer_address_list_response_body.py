# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryCustomerAddressListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryCustomerAddressListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryCustomerAddressListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryCustomerAddressListResponseBodyData(DaraModel):
    def __init__(
        self,
        customer_invoice_address_list: main_models.QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressList = None,
    ):
        # The details of addresses to which invoices are mailed.
        self.customer_invoice_address_list = customer_invoice_address_list

    def validate(self):
        if self.customer_invoice_address_list:
            self.customer_invoice_address_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_invoice_address_list is not None:
            result['CustomerInvoiceAddressList'] = self.customer_invoice_address_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerInvoiceAddressList') is not None:
            temp_model = main_models.QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressList()
            self.customer_invoice_address_list = temp_model.from_map(m.get('CustomerInvoiceAddressList'))

        return self

class QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressList(DaraModel):
    def __init__(
        self,
        customer_invoice_address: List[main_models.QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressListCustomerInvoiceAddress] = None,
    ):
        self.customer_invoice_address = customer_invoice_address

    def validate(self):
        if self.customer_invoice_address:
            for v1 in self.customer_invoice_address:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomerInvoiceAddress'] = []
        if self.customer_invoice_address is not None:
            for k1 in self.customer_invoice_address:
                result['CustomerInvoiceAddress'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customer_invoice_address = []
        if m.get('CustomerInvoiceAddress') is not None:
            for k1 in m.get('CustomerInvoiceAddress'):
                temp_model = main_models.QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressListCustomerInvoiceAddress()
                self.customer_invoice_address.append(temp_model.from_map(k1))

        return self

class QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressListCustomerInvoiceAddress(DaraModel):
    def __init__(
        self,
        addressee: str = None,
        biz_type: str = None,
        city: str = None,
        county: str = None,
        delivery_address: str = None,
        id: int = None,
        phone: str = None,
        postal_code: str = None,
        province: str = None,
        street: str = None,
        user_id: int = None,
        user_nick: str = None,
    ):
        # The addressee.
        self.addressee = addressee
        # The business type.
        self.biz_type = biz_type
        # The city to which the invoice is mailed.
        self.city = city
        # The name of the district to which the invoice is mailed.
        self.county = county
        # The detailed address to which the invoice is mailed. This parameter is returned after fields are concatenated.
        self.delivery_address = delivery_address
        # The ID.
        self.id = id
        # The phone number of the addressee.
        self.phone = phone
        # The postcode.
        self.postal_code = postal_code
        # The province to which the invoice is mailed.
        self.province = province
        # The name of the street to which the invoice is mailed.
        self.street = street
        # The ID of the user.
        self.user_id = user_id
        # The nickname of the user.
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addressee is not None:
            result['Addressee'] = self.addressee

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.city is not None:
            result['City'] = self.city

        if self.county is not None:
            result['County'] = self.county

        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address

        if self.id is not None:
            result['Id'] = self.id

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code

        if self.province is not None:
            result['Province'] = self.province

        if self.street is not None:
            result['Street'] = self.street

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_nick is not None:
            result['UserNick'] = self.user_nick

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addressee') is not None:
            self.addressee = m.get('Addressee')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('County') is not None:
            self.county = m.get('County')

        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('Street') is not None:
            self.street = m.get('Street')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')

        return self

