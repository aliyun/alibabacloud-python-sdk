# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryDomainListResponseBody(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: main_models.QueryDomainListResponseBodyData = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        # The page number.
        self.current_page_num = current_page_num
        # The domain names.
        self.data = data
        # Indicates whether the current page is followed by a page.
        self.next_page = next_page
        # The number of entries per page.
        self.page_size = page_size
        # Indicates whether the current page is preceded by a page.
        self.pre_page = pre_page
        # The ID of the request.
        self.request_id = request_id
        # The total number of domain names returned.
        self.total_item_num = total_item_num
        # The total number of pages returned.
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page is not None:
            result['PrePage'] = self.pre_page

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        if m.get('Data') is not None:
            temp_model = main_models.QueryDomainListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class QueryDomainListResponseBodyData(DaraModel):
    def __init__(
        self,
        domain: List[main_models.QueryDomainListResponseBodyDataDomain] = None,
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
                temp_model = main_models.QueryDomainListResponseBodyDataDomain()
                self.domain.append(temp_model.from_map(k1))

        return self

class QueryDomainListResponseBodyDataDomain(DaraModel):
    def __init__(
        self,
        ccompany: str = None,
        chgholder_status: str = None,
        dns_list: main_models.QueryDomainListResponseBodyDataDomainDnsList = None,
        domain_audit_status: str = None,
        domain_group_id: str = None,
        domain_group_name: str = None,
        domain_name: str = None,
        domain_status: str = None,
        domain_type: str = None,
        expiration_curr_date_diff: int = None,
        expiration_date: str = None,
        expiration_date_long: int = None,
        expiration_date_status: str = None,
        instance_id: str = None,
        premium: bool = None,
        product_id: str = None,
        registrant_type: str = None,
        registrar: str = None,
        registration_date: str = None,
        registration_date_long: int = None,
        remark: str = None,
        resource_group_id: str = None,
        tag: main_models.QueryDomainListResponseBodyDataDomainTag = None,
    ):
        # The name of the domain name registrant.
        self.ccompany = ccompany
        # domain transfer status. value:
        # - 0: domain status normal.
        # - 1: domain is pending change holder.
        # - 2: change holder failed.
        self.chgholder_status = chgholder_status
        self.dns_list = dns_list
        # The state of real-name verification for the domain name. Valid values:
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
        # The state of the domain name. Valid values:
        # 
        # *   **1**: The domain name needs to be renewed.
        # *   **2**: The domain name needs to be redeemed.
        # *   **3**: The domain name is normal.
        self.domain_status = domain_status
        # The type of the domain name. Valid values:
        # 
        # *   **New gTLD**
        # *   **gTLD**
        # *   **ccTLD**
        self.domain_type = domain_type
        # The number of days from the expiration date of the domain name to the current date.
        self.expiration_curr_date_diff = expiration_curr_date_diff
        # The time when the domain name expires.
        self.expiration_date = expiration_date
        # The validity period of the domain name. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.expiration_date_long = expiration_date_long
        # Indicates whether the domain name expires. Valid values:
        # 
        # *   **1**: The domain name does not expire.
        # *   **2**: The domain name expires.
        self.expiration_date_status = expiration_date_status
        # The instance ID.
        self.instance_id = instance_id
        # Indicates whether the domain name is a premium domain name.
        self.premium = premium
        # The service ID.
        self.product_id = product_id
        # The registration type of the domain name. Valid values:
        # 
        # *   **1**: individual
        # *   **2**: enterprise
        self.registrant_type = registrant_type
        self.registrar = registrar
        # The time when the domain name was registered.
        self.registration_date = registration_date
        # Indicates how long the domain name has been registered. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.registration_date_long = registration_date_long
        # The remarks of the domain name.
        self.remark = remark
        # The ID of the resource group to which the domain name belongs.
        self.resource_group_id = resource_group_id
        # The tags added to the resource.
        self.tag = tag

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
        if self.ccompany is not None:
            result['Ccompany'] = self.ccompany

        if self.chgholder_status is not None:
            result['ChgholderStatus'] = self.chgholder_status

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

        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type

        if self.registrar is not None:
            result['Registrar'] = self.registrar

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ccompany') is not None:
            self.ccompany = m.get('Ccompany')

        if m.get('ChgholderStatus') is not None:
            self.chgholder_status = m.get('ChgholderStatus')

        if m.get('DnsList') is not None:
            temp_model = main_models.QueryDomainListResponseBodyDataDomainDnsList()
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

        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')

        if m.get('Registrar') is not None:
            self.registrar = m.get('Registrar')

        if m.get('RegistrationDate') is not None:
            self.registration_date = m.get('RegistrationDate')

        if m.get('RegistrationDateLong') is not None:
            self.registration_date_long = m.get('RegistrationDateLong')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tag') is not None:
            temp_model = main_models.QueryDomainListResponseBodyDataDomainTag()
            self.tag = temp_model.from_map(m.get('Tag'))

        return self

class QueryDomainListResponseBodyDataDomainTag(DaraModel):
    def __init__(
        self,
        tag: List[main_models.QueryDomainListResponseBodyDataDomainTagTag] = None,
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
                temp_model = main_models.QueryDomainListResponseBodyDataDomainTagTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class QueryDomainListResponseBodyDataDomainTagTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag added to the resource.
        self.key = key
        # The value of the tag added to the resource.
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

class QueryDomainListResponseBodyDataDomainDnsList(DaraModel):
    def __init__(
        self,
        dns_list: List[str] = None,
    ):
        self.dns_list = dns_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_list is not None:
            result['DnsList'] = self.dns_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsList') is not None:
            self.dns_list = m.get('DnsList')

        return self

