# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeVulWhitelistResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vul_whitelists: List[main_models.DescribeVulWhitelistResponseBodyVulWhitelists] = None,
    ):
        # The number of entries on the current page in paging.
        self.count = count
        # The page number of the current page in paging.
        self.current_page = current_page
        # The number of entries per page in paging.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count
        # The list of whitelisted vulnerabilities.
        self.vul_whitelists = vul_whitelists

    def validate(self):
        if self.vul_whitelists:
            for v1 in self.vul_whitelists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VulWhitelists'] = []
        if self.vul_whitelists is not None:
            for k1 in self.vul_whitelists:
                result['VulWhitelists'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vul_whitelists = []
        if m.get('VulWhitelists') is not None:
            for k1 in m.get('VulWhitelists'):
                temp_model = main_models.DescribeVulWhitelistResponseBodyVulWhitelists()
                self.vul_whitelists.append(temp_model.from_map(k1))

        return self

class DescribeVulWhitelistResponseBodyVulWhitelists(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        id: str = None,
        name: str = None,
        reason: str = None,
        target_info: str = None,
        type: str = None,
        whitelist: str = None,
    ):
        # The alias of the vulnerability.
        self.alias_name = alias_name
        # The rule ID.
        self.id = id
        # The name of the vulnerability.
        self.name = name
        # The reason for adding the vulnerability to the whitelist.
        self.reason = reason
        # The scope of the rule. The value is a JSON string that contains the following fields:
        # 
        # - **type**: The applicable type. Valid values:
        # 
        #      - **Uuid**: host
        #      - **GroupId**: group
        # 
        # - **groupIds**: The IDs of the applicable asset groups.
        # - **uuids**: The UUIDs of the applicable assets.
        # 
        # > If this value is empty, the rule applies to all assets.
        self.target_info = target_info
        # The vulnerability type.
        self.type = type
        # The vulnerability information. The value is in JSON format.
        # 
        # - **name**: The name of the vulnerability.
        # - **type**: The type of the vulnerability.
        # - **aliasName**: The alias of the vulnerability.
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.target_info is not None:
            result['TargetInfo'] = self.target_info

        if self.type is not None:
            result['Type'] = self.type

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('TargetInfo') is not None:
            self.target_info = m.get('TargetInfo')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

