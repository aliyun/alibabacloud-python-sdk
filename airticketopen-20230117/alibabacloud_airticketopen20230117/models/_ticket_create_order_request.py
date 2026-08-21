# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class TicketCreateOrderRequest(DaraModel):
    def __init__(
        self,
        account_no: int = None,
        contact: main_models.TicketCreateOrderRequestContact = None,
        distributor_order_id: str = None,
        order_product: main_models.TicketCreateOrderRequestOrderProduct = None,
        quantity: int = None,
        total_distribution_price: main_models.TicketCreateOrderRequestTotalDistributionPrice = None,
        travelers: List[main_models.TicketCreateOrderRequestTravelers] = None,
    ):
        # This parameter is required.
        self.account_no = account_no
        # This parameter is required.
        self.contact = contact
        # This parameter is required.
        self.distributor_order_id = distributor_order_id
        # This parameter is required.
        self.order_product = order_product
        # This parameter is required.
        self.quantity = quantity
        # This parameter is required.
        self.total_distribution_price = total_distribution_price
        self.travelers = travelers

    def validate(self):
        if self.contact:
            self.contact.validate()
        if self.order_product:
            self.order_product.validate()
        if self.total_distribution_price:
            self.total_distribution_price.validate()
        if self.travelers:
            for v1 in self.travelers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_no is not None:
            result['AccountNo'] = self.account_no

        if self.contact is not None:
            result['Contact'] = self.contact.to_map()

        if self.distributor_order_id is not None:
            result['DistributorOrderId'] = self.distributor_order_id

        if self.order_product is not None:
            result['OrderProduct'] = self.order_product.to_map()

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.total_distribution_price is not None:
            result['TotalDistributionPrice'] = self.total_distribution_price.to_map()

        result['Travelers'] = []
        if self.travelers is not None:
            for k1 in self.travelers:
                result['Travelers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')

        if m.get('Contact') is not None:
            temp_model = main_models.TicketCreateOrderRequestContact()
            self.contact = temp_model.from_map(m.get('Contact'))

        if m.get('DistributorOrderId') is not None:
            self.distributor_order_id = m.get('DistributorOrderId')

        if m.get('OrderProduct') is not None:
            temp_model = main_models.TicketCreateOrderRequestOrderProduct()
            self.order_product = temp_model.from_map(m.get('OrderProduct'))

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('TotalDistributionPrice') is not None:
            temp_model = main_models.TicketCreateOrderRequestTotalDistributionPrice()
            self.total_distribution_price = temp_model.from_map(m.get('TotalDistributionPrice'))

        self.travelers = []
        if m.get('Travelers') is not None:
            for k1 in m.get('Travelers'):
                temp_model = main_models.TicketCreateOrderRequestTravelers()
                self.travelers.append(temp_model.from_map(k1))

        return self

class TicketCreateOrderRequestTravelers(DaraModel):
    def __init__(
        self,
        birthday: str = None,
        certificate_no: str = None,
        certificate_type: int = None,
        dialing_code: str = None,
        email: str = None,
        first_name: str = None,
        gender: int = None,
        last_name: str = None,
        mobile: str = None,
        name: str = None,
        nationality: str = None,
    ):
        self.birthday = birthday
        self.certificate_no = certificate_no
        self.certificate_type = certificate_type
        self.dialing_code = dialing_code
        self.email = email
        self.first_name = first_name
        self.gender = gender
        self.last_name = last_name
        self.mobile = mobile
        self.name = name
        self.nationality = nationality

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birthday is not None:
            result['Birthday'] = self.birthday

        if self.certificate_no is not None:
            result['CertificateNo'] = self.certificate_no

        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type

        if self.dialing_code is not None:
            result['DialingCode'] = self.dialing_code

        if self.email is not None:
            result['Email'] = self.email

        if self.first_name is not None:
            result['FirstName'] = self.first_name

        if self.gender is not None:
            result['Gender'] = self.gender

        if self.last_name is not None:
            result['LastName'] = self.last_name

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.name is not None:
            result['Name'] = self.name

        if self.nationality is not None:
            result['Nationality'] = self.nationality

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Birthday') is not None:
            self.birthday = m.get('Birthday')

        if m.get('CertificateNo') is not None:
            self.certificate_no = m.get('CertificateNo')

        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')

        if m.get('DialingCode') is not None:
            self.dialing_code = m.get('DialingCode')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')

        if m.get('Gender') is not None:
            self.gender = m.get('Gender')

        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')

        return self

class TicketCreateOrderRequestTotalDistributionPrice(DaraModel):
    def __init__(
        self,
        amount: int = None,
        currency_code: str = None,
    ):
        # This parameter is required.
        self.amount = amount
        # This parameter is required.
        self.currency_code = currency_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')

        return self

class TicketCreateOrderRequestOrderProduct(DaraModel):
    def __init__(
        self,
        distribution_price: main_models.TicketCreateOrderRequestOrderProductDistributionPrice = None,
        product_id: str = None,
        travel_date: str = None,
    ):
        # This parameter is required.
        self.distribution_price = distribution_price
        # This parameter is required.
        self.product_id = product_id
        # This parameter is required.
        self.travel_date = travel_date

    def validate(self):
        if self.distribution_price:
            self.distribution_price.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distribution_price is not None:
            result['DistributionPrice'] = self.distribution_price.to_map()

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.travel_date is not None:
            result['TravelDate'] = self.travel_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributionPrice') is not None:
            temp_model = main_models.TicketCreateOrderRequestOrderProductDistributionPrice()
            self.distribution_price = temp_model.from_map(m.get('DistributionPrice'))

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('TravelDate') is not None:
            self.travel_date = m.get('TravelDate')

        return self

class TicketCreateOrderRequestOrderProductDistributionPrice(DaraModel):
    def __init__(
        self,
        amount: int = None,
        currency_code: str = None,
    ):
        # This parameter is required.
        self.amount = amount
        # This parameter is required.
        self.currency_code = currency_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')

        return self

class TicketCreateOrderRequestContact(DaraModel):
    def __init__(
        self,
        certificate_no: str = None,
        certificate_type: int = None,
        dialing_code: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
        mobile: str = None,
        name: str = None,
    ):
        self.certificate_no = certificate_no
        self.certificate_type = certificate_type
        self.dialing_code = dialing_code
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_no is not None:
            result['CertificateNo'] = self.certificate_no

        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type

        if self.dialing_code is not None:
            result['DialingCode'] = self.dialing_code

        if self.email is not None:
            result['Email'] = self.email

        if self.first_name is not None:
            result['FirstName'] = self.first_name

        if self.last_name is not None:
            result['LastName'] = self.last_name

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateNo') is not None:
            self.certificate_no = m.get('CertificateNo')

        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')

        if m.get('DialingCode') is not None:
            self.dialing_code = m.get('DialingCode')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')

        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

