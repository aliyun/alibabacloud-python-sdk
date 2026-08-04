# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class GetIdentityRegistrationByCustomerResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetIdentityRegistrationByCustomerResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.GetIdentityRegistrationByCustomerResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetIdentityRegistrationByCustomerResponseBodyData(DaraModel):
    def __init__(
        self,
        account_type: int = None,
        application_id: int = None,
        apply_status: str = None,
        audit_code: str = None,
        customer_id: int = None,
        doc_back_pic: str = None,
        doc_front_pic: str = None,
        doc_num: str = None,
        doc_type: str = None,
        email: str = None,
        full_name: str = None,
        registered_address: str = None,
        registered_country: str = None,
        registered_num: str = None,
        tel: str = None,
    ):
        self.account_type = account_type
        self.application_id = application_id
        self.apply_status = apply_status
        self.audit_code = audit_code
        self.customer_id = customer_id
        self.doc_back_pic = doc_back_pic
        self.doc_front_pic = doc_front_pic
        self.doc_num = doc_num
        self.doc_type = doc_type
        self.email = email
        self.full_name = full_name
        self.registered_address = registered_address
        self.registered_country = registered_country
        self.registered_num = registered_num
        self.tel = tel

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.apply_status is not None:
            result['ApplyStatus'] = self.apply_status

        if self.audit_code is not None:
            result['AuditCode'] = self.audit_code

        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id

        if self.doc_back_pic is not None:
            result['DocBackPic'] = self.doc_back_pic

        if self.doc_front_pic is not None:
            result['DocFrontPic'] = self.doc_front_pic

        if self.doc_num is not None:
            result['DocNum'] = self.doc_num

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.email is not None:
            result['Email'] = self.email

        if self.full_name is not None:
            result['FullName'] = self.full_name

        if self.registered_address is not None:
            result['RegisteredAddress'] = self.registered_address

        if self.registered_country is not None:
            result['RegisteredCountry'] = self.registered_country

        if self.registered_num is not None:
            result['RegisteredNum'] = self.registered_num

        if self.tel is not None:
            result['Tel'] = self.tel

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplyStatus') is not None:
            self.apply_status = m.get('ApplyStatus')

        if m.get('AuditCode') is not None:
            self.audit_code = m.get('AuditCode')

        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')

        if m.get('DocBackPic') is not None:
            self.doc_back_pic = m.get('DocBackPic')

        if m.get('DocFrontPic') is not None:
            self.doc_front_pic = m.get('DocFrontPic')

        if m.get('DocNum') is not None:
            self.doc_num = m.get('DocNum')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')

        if m.get('RegisteredAddress') is not None:
            self.registered_address = m.get('RegisteredAddress')

        if m.get('RegisteredCountry') is not None:
            self.registered_country = m.get('RegisteredCountry')

        if m.get('RegisteredNum') is not None:
            self.registered_num = m.get('RegisteredNum')

        if m.get('Tel') is not None:
            self.tel = m.get('Tel')

        return self

