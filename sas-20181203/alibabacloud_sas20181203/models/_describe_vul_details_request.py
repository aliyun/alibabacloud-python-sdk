# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVulDetailsRequest(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        lang: str = None,
        name: str = None,
        resource_directory_account_id: int = None,
        type: str = None,
    ):
        # The vulnerability announcement.
        self.alias_name = alias_name
        # The language type for the request and response. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English.
        # 
        # This parameter is required.
        self.lang = lang
        # The vulnerability name.
        # > You can call [DescribeGroupedVul](~~DescribeGroupedVul~~) or [DescribeVulList](~~DescribeVulList~~) to obtain this parameter.
        # 
        # This parameter is required.
        self.name = name
        # The Alibaba Cloud account ID of the member accounts in the resource directory folder.
        # > You can invoke [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The type of vulnerability to query. Valid values:
        # 
        # - **cve**: Linux software vulnerability
        # - **sys**: Windows system vulnerability
        # - **cms**: Web-CMS vulnerability
        # - **app**: application vulnerability
        # - **emg**: emergency vulnerability
        # - **sca**: software constituency parsing vulnerability.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

