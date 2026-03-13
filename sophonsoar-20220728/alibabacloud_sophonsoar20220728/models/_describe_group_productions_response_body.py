# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribeGroupProductionsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeGroupProductionsResponseBodyData] = None,
        page: main_models.DescribeGroupProductionsResponseBodyPage = None,
        request_id: str = None,
    ):
        # The information about the groups.
        self.data = data
        # The pagination information.
        self.page = page
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeGroupProductionsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            temp_model = main_models.DescribeGroupProductionsResponseBodyPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeGroupProductionsResponseBodyPage(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeGroupProductionsResponseBodyData(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        productions: List[main_models.DescribeGroupProductionsResponseBodyDataProductions] = None,
    ):
        # The name of the cloud service.
        self.group_name = group_name
        # The information about the cloud services.
        self.productions = productions

    def validate(self):
        if self.productions:
            for v1 in self.productions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        result['Productions'] = []
        if self.productions is not None:
            for k1 in self.productions:
                result['Productions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        self.productions = []
        if m.get('Productions') is not None:
            for k1 in m.get('Productions'):
                temp_model = main_models.DescribeGroupProductionsResponseBodyDataProductions()
                self.productions.append(temp_model.from_map(k1))

        return self

class DescribeGroupProductionsResponseBodyDataProductions(DaraModel):
    def __init__(
        self,
        code: str = None,
        default_domain: str = None,
        default_version: str = None,
        description: str = None,
        full_domains: List[str] = None,
        group: str = None,
        name: str = None,
        policy_list: List[main_models.DescribeGroupProductionsResponseBodyDataProductionsPolicyList] = None,
        ram_code: str = None,
        short_name: str = None,
        source: str = None,
        versions: List[str] = None,
    ):
        # The code of the cloud service.
        self.code = code
        # The default requested domain name.
        self.default_domain = default_domain
        # The default version.
        self.default_version = default_version
        # The description of the cloud service.
        self.description = description
        # The requested domain names.
        self.full_domains = full_domains
        # The name of the group.
        self.group = group
        # The name of the cloud service.
        self.name = name
        # The RAM policies of the cloud service.
        self.policy_list = policy_list
        # The Resource Access Management (RAM) code of the POP to which the resource belongs.
        self.ram_code = ram_code
        # The short name of the cloud service.
        self.short_name = short_name
        # The information source of the cloud service.
        self.source = source
        # The API versions.
        self.versions = versions

    def validate(self):
        if self.policy_list:
            for v1 in self.policy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain

        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version

        if self.description is not None:
            result['Description'] = self.description

        if self.full_domains is not None:
            result['FullDomains'] = self.full_domains

        if self.group is not None:
            result['Group'] = self.group

        if self.name is not None:
            result['Name'] = self.name

        result['PolicyList'] = []
        if self.policy_list is not None:
            for k1 in self.policy_list:
                result['PolicyList'].append(k1.to_map() if k1 else None)

        if self.ram_code is not None:
            result['RamCode'] = self.ram_code

        if self.short_name is not None:
            result['ShortName'] = self.short_name

        if self.source is not None:
            result['Source'] = self.source

        if self.versions is not None:
            result['Versions'] = self.versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')

        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FullDomains') is not None:
            self.full_domains = m.get('FullDomains')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.policy_list = []
        if m.get('PolicyList') is not None:
            for k1 in m.get('PolicyList'):
                temp_model = main_models.DescribeGroupProductionsResponseBodyDataProductionsPolicyList()
                self.policy_list.append(temp_model.from_map(k1))

        if m.get('RamCode') is not None:
            self.ram_code = m.get('RamCode')

        if m.get('ShortName') is not None:
            self.short_name = m.get('ShortName')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Versions') is not None:
            self.versions = m.get('Versions')

        return self

class DescribeGroupProductionsResponseBodyDataProductionsPolicyList(DaraModel):
    def __init__(
        self,
        policy_name: str = None,
        type: str = None,
    ):
        # The name of the RAM policy.
        self.policy_name = policy_name
        # The type of the RAM policy. Valid values:
        # 
        # *   **All**: permissions.
        # *   **Read-only**: permissions.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

