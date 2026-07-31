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
        # The command ID.
        self.command_id = command_id
        # The encoding mode of the CommandContent and Output fields in the response. Valid values:
        # - PlainText: returns the original script content and output.
        # - Base64: returns Base64-encoded script content and output.
        # 
        # Default value: Base64.
        self.content_encoding = content_encoding
        # The description of the command.
        # 
        # - If the Provider parameter is specified parameter query public commands, fuzzy match is supported by default.
        # 
        # - If the Provider parameter is not specified parameter query private commands, fuzzy match is supported. For example, enter `test*` to search for all commands whose descriptions start with `test`, enter `*test` to search for all commands whose descriptions end with `test`, or enter `*test*` to search for all commands whose descriptions contain `test`.
        self.description = description
        # Specifies whether to query only the latest version of public commands when the query results include public commands. This parameter does not affect the query of private commands.
        # 
        # - true: queries only the latest version of public commands.
        # 
        # - false: queries all versions of public commands.
        # 
        # Default value: false.
        self.latest = latest
        # The maximum number of entries per page for paging queries.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The name of the command.
        # 
        # - If the Provider parameter is specified parameter query public commands, fuzzy match is supported by default.
        # 
        # - If the Provider parameter is not specified parameter query private commands, fuzzy match is supported. For example, enter `command*` to search for all commands whose names start with `command`, enter `*command` to search for all commands whose names end with `command`, or enter `*command*` to search for all commands whose names contain `command`.
        self.name = name
        # The pagination token. Set this parameter to the NextToken value returned in the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # > This parameter is about to be deprecated. Use NextToken and MaxResults to perform paging queries.
        self.page_number = page_number
        # > This parameter is about to be deprecated. Use NextToken and MaxResults to perform paging queries.
        self.page_size = page_size
        # The provider of the public command. Valid values:
        # 
        # - If you do not specify this parameter, all Cloud Assistant commands that you manually created are queried by default.
        # - If you set this parameter to `AlibabaCloud`, all public commands provided by Alibaba Cloud are queried.
        # - If you set this parameter to a specific public command provider, all public commands provided by the provider are queried. Examples:
        #     - If you set Provider to `AlibabaCloud.ECS.GuestOS`, all public commands provided by `AlibabaCloud.ECS.GuestOS` are queried.
        #     - If you set Provider to `AlibabaCloud.ECS.GuestOSDiagnose`, all public commands provided by `AlibabaCloud.ECS.GuestOSDiagnose` are queried.
        self.provider = provider
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the command belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags.
        self.tag = tag
        # The type of the command. Valid values: 
        # 
        # - RunBatScript: Bat script that runs on Windows instances.
        # - RunPowerShellScript: PowerShell script that runs on Windows instances.
        # - RunShellScript: shell script that runs on Linux instances.
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
        # The tag key of the command. Valid values of N: 1 to 20. The tag key cannot be an empty string.
        # 
        # If you use a single tag to filter resources, the resource count with the tag cannot exceed 1,000. If you use multiple tags to filter resources, the resource count with all the specified tags attached cannot exceed 1,000. If the resource count exceeds 1,000, use the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation to query resources.
        # 
        # The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the command. Valid values of N: 1 to 20. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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

