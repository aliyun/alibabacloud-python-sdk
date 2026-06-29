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
        # The request for creating an API.
        # 
        # This parameter is required.
        self.create_command = create_command
        # The tenant ID.
        # 
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
        dml_config: main_models.CreateDataServiceApiRequestCreateCommandDmlConfig = None,
        execution_timeout: int = None,
        mode: int = None,
        project_id: int = None,
        request_type: int = None,
        return_sql_switch: bool = None,
        row_permission_ids: List[int] = None,
        script_details: main_models.CreateDataServiceApiRequestCreateCommandScriptDetails = None,
        timeout: int = None,
        update_rate: int = None,
        version: str = None,
    ):
        # The group ID of the API.
        # 
        # This parameter is required.
        self.api_group_id = api_group_id
        # The group name of the API.
        # 
        # This parameter is required.
        self.api_group_name = api_group_name
        # The name of the API.
        # 
        # This parameter is required.
        self.api_name = api_name
        # The type of the API. Valid values:
        # 
        # - 3: datasource SQL mode.
        # 
        # This parameter is required.
        self.api_type = api_type
        # The protocol. Different gateway types support different protocols. For more information, see the documentation. Valid values:
        # - 0: HTTP 
        # - 1: HTTPS.
        # 
        # This parameter is required.
        self.biz_protocol = biz_protocol
        # The cache timeout period, in seconds.
        self.cache_timeout = cache_timeout
        # The call mode of the API. Default value: 1. Valid values:
        # 
        # - 1: synchronous call
        # - 2: asynchronous call.
        self.call_mode = call_mode
        # The custom update frequency. This parameter is required when the update frequency is set to custom.
        self.custom_update_rate = custom_update_rate
        # The description of the API.
        self.description = description
        # The configuration of the operation-type API. This parameter is not required when creating a query-type API.
        self.dml_config = dml_config
        # The execution timeout period for asynchronous API calls. This parameter takes effect only for asynchronous API calls and is required when the call mode is asynchronous.
        self.execution_timeout = execution_timeout
        # The development mode of the API. Valid values:
        # 
        # - 0: Basic mode 
        # - 1: Dev-Prod mode.
        # 
        # This parameter is required.
        self.mode = mode
        # The ID of the data service project.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The request method of the API. Valid values:
        # 
        # - 0 (GET): Returns a single record. The query result is unique. 
        # - 1 (LIST): Returns multiple records.
        # - 2 (CREATE): Creates objects. Supports single or batch creation.
        # - 3 (UPDATE): Updates objects. Supports single or batch updates.
        # - 4 (DELETE): Deletes objects. Supports single or batch deletions.
        # 
        # This parameter is required.
        self.request_type = request_type
        # Specifies whether to return the SQL in the result.
        self.return_sql_switch = return_sql_switch
        # The list of row-level permission IDs.
        self.row_permission_ids = row_permission_ids
        # The details of the script API.
        # 
        # This parameter is required.
        self.script_details = script_details
        # The timeout period, in seconds.
        # 
        # This parameter is required.
        self.timeout = timeout
        # The update frequency. Default value: 1. Valid values:
        # 
        # - 0: custom
        # - 1: day
        # - 2: hour
        # - 3: minute.
        self.update_rate = update_rate
        # The version of the API.
        # 
        # This parameter is required.
        self.version = version

    def validate(self):
        if self.dml_config:
            self.dml_config.validate()
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

        if self.dml_config is not None:
            result['DmlConfig'] = self.dml_config.to_map()

        if self.execution_timeout is not None:
            result['ExecutionTimeout'] = self.execution_timeout

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.request_type is not None:
            result['RequestType'] = self.request_type

        if self.return_sql_switch is not None:
            result['ReturnSqlSwitch'] = self.return_sql_switch

        if self.row_permission_ids is not None:
            result['RowPermissionIds'] = self.row_permission_ids

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

        if m.get('DmlConfig') is not None:
            temp_model = main_models.CreateDataServiceApiRequestCreateCommandDmlConfig()
            self.dml_config = temp_model.from_map(m.get('DmlConfig'))

        if m.get('ExecutionTimeout') is not None:
            self.execution_timeout = m.get('ExecutionTimeout')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RequestType') is not None:
            self.request_type = m.get('RequestType')

        if m.get('ReturnSqlSwitch') is not None:
            self.return_sql_switch = m.get('ReturnSqlSwitch')

        if m.get('RowPermissionIds') is not None:
            self.row_permission_ids = m.get('RowPermissionIds')

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
        # The ID of the datasource. This parameter is required when the API mode is direct datasource connection.
        self.datasource_id = datasource_id
        # The data type on which the API is based. Valid values:
        # - 1: datasource.
        # 
        # This parameter is required.
        self.datasource_type = datasource_type
        # Specifies whether to paginate the results. This parameter is required only when RequestType is set to List. Default value: false. Pagination is not supported in asynchronous call mode.
        self.is_paginated = is_paginated
        # The SQL script.
        # 
        # This parameter is required.
        self.script = script
        # The list of request parameters for the script API.
        self.script_request_parameters = script_request_parameters
        # The list of response parameters for the script API.
        self.script_response_parameters = script_response_parameters
        # The sorting priority. This parameter takes effect only when the SQL mode is basic mode. Default value: 2. Valid values:
        # 
        # - 1: SQL script 
        # - 2: OrderByList request parameter.
        self.sort_priority = sort_priority
        # The SQL mode. Valid values:
        # 
        # - 1: basic mode
        # - 2: advanced mode.
        # 
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
        parameter_location: str = None,
        parameter_name: str = None,
    ):
        # The example value.
        self.example_value = example_value
        # The data type. Valid values:
        # - "STRING"
        # - "DOUBLE"
        # - "INT"
        # - "DATE"
        # - "LONG"
        # - "FLOAT"
        # - "BOOLEAN"
        # - "SHORT"
        # - "BYTE"
        # - "BIGDECIMAL"
        # - "BINARY"
        # - "ARRAY"
        # - "Array(int)"
        # - "Array(string)".
        # 
        # This parameter is required.
        self.parameter_data_type = parameter_data_type
        # The parameter description.
        self.parameter_description = parameter_description
        # The location of the response parameter for operation-type APIs. This parameter must be set when the API is an operation-type API with batch data volume. Valid values:
        # - success: the response data of a successful operation
        # - failed: the response data of a failed operation.
        self.parameter_location = parameter_location
        # The parameter name.
        # 
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

        if self.parameter_location is not None:
            result['ParameterLocation'] = self.parameter_location

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

        if m.get('ParameterLocation') is not None:
            self.parameter_location = m.get('ParameterLocation')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        return self

class CreateDataServiceApiRequestCreateCommandScriptDetailsScriptRequestParameters(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        example_value: str = None,
        is_required_parameter: bool = None,
        parameter_data_type: str = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value_type: str = None,
    ):
        # The default value of the input parameter for operation-type APIs. This parameter takes effect when the parameter is not required. If not specified, the value is null.
        self.default_value = default_value
        # The example value.
        self.example_value = example_value
        # Specifies whether the parameter is required.
        # 
        # This parameter is required.
        self.is_required_parameter = is_required_parameter
        # The data type. Valid values:
        # - "STRING"
        # - "DOUBLE"
        # - "INT"
        # - "DATE"
        # - "LONG"
        # - "FLOAT"
        # - "BOOLEAN"
        # - "SHORT"
        # - "BYTE"
        # - "BIGDECIMAL"
        # - "BINARY"
        # - "ARRAY"
        # - "Array(int)"
        # - "Array(string)".
        # 
        # This parameter is required.
        self.parameter_data_type = parameter_data_type
        # The parameter description.
        self.parameter_description = parameter_description
        # The parameter name.
        # 
        # This parameter is required.
        self.parameter_name = parameter_name
        # The value type of the parameter. Valid values:
        # 
        # - 1 (single value): A fixed value used for operators such as =, >=, <=, >, <, !=, and between. 
        # - 2 (multiple values): The input parameter contains multiple values separated by commas (,). Used for In and Not In operators.
        # 
        # This parameter is required.
        self.parameter_value_type = parameter_value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

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
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

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

class CreateDataServiceApiRequestCreateCommandDmlConfig(DaraModel):
    def __init__(
        self,
        batch_input_data_size: int = None,
        data_volume_type: int = None,
        error_handling_type: int = None,
        max_input_data_size: int = None,
        parallel_num: int = None,
        transaction_type: int = None,
    ):
        # The data volume per batch. Valid values:
        # - When the data volume type is single record, this parameter cannot be set.
        # - When the data volume type is batch:
        #   - If the transaction processing mode is 1, this parameter cannot be set.
        #   - If the transaction processing mode is 2, the value ranges from 1 to 1000000.
        self.batch_input_data_size = batch_input_data_size
        # The data volume type. Valid values:
        # - 1: single record
        # - 2: batch.
        self.data_volume_type = data_volume_type
        # The error handling method. Valid values:
        # - 1: partial success allowed
        # - 2: all must succeed
        # 
        # Parameter rules:
        # - When the data volume type is single record, this parameter cannot be set.
        # - When the data volume type is batch, the value is 1 or 2.
        self.error_handling_type = error_handling_type
        # The maximum number of input records. Valid values:
        # - When the data volume type is single record, this parameter cannot be set.
        # - When the data volume type is batch, the value ranges from 1 to 1000000.
        self.max_input_data_size = max_input_data_size
        # The degree of parallelism. Valid values:
        # - When the data volume type is single record, this parameter cannot be set.
        # - When the data volume type is batch:
        #   - If the transaction processing mode is 1, this parameter cannot be set.
        #   - If the transaction processing mode is 2, the value ranges from 1 to 5.
        self.parallel_num = parallel_num
        # The transaction processing mode. Valid values:
        # - 0: no transaction
        # - 1: no batching
        # - 2: batch processing
        # 
        # Parameter rules:
        # - When the data volume type is single record, the transaction processing mode is 0.
        # - When the data volume type is batch:
        #   - If the error handling method is 1, the transaction processing mode is 1 or 2.
        #   - If the error handling method is 2, the transaction processing mode can only be 1.
        self.transaction_type = transaction_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_input_data_size is not None:
            result['BatchInputDataSize'] = self.batch_input_data_size

        if self.data_volume_type is not None:
            result['DataVolumeType'] = self.data_volume_type

        if self.error_handling_type is not None:
            result['ErrorHandlingType'] = self.error_handling_type

        if self.max_input_data_size is not None:
            result['MaxInputDataSize'] = self.max_input_data_size

        if self.parallel_num is not None:
            result['ParallelNum'] = self.parallel_num

        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchInputDataSize') is not None:
            self.batch_input_data_size = m.get('BatchInputDataSize')

        if m.get('DataVolumeType') is not None:
            self.data_volume_type = m.get('DataVolumeType')

        if m.get('ErrorHandlingType') is not None:
            self.error_handling_type = m.get('ErrorHandlingType')

        if m.get('MaxInputDataSize') is not None:
            self.max_input_data_size = m.get('MaxInputDataSize')

        if m.get('ParallelNum') is not None:
            self.parallel_num = m.get('ParallelNum')

        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')

        return self

