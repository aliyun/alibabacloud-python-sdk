# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateDataServiceApiRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateDataServiceApiRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_command = create_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateDataServiceApiRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreateDataServiceApiRequestCreateCommand(DaraModel):
    def __init__(
        self,
        api_group_id: int = None,
        api_group_name: str = None,
        api_name: str = None,
        api_type: int = None,
        biz_protocol: List[int] = None,
        cache_timeout: int = None,
        call_mode: int = None,
        custom_update_rate: str = None,
        description: str = None,
        execution_timeout: int = None,
        mode: int = None,
        project_id: int = None,
        request_type: int = None,
        script_details: main_models.CreateDataServiceApiRequestCreateCommandScriptDetails = None,
        timeout: int = None,
        update_rate: int = None,
        version: str = None,
    ):
        # This parameter is required.
        self.api_group_id = api_group_id
        # This parameter is required.
        self.api_group_name = api_group_name
        # This parameter is required.
        self.api_name = api_name
        # This parameter is required.
        self.api_type = api_type
        # This parameter is required.
        self.biz_protocol = biz_protocol
        # This parameter is required.
        self.cache_timeout = cache_timeout
        self.call_mode = call_mode
        self.custom_update_rate = custom_update_rate
        self.description = description
        self.execution_timeout = execution_timeout
        # This parameter is required.
        self.mode = mode
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.request_type = request_type
        # This parameter is required.
        self.script_details = script_details
        # This parameter is required.
        self.timeout = timeout
        self.update_rate = update_rate
        # This parameter is required.
        self.version = version

    def validate(self):
        if self.script_details:
            self.script_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_group_id is not None:
            result['ApiGroupId'] = self.api_group_id

        if self.api_group_name is not None:
            result['ApiGroupName'] = self.api_group_name

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.api_type is not None:
            result['ApiType'] = self.api_type

        if self.biz_protocol is not None:
            result['BizProtocol'] = self.biz_protocol

        if self.cache_timeout is not None:
            result['CacheTimeout'] = self.cache_timeout

        if self.call_mode is not None:
            result['CallMode'] = self.call_mode

        if self.custom_update_rate is not None:
            result['CustomUpdateRate'] = self.custom_update_rate

        if self.description is not None:
            result['Description'] = self.description

        if self.execution_timeout is not None:
            result['ExecutionTimeout'] = self.execution_timeout

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.request_type is not None:
            result['RequestType'] = self.request_type

        if self.script_details is not None:
            result['ScriptDetails'] = self.script_details.to_map()

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.update_rate is not None:
            result['UpdateRate'] = self.update_rate

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiGroupId') is not None:
            self.api_group_id = m.get('ApiGroupId')

        if m.get('ApiGroupName') is not None:
            self.api_group_name = m.get('ApiGroupName')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')

        if m.get('BizProtocol') is not None:
            self.biz_protocol = m.get('BizProtocol')

        if m.get('CacheTimeout') is not None:
            self.cache_timeout = m.get('CacheTimeout')

        if m.get('CallMode') is not None:
            self.call_mode = m.get('CallMode')

        if m.get('CustomUpdateRate') is not None:
            self.custom_update_rate = m.get('CustomUpdateRate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExecutionTimeout') is not None:
            self.execution_timeout = m.get('ExecutionTimeout')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RequestType') is not None:
            self.request_type = m.get('RequestType')

        if m.get('ScriptDetails') is not None:
            temp_model = main_models.CreateDataServiceApiRequestCreateCommandScriptDetails()
            self.script_details = temp_model.from_map(m.get('ScriptDetails'))

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('UpdateRate') is not None:
            self.update_rate = m.get('UpdateRate')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class CreateDataServiceApiRequestCreateCommandScriptDetails(DaraModel):
    def __init__(
        self,
        datasource_id: int = None,
        datasource_type: int = None,
        is_paginated: bool = None,
        script: str = None,
        script_request_parameters: List[main_models.CreateDataServiceApiRequestCreateCommandScriptDetailsScriptRequestParameters] = None,
        script_response_parameters: List[main_models.CreateDataServiceApiRequestCreateCommandScriptDetailsScriptResponseParameters] = None,
        sort_priority: int = None,
        sql_mode: int = None,
    ):
        self.datasource_id = datasource_id
        # This parameter is required.
        self.datasource_type = datasource_type
        self.is_paginated = is_paginated
        # This parameter is required.
        self.script = script
        # This parameter is required.
        self.script_request_parameters = script_request_parameters
        # This parameter is required.
        self.script_response_parameters = script_response_parameters
        self.sort_priority = sort_priority
        # This parameter is required.
        self.sql_mode = sql_mode

    def validate(self):
        if self.script_request_parameters:
            for v1 in self.script_request_parameters:
                 if v1:
                    v1.validate()
        if self.script_response_parameters:
            for v1 in self.script_response_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datasource_id is not None:
            result['DatasourceID'] = self.datasource_id

        if self.datasource_type is not None:
            result['DatasourceType'] = self.datasource_type

        if self.is_paginated is not None:
            result['IsPaginated'] = self.is_paginated

        if self.script is not None:
            result['Script'] = self.script

        result['ScriptRequestParameters'] = []
        if self.script_request_parameters is not None:
            for k1 in self.script_request_parameters:
                result['ScriptRequestParameters'].append(k1.to_map() if k1 else None)

        result['ScriptResponseParameters'] = []
        if self.script_response_parameters is not None:
            for k1 in self.script_response_parameters:
                result['ScriptResponseParameters'].append(k1.to_map() if k1 else None)

        if self.sort_priority is not None:
            result['SortPriority'] = self.sort_priority

        if self.sql_mode is not None:
            result['SqlMode'] = self.sql_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceID') is not None:
            self.datasource_id = m.get('DatasourceID')

        if m.get('DatasourceType') is not None:
            self.datasource_type = m.get('DatasourceType')

        if m.get('IsPaginated') is not None:
            self.is_paginated = m.get('IsPaginated')

        if m.get('Script') is not None:
            self.script = m.get('Script')

        self.script_request_parameters = []
        if m.get('ScriptRequestParameters') is not None:
            for k1 in m.get('ScriptRequestParameters'):
                temp_model = main_models.CreateDataServiceApiRequestCreateCommandScriptDetailsScriptRequestParameters()
                self.script_request_parameters.append(temp_model.from_map(k1))

        self.script_response_parameters = []
        if m.get('ScriptResponseParameters') is not None:
            for k1 in m.get('ScriptResponseParameters'):
                temp_model = main_models.CreateDataServiceApiRequestCreateCommandScriptDetailsScriptResponseParameters()
                self.script_response_parameters.append(temp_model.from_map(k1))

        if m.get('SortPriority') is not None:
            self.sort_priority = m.get('SortPriority')

        if m.get('SqlMode') is not None:
            self.sql_mode = m.get('SqlMode')

        return self

class CreateDataServiceApiRequestCreateCommandScriptDetailsScriptResponseParameters(DaraModel):
    def __init__(
        self,
        example_value: str = None,
        parameter_data_type: str = None,
        parameter_description: str = None,
        parameter_name: str = None,
    ):
        self.example_value = example_value
        # This parameter is required.
        self.parameter_data_type = parameter_data_type
        self.parameter_description = parameter_description
        # This parameter is required.
        self.parameter_name = parameter_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.example_value is not None:
            result['ExampleValue'] = self.example_value

        if self.parameter_data_type is not None:
            result['ParameterDataType'] = self.parameter_data_type

        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExampleValue') is not None:
            self.example_value = m.get('ExampleValue')

        if m.get('ParameterDataType') is not None:
            self.parameter_data_type = m.get('ParameterDataType')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        return self

class CreateDataServiceApiRequestCreateCommandScriptDetailsScriptRequestParameters(DaraModel):
    def __init__(
        self,
        example_value: str = None,
        is_required_parameter: bool = None,
        parameter_data_type: str = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value_type: str = None,
    ):
        self.example_value = example_value
        # This parameter is required.
        self.is_required_parameter = is_required_parameter
        # This parameter is required.
        self.parameter_data_type = parameter_data_type
        self.parameter_description = parameter_description
        # This parameter is required.
        self.parameter_name = parameter_name
        # This parameter is required.
        self.parameter_value_type = parameter_value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.example_value is not None:
            result['ExampleValue'] = self.example_value

        if self.is_required_parameter is not None:
            result['IsRequiredParameter'] = self.is_required_parameter

        if self.parameter_data_type is not None:
            result['ParameterDataType'] = self.parameter_data_type

        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_value_type is not None:
            result['ParameterValueType'] = self.parameter_value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExampleValue') is not None:
            self.example_value = m.get('ExampleValue')

        if m.get('IsRequiredParameter') is not None:
            self.is_required_parameter = m.get('IsRequiredParameter')

        if m.get('ParameterDataType') is not None:
            self.parameter_data_type = m.get('ParameterDataType')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValueType') is not None:
            self.parameter_value_type = m.get('ParameterValueType')

        return self

