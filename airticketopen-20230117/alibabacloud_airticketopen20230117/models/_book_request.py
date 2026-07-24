# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class BookRequest(DaraModel):
    def __init__(
        self,
        contact: main_models.BookRequestContact = None,
        out_order_num: str = None,
        passenger_ancillary_purchase_map_list: List[main_models.BookRequestPassengerAncillaryPurchaseMapList] = None,
        passenger_list: List[main_models.BookRequestPassengerList] = None,
        solution_id: str = None,
    ):
        # The contact information.
        # 
        # This parameter is required.
        self.contact = contact
        # The external order number.
        # 
        # This parameter is required.
        self.out_order_num = out_order_num
        # The mapping between passengers and ancillary purchases.
        self.passenger_ancillary_purchase_map_list = passenger_ancillary_purchase_map_list
        # The list of passengers.
        # 
        # This parameter is required.
        self.passenger_list = passenger_list
        # solution_id.
        # 
        # This parameter is required.
        self.solution_id = solution_id

    def validate(self):
        if self.contact:
            self.contact.validate()
        if self.passenger_ancillary_purchase_map_list:
            for v1 in self.passenger_ancillary_purchase_map_list:
                 if v1:
                    v1.validate()
        if self.passenger_list:
            for v1 in self.passenger_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact is not None:
            result['contact'] = self.contact.to_map()

        if self.out_order_num is not None:
            result['out_order_num'] = self.out_order_num

        result['passenger_ancillary_purchase_map_list'] = []
        if self.passenger_ancillary_purchase_map_list is not None:
            for k1 in self.passenger_ancillary_purchase_map_list:
                result['passenger_ancillary_purchase_map_list'].append(k1.to_map() if k1 else None)

        result['passenger_list'] = []
        if self.passenger_list is not None:
            for k1 in self.passenger_list:
                result['passenger_list'].append(k1.to_map() if k1 else None)

        if self.solution_id is not None:
            result['solution_id'] = self.solution_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contact') is not None:
            temp_model = main_models.BookRequestContact()
            self.contact = temp_model.from_map(m.get('contact'))

        if m.get('out_order_num') is not None:
            self.out_order_num = m.get('out_order_num')

        self.passenger_ancillary_purchase_map_list = []
        if m.get('passenger_ancillary_purchase_map_list') is not None:
            for k1 in m.get('passenger_ancillary_purchase_map_list'):
                temp_model = main_models.BookRequestPassengerAncillaryPurchaseMapList()
                self.passenger_ancillary_purchase_map_list.append(temp_model.from_map(k1))

        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k1 in m.get('passenger_list'):
                temp_model = main_models.BookRequestPassengerList()
                self.passenger_list.append(temp_model.from_map(k1))

        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')

        return self

class BookRequestPassengerList(DaraModel):
    def __init__(
        self,
        birthday: str = None,
        credential: main_models.BookRequestPassengerListCredential = None,
        first_name: str = None,
        gender: int = None,
        last_name: str = None,
        mobile_country_code: str = None,
        mobile_phone_number: str = None,
        nationality: str = None,
        type: int = None,
    ):
        # The date of birth in yyyyMMdd format.
        self.birthday = birthday
        # The credential information.
        self.credential = credential
        # The first name.
        # 
        # This parameter is required.
        self.first_name = first_name
        # The gender. Valid values:
        # - 0: MALE
        # - 1: FEMALE.
        self.gender = gender
        # The last name.
        # 
        # This parameter is required.
        self.last_name = last_name
        # The country calling code for the mobile phone number.
        # 
        # This parameter is required.
        self.mobile_country_code = mobile_country_code
        # The mobile phone number.
        # 
        # This parameter is required.
        self.mobile_phone_number = mobile_phone_number
        # The nationality. Use a two-letter country code.
        self.nationality = nationality
        # The passenger type. Valid values:
        # - 0: adult
        # - 1: child
        # - 8: infant.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birthday is not None:
            result['birthday'] = self.birthday

        if self.credential is not None:
            result['credential'] = self.credential.to_map()

        if self.first_name is not None:
            result['first_name'] = self.first_name

        if self.gender is not None:
            result['gender'] = self.gender

        if self.last_name is not None:
            result['last_name'] = self.last_name

        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code

        if self.mobile_phone_number is not None:
            result['mobile_phone_number'] = self.mobile_phone_number

        if self.nationality is not None:
            result['nationality'] = self.nationality

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

        if m.get('credential') is not None:
            temp_model = main_models.BookRequestPassengerListCredential()
            self.credential = temp_model.from_map(m.get('credential'))

        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')

        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')

        if m.get('mobile_phone_number') is not None:
            self.mobile_phone_number = m.get('mobile_phone_number')

        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class BookRequestPassengerListCredential(DaraModel):
    def __init__(
        self,
        cert_issue_place: str = None,
        credential_num: str = None,
        credential_type: int = None,
        expire_date: str = None,
    ):
        # The place of issue. Use a two-letter country code.
        self.cert_issue_place = cert_issue_place
        # The credential number.
        self.credential_num = credential_num
        # The credential type. Valid values:
        # - 0: ID card
        # - 1: passport
        # - 4: Home Return Permit
        # - 5: Taiwan Compatriot Permit
        # - 6: Hong Kong and Macau Travel Permit
        # - 12: Taiwan Travel Permit
        # - 19: no credential.
        self.credential_type = credential_type
        # The expiration date of the credential.
        self.expire_date = expire_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_issue_place is not None:
            result['cert_issue_place'] = self.cert_issue_place

        if self.credential_num is not None:
            result['credential_num'] = self.credential_num

        if self.credential_type is not None:
            result['credential_type'] = self.credential_type

        if self.expire_date is not None:
            result['expire_date'] = self.expire_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert_issue_place') is not None:
            self.cert_issue_place = m.get('cert_issue_place')

        if m.get('credential_num') is not None:
            self.credential_num = m.get('credential_num')

        if m.get('credential_type') is not None:
            self.credential_type = m.get('credential_type')

        if m.get('expire_date') is not None:
            self.expire_date = m.get('expire_date')

        return self

class BookRequestPassengerAncillaryPurchaseMapList(DaraModel):
    def __init__(
        self,
        book_ancillary_req_item: main_models.BookRequestPassengerAncillaryPurchaseMapListBookAncillaryReqItem = None,
        passenger_list: List[main_models.BookRequestPassengerAncillaryPurchaseMapListPassengerList] = None,
    ):
        # The ancillary product object for the booking request.
        self.book_ancillary_req_item = book_ancillary_req_item
        # The list of passengers who purchase the same ancillary product.
        self.passenger_list = passenger_list

    def validate(self):
        if self.book_ancillary_req_item:
            self.book_ancillary_req_item.validate()
        if self.passenger_list:
            for v1 in self.passenger_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.book_ancillary_req_item is not None:
            result['book_ancillary_req_item'] = self.book_ancillary_req_item.to_map()

        result['passenger_list'] = []
        if self.passenger_list is not None:
            for k1 in self.passenger_list:
                result['passenger_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('book_ancillary_req_item') is not None:
            temp_model = main_models.BookRequestPassengerAncillaryPurchaseMapListBookAncillaryReqItem()
            self.book_ancillary_req_item = temp_model.from_map(m.get('book_ancillary_req_item'))

        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k1 in m.get('passenger_list'):
                temp_model = main_models.BookRequestPassengerAncillaryPurchaseMapListPassengerList()
                self.passenger_list.append(temp_model.from_map(k1))

        return self

class BookRequestPassengerAncillaryPurchaseMapListPassengerList(DaraModel):
    def __init__(
        self,
        birthday: str = None,
        credential: main_models.BookRequestPassengerAncillaryPurchaseMapListPassengerListCredential = None,
        first_name: str = None,
        gender: int = None,
        last_name: str = None,
        mobile_country_code: str = None,
        mobile_phone_number: str = None,
        nationality: str = None,
        type: int = None,
    ):
        # The date of birth in yyyyMMdd format.
        self.birthday = birthday
        # The credential information.
        self.credential = credential
        # The first name.
        # 
        # This parameter is required.
        self.first_name = first_name
        # The gender. Valid values:
        # - 0: MALE
        # - 1: FEMALE.
        self.gender = gender
        # The last name.
        # 
        # This parameter is required.
        self.last_name = last_name
        # The country calling code for the mobile phone number.
        # 
        # This parameter is required.
        self.mobile_country_code = mobile_country_code
        # The mobile phone number.
        # 
        # This parameter is required.
        self.mobile_phone_number = mobile_phone_number
        # The nationality.
        self.nationality = nationality
        # The passenger type. Valid values:
        # - 0: adult
        # - 1: child
        # - 8: infant.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birthday is not None:
            result['birthday'] = self.birthday

        if self.credential is not None:
            result['credential'] = self.credential.to_map()

        if self.first_name is not None:
            result['first_name'] = self.first_name

        if self.gender is not None:
            result['gender'] = self.gender

        if self.last_name is not None:
            result['last_name'] = self.last_name

        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code

        if self.mobile_phone_number is not None:
            result['mobile_phone_number'] = self.mobile_phone_number

        if self.nationality is not None:
            result['nationality'] = self.nationality

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

        if m.get('credential') is not None:
            temp_model = main_models.BookRequestPassengerAncillaryPurchaseMapListPassengerListCredential()
            self.credential = temp_model.from_map(m.get('credential'))

        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')

        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')

        if m.get('mobile_phone_number') is not None:
            self.mobile_phone_number = m.get('mobile_phone_number')

        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class BookRequestPassengerAncillaryPurchaseMapListPassengerListCredential(DaraModel):
    def __init__(
        self,
        cert_issue_place: str = None,
        credential_num: str = None,
        credential_type: int = None,
        expire_date: str = None,
    ):
        # The place of issue. Use a two-letter country code.
        self.cert_issue_place = cert_issue_place
        # The credential number.
        self.credential_num = credential_num
        # The credential type. Valid values:
        # - 0: ID card
        # - 1: passport
        # - 2: student ID
        # - 3: military ID
        # - 4: Home Return Permit
        # - 5: Taiwan Compatriot Permit
        # - 6: Hong Kong and Macau Travel Permit
        # - 7: international seafarer certificate
        # - 8: foreigner permanent residence permit
        # - 10: police officer certificate
        # - 11: soldier certificate
        # - 12: Taiwan Travel Permit
        # - 13: Taiwan Entry Permit
        # - 14: household register
        # - 15: birth certificate
        # - 16: driver license
        # - 17: Hong Kong and Macau resident residence permit
        # - 18: Taiwan resident residence permit.
        self.credential_type = credential_type
        # The expiration date of the credential.
        self.expire_date = expire_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_issue_place is not None:
            result['cert_issue_place'] = self.cert_issue_place

        if self.credential_num is not None:
            result['credential_num'] = self.credential_num

        if self.credential_type is not None:
            result['credential_type'] = self.credential_type

        if self.expire_date is not None:
            result['expire_date'] = self.expire_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert_issue_place') is not None:
            self.cert_issue_place = m.get('cert_issue_place')

        if m.get('credential_num') is not None:
            self.credential_num = m.get('credential_num')

        if m.get('credential_type') is not None:
            self.credential_type = m.get('credential_type')

        if m.get('expire_date') is not None:
            self.expire_date = m.get('expire_date')

        return self

class BookRequestPassengerAncillaryPurchaseMapListBookAncillaryReqItem(DaraModel):
    def __init__(
        self,
        ancillary_id: str = None,
        ancillary_type: int = None,
    ):
        # The ancillary product ID.
        self.ancillary_id = ancillary_id
        # The ancillary product type. Currently supported value: 4 (paid baggage). More types will be supported in the future.
        self.ancillary_type = ancillary_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ancillary_id is not None:
            result['ancillary_id'] = self.ancillary_id

        if self.ancillary_type is not None:
            result['ancillary_type'] = self.ancillary_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ancillary_id') is not None:
            self.ancillary_id = m.get('ancillary_id')

        if m.get('ancillary_type') is not None:
            self.ancillary_type = m.get('ancillary_type')

        return self

class BookRequestContact(DaraModel):
    def __init__(
        self,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
        mobile_country_code: str = None,
        mobile_phone_num: str = None,
    ):
        # The email address.
        self.email = email
        # The first name.
        self.first_name = first_name
        # The last name.
        self.last_name = last_name
        # The country calling code.
        self.mobile_country_code = mobile_country_code
        # The mobile phone number.
        self.mobile_phone_num = mobile_phone_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['email'] = self.email

        if self.first_name is not None:
            result['first_name'] = self.first_name

        if self.last_name is not None:
            result['last_name'] = self.last_name

        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code

        if self.mobile_phone_num is not None:
            result['mobile_phone_num'] = self.mobile_phone_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')

        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')

        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')

        if m.get('mobile_phone_num') is not None:
            self.mobile_phone_num = m.get('mobile_phone_num')

        return self

