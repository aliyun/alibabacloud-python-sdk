# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateCommandRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        command_content: str = None,
        content_encoding: str = None,
        description: str = None,
        enable_parameter: bool = None,
        launcher: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateCommandRequestTag] = None,
        timeout: int = None,
        type: str = None,
        working_dir: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. **ClientToken** supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The Base64-encoded content of the command.
        # 
        # - The value of this parameter must be Base64-encoded, and the script content cannot exceed 18 KB in size after Base64 encoding.
        # - The command content supports custom parameters. To enable the custom parameter feature, set `EnableParameter=true`:
        #     - Custom parameters are defined by enclosing them in `{{}}`. Spaces and line breaks before and after the parameter name within `{{}}` are ignored.
        #     - The number of custom parameters cannot exceed 20.
        #     - Custom parameter names can contain letters (a-z, A-Z), digits (0-9), hyphens (-), and underscores (_). The acs:: prefix for specifying non-built-in environment parameters is not supported. Other characters are not supported. Parameter names are case-insensitive.
        #     - Each parameter name cannot exceed 64 bytes in length.
        # 
        # - You can specify built-in environment parameters as custom parameters. When the command is run, Cloud Assistant automatically replaces them with the corresponding values from the environment without requiring manual assignment. The following built-in environment parameters are supported:
        #     - `{{ACS::RegionId}}`: the region ID.
        #     - `{{ACS::AccountId}}`: the UID of the Alibaba Cloud account.
        #     - `{{ACS::InstanceId}}`: the instance ID. When a command is sent to multiple instances and you want to use `{{ACS::InstanceId}}` as a built-in environment parameter, make sure that the Cloud Assistant Agent version is not earlier than:
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        #     - `{{ACS::InstanceName}}`: the instance name. When a command is sent to multiple instances and you want to use `{{ACS::InstanceName}}` as a built-in environment parameter, make sure that the Cloud Assistant Agent version is not earlier than:
        #         - Linux: 2.2.3.344
        #         - Windows: 2.1.3.344
        # 
        #     - `{{ACS::InvokeId}}`: the command execution ID. To use `{{ACS::InvokeId}}` as a built-in environment parameter, make sure that the Cloud Assistant Agent version is not earlier than:
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309
        #      
        #     - `{{ACS::CommandId}}`: the command ID. When you run a command by calling the [RunCommand](https://help.aliyun.com/document_detail/141751.html) operation and want to use `{{ACS::CommandId}}` as a built-in environment parameter, make sure that the Cloud Assistant Agent version is not earlier than:
        #         - Linux: 2.2.3.309
        #         - Windows: 2.1.3.309.
        # 
        # This parameter is required.
        self.command_content = command_content
        # The encoding mode of the command content (CommandContent). Valid values:
        # 
        # - PlainText: no encoding. The content is transmitted in plaintext.
        # 
        # - Base64: Base64 encoding.
        # 
        # Default value: Base64.
        # 
        # > If an invalid value is specified, it is treated as Base64.
        self.content_encoding = content_encoding
        # The command description. All character sets are supported. The description cannot exceed 512 characters in length.
        self.description = description
        # Specifies whether the command uses custom parameters.
        # 
        # Default value: false.
        self.enable_parameter = enable_parameter
        # The bootstrap program for script execution. The value cannot exceed 1 KB in length.
        self.launcher = launcher
        # The command name. All character sets are supported. The name cannot exceed 128 characters in length.
        # 
        # This parameter is required.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the command belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of tags.
        self.tag = tag
        # The maximum timeout period for the command to run on the ECS instance. Unit: seconds. If the command cannot be run for any reason, a timeout occurs. After the timeout, the command process is forcefully terminated by canceling the PID of the command.
        # 
        # Default value: 60.
        self.timeout = timeout
        # The type of the command. Valid values: 
        # 
        # - RunBatScript: creates a Bat script to run on Windows instances.
        # - RunPowerShellScript: creates a PowerShell script to run on Windows instances.
        # - RunShellScript: creates a Shell script to run on Linux instances.
        # 
        # This parameter is required.
        self.type = type
        # The directory where the command is run on the ECS instance. The value cannot exceed 200 characters in length.
        # 
        # Default value: 
        # - Linux instances: the home directory of the root user, which is `/root`.  
        # - Windows instances: the directory where the Cloud Assistant Agent process is located, such as `C:\\Windows\\System32`.
        # 
        # > If you set this parameter to a different directory, make sure that the directory exists on the instance.
        self.working_dir = working_dir

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter

        if self.launcher is not None:
            result['Launcher'] = self.launcher

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

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

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.type is not None:
            result['Type'] = self.type

        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')

        if m.get('Launcher') is not None:
            self.launcher = m.get('Launcher')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

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
                temp_model = main_models.CreateCommandRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

class CreateCommandRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the command. Valid values of N: 1 to 20. The tag key cannot be an empty string.
        # 
        # If you use a single tag to filter resources, the resource count with the specified tag cannot exceed 1,000. If you use multiple tags to filter resources, the resource count of resources that have all specified tags attached cannot exceed 1,000. If the resource count exceeds 1,000, use the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation to query resources.
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

