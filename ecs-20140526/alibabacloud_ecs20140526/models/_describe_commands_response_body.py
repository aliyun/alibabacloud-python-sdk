# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeCommandsResponseBody(DaraModel):
    def __init__(
        self,
        commands: main_models.DescribeCommandsResponseBodyCommands = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried commands.
        self.commands = commands
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of commands.
        self.total_count = total_count

    def validate(self):
        if self.commands:
            self.commands.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commands is not None:
            result['Commands'] = self.commands.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        if m.get('Commands') is not None:
            temp_model = main_models.DescribeCommandsResponseBodyCommands()
            self.commands = temp_model.from_map(m.get('Commands'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

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
        command: List[main_models.DescribeCommandsResponseBodyCommandsCommand] = None,
    ):
        self.command = command

    def validate(self):
        if self.command:
            for v1 in self.command:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Command'] = []
        if self.command is not None:
            for k1 in self.command:
                result['Command'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.command = []
        if m.get('Command') is not None:
            for k1 in m.get('Command'):
                temp_model = main_models.DescribeCommandsResponseBodyCommandsCommand()
                self.command.append(temp_model.from_map(k1))

        return self

class DescribeCommandsResponseBodyCommandsCommand(DaraModel):
    def __init__(
        self,
        category: str = None,
        command_content: str = None,
        command_id: str = None,
        creation_time: str = None,
        description: str = None,
        enable_parameter: bool = None,
        invoke_times: int = None,
        latest: bool = None,
        launcher: str = None,
        name: str = None,
        parameter_definitions: main_models.DescribeCommandsResponseBodyCommandsCommandParameterDefinitions = None,
        parameter_names: main_models.DescribeCommandsResponseBodyCommandsCommandParameterNames = None,
        provider: str = None,
        resource_group_id: str = None,
        tags: main_models.DescribeCommandsResponseBodyCommandsCommandTags = None,
        timeout: int = None,
        type: str = None,
        version: int = None,
        working_dir: str = None,
    ):
        # The category of the common command.
        self.category = category
        # The content of the command, which is Base64-encoded.
        # 
        # *   If ContentEncoding is set to PlainText in the request, the original command content is returned.
        # *   If ContentEncoding is set to Base64 in the request, the Base64-encoded command content is returned.
        self.command_content = command_content
        # The command ID.
        self.command_id = command_id
        # The time when the command was created.
        self.creation_time = creation_time
        # The description of the command.
        self.description = description
        # Indicates whether the custom parameter feature is enabled for the command.
        self.enable_parameter = enable_parameter
        # The number of tasks created by using the command.
        self.invoke_times = invoke_times
        # Indicates whether the common command is of the latest version. If multiple common commands from the same provider (`Provider`) belong to the same category and have the same name, these commands are different versions of the same command. This parameter is not returned for the Cloud Assistant commands that you created.
        self.latest = latest
        # The launcher for script execution. The value cannot exceed 1 KB in length.
        self.launcher = launcher
        # The name of the command.
        self.name = name
        # The custom parameters of the command.
        self.parameter_definitions = parameter_definitions
        # The custom parameter names that are parsed from the command content specified when the command was created. If the custom parameter feature is disabled, an empty list is returned.
        self.parameter_names = parameter_names
        # The provider of the common command.
        self.provider = provider
        # The ID of the resource group to which the command belongs.
        self.resource_group_id = resource_group_id
        # The tags of the command.
        self.tags = tags
        # The timeout period. Unit: seconds.
        self.timeout = timeout
        # The type of the command.
        self.type = type
        # The version of the common command. If multiple common commands from the same provider (`Provider`) belong to the same category and have the same name, these commands are different versions of the same command. This parameter is not returned for the Cloud Assistant commands that you created.
        self.version = version
        # The execution path of the command.
        self.working_dir = working_dir

    def validate(self):
        if self.parameter_definitions:
            self.parameter_definitions.validate()
        if self.parameter_names:
            self.parameter_names.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

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

        if self.invoke_times is not None:
            result['InvokeTimes'] = self.invoke_times

        if self.latest is not None:
            result['Latest'] = self.latest

        if self.launcher is not None:
            result['Launcher'] = self.launcher

        if self.name is not None:
            result['Name'] = self.name

        if self.parameter_definitions is not None:
            result['ParameterDefinitions'] = self.parameter_definitions.to_map()

        if self.parameter_names is not None:
            result['ParameterNames'] = self.parameter_names.to_map()

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

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

        if m.get('InvokeTimes') is not None:
            self.invoke_times = m.get('InvokeTimes')

        if m.get('Latest') is not None:
            self.latest = m.get('Latest')

        if m.get('Launcher') is not None:
            self.launcher = m.get('Launcher')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParameterDefinitions') is not None:
            temp_model = main_models.DescribeCommandsResponseBodyCommandsCommandParameterDefinitions()
            self.parameter_definitions = temp_model.from_map(m.get('ParameterDefinitions'))

        if m.get('ParameterNames') is not None:
            temp_model = main_models.DescribeCommandsResponseBodyCommandsCommandParameterNames()
            self.parameter_names = temp_model.from_map(m.get('ParameterNames'))

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeCommandsResponseBodyCommandsCommandTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

class DescribeCommandsResponseBodyCommandsCommandTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeCommandsResponseBodyCommandsCommandTagsTag] = None,
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
                temp_model = main_models.DescribeCommandsResponseBodyCommandsCommandTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeCommandsResponseBodyCommandsCommandTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the command.
        self.tag_key = tag_key
        # The tag value of the command.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeCommandsResponseBodyCommandsCommandParameterNames(DaraModel):
    def __init__(
        self,
        parameter_name: List[str] = None,
    ):
        self.parameter_name = parameter_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        return self

class DescribeCommandsResponseBodyCommandsCommandParameterDefinitions(DaraModel):
    def __init__(
        self,
        parameter_definition: List[main_models.DescribeCommandsResponseBodyCommandsCommandParameterDefinitionsParameterDefinition] = None,
    ):
        self.parameter_definition = parameter_definition

    def validate(self):
        if self.parameter_definition:
            for v1 in self.parameter_definition:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ParameterDefinition'] = []
        if self.parameter_definition is not None:
            for k1 in self.parameter_definition:
                result['ParameterDefinition'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameter_definition = []
        if m.get('ParameterDefinition') is not None:
            for k1 in m.get('ParameterDefinition'):
                temp_model = main_models.DescribeCommandsResponseBodyCommandsCommandParameterDefinitionsParameterDefinition()
                self.parameter_definition.append(temp_model.from_map(k1))

        return self

class DescribeCommandsResponseBodyCommandsCommandParameterDefinitionsParameterDefinition(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        parameter_name: str = None,
        pattern_regex: str = None,
        possible_values: main_models.DescribeCommandsResponseBodyCommandsCommandParameterDefinitionsParameterDefinitionPossibleValues = None,
        required: bool = None,
    ):
        # The default value of the custom parameter.
        self.default_value = default_value
        # The description of the custom parameter.
        self.description = description
        # The name of the custom parameter.
        self.parameter_name = parameter_name
        # The regular expression of the custom parameter.
        self.pattern_regex = pattern_regex
        # The valid values of the custom parameter of the enumeration type.
        self.possible_values = possible_values
        # Indicates whether the custom parameter is required. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.required = required

    def validate(self):
        if self.possible_values:
            self.possible_values.validate()

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

        if self.pattern_regex is not None:
            result['PatternRegex'] = self.pattern_regex

        if self.possible_values is not None:
            result['PossibleValues'] = self.possible_values.to_map()

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

        if m.get('PatternRegex') is not None:
            self.pattern_regex = m.get('PatternRegex')

        if m.get('PossibleValues') is not None:
            temp_model = main_models.DescribeCommandsResponseBodyCommandsCommandParameterDefinitionsParameterDefinitionPossibleValues()
            self.possible_values = temp_model.from_map(m.get('PossibleValues'))

        if m.get('Required') is not None:
            self.required = m.get('Required')

        return self

class DescribeCommandsResponseBodyCommandsCommandParameterDefinitionsParameterDefinitionPossibleValues(DaraModel):
    def __init__(
        self,
        possible_value: List[str] = None,
    ):
        self.possible_value = possible_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.possible_value is not None:
            result['PossibleValue'] = self.possible_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PossibleValue') is not None:
            self.possible_value = m.get('PossibleValue')

        return self

