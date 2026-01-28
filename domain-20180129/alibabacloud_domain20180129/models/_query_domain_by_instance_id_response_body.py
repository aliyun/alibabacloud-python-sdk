# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryDomainByInstanceIdResponseBody(DaraModel):
    def __init__(
        self,
        dns_list: main_models.QueryDomainByInstanceIdResponseBodyDnsList = None,
        domain_group_id: int = None,
        domain_group_name: str = None,
        domain_lifecycle_status: str = None,
        domain_name: str = None,
        domain_name_proxy_service: bool = None,
        domain_name_verification_status: str = None,
        domain_status: str = None,
        domain_type: str = None,
        email: str = None,
        email_verification_client_hold: bool = None,
        email_verification_status: int = None,
        expiration_curr_date_diff: int = None,
        expiration_date: str = None,
        expiration_date_long: int = None,
        expiration_date_status: str = None,
        instance_id: str = None,
        premium: bool = None,
        privacy_service_status: str = None,
        real_name_status: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        registrant_type: str = None,
        registrant_updating_status: str = None,
        registration_date: str = None,
        registration_date_long: int = None,
        remark: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        tag: main_models.QueryDomainByInstanceIdResponseBodyTag = None,
        transfer_out_status: str = None,
        transfer_prohibition_lock: str = None,
        update_prohibition_lock: str = None,
        user_id: str = None,
        zh_registrant_name: str = None,
        zh_registrant_organization: str = None,
    ):
        self.dns_list = dns_list
        self.domain_group_id = domain_group_id
        self.domain_group_name = domain_group_name
        self.domain_lifecycle_status = domain_lifecycle_status
        self.domain_name = domain_name
        self.domain_name_proxy_service = domain_name_proxy_service
        self.domain_name_verification_status = domain_name_verification_status
        self.domain_status = domain_status
        self.domain_type = domain_type
        self.email = email
        self.email_verification_client_hold = email_verification_client_hold
        self.email_verification_status = email_verification_status
        self.expiration_curr_date_diff = expiration_curr_date_diff
        self.expiration_date = expiration_date
        self.expiration_date_long = expiration_date_long
        self.expiration_date_status = expiration_date_status
        self.instance_id = instance_id
        self.premium = premium
        self.privacy_service_status = privacy_service_status
        self.real_name_status = real_name_status
        self.registrant_name = registrant_name
        self.registrant_organization = registrant_organization
        self.registrant_type = registrant_type
        self.registrant_updating_status = registrant_updating_status
        self.registration_date = registration_date
        self.registration_date_long = registration_date_long
        self.remark = remark
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.tag = tag
        self.transfer_out_status = transfer_out_status
        self.transfer_prohibition_lock = transfer_prohibition_lock
        self.update_prohibition_lock = update_prohibition_lock
        self.user_id = user_id
        self.zh_registrant_name = zh_registrant_name
        self.zh_registrant_organization = zh_registrant_organization

    def validate(self):
        if self.dns_list:
            self.dns_list.validate()
        if self.tag:
            self.tag.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_list is not None:
            result['DnsList'] = self.dns_list.to_map()

        if self.domain_group_id is not None:
            result['DomainGroupId'] = self.domain_group_id

        if self.domain_group_name is not None:
            result['DomainGroupName'] = self.domain_group_name

        if self.domain_lifecycle_status is not None:
            result['DomainLifecycleStatus'] = self.domain_lifecycle_status

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_name_proxy_service is not None:
            result['DomainNameProxyService'] = self.domain_name_proxy_service

        if self.domain_name_verification_status is not None:
            result['DomainNameVerificationStatus'] = self.domain_name_verification_status

        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.email is not None:
            result['Email'] = self.email

        if self.email_verification_client_hold is not None:
            result['EmailVerificationClientHold'] = self.email_verification_client_hold

        if self.email_verification_status is not None:
            result['EmailVerificationStatus'] = self.email_verification_status

        if self.expiration_curr_date_diff is not None:
            result['ExpirationCurrDateDiff'] = self.expiration_curr_date_diff

        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date

        if self.expiration_date_long is not None:
            result['ExpirationDateLong'] = self.expiration_date_long

        if self.expiration_date_status is not None:
            result['ExpirationDateStatus'] = self.expiration_date_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.premium is not None:
            result['Premium'] = self.premium

        if self.privacy_service_status is not None:
            result['PrivacyServiceStatus'] = self.privacy_service_status

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

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tag is not None:
            result['Tag'] = self.tag.to_map()

        if self.transfer_out_status is not None:
            result['TransferOutStatus'] = self.transfer_out_status

        if self.transfer_prohibition_lock is not None:
            result['TransferProhibitionLock'] = self.transfer_prohibition_lock

        if self.update_prohibition_lock is not None:
            result['UpdateProhibitionLock'] = self.update_prohibition_lock

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.zh_registrant_name is not None:
            result['ZhRegistrantName'] = self.zh_registrant_name

        if self.zh_registrant_organization is not None:
            result['ZhRegistrantOrganization'] = self.zh_registrant_organization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsList') is not None:
            temp_model = main_models.QueryDomainByInstanceIdResponseBodyDnsList()
            self.dns_list = temp_model.from_map(m.get('DnsList'))

        if m.get('DomainGroupId') is not None:
            self.domain_group_id = m.get('DomainGroupId')

        if m.get('DomainGroupName') is not None:
            self.domain_group_name = m.get('DomainGroupName')

        if m.get('DomainLifecycleStatus') is not None:
            self.domain_lifecycle_status = m.get('DomainLifecycleStatus')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainNameProxyService') is not None:
            self.domain_name_proxy_service = m.get('DomainNameProxyService')

        if m.get('DomainNameVerificationStatus') is not None:
            self.domain_name_verification_status = m.get('DomainNameVerificationStatus')

        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EmailVerificationClientHold') is not None:
            self.email_verification_client_hold = m.get('EmailVerificationClientHold')

        if m.get('EmailVerificationStatus') is not None:
            self.email_verification_status = m.get('EmailVerificationStatus')

        if m.get('ExpirationCurrDateDiff') is not None:
            self.expiration_curr_date_diff = m.get('ExpirationCurrDateDiff')

        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')

        if m.get('ExpirationDateLong') is not None:
            self.expiration_date_long = m.get('ExpirationDateLong')

        if m.get('ExpirationDateStatus') is not None:
            self.expiration_date_status = m.get('ExpirationDateStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Premium') is not None:
            self.premium = m.get('Premium')

        if m.get('PrivacyServiceStatus') is not None:
            self.privacy_service_status = m.get('PrivacyServiceStatus')

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

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tag') is not None:
            temp_model = main_models.QueryDomainByInstanceIdResponseBodyTag()
            self.tag = temp_model.from_map(m.get('Tag'))

        if m.get('TransferOutStatus') is not None:
            self.transfer_out_status = m.get('TransferOutStatus')

        if m.get('TransferProhibitionLock') is not None:
            self.transfer_prohibition_lock = m.get('TransferProhibitionLock')

        if m.get('UpdateProhibitionLock') is not None:
            self.update_prohibition_lock = m.get('UpdateProhibitionLock')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('ZhRegistrantName') is not None:
            self.zh_registrant_name = m.get('ZhRegistrantName')

        if m.get('ZhRegistrantOrganization') is not None:
            self.zh_registrant_organization = m.get('ZhRegistrantOrganization')

        return self

class QueryDomainByInstanceIdResponseBodyTag(DaraModel):
    def __init__(
        self,
        tag: List[main_models.QueryDomainByInstanceIdResponseBodyTagTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.QueryDomainByInstanceIdResponseBodyTagTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class QueryDomainByInstanceIdResponseBodyTagTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

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

