# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryDomainByDomainNameResponseBody(DaraModel):
    def __init__(
        self,
        dns_list: main_models.QueryDomainByDomainNameResponseBodyDnsList = None,
        domain_group_id: int = None,
        domain_group_name: str = None,
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
        tag: main_models.QueryDomainByDomainNameResponseBodyTag = None,
        transfer_out_status: str = None,
        transfer_prohibition_lock: str = None,
        update_prohibition_lock: str = None,
        user_id: str = None,
        zh_registrant_name: str = None,
        zh_registrant_organization: str = None,
    ):
        # The Domain Name System (DNS) servers of the domain name.
        self.dns_list = dns_list
        # The ID of the domain name group. You can call the [QueryDomainGroupList](https://help.aliyun.com/document_detail/69362.html) operation to query the ID of the domain name group.
        self.domain_group_id = domain_group_id
        # The name of the domain name group.
        self.domain_group_name = domain_group_name
        # The domain name.
        self.domain_name = domain_name
        # Indicates whether privacy protection is enabled for the domain name.
        self.domain_name_proxy_service = domain_name_proxy_service
        # The status of name auditing for the domain name. Valid values:
        # 
        # *   **NONAUDIT**: The name auditing for the domain name is not performed.
        # *   **SUCCEED**: The name auditing for the domain name is successful.
        # *   **FAILED**: The name auditing for the domain name fails.
        # *   **AUDITING**: The name auditing for the domain name is in progress.
        self.domain_name_verification_status = domain_name_verification_status
        # The status of the domain name. Valid values:
        # 
        # *   1: The domain name needs to be renewed.
        # *   2: The domain name needs to be redeemed.
        # *   3: The domain name is normal.
        self.domain_status = domain_status
        # The type of the domain name. Valid values:
        # 
        # *   New gTLD
        # *   gTLD
        # *   ccTLD
        self.domain_type = domain_type
        # The email address of the domain name registrant.
        self.email = email
        # Indicates whether the domain name is in the ClientHold state.
        self.email_verification_client_hold = email_verification_client_hold
        # Indicates whether the email address passes verification. Valid values:
        # 
        # *   **0**: The email address fails the verification.
        # *   **1**: The email address passes the verification.
        self.email_verification_status = email_verification_status
        # The number of days from the expiration date of the domain name to the current date.
        self.expiration_curr_date_diff = expiration_curr_date_diff
        # The expiration date.
        self.expiration_date = expiration_date
        # The timestamp generated when the domain name expired.
        self.expiration_date_long = expiration_date_long
        # Indicates whether the domain name expires. Valid values:
        # 
        # *   **1**: The domain name does not expire.
        # *   **2**: The domain name expires.
        self.expiration_date_status = expiration_date_status
        # The instance ID of the domain name.
        self.instance_id = instance_id
        # Indicates whether the domain name is a premium domain name.
        self.premium = premium
        # The status of real-name verification for the domain name. Valid values:
        # 
        # *   **NONAUDIT**: The real-name verification is not performed.
        # *   **SUCCEED**: The real-name verification is successful.
        # *   **FAILED**: The real-name verification fails.
        # *   **AUDITING**: The real-name verification is in progress.
        self.real_name_status = real_name_status
        # The name of the contact.
        self.registrant_name = registrant_name
        # The registrant of the domain name.
        self.registrant_organization = registrant_organization
        # The type of contact who registers the domain name. Valid values:
        # 
        # *   **1**: individual.
        # *   **2**: enterprise.
        self.registrant_type = registrant_type
        # The status of the information about the domain name registrant. Valid values:
        # 
        # *   **PENDING**: The information about the domain name registrant is being modified.
        # *   **NORMAL**: normal.
        self.registrant_updating_status = registrant_updating_status
        # The time when the domain name was registered.
        self.registration_date = registration_date
        # The timestamp generated when the domain name was registered.
        self.registration_date_long = registration_date_long
        # The remarks on the domain name.
        self.remark = remark
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tag = tag
        # The transfer status of the domain name. Valid values:
        # 
        # *   **NORMAL**: The domain name is normal.
        # *   **PENDING**: The domain name is being transferred out from Alibaba Cloud.
        self.transfer_out_status = transfer_out_status
        # The status of the transfer lock for the domain name. Valid values:
        # 
        # *   **NONE_SETTING**: No transfer lock is configured.
        # *   **OPEN**: The transfer lock is enabled.
        # *   **CLOSE**: The transfer lock is disabled.
        self.transfer_prohibition_lock = transfer_prohibition_lock
        # The status of the security lock for the domain name. Valid values:
        # 
        # *   **NONE_SETTING**: No security lock is configured.
        # *   **OPEN**: The security lock is enabled.
        # *   **CLOSE**: The security lock is disabled.
        self.update_prohibition_lock = update_prohibition_lock
        # The user ID.
        self.user_id = user_id
        # The Chinese name of the domain name contact.
        self.zh_registrant_name = zh_registrant_name
        # The Chinese name of the domain name registrant.
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
            temp_model = main_models.QueryDomainByDomainNameResponseBodyDnsList()
            self.dns_list = temp_model.from_map(m.get('DnsList'))

        if m.get('DomainGroupId') is not None:
            self.domain_group_id = m.get('DomainGroupId')

        if m.get('DomainGroupName') is not None:
            self.domain_group_name = m.get('DomainGroupName')

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
            temp_model = main_models.QueryDomainByDomainNameResponseBodyTag()
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

class QueryDomainByDomainNameResponseBodyTag(DaraModel):
    def __init__(
        self,
        tag: List[main_models.QueryDomainByDomainNameResponseBodyTagTag] = None,
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
                temp_model = main_models.QueryDomainByDomainNameResponseBodyTagTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class QueryDomainByDomainNameResponseBodyTagTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        vaue: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.vaue = vaue

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.vaue is not None:
            result['Vaue'] = self.vaue

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Vaue') is not None:
            self.vaue = m.get('Vaue')

        return self

class QueryDomainByDomainNameResponseBodyDnsList(DaraModel):
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

