# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class CreateCommandRequest(DaraModel):
    def __init__(
        self,
        command_content: str = None,
        description: str = None,
        enable_parameter: bool = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[main_models.CreateCommandRequestTag] = None,
        timeout: int = None,
        type: str = None,
        working_dir: str = None,
    ):
        # The content of the command. Take note of the following items:
        # 
        # - If you set the EnableParameter parameter to true, you can use custom parameters in the command content.
        # - Custom parameters are enclosed in braces ({{}}). Spaces and line breaks before and after the parameter names within the braces are ignored.
        # - You can specify a maximum of 20 custom parameters.
        # - A custom parameter name can contain only letters, digits, hyphens (-), and underscores (_). Parameter names are not case-sensitive.
        # - A custom parameter name cannot exceed 64 bytes in length.
        # 
        # This parameter is required.
        self.command_content = command_content
        # The description of the command. All characters are supported. The description cannot exceed 512 characters in length.
        self.description = description
        # Specifies whether the created command uses custom parameters.
        # 
        # Default value: false.
        self.enable_parameter = enable_parameter
        # The name of the command. All characters are supported. The name cannot exceed 128 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The region ID. You can call [ListRegions](https://help.aliyun.com/document_detail/189315.html) to query available regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The list of tags. You can specify up to 20 tags.
        self.tag = tag
        # The timeout period for running the command on the instance, in seconds.
        # 
        # If the task that runs the command times out, Cloud Assistant forcibly terminates the task process. Valid values: 10 to 86400 (24 hours).
        # 
        # Default value: 60.
        self.timeout = timeout
        # The language type of the command. Valid values:
        # 
        # - RunBatScript: bat commands for Windows instances
        # - RunPowerShellScript: PowerShell commands for Windows instances
        # - RunShellScript: shell commands for Linux instances
        # 
        # This parameter is required.
        self.type = type
        # The directory in which the created command is run on the ECS instance.
        # 
        # Default value: 
        # - Linux instances: the home directory of the root user, which is /root.  
        # - Windows instances: the directory where the Cloud Assistant client process is located, such as C:\\Windows\\System32.
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
        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

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
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

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
        # The key of tag N that is added to the command. Valid values of N: 1 to 20.
        # 
        # The tag key cannot be an empty string. The tag key can be up to 64 characters in length, and cannot start with aliyun or acs:, or contain http:// or https://.
        self.key = key
        # The value of tag N that is added to the command. Valid values of N: 1 to 20.
        # 
        # The tag value can be an empty string. The tag value can be up to 64 characters in length, and cannot contain http:// or https://.
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

