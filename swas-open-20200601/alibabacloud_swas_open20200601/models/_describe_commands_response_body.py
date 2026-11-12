# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class DescribeCommandsResponseBody(DaraModel):
    def __init__(
        self,
        commands: List[main_models.DescribeCommandsResponseBodyCommands] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The commands.
        self.commands = commands
        # The page number of the command list.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of commands.
        self.total_count = total_count

    def validate(self):
        if self.commands:
            for v1 in self.commands:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Commands'] = []
        if self.commands is not None:
            for k1 in self.commands:
                result['Commands'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commands = []
        if m.get('Commands') is not None:
            for k1 in m.get('Commands'):
                temp_model = main_models.DescribeCommandsResponseBodyCommands()
                self.commands.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCommandsResponseBodyCommands(DaraModel):
    def __init__(
        self,
        command_content: str = None,
        command_id: str = None,
        creation_time: str = None,
        description: str = None,
        enable_parameter: bool = None,
        name: str = None,
        parameter_definitions: List[main_models.DescribeCommandsResponseBodyCommandsParameterDefinitions] = None,
        parameter_names: List[str] = None,
        provider: str = None,
        resource_group_id: str = None,
        tags: List[main_models.DescribeCommandsResponseBodyCommandsTags] = None,
        timeout: int = None,
        type: str = None,
        working_dir: str = None,
    ):
        # The command content.
        self.command_content = command_content
        # The command ID.
        self.command_id = command_id
        # The time when the command was created. The time is displayed in UTC (Z) in the YYYY-MM-DDThh:mm:ssZ format.
        self.creation_time = creation_time
        # The command description.
        self.description = description
        # Indicates whether custom parameters are enabled for the command.
        self.enable_parameter = enable_parameter
        # The command name.
        self.name = name
        # The list of custom parameter details.
        self.parameter_definitions = parameter_definitions
        # The list of custom parameter names parsed from CommandContent when the command was created. The list is returned in the List format. If the custom parameter feature is not enabled, an empty list is returned.
        self.parameter_names = parameter_names
        # The provider of the command.
        self.provider = provider
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags of the command.
        self.tags = tags
        # The timeout period. Unit: seconds.
        self.timeout = timeout
        # The command type.
        self.type = type
        # The execution path.
        self.working_dir = working_dir

    def validate(self):
        if self.parameter_definitions:
            for v1 in self.parameter_definitions:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_content is not None:
            result['CommandContent'] = self.command_content

        if self.command_id is not None:
            result['CommandId'] = self.command_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter

        if self.name is not None:
            result['Name'] = self.name

        result['ParameterDefinitions'] = []
        if self.parameter_definitions is not None:
            for k1 in self.parameter_definitions:
                result['ParameterDefinitions'].append(k1.to_map() if k1 else None)

        if self.parameter_names is not None:
            result['ParameterNames'] = self.parameter_names

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

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

        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.parameter_definitions = []
        if m.get('ParameterDefinitions') is not None:
            for k1 in m.get('ParameterDefinitions'):
                temp_model = main_models.DescribeCommandsResponseBodyCommandsParameterDefinitions()
                self.parameter_definitions.append(temp_model.from_map(k1))

        if m.get('ParameterNames') is not None:
            self.parameter_names = m.get('ParameterNames')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeCommandsResponseBodyCommandsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

class DescribeCommandsResponseBodyCommandsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the command.
        self.key = key
        # The tag value of the command.
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

class DescribeCommandsResponseBodyCommandsParameterDefinitions(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        parameter_name: str = None,
        possible_values: List[str] = None,
        required: bool = None,
    ):
        # The default value of the custom parameter.
        self.default_value = default_value
        # The description of the custom parameter.
        self.description = description
        # The name of the custom parameter.
        self.parameter_name = parameter_name
        # The possible values of the enumeration-type custom parameter.
        self.possible_values = possible_values
        # Indicates whether the custom parameter is required. Valid values:
        # 
        # - true: Required.
        # 
        # - false: Not required.
        # 
        # Default value: false.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.possible_values is not None:
            result['PossibleValues'] = self.possible_values

        if self.required is not None:
            result['Required'] = self.required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('PossibleValues') is not None:
            self.possible_values = m.get('PossibleValues')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        return self

