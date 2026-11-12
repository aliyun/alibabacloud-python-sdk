# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class DescribeCommandsRequest(DaraModel):
    def __init__(
        self,
        command_id: str = None,
        name: str = None,
        page_number: str = None,
        page_size: str = None,
        provider: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[main_models.DescribeCommandsRequestTag] = None,
        type: str = None,
    ):
        # The command ID.
        self.command_id = command_id
        # The name of the command. Fuzzy match is not supported.
        self.name = name
        # The page number.
        # 
        # Minimum value: 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page for a paged query.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The provider of the public command. Valid values:
        # 
        # - AlibabaCloud: queries all public commands provided by Alibaba Cloud.
        # - User: queries all custom commands that you created.
        # 
        # This parameter is required.
        self.provider = provider
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags of the command.
        self.tag = tag
        # The language type of the command. Valid values:
        # 
        # - RunBatScript: Bat command for Windows instances.
        # - RunPowerShellScript: PowerShell command for Windows instances.
        # - RunShellScript: Shell command for Linux instances.
        self.type = type

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
        if self.command_id is not None:
            result['CommandId'] = self.command_id

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeCommandsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeCommandsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the command. The tag key must be 1 to 64 characters in length. Valid values of N: 1 to 20.
        self.key = key
        # The tag value of the command. The tag value must be 1 to 64 characters in length. Valid values of N: 1 to 20.
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

