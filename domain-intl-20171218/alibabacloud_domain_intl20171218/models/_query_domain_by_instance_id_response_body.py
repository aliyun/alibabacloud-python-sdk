# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain_intl20171218 import models as main_models
from darabonba.model import DaraModel

class QueryDomainByInstanceIdResponseBody(DaraModel):
    def __init__(
        self,
        dns_list: main_models.QueryDomainByInstanceIdResponseBodyDnsList = None,
        domain_name: str = None,
        domain_name_proxy_service: bool = None,
        domain_name_verification_status: str = None,
        email: str = None,
        email_verification_client_hold: bool = None,
        email_verification_status: int = None,
        expiration_date: str = None,
        expiration_date_long: int = None,
        instance_id: str = None,
        premium: bool = None,
        real_name_status: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        registrant_type: str = None,
        registrant_updating_status: str = None,
        registration_date: str = None,
        registration_date_long: int = None,
        request_id: str = None,
        transfer_out_status: str = None,
        transfer_prohibition_lock: str = None,
        update_prohibition_lock: str = None,
        user_id: str = None,
    ):
        self.dns_list = dns_list
        self.domain_name = domain_name
        self.domain_name_proxy_service = domain_name_proxy_service
        self.domain_name_verification_status = domain_name_verification_status
        self.email = email
        self.email_verification_client_hold = email_verification_client_hold
        self.email_verification_status = email_verification_status
        self.expiration_date = expiration_date
        self.expiration_date_long = expiration_date_long
        self.instance_id = instance_id
        self.premium = premium
        self.real_name_status = real_name_status
        self.registrant_name = registrant_name
        self.registrant_organization = registrant_organization
        self.registrant_type = registrant_type
        self.registrant_updating_status = registrant_updating_status
        self.registration_date = registration_date
        self.registration_date_long = registration_date_long
        self.request_id = request_id
        self.transfer_out_status = transfer_out_status
        self.transfer_prohibition_lock = transfer_prohibition_lock
        self.update_prohibition_lock = update_prohibition_lock
        self.user_id = user_id

    def validate(self):
        if self.dns_list:
            self.dns_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_list is not None:
            result['DnsList'] = self.dns_list.to_map()

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_name_proxy_service is not None:
            result['DomainNameProxyService'] = self.domain_name_proxy_service

        if self.domain_name_verification_status is not None:
            result['DomainNameVerificationStatus'] = self.domain_name_verification_status

        if self.email is not None:
            result['Email'] = self.email

        if self.email_verification_client_hold is not None:
            result['EmailVerificationClientHold'] = self.email_verification_client_hold

        if self.email_verification_status is not None:
            result['EmailVerificationStatus'] = self.email_verification_status

        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date

        if self.expiration_date_long is not None:
            result['ExpirationDateLong'] = self.expiration_date_long

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.premium is not None:
            result['Premium'] = self.premium

        if self.real_name_status is not None:
            result['RealNameStatus'] = self.real_name_status

        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name

        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization

        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type

        if self.registrant_updating_status is not None:
            result['RegistrantUpdatingStatus'] = self.registrant_updating_status

        if self.registration_date is not None:
            result['RegistrationDate'] = self.registration_date

        if self.registration_date_long is not None:
            result['RegistrationDateLong'] = self.registration_date_long

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.transfer_out_status is not None:
            result['TransferOutStatus'] = self.transfer_out_status

        if self.transfer_prohibition_lock is not None:
            result['TransferProhibitionLock'] = self.transfer_prohibition_lock

        if self.update_prohibition_lock is not None:
            result['UpdateProhibitionLock'] = self.update_prohibition_lock

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsList') is not None:
            temp_model = main_models.QueryDomainByInstanceIdResponseBodyDnsList()
            self.dns_list = temp_model.from_map(m.get('DnsList'))

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainNameProxyService') is not None:
            self.domain_name_proxy_service = m.get('DomainNameProxyService')

        if m.get('DomainNameVerificationStatus') is not None:
            self.domain_name_verification_status = m.get('DomainNameVerificationStatus')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EmailVerificationClientHold') is not None:
            self.email_verification_client_hold = m.get('EmailVerificationClientHold')

        if m.get('EmailVerificationStatus') is not None:
            self.email_verification_status = m.get('EmailVerificationStatus')

        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')

        if m.get('ExpirationDateLong') is not None:
            self.expiration_date_long = m.get('ExpirationDateLong')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Premium') is not None:
            self.premium = m.get('Premium')

        if m.get('RealNameStatus') is not None:
            self.real_name_status = m.get('RealNameStatus')

        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')

        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')

        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')

        if m.get('RegistrantUpdatingStatus') is not None:
            self.registrant_updating_status = m.get('RegistrantUpdatingStatus')

        if m.get('RegistrationDate') is not None:
            self.registration_date = m.get('RegistrationDate')

        if m.get('RegistrationDateLong') is not None:
            self.registration_date_long = m.get('RegistrationDateLong')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TransferOutStatus') is not None:
            self.transfer_out_status = m.get('TransferOutStatus')

        if m.get('TransferProhibitionLock') is not None:
            self.transfer_prohibition_lock = m.get('TransferProhibitionLock')

        if m.get('UpdateProhibitionLock') is not None:
            self.update_prohibition_lock = m.get('UpdateProhibitionLock')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class QueryDomainByInstanceIdResponseBodyDnsList(DaraModel):
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

