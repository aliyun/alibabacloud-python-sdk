# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetDataServiceApiDocumentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDataServiceApiDocumentResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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

        if m.get('Data') is not None:
            temp_model = main_models.GetDataServiceApiDocumentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataServiceApiDocumentResponseBodyData(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        api_register_info: main_models.GetDataServiceApiDocumentResponseBodyDataApiRegisterInfo = None,
        api_timeout: int = None,
        biz_unit_name: str = None,
        cache_time: str = None,
        create_type: int = None,
        description: str = None,
        direct_datasource_id: int = None,
        direct_datasource_name: str = None,
        env: int = None,
        group_id: int = None,
        group_name: str = None,
        is_logical_table: bool = None,
        is_paged_query: bool = None,
        is_special_sql: bool = None,
        mode: int = None,
        name: str = None,
        open_cache: bool = None,
        project_id: int = None,
        project_name: str = None,
        protocol: int = None,
        public_param_list: List[main_models.GetDataServiceApiDocumentResponseBodyDataPublicParamList] = None,
        request_method: int = None,
        request_param_list: List[main_models.GetDataServiceApiDocumentResponseBodyDataRequestParamList] = None,
        resource_group_id: str = None,
        resource_group_name: str = None,
        response_param_list: List[main_models.GetDataServiceApiDocumentResponseBodyDataResponseParamList] = None,
        result_sample: str = None,
        return_limit: int = None,
        return_type: int = None,
        script_type: str = None,
        sql: str = None,
        table_name: str = None,
        timeout: str = None,
        update_rate: int = None,
        version: str = None,
    ):
        self.api_id = api_id
        self.api_register_info = api_register_info
        self.api_timeout = api_timeout
        self.biz_unit_name = biz_unit_name
        self.cache_time = cache_time
        self.create_type = create_type
        self.description = description
        self.direct_datasource_id = direct_datasource_id
        self.direct_datasource_name = direct_datasource_name
        self.env = env
        self.group_id = group_id
        self.group_name = group_name
        self.is_logical_table = is_logical_table
        self.is_paged_query = is_paged_query
        self.is_special_sql = is_special_sql
        self.mode = mode
        self.name = name
        self.open_cache = open_cache
        self.project_id = project_id
        self.project_name = project_name
        self.protocol = protocol
        self.public_param_list = public_param_list
        self.request_method = request_method
        self.request_param_list = request_param_list
        self.resource_group_id = resource_group_id
        self.resource_group_name = resource_group_name
        self.response_param_list = response_param_list
        self.result_sample = result_sample
        self.return_limit = return_limit
        self.return_type = return_type
        self.script_type = script_type
        self.sql = sql
        self.table_name = table_name
        self.timeout = timeout
        self.update_rate = update_rate
        self.version = version

    def validate(self):
        if self.api_register_info:
            self.api_register_info.validate()
        if self.public_param_list:
            for v1 in self.public_param_list:
                 if v1:
                    v1.validate()
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
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_register_info is not None:
            result['ApiRegisterInfo'] = self.api_register_info.to_map()

        if self.api_timeout is not None:
            result['ApiTimeout'] = self.api_timeout

        if self.biz_unit_name is not None:
            result['BizUnitName'] = self.biz_unit_name

        if self.cache_time is not None:
            result['CacheTime'] = self.cache_time

        if self.create_type is not None:
            result['CreateType'] = self.create_type

        if self.description is not None:
            result['Description'] = self.description

        if self.direct_datasource_id is not None:
            result['DirectDatasourceId'] = self.direct_datasource_id

        if self.direct_datasource_name is not None:
            result['DirectDatasourceName'] = self.direct_datasource_name

        if self.env is not None:
            result['Env'] = self.env

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.is_logical_table is not None:
            result['IsLogicalTable'] = self.is_logical_table

        if self.is_paged_query is not None:
            result['IsPagedQuery'] = self.is_paged_query

        if self.is_special_sql is not None:
            result['IsSpecialSql'] = self.is_special_sql

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.open_cache is not None:
            result['OpenCache'] = self.open_cache

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        result['PublicParamList'] = []
        if self.public_param_list is not None:
            for k1 in self.public_param_list:
                result['PublicParamList'].append(k1.to_map() if k1 else None)

        if self.request_method is not None:
            result['RequestMethod'] = self.request_method

        result['RequestParamList'] = []
        if self.request_param_list is not None:
            for k1 in self.request_param_list:
                result['RequestParamList'].append(k1.to_map() if k1 else None)

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        result['ResponseParamList'] = []
        if self.response_param_list is not None:
            for k1 in self.response_param_list:
                result['ResponseParamList'].append(k1.to_map() if k1 else None)

        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample

        if self.return_limit is not None:
            result['ReturnLimit'] = self.return_limit

        if self.return_type is not None:
            result['ReturnType'] = self.return_type

        if self.script_type is not None:
            result['ScriptType'] = self.script_type

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.update_rate is not None:
            result['UpdateRate'] = self.update_rate

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiRegisterInfo') is not None:
            temp_model = main_models.GetDataServiceApiDocumentResponseBodyDataApiRegisterInfo()
            self.api_register_info = temp_model.from_map(m.get('ApiRegisterInfo'))

        if m.get('ApiTimeout') is not None:
            self.api_timeout = m.get('ApiTimeout')

        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')

        if m.get('CacheTime') is not None:
            self.cache_time = m.get('CacheTime')

        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DirectDatasourceId') is not None:
            self.direct_datasource_id = m.get('DirectDatasourceId')

        if m.get('DirectDatasourceName') is not None:
            self.direct_datasource_name = m.get('DirectDatasourceName')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IsLogicalTable') is not None:
            self.is_logical_table = m.get('IsLogicalTable')

        if m.get('IsPagedQuery') is not None:
            self.is_paged_query = m.get('IsPagedQuery')

        if m.get('IsSpecialSql') is not None:
            self.is_special_sql = m.get('IsSpecialSql')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OpenCache') is not None:
            self.open_cache = m.get('OpenCache')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        self.public_param_list = []
        if m.get('PublicParamList') is not None:
            for k1 in m.get('PublicParamList'):
                temp_model = main_models.GetDataServiceApiDocumentResponseBodyDataPublicParamList()
                self.public_param_list.append(temp_model.from_map(k1))

        if m.get('RequestMethod') is not None:
            self.request_method = m.get('RequestMethod')

        self.request_param_list = []
        if m.get('RequestParamList') is not None:
            for k1 in m.get('RequestParamList'):
                temp_model = main_models.GetDataServiceApiDocumentResponseBodyDataRequestParamList()
                self.request_param_list.append(temp_model.from_map(k1))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        self.response_param_list = []
        if m.get('ResponseParamList') is not None:
            for k1 in m.get('ResponseParamList'):
                temp_model = main_models.GetDataServiceApiDocumentResponseBodyDataResponseParamList()
                self.response_param_list.append(temp_model.from_map(k1))

        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')

        if m.get('ReturnLimit') is not None:
            self.return_limit = m.get('ReturnLimit')

        if m.get('ReturnType') is not None:
            self.return_type = m.get('ReturnType')

        if m.get('ScriptType') is not None:
            self.script_type = m.get('ScriptType')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('UpdateRate') is not None:
            self.update_rate = m.get('UpdateRate')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetDataServiceApiDocumentResponseBodyDataResponseParamList(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        sample: str = None,
        type: str = None,
    ):
        self.description = description
        self.name = name
        self.sample = sample
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.sample is not None:
            result['Sample'] = self.sample

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetDataServiceApiDocumentResponseBodyDataRequestParamList(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        is_required: bool = None,
        name: str = None,
        sample: str = None,
        type: str = None,
    ):
        self.default_value = default_value
        self.description = description
        self.is_required = is_required
        self.name = name
        self.sample = sample
        self.type = type

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

        if self.is_required is not None:
            result['IsRequired'] = self.is_required

        if self.name is not None:
            result['Name'] = self.name

        if self.sample is not None:
            result['Sample'] = self.sample

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsRequired') is not None:
            self.is_required = m.get('IsRequired')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetDataServiceApiDocumentResponseBodyDataPublicParamList(DaraModel):
    def __init__(
        self,
        description: str = None,
        is_required: bool = None,
        name: str = None,
        sample: str = None,
        type: str = None,
    ):
        self.description = description
        self.is_required = is_required
        self.name = name
        self.sample = sample
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.is_required is not None:
            result['IsRequired'] = self.is_required

        if self.name is not None:
            result['Name'] = self.name

        if self.sample is not None:
            result['Sample'] = self.sample

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsRequired') is not None:
            self.is_required = m.get('IsRequired')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetDataServiceApiDocumentResponseBodyDataApiRegisterInfo(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        datasource_id: str = None,
        datasource_name: str = None,
        http_method: int = None,
        mode: int = None,
        path: str = None,
        protocol: str = None,
        timeout: int = None,
        url: str = None,
    ):
        self.auth_type = auth_type
        self.datasource_id = datasource_id
        self.datasource_name = datasource_name
        self.http_method = http_method
        self.mode = mode
        self.path = path
        self.protocol = protocol
        self.timeout = timeout
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id

        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        if self.http_method is not None:
            result['HttpMethod'] = self.http_method

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.path is not None:
            result['Path'] = self.path

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')

        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

