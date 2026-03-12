# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20160511 import models as main_models
from darabonba.model import DaraModel

class QueryDomainBySaleIdResponseBody(DaraModel):
    def __init__(
        self,
        chinese_contact_person: str = None,
        chinese_holder: str = None,
        creation_date: str = None,
        dns_list: main_models.QueryDomainBySaleIdResponseBodyDnsList = None,
        domain_name: str = None,
        domain_reg_type: str = None,
        email_verification_client_hold: bool = None,
        email_verification_status: int = None,
        english_contact_person: str = None,
        english_holder: str = None,
        expiration_date: str = None,
        holder_email: str = None,
        premium: bool = None,
        remark: str = None,
        safety_lock: str = None,
        sale_id: str = None,
        transfer_lock: str = None,
        transfer_out_status: str = None,
        user_id: str = None,
        whois_protected: bool = None,
    ):
        self.chinese_contact_person = chinese_contact_person
        self.chinese_holder = chinese_holder
        self.creation_date = creation_date
        self.dns_list = dns_list
        self.domain_name = domain_name
        self.domain_reg_type = domain_reg_type
        self.email_verification_client_hold = email_verification_client_hold
        self.email_verification_status = email_verification_status
        self.english_contact_person = english_contact_person
        self.english_holder = english_holder
        self.expiration_date = expiration_date
        self.holder_email = holder_email
        self.premium = premium
        self.remark = remark
        self.safety_lock = safety_lock
        self.sale_id = sale_id
        self.transfer_lock = transfer_lock
        self.transfer_out_status = transfer_out_status
        self.user_id = user_id
        self.whois_protected = whois_protected

    def validate(self):
        if self.dns_list:
            self.dns_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chinese_contact_person is not None:
            result['ChineseContactPerson'] = self.chinese_contact_person

        if self.chinese_holder is not None:
            result['ChineseHolder'] = self.chinese_holder

        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date

        if self.dns_list is not None:
            result['DnsList'] = self.dns_list.to_map()

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_reg_type is not None:
            result['DomainRegType'] = self.domain_reg_type

        if self.email_verification_client_hold is not None:
            result['EmailVerificationClientHold'] = self.email_verification_client_hold

        if self.email_verification_status is not None:
            result['EmailVerificationStatus'] = self.email_verification_status

        if self.english_contact_person is not None:
            result['EnglishContactPerson'] = self.english_contact_person

        if self.english_holder is not None:
            result['EnglishHolder'] = self.english_holder

        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date

        if self.holder_email is not None:
            result['HolderEmail'] = self.holder_email

        if self.premium is not None:
            result['Premium'] = self.premium

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.safety_lock is not None:
            result['SafetyLock'] = self.safety_lock

        if self.sale_id is not None:
            result['SaleId'] = self.sale_id

        if self.transfer_lock is not None:
            result['TransferLock'] = self.transfer_lock

        if self.transfer_out_status is not None:
            result['TransferOutStatus'] = self.transfer_out_status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.whois_protected is not None:
            result['WhoisProtected'] = self.whois_protected

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChineseContactPerson') is not None:
            self.chinese_contact_person = m.get('ChineseContactPerson')

        if m.get('ChineseHolder') is not None:
            self.chinese_holder = m.get('ChineseHolder')

        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')

        if m.get('DnsList') is not None:
            temp_model = main_models.QueryDomainBySaleIdResponseBodyDnsList()
            self.dns_list = temp_model.from_map(m.get('DnsList'))

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainRegType') is not None:
            self.domain_reg_type = m.get('DomainRegType')

        if m.get('EmailVerificationClientHold') is not None:
            self.email_verification_client_hold = m.get('EmailVerificationClientHold')

        if m.get('EmailVerificationStatus') is not None:
            self.email_verification_status = m.get('EmailVerificationStatus')

        if m.get('EnglishContactPerson') is not None:
            self.english_contact_person = m.get('EnglishContactPerson')

        if m.get('EnglishHolder') is not None:
            self.english_holder = m.get('EnglishHolder')

        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')

        if m.get('HolderEmail') is not None:
            self.holder_email = m.get('HolderEmail')

        if m.get('Premium') is not None:
            self.premium = m.get('Premium')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SafetyLock') is not None:
            self.safety_lock = m.get('SafetyLock')

        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')

        if m.get('TransferLock') is not None:
            self.transfer_lock = m.get('TransferLock')

        if m.get('TransferOutStatus') is not None:
            self.transfer_out_status = m.get('TransferOutStatus')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WhoisProtected') is not None:
            self.whois_protected = m.get('WhoisProtected')

        return self

class QueryDomainBySaleIdResponseBodyDnsList(DaraModel):
    def __init__(
        self,
        dns: List[str] = None,
    ):
        self.dns = dns

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns is not None:
            result['Dns'] = self.dns

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dns') is not None:
            self.dns = m.get('Dns')

        return self

