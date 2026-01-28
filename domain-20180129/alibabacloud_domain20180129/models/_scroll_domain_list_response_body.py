# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class ScrollDomainListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ScrollDomainListResponseBodyData = None,
        page_size: int = None,
        request_id: str = None,
        scroll_id: str = None,
        total_item_num: int = None,
    ):
        # The domain names.
        self.data = data
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The scroll ID.
        self.scroll_id = scroll_id
        # The number of remaining domain names to be queried.
        self.total_item_num = total_item_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scroll_id is not None:
            result['ScrollId'] = self.scroll_id

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ScrollDomainListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScrollId') is not None:
            self.scroll_id = m.get('ScrollId')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        return self

class ScrollDomainListResponseBodyData(DaraModel):
    def __init__(
        self,
        domain: List[main_models.ScrollDomainListResponseBodyDataDomain] = None,
    ):
        self.domain = domain

    def validate(self):
        if self.domain:
            for v1 in self.domain:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Domain'] = []
        if self.domain is not None:
            for k1 in self.domain:
                result['Domain'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain = []
        if m.get('Domain') is not None:
            for k1 in m.get('Domain'):
                temp_model = main_models.ScrollDomainListResponseBodyDataDomain()
                self.domain.append(temp_model.from_map(k1))

        return self

class ScrollDomainListResponseBodyDataDomain(DaraModel):
    def __init__(
        self,
        dns_list: main_models.ScrollDomainListResponseBodyDataDomainDnsList = None,
        domain_audit_status: str = None,
        domain_group_id: str = None,
        domain_group_name: str = None,
        domain_name: str = None,
        domain_status: str = None,
        domain_type: str = None,
        email: str = None,
        expiration_curr_date_diff: int = None,
        expiration_date: str = None,
        expiration_date_long: int = None,
        expiration_date_status: str = None,
        instance_id: str = None,
        premium: bool = None,
        product_id: str = None,
        registrant_organization: str = None,
        registrant_type: str = None,
        registration_date: str = None,
        registration_date_long: int = None,
        remark: str = None,
        resource_group_id: str = None,
        tag: main_models.ScrollDomainListResponseBodyDataDomainTag = None,
        zh_registrant_organization: str = None,
    ):
        # The Domain Name System (DNS) servers of the domain name.
        self.dns_list = dns_list
        # The status of real-name verification for the domain name. Valid values:
        # 
        # *   **FAILED**: Real-name verification for the domain name fails.
        # *   **SUCCEED**: Real-name verification for the domain name is successful.
        # *   **NONAUDIT**: Real-name verification for the domain name is not performed.
        # *   **AUDITING**: Real-name verification for the domain name is in progress.
        self.domain_audit_status = domain_audit_status
        # The ID of the domain name group.
        self.domain_group_id = domain_group_id
        # The name of the domain name group.
        self.domain_group_name = domain_group_name
        # The domain name.
        self.domain_name = domain_name
        # The status of the domain name. Valid values:
        # 
        # *   **1**: The domain name needs to be renewed.
        # *   **2**: The domain name needs to be redeemed.
        # *   **3**: The domain name is normal.
        # *   **4**: The domain name is being transferred out.
        # *   **5**: The information about the domain name registrant is being modified.
        # *   **6**: Real-name verification is not performed on the domain name.
        # *   **7**: Real-name verification for the domain name fails.
        # *   **8**: The real-name verification is being reviewed.
        self.domain_status = domain_status
        # The type of the domain name. Valid values:
        # 
        # *   **New gTLD**
        # *   **gTLD**
        # *   **ccTLD**
        self.domain_type = domain_type
        # The email address.
        self.email = email
        # The number of days from the expiration date of the domain name to the current date.
        self.expiration_curr_date_diff = expiration_curr_date_diff
        # The time when the domain name expires.
        self.expiration_date = expiration_date
        # The time when the domain name expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
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
        # The service ID.
        self.product_id = product_id
        # The registrant of the domain name.
        self.registrant_organization = registrant_organization
        # The registration type of the domain name. Valid values:
        # 
        # *   **1**: individual.
        # *   **2**: enterprise.
        self.registrant_type = registrant_type
        # The time when the domain name was registered.
        self.registration_date = registration_date
        # The time when the domain name was registered. This value is a UNIX timestamp that indicates the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.registration_date_long = registration_date_long
        # The remarks on the domain name.
        self.remark = remark
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The resource tag.
        self.tag = tag
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

        if self.domain_audit_status is not None:
            result['DomainAuditStatus'] = self.domain_audit_status

        if self.domain_group_id is not None:
            result['DomainGroupId'] = self.domain_group_id

        if self.domain_group_name is not None:
            result['DomainGroupName'] = self.domain_group_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.email is not None:
            result['Email'] = self.email

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

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization

        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type

        if self.registration_date is not None:
            result['RegistrationDate'] = self.registration_date

        if self.registration_date_long is not None:
            result['RegistrationDateLong'] = self.registration_date_long

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tag is not None:
            result['Tag'] = self.tag.to_map()

        if self.zh_registrant_organization is not None:
            result['ZhRegistrantOrganization'] = self.zh_registrant_organization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsList') is not None:
            temp_model = main_models.ScrollDomainListResponseBodyDataDomainDnsList()
            self.dns_list = temp_model.from_map(m.get('DnsList'))

        if m.get('DomainAuditStatus') is not None:
            self.domain_audit_status = m.get('DomainAuditStatus')

        if m.get('DomainGroupId') is not None:
            self.domain_group_id = m.get('DomainGroupId')

        if m.get('DomainGroupName') is not None:
            self.domain_group_name = m.get('DomainGroupName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('Email') is not None:
            self.email = m.get('Email')

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

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')

        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')

        if m.get('RegistrationDate') is not None:
            self.registration_date = m.get('RegistrationDate')

        if m.get('RegistrationDateLong') is not None:
            self.registration_date_long = m.get('RegistrationDateLong')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tag') is not None:
            temp_model = main_models.ScrollDomainListResponseBodyDataDomainTag()
            self.tag = temp_model.from_map(m.get('Tag'))

        if m.get('ZhRegistrantOrganization') is not None:
            self.zh_registrant_organization = m.get('ZhRegistrantOrganization')

        return self

class ScrollDomainListResponseBodyDataDomainTag(DaraModel):
    def __init__(
        self,
        tag: List[main_models.ScrollDomainListResponseBodyDataDomainTagTag] = None,
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
                temp_model = main_models.ScrollDomainListResponseBodyDataDomainTagTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ScrollDomainListResponseBodyDataDomainTagTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class ScrollDomainListResponseBodyDataDomainDnsList(DaraModel):
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

