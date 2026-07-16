# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeCommandsRequest(DaraModel):
    def __init__(
        self,
        command_id: str = None,
        content_encoding: str = None,
        description: str = None,
        latest: bool = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        provider: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.DescribeCommandsRequestTag] = None,
        type: str = None,
    ):
        # The ID of the command.
        self.command_id = command_id
        # The encoding format for the `CommandContent` and `Output` values in the response. Valid values:
        # 
        # - PlainText: returns the raw script content and output.
        # 
        # - Base64: returns the Base64-encoded script content and output.
        # 
        # Default value: Base64.
        self.content_encoding = content_encoding
        # The description of the command.
        # 
        # - If you specify the `Provider` parameter to query public commands, fuzzy search is supported by default.
        # 
        # - If you do not specify the `Provider` parameter to query private commands, fuzzy search is supported. You can use an asterisk (\\*) as a wildcard. For example, `test*` returns all commands whose descriptions start with `test`, `*test` returns all commands whose descriptions end with `test`, and `*test*` returns all commands whose descriptions contain `test`.
        self.description = description
        # Specifies whether to return only the latest version of public commands. This parameter does not affect private commands.
        # 
        # - true: returns only the latest version of public commands.
        # 
        # - false: returns all versions of public commands.
        # 
        # Default value: false.
        self.latest = latest
        # The maximum number of entries to return per page.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The name of the command.
        # 
        # - If you specify the `Provider` parameter to query public commands, fuzzy search is supported by default.
        # 
        # - If you do not specify the `Provider` parameter to query private commands, fuzzy search is supported. You can use an asterisk (\\*) as a wildcard. For example, `command*` returns all commands whose names start with `command`, `*command` returns all commands whose names end with `command`, and `*command*` returns all commands whose names contain `command`.
        self.name = name
        # The pagination token for the next page of results. To retrieve the next page, set this parameter to the `NextToken` value from a previous call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # > This parameter is being deprecated. We recommend using NextToken and MaxResults for pagination instead.
        self.page_number = page_number
        # > This parameter is being deprecated. We recommend using NextToken and MaxResults for pagination instead.
        self.page_size = page_size
        # The provider of the public command.
        # 
        # - If you omit this parameter, the operation queries your private commands by default.
        # 
        # - Set this parameter to `AlibabaCloud` to query all public commands from Alibaba Cloud.
        # 
        # - If you set the value to a specific provider, the public commands from that provider are queried. For example:
        # 
        #   - If you set `Provider` to `AlibabaCloud.ECS.GuestOS`, the public commands provided by AlibabaCloud.ECS.GuestOS are queried.
        # 
        #   - If you set `Provider` to `AlibabaCloud.ECS.GuestOSDiagnose`, the public commands provided by AlibabaCloud.ECS.GuestOSDiagnose are queried.
        self.provider = provider
        # The ID of the region. To view the latest list of regions, call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the command belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags used to filter commands.
        self.tag = tag
        # The type of the command. Valid values:
        # 
        # - RunBatScript: A Bat script for Windows instances.
        # 
        # - RunPowerShellScript: A PowerShell script for Windows instances.
        # 
        # - RunShellScript: A Shell script for Linux instances.
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

        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding

        if self.description is not None:
            result['Description'] = self.description

        if self.latest is not None:
            result['Latest'] = self.latest

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

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

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

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

        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Latest') is not None:
            self.latest = m.get('Latest')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

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

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

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
        # The key of the tag. You can specify up to 20 tags. The tag key cannot be an empty string.
        # 
        # A query can return a maximum of 1,000 resources that match the specified tags. If more than 1,000 resources match, call the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation to query all matching resources.
        # 
        # The key can be up to 64 characters in length, cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The value of the tag. You can specify up to 20 tags. The tag value can be an empty string.
        # 
        # The value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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

