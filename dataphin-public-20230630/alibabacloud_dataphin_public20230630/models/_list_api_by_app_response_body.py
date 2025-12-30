# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListApiByAppResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        list_result: main_models.ListApiByAppResponseBodyListResult = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.list_result = list_result
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.list_result:
            self.list_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.list_result is not None:
            result['ListResult'] = self.list_result.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('ListResult') is not None:
            temp_model = main_models.ListApiByAppResponseBodyListResult()
            self.list_result = temp_model.from_map(m.get('ListResult'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListApiByAppResponseBodyListResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListApiByAppResponseBodyListResultData] = None,
        total_count: int = None,
    ):
        self.data = data
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListApiByAppResponseBodyListResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApiByAppResponseBodyListResultData(DaraModel):
    def __init__(
        self,
        api_no: int = None,
        api_timeout: int = None,
        app_name: str = None,
        biz_module_en_name: str = None,
        cache_switch: str = None,
        cache_time: str = None,
        create_type: int = None,
        db_env: int = None,
        description: str = None,
        direct_datasource_id: int = None,
        direct_datasource_name: str = None,
        group_id: int = None,
        group_name: str = None,
        id: int = None,
        is_logical_table: bool = None,
        is_paged_query: int = None,
        max_return_num: int = None,
        model_type: int = None,
        name: str = None,
        proj_id: int = None,
        proj_name: str = None,
        protocol: int = None,
        protocol_name: str = None,
        public_param_list: List[main_models.ListApiByAppResponseBodyListResultDataPublicParamList] = None,
        register_api: main_models.ListApiByAppResponseBodyListResultDataRegisterApi = None,
        request_method: int = None,
        request_method_name: str = None,
        request_param_list: List[main_models.ListApiByAppResponseBodyListResultDataRequestParamList] = None,
        resource_group_name: str = None,
        response_param_list: List[main_models.ListApiByAppResponseBodyListResultDataResponseParamList] = None,
        result_sample: str = None,
        return_type: int = None,
        return_type_name: str = None,
        rs_grp_id: str = None,
        script_type: str = None,
        special_sql: int = None,
        sql_statement: str = None,
        table_name: str = None,
        timeout: str = None,
        update_rate: int = None,
        update_rate_name: str = None,
        version: str = None,
    ):
        self.api_no = api_no
        self.api_timeout = api_timeout
        self.app_name = app_name
        self.biz_module_en_name = biz_module_en_name
        self.cache_switch = cache_switch
        self.cache_time = cache_time
        self.create_type = create_type
        self.db_env = db_env
        self.description = description
        self.direct_datasource_id = direct_datasource_id
        self.direct_datasource_name = direct_datasource_name
        self.group_id = group_id
        self.group_name = group_name
        self.id = id
        self.is_logical_table = is_logical_table
        self.is_paged_query = is_paged_query
        self.max_return_num = max_return_num
        self.model_type = model_type
        self.name = name
        self.proj_id = proj_id
        self.proj_name = proj_name
        self.protocol = protocol
        self.protocol_name = protocol_name
        # -
        self.public_param_list = public_param_list
        self.register_api = register_api
        self.request_method = request_method
        self.request_method_name = request_method_name
        # -
        self.request_param_list = request_param_list
        self.resource_group_name = resource_group_name
        # -
        self.response_param_list = response_param_list
        self.result_sample = result_sample
        self.return_type = return_type
        self.return_type_name = return_type_name
        self.rs_grp_id = rs_grp_id
        self.script_type = script_type
        self.special_sql = special_sql
        self.sql_statement = sql_statement
        self.table_name = table_name
        self.timeout = timeout
        self.update_rate = update_rate
        self.update_rate_name = update_rate_name
        self.version = version

    def validate(self):
        if self.public_param_list:
            for v1 in self.public_param_list:
                 if v1:
                    v1.validate()
        if self.register_api:
            self.register_api.validate()
        if self.request_param_list:
            for v1 in self.request_param_list:
                 if v1:
                    v1.validate()
        if self.response_param_list:
            for v1 in self.response_param_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_no is not None:
            result['ApiNo'] = self.api_no

        if self.api_timeout is not None:
            result['ApiTimeout'] = self.api_timeout

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.biz_module_en_name is not None:
            result['BizModuleEnName'] = self.biz_module_en_name

        if self.cache_switch is not None:
            result['CacheSwitch'] = self.cache_switch

        if self.cache_time is not None:
            result['CacheTime'] = self.cache_time

        if self.create_type is not None:
            result['CreateType'] = self.create_type

        if self.db_env is not None:
            result['DbEnv'] = self.db_env

        if self.description is not None:
            result['Description'] = self.description

        if self.direct_datasource_id is not None:
            result['DirectDatasourceId'] = self.direct_datasource_id

        if self.direct_datasource_name is not None:
            result['DirectDatasourceName'] = self.direct_datasource_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.id is not None:
            result['Id'] = self.id

        if self.is_logical_table is not None:
            result['IsLogicalTable'] = self.is_logical_table

        if self.is_paged_query is not None:
            result['IsPagedQuery'] = self.is_paged_query

        if self.max_return_num is not None:
            result['MaxReturnNum'] = self.max_return_num

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.name is not None:
            result['Name'] = self.name

        if self.proj_id is not None:
            result['ProjId'] = self.proj_id

        if self.proj_name is not None:
            result['ProjName'] = self.proj_name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name

        result['PublicParamList'] = []
        if self.public_param_list is not None:
            for k1 in self.public_param_list:
                result['PublicParamList'].append(k1.to_map() if k1 else None)

        if self.register_api is not None:
            result['RegisterApi'] = self.register_api.to_map()

        if self.request_method is not None:
            result['RequestMethod'] = self.request_method

        if self.request_method_name is not None:
            result['RequestMethodName'] = self.request_method_name

        result['RequestParamList'] = []
        if self.request_param_list is not None:
            for k1 in self.request_param_list:
                result['RequestParamList'].append(k1.to_map() if k1 else None)

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        result['ResponseParamList'] = []
        if self.response_param_list is not None:
            for k1 in self.response_param_list:
                result['ResponseParamList'].append(k1.to_map() if k1 else None)

        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample

        if self.return_type is not None:
            result['ReturnType'] = self.return_type

        if self.return_type_name is not None:
            result['ReturnTypeName'] = self.return_type_name

        if self.rs_grp_id is not None:
            result['RsGrpId'] = self.rs_grp_id

        if self.script_type is not None:
            result['ScriptType'] = self.script_type

        if self.special_sql is not None:
            result['SpecialSql'] = self.special_sql

        if self.sql_statement is not None:
            result['SqlStatement'] = self.sql_statement

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.update_rate is not None:
            result['UpdateRate'] = self.update_rate

        if self.update_rate_name is not None:
            result['UpdateRateName'] = self.update_rate_name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiNo') is not None:
            self.api_no = m.get('ApiNo')

        if m.get('ApiTimeout') is not None:
            self.api_timeout = m.get('ApiTimeout')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BizModuleEnName') is not None:
            self.biz_module_en_name = m.get('BizModuleEnName')

        if m.get('CacheSwitch') is not None:
            self.cache_switch = m.get('CacheSwitch')

        if m.get('CacheTime') is not None:
            self.cache_time = m.get('CacheTime')

        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')

        if m.get('DbEnv') is not None:
            self.db_env = m.get('DbEnv')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DirectDatasourceId') is not None:
            self.direct_datasource_id = m.get('DirectDatasourceId')

        if m.get('DirectDatasourceName') is not None:
            self.direct_datasource_name = m.get('DirectDatasourceName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsLogicalTable') is not None:
            self.is_logical_table = m.get('IsLogicalTable')

        if m.get('IsPagedQuery') is not None:
            self.is_paged_query = m.get('IsPagedQuery')

        if m.get('MaxReturnNum') is not None:
            self.max_return_num = m.get('MaxReturnNum')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjId') is not None:
            self.proj_id = m.get('ProjId')

        if m.get('ProjName') is not None:
            self.proj_name = m.get('ProjName')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')

        self.public_param_list = []
        if m.get('PublicParamList') is not None:
            for k1 in m.get('PublicParamList'):
                temp_model = main_models.ListApiByAppResponseBodyListResultDataPublicParamList()
                self.public_param_list.append(temp_model.from_map(k1))

        if m.get('RegisterApi') is not None:
            temp_model = main_models.ListApiByAppResponseBodyListResultDataRegisterApi()
            self.register_api = temp_model.from_map(m.get('RegisterApi'))

        if m.get('RequestMethod') is not None:
            self.request_method = m.get('RequestMethod')

        if m.get('RequestMethodName') is not None:
            self.request_method_name = m.get('RequestMethodName')

        self.request_param_list = []
        if m.get('RequestParamList') is not None:
            for k1 in m.get('RequestParamList'):
                temp_model = main_models.ListApiByAppResponseBodyListResultDataRequestParamList()
                self.request_param_list.append(temp_model.from_map(k1))

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        self.response_param_list = []
        if m.get('ResponseParamList') is not None:
            for k1 in m.get('ResponseParamList'):
                temp_model = main_models.ListApiByAppResponseBodyListResultDataResponseParamList()
                self.response_param_list.append(temp_model.from_map(k1))

        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')

        if m.get('ReturnType') is not None:
            self.return_type = m.get('ReturnType')

        if m.get('ReturnTypeName') is not None:
            self.return_type_name = m.get('ReturnTypeName')

        if m.get('RsGrpId') is not None:
            self.rs_grp_id = m.get('RsGrpId')

        if m.get('ScriptType') is not None:
            self.script_type = m.get('ScriptType')

        if m.get('SpecialSql') is not None:
            self.special_sql = m.get('SpecialSql')

        if m.get('SqlStatement') is not None:
            self.sql_statement = m.get('SqlStatement')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('UpdateRate') is not None:
            self.update_rate = m.get('UpdateRate')

        if m.get('UpdateRateName') is not None:
            self.update_rate_name = m.get('UpdateRateName')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListApiByAppResponseBodyListResultDataResponseParamList(DaraModel):
    def __init__(
        self,
        date_format: str = None,
        default_value: str = None,
        description: str = None,
        description_code: str = None,
        id: int = None,
        initial_value: str = None,
        mapping_column: str = None,
        must: int = None,
        operator: str = None,
        optional: int = None,
        original_column: str = None,
        param_name: str = None,
        param_type: str = None,
        parameter_location: str = None,
        sample: str = None,
        table_and_ds_list: List[main_models.ListApiByAppResponseBodyListResultDataResponseParamListTableAndDsList] = None,
    ):
        self.date_format = date_format
        self.default_value = default_value
        self.description = description
        self.description_code = description_code
        self.id = id
        self.initial_value = initial_value
        self.mapping_column = mapping_column
        self.must = must
        self.operator = operator
        self.optional = optional
        self.original_column = original_column
        self.param_name = param_name
        self.param_type = param_type
        self.parameter_location = parameter_location
        self.sample = sample
        # -
        self.table_and_ds_list = table_and_ds_list

    def validate(self):
        if self.table_and_ds_list:
            for v1 in self.table_and_ds_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_format is not None:
            result['DateFormat'] = self.date_format

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.description_code is not None:
            result['DescriptionCode'] = self.description_code

        if self.id is not None:
            result['Id'] = self.id

        if self.initial_value is not None:
            result['InitialValue'] = self.initial_value

        if self.mapping_column is not None:
            result['MappingColumn'] = self.mapping_column

        if self.must is not None:
            result['Must'] = self.must

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.optional is not None:
            result['Optional'] = self.optional

        if self.original_column is not None:
            result['OriginalColumn'] = self.original_column

        if self.param_name is not None:
            result['ParamName'] = self.param_name

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.parameter_location is not None:
            result['ParameterLocation'] = self.parameter_location

        if self.sample is not None:
            result['Sample'] = self.sample

        result['TableAndDsList'] = []
        if self.table_and_ds_list is not None:
            for k1 in self.table_and_ds_list:
                result['TableAndDsList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateFormat') is not None:
            self.date_format = m.get('DateFormat')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DescriptionCode') is not None:
            self.description_code = m.get('DescriptionCode')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InitialValue') is not None:
            self.initial_value = m.get('InitialValue')

        if m.get('MappingColumn') is not None:
            self.mapping_column = m.get('MappingColumn')

        if m.get('Must') is not None:
            self.must = m.get('Must')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Optional') is not None:
            self.optional = m.get('Optional')

        if m.get('OriginalColumn') is not None:
            self.original_column = m.get('OriginalColumn')

        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('ParameterLocation') is not None:
            self.parameter_location = m.get('ParameterLocation')

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        self.table_and_ds_list = []
        if m.get('TableAndDsList') is not None:
            for k1 in m.get('TableAndDsList'):
                temp_model = main_models.ListApiByAppResponseBodyListResultDataResponseParamListTableAndDsList()
                self.table_and_ds_list.append(temp_model.from_map(k1))

        return self

class ListApiByAppResponseBodyListResultDataResponseParamListTableAndDsList(DaraModel):
    def __init__(
        self,
        datasource_id: str = None,
        datasource_name: str = None,
        datasource_type: int = None,
        datasource_url: str = None,
        table_name: str = None,
    ):
        self.datasource_id = datasource_id
        self.datasource_name = datasource_name
        self.datasource_type = datasource_type
        self.datasource_url = datasource_url
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        if self.datasource_type is not None:
            result['DatasourceType'] = self.datasource_type

        if self.datasource_url is not None:
            result['DatasourceUrl'] = self.datasource_url

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('DatasourceType') is not None:
            self.datasource_type = m.get('DatasourceType')

        if m.get('DatasourceUrl') is not None:
            self.datasource_url = m.get('DatasourceUrl')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class ListApiByAppResponseBodyListResultDataRequestParamList(DaraModel):
    def __init__(
        self,
        date_format: str = None,
        default_value: str = None,
        description: str = None,
        description_code: str = None,
        id: int = None,
        initial_value: str = None,
        mapping_column: str = None,
        must: int = None,
        operator: str = None,
        optional: int = None,
        original_column: str = None,
        param_name: str = None,
        param_type: str = None,
        parameter_location: str = None,
        sample: str = None,
        table_and_ds_list: List[main_models.ListApiByAppResponseBodyListResultDataRequestParamListTableAndDsList] = None,
    ):
        self.date_format = date_format
        self.default_value = default_value
        self.description = description
        self.description_code = description_code
        self.id = id
        self.initial_value = initial_value
        self.mapping_column = mapping_column
        self.must = must
        self.operator = operator
        self.optional = optional
        self.original_column = original_column
        self.param_name = param_name
        self.param_type = param_type
        self.parameter_location = parameter_location
        self.sample = sample
        # -
        self.table_and_ds_list = table_and_ds_list

    def validate(self):
        if self.table_and_ds_list:
            for v1 in self.table_and_ds_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_format is not None:
            result['DateFormat'] = self.date_format

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.description_code is not None:
            result['DescriptionCode'] = self.description_code

        if self.id is not None:
            result['Id'] = self.id

        if self.initial_value is not None:
            result['InitialValue'] = self.initial_value

        if self.mapping_column is not None:
            result['MappingColumn'] = self.mapping_column

        if self.must is not None:
            result['Must'] = self.must

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.optional is not None:
            result['Optional'] = self.optional

        if self.original_column is not None:
            result['OriginalColumn'] = self.original_column

        if self.param_name is not None:
            result['ParamName'] = self.param_name

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.parameter_location is not None:
            result['ParameterLocation'] = self.parameter_location

        if self.sample is not None:
            result['Sample'] = self.sample

        result['TableAndDsList'] = []
        if self.table_and_ds_list is not None:
            for k1 in self.table_and_ds_list:
                result['TableAndDsList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateFormat') is not None:
            self.date_format = m.get('DateFormat')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DescriptionCode') is not None:
            self.description_code = m.get('DescriptionCode')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InitialValue') is not None:
            self.initial_value = m.get('InitialValue')

        if m.get('MappingColumn') is not None:
            self.mapping_column = m.get('MappingColumn')

        if m.get('Must') is not None:
            self.must = m.get('Must')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Optional') is not None:
            self.optional = m.get('Optional')

        if m.get('OriginalColumn') is not None:
            self.original_column = m.get('OriginalColumn')

        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('ParameterLocation') is not None:
            self.parameter_location = m.get('ParameterLocation')

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        self.table_and_ds_list = []
        if m.get('TableAndDsList') is not None:
            for k1 in m.get('TableAndDsList'):
                temp_model = main_models.ListApiByAppResponseBodyListResultDataRequestParamListTableAndDsList()
                self.table_and_ds_list.append(temp_model.from_map(k1))

        return self

class ListApiByAppResponseBodyListResultDataRequestParamListTableAndDsList(DaraModel):
    def __init__(
        self,
        datasource_id: str = None,
        datasource_name: str = None,
        datasource_type: int = None,
        datasource_url: str = None,
        table_name: str = None,
    ):
        self.datasource_id = datasource_id
        self.datasource_name = datasource_name
        self.datasource_type = datasource_type
        self.datasource_url = datasource_url
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        if self.datasource_type is not None:
            result['DatasourceType'] = self.datasource_type

        if self.datasource_url is not None:
            result['DatasourceUrl'] = self.datasource_url

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('DatasourceType') is not None:
            self.datasource_type = m.get('DatasourceType')

        if m.get('DatasourceUrl') is not None:
            self.datasource_url = m.get('DatasourceUrl')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class ListApiByAppResponseBodyListResultDataRegisterApi(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        authentication_mode: str = None,
        datasource_id: str = None,
        datasource_name: str = None,
        fail_example: str = None,
        http_method: int = None,
        model_type: int = None,
        path: str = None,
        protocol: str = None,
        success_example: str = None,
        timeout: int = None,
        url: str = None,
    ):
        self.api_id = api_id
        self.authentication_mode = authentication_mode
        self.datasource_id = datasource_id
        self.datasource_name = datasource_name
        self.fail_example = fail_example
        self.http_method = http_method
        self.model_type = model_type
        self.path = path
        self.protocol = protocol
        self.success_example = success_example
        self.timeout = timeout
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.authentication_mode is not None:
            result['AuthenticationMode'] = self.authentication_mode

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        if self.fail_example is not None:
            result['FailExample'] = self.fail_example

        if self.http_method is not None:
            result['HttpMethod'] = self.http_method

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.path is not None:
            result['Path'] = self.path

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.success_example is not None:
            result['SuccessExample'] = self.success_example

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('AuthenticationMode') is not None:
            self.authentication_mode = m.get('AuthenticationMode')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('FailExample') is not None:
            self.fail_example = m.get('FailExample')

        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('SuccessExample') is not None:
            self.success_example = m.get('SuccessExample')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class ListApiByAppResponseBodyListResultDataPublicParamList(DaraModel):
    def __init__(
        self,
        date_format: str = None,
        default_value: str = None,
        description: str = None,
        description_code: str = None,
        id: int = None,
        initial_value: str = None,
        mapping_column: str = None,
        must: int = None,
        operator: str = None,
        optional: int = None,
        original_column: str = None,
        param_name: str = None,
        param_type: str = None,
        parameter_location: str = None,
        sample: str = None,
        table_and_ds_list: List[main_models.ListApiByAppResponseBodyListResultDataPublicParamListTableAndDsList] = None,
    ):
        self.date_format = date_format
        self.default_value = default_value
        self.description = description
        self.description_code = description_code
        self.id = id
        self.initial_value = initial_value
        self.mapping_column = mapping_column
        self.must = must
        self.operator = operator
        self.optional = optional
        self.original_column = original_column
        self.param_name = param_name
        self.param_type = param_type
        self.parameter_location = parameter_location
        self.sample = sample
        # -
        self.table_and_ds_list = table_and_ds_list

    def validate(self):
        if self.table_and_ds_list:
            for v1 in self.table_and_ds_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_format is not None:
            result['DateFormat'] = self.date_format

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.description_code is not None:
            result['DescriptionCode'] = self.description_code

        if self.id is not None:
            result['Id'] = self.id

        if self.initial_value is not None:
            result['InitialValue'] = self.initial_value

        if self.mapping_column is not None:
            result['MappingColumn'] = self.mapping_column

        if self.must is not None:
            result['Must'] = self.must

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.optional is not None:
            result['Optional'] = self.optional

        if self.original_column is not None:
            result['OriginalColumn'] = self.original_column

        if self.param_name is not None:
            result['ParamName'] = self.param_name

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.parameter_location is not None:
            result['ParameterLocation'] = self.parameter_location

        if self.sample is not None:
            result['Sample'] = self.sample

        result['TableAndDsList'] = []
        if self.table_and_ds_list is not None:
            for k1 in self.table_and_ds_list:
                result['TableAndDsList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateFormat') is not None:
            self.date_format = m.get('DateFormat')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DescriptionCode') is not None:
            self.description_code = m.get('DescriptionCode')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InitialValue') is not None:
            self.initial_value = m.get('InitialValue')

        if m.get('MappingColumn') is not None:
            self.mapping_column = m.get('MappingColumn')

        if m.get('Must') is not None:
            self.must = m.get('Must')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Optional') is not None:
            self.optional = m.get('Optional')

        if m.get('OriginalColumn') is not None:
            self.original_column = m.get('OriginalColumn')

        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('ParameterLocation') is not None:
            self.parameter_location = m.get('ParameterLocation')

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        self.table_and_ds_list = []
        if m.get('TableAndDsList') is not None:
            for k1 in m.get('TableAndDsList'):
                temp_model = main_models.ListApiByAppResponseBodyListResultDataPublicParamListTableAndDsList()
                self.table_and_ds_list.append(temp_model.from_map(k1))

        return self

class ListApiByAppResponseBodyListResultDataPublicParamListTableAndDsList(DaraModel):
    def __init__(
        self,
        datasource_id: str = None,
        datasource_name: str = None,
        datasource_type: int = None,
        datasource_url: str = None,
        table_name: str = None,
    ):
        self.datasource_id = datasource_id
        self.datasource_name = datasource_name
        self.datasource_type = datasource_type
        self.datasource_url = datasource_url
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        if self.datasource_type is not None:
            result['DatasourceType'] = self.datasource_type

        if self.datasource_url is not None:
            result['DatasourceUrl'] = self.datasource_url

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('DatasourceType') is not None:
            self.datasource_type = m.get('DatasourceType')

        if m.get('DatasourceUrl') is not None:
            self.datasource_url = m.get('DatasourceUrl')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

