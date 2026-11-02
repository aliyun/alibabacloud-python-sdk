# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class ListGatewayApisResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        apis: List[main_models.ListGatewayApisResponseBodyApis] = None,
        error_field: str = None,
        http_status_code: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.apis = apis
        self.error_field = error_field
        self.http_status_code = http_status_code
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
        self.success = success
        self.total = total

    def validate(self):
        if self.apis:
            for v1 in self.apis:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['Apis'] = []
        if self.apis is not None:
            for k1 in self.apis:
                result['Apis'].append(k1.to_map() if k1 else None)

        if self.error_field is not None:
            result['ErrorField'] = self.error_field

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.apis = []
        if m.get('Apis') is not None:
            for k1 in m.get('Apis'):
                temp_model = main_models.ListGatewayApisResponseBodyApis()
                self.apis.append(temp_model.from_map(k1))

        if m.get('ErrorField') is not None:
            self.error_field = m.get('ErrorField')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListGatewayApisResponseBodyApis(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        api_name: str = None,
        api_status: str = None,
        api_type: str = None,
        auth_rule_name: str = None,
        cache_rule: main_models.ListGatewayApisResponseBodyApisCacheRule = None,
        charset: str = None,
        content_type: str = None,
        default_limit_rule: main_models.ListGatewayApisResponseBodyApisDefaultLimitRule = None,
        description: str = None,
        group_id: int = None,
        header_rules: List[main_models.ListGatewayApisResponseBodyApisHeaderRules] = None,
        interface_type: str = None,
        limit_rule: main_models.ListGatewayApisResponseBodyApisLimitRule = None,
        method: str = None,
        method_name: str = None,
        migrate_rule: main_models.ListGatewayApisResponseBodyApisMigrateRule = None,
        mock_rule: main_models.ListGatewayApisResponseBodyApisMockRule = None,
        need_encrypt: bool = None,
        need_jsonp: bool = None,
        need_sign: bool = None,
        operation_type: str = None,
        path: str = None,
        request_body_model: str = None,
        request_params: List[main_models.ListGatewayApisResponseBodyApisRequestParams] = None,
        response_body_model: str = None,
        rpc_parameter_types: List[str] = None,
        serialization: str = None,
        sys_name: str = None,
        timeout: int = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.api_status = api_status
        self.api_type = api_type
        self.auth_rule_name = auth_rule_name
        self.cache_rule = cache_rule
        self.charset = charset
        self.content_type = content_type
        self.default_limit_rule = default_limit_rule
        self.description = description
        self.group_id = group_id
        self.header_rules = header_rules
        self.interface_type = interface_type
        self.limit_rule = limit_rule
        self.method = method
        self.method_name = method_name
        self.migrate_rule = migrate_rule
        self.mock_rule = mock_rule
        self.need_encrypt = need_encrypt
        self.need_jsonp = need_jsonp
        self.need_sign = need_sign
        self.operation_type = operation_type
        self.path = path
        self.request_body_model = request_body_model
        self.request_params = request_params
        self.response_body_model = response_body_model
        self.rpc_parameter_types = rpc_parameter_types
        self.serialization = serialization
        self.sys_name = sys_name
        self.timeout = timeout

    def validate(self):
        if self.cache_rule:
            self.cache_rule.validate()
        if self.default_limit_rule:
            self.default_limit_rule.validate()
        if self.header_rules:
            for v1 in self.header_rules:
                 if v1:
                    v1.validate()
        if self.limit_rule:
            self.limit_rule.validate()
        if self.migrate_rule:
            self.migrate_rule.validate()
        if self.mock_rule:
            self.mock_rule.validate()
        if self.request_params:
            for v1 in self.request_params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.api_status is not None:
            result['ApiStatus'] = self.api_status

        if self.api_type is not None:
            result['ApiType'] = self.api_type

        if self.auth_rule_name is not None:
            result['AuthRuleName'] = self.auth_rule_name

        if self.cache_rule is not None:
            result['CacheRule'] = self.cache_rule.to_map()

        if self.charset is not None:
            result['Charset'] = self.charset

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.default_limit_rule is not None:
            result['DefaultLimitRule'] = self.default_limit_rule.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        result['HeaderRules'] = []
        if self.header_rules is not None:
            for k1 in self.header_rules:
                result['HeaderRules'].append(k1.to_map() if k1 else None)

        if self.interface_type is not None:
            result['InterfaceType'] = self.interface_type

        if self.limit_rule is not None:
            result['LimitRule'] = self.limit_rule.to_map()

        if self.method is not None:
            result['Method'] = self.method

        if self.method_name is not None:
            result['MethodName'] = self.method_name

        if self.migrate_rule is not None:
            result['MigrateRule'] = self.migrate_rule.to_map()

        if self.mock_rule is not None:
            result['MockRule'] = self.mock_rule.to_map()

        if self.need_encrypt is not None:
            result['NeedEncrypt'] = self.need_encrypt

        if self.need_jsonp is not None:
            result['NeedJsonp'] = self.need_jsonp

        if self.need_sign is not None:
            result['NeedSign'] = self.need_sign

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.path is not None:
            result['Path'] = self.path

        if self.request_body_model is not None:
            result['RequestBodyModel'] = self.request_body_model

        result['RequestParams'] = []
        if self.request_params is not None:
            for k1 in self.request_params:
                result['RequestParams'].append(k1.to_map() if k1 else None)

        if self.response_body_model is not None:
            result['ResponseBodyModel'] = self.response_body_model

        if self.rpc_parameter_types is not None:
            result['RpcParameterTypes'] = self.rpc_parameter_types

        if self.serialization is not None:
            result['Serialization'] = self.serialization

        if self.sys_name is not None:
            result['SysName'] = self.sys_name

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('ApiStatus') is not None:
            self.api_status = m.get('ApiStatus')

        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')

        if m.get('AuthRuleName') is not None:
            self.auth_rule_name = m.get('AuthRuleName')

        if m.get('CacheRule') is not None:
            temp_model = main_models.ListGatewayApisResponseBodyApisCacheRule()
            self.cache_rule = temp_model.from_map(m.get('CacheRule'))

        if m.get('Charset') is not None:
            self.charset = m.get('Charset')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('DefaultLimitRule') is not None:
            temp_model = main_models.ListGatewayApisResponseBodyApisDefaultLimitRule()
            self.default_limit_rule = temp_model.from_map(m.get('DefaultLimitRule'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        self.header_rules = []
        if m.get('HeaderRules') is not None:
            for k1 in m.get('HeaderRules'):
                temp_model = main_models.ListGatewayApisResponseBodyApisHeaderRules()
                self.header_rules.append(temp_model.from_map(k1))

        if m.get('InterfaceType') is not None:
            self.interface_type = m.get('InterfaceType')

        if m.get('LimitRule') is not None:
            temp_model = main_models.ListGatewayApisResponseBodyApisLimitRule()
            self.limit_rule = temp_model.from_map(m.get('LimitRule'))

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')

        if m.get('MigrateRule') is not None:
            temp_model = main_models.ListGatewayApisResponseBodyApisMigrateRule()
            self.migrate_rule = temp_model.from_map(m.get('MigrateRule'))

        if m.get('MockRule') is not None:
            temp_model = main_models.ListGatewayApisResponseBodyApisMockRule()
            self.mock_rule = temp_model.from_map(m.get('MockRule'))

        if m.get('NeedEncrypt') is not None:
            self.need_encrypt = m.get('NeedEncrypt')

        if m.get('NeedJsonp') is not None:
            self.need_jsonp = m.get('NeedJsonp')

        if m.get('NeedSign') is not None:
            self.need_sign = m.get('NeedSign')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('RequestBodyModel') is not None:
            self.request_body_model = m.get('RequestBodyModel')

        self.request_params = []
        if m.get('RequestParams') is not None:
            for k1 in m.get('RequestParams'):
                temp_model = main_models.ListGatewayApisResponseBodyApisRequestParams()
                self.request_params.append(temp_model.from_map(k1))

        if m.get('ResponseBodyModel') is not None:
            self.response_body_model = m.get('ResponseBodyModel')

        if m.get('RpcParameterTypes') is not None:
            self.rpc_parameter_types = m.get('RpcParameterTypes')

        if m.get('Serialization') is not None:
            self.serialization = m.get('Serialization')

        if m.get('SysName') is not None:
            self.sys_name = m.get('SysName')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class ListGatewayApisResponseBodyApisRequestParams(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        location: str = None,
        name: str = None,
        ref_type: str = None,
        type: str = None,
    ):
        self.default_value = default_value
        self.description = description
        self.location = location
        self.name = name
        self.ref_type = ref_type
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

        if self.location is not None:
            result['Location'] = self.location

        if self.name is not None:
            result['Name'] = self.name

        if self.ref_type is not None:
            result['RefType'] = self.ref_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RefType') is not None:
            self.ref_type = m.get('RefType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListGatewayApisResponseBodyApisMockRule(DaraModel):
    def __init__(
        self,
        mock_data: str = None,
        need_mock: bool = None,
        percentage: int = None,
        type: str = None,
    ):
        self.mock_data = mock_data
        self.need_mock = need_mock
        self.percentage = percentage
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mock_data is not None:
            result['MockData'] = self.mock_data

        if self.need_mock is not None:
            result['NeedMock'] = self.need_mock

        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MockData') is not None:
            self.mock_data = m.get('MockData')

        if m.get('NeedMock') is not None:
            self.need_mock = m.get('NeedMock')

        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListGatewayApisResponseBodyApisMigrateRule(DaraModel):
    def __init__(
        self,
        flow_percent: int = None,
        group_id: int = None,
        group_name: str = None,
        need_migrate: bool = None,
        need_switch_completely: bool = None,
        upstream_type: str = None,
    ):
        self.flow_percent = flow_percent
        self.group_id = group_id
        self.group_name = group_name
        self.need_migrate = need_migrate
        self.need_switch_completely = need_switch_completely
        self.upstream_type = upstream_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.need_migrate is not None:
            result['NeedMigrate'] = self.need_migrate

        if self.need_switch_completely is not None:
            result['NeedSwitchCompletely'] = self.need_switch_completely

        if self.upstream_type is not None:
            result['UpstreamType'] = self.upstream_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('NeedMigrate') is not None:
            self.need_migrate = m.get('NeedMigrate')

        if m.get('NeedSwitchCompletely') is not None:
            self.need_switch_completely = m.get('NeedSwitchCompletely')

        if m.get('UpstreamType') is not None:
            self.upstream_type = m.get('UpstreamType')

        return self

class ListGatewayApisResponseBodyApisLimitRule(DaraModel):
    def __init__(
        self,
        default_response: str = None,
        limit: float = None,
        mode: str = None,
    ):
        self.default_response = default_response
        self.limit = limit
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_response is not None:
            result['DefaultResponse'] = self.default_response

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultResponse') is not None:
            self.default_response = m.get('DefaultResponse')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

class ListGatewayApisResponseBodyApisHeaderRules(DaraModel):
    def __init__(
        self,
        header_key: str = None,
        location: str = None,
        type: str = None,
        value: str = None,
    ):
        self.header_key = header_key
        self.location = location
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.header_key is not None:
            result['HeaderKey'] = self.header_key

        if self.location is not None:
            result['Location'] = self.location

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeaderKey') is not None:
            self.header_key = m.get('HeaderKey')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListGatewayApisResponseBodyApisDefaultLimitRule(DaraModel):
    def __init__(
        self,
        default_limit: bool = None,
    ):
        self.default_limit = default_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_limit is not None:
            result['DefaultLimit'] = self.default_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultLimit') is not None:
            self.default_limit = m.get('DefaultLimit')

        return self

class ListGatewayApisResponseBodyApisCacheRule(DaraModel):
    def __init__(
        self,
        cache_key: str = None,
        need_cache: bool = None,
        ttl: int = None,
    ):
        self.cache_key = cache_key
        self.need_cache = need_cache
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_key is not None:
            result['CacheKey'] = self.cache_key

        if self.need_cache is not None:
            result['NeedCache'] = self.need_cache

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheKey') is not None:
            self.cache_key = m.get('CacheKey')

        if m.get('NeedCache') is not None:
            self.need_cache = m.get('NeedCache')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

