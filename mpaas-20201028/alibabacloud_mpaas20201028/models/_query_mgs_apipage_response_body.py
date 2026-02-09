# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class QueryMgsApipageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: main_models.QueryMgsApipageResponseBodyResultContent = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultContent') is not None:
            temp_model = main_models.QueryMgsApipageResponseBodyResultContent()
            self.result_content = temp_model.from_map(m.get('ResultContent'))

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class QueryMgsApipageResponseBodyResultContent(DaraModel):
    def __init__(
        self,
        current: int = None,
        list: List[main_models.QueryMgsApipageResponseBodyResultContentList] = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current = current
        self.list = list
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current is not None:
            result['Current'] = self.current

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.QueryMgsApipageResponseBodyResultContentList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryMgsApipageResponseBodyResultContentList(DaraModel):
    def __init__(
        self,
        api_invoker: main_models.QueryMgsApipageResponseBodyResultContentListApiInvoker = None,
        api_name: str = None,
        api_status: str = None,
        api_type: str = None,
        app_id: str = None,
        auth_rule_name: str = None,
        cache_rule: main_models.QueryMgsApipageResponseBodyResultContentListCacheRule = None,
        charset: str = None,
        circuit_breaker_rule: main_models.QueryMgsApipageResponseBodyResultContentListCircuitBreakerRule = None,
        content_type: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        header_rule: List[main_models.QueryMgsApipageResponseBodyResultContentListHeaderRule] = None,
        header_rules: List[main_models.QueryMgsApipageResponseBodyResultContentListHeaderRules] = None,
        host: str = None,
        id: int = None,
        interface_type: str = None,
        limit_rule: main_models.QueryMgsApipageResponseBodyResultContentListLimitRule = None,
        method: str = None,
        method_name: str = None,
        migrate_rule: main_models.QueryMgsApipageResponseBodyResultContentListMigrateRule = None,
        mock_rule: main_models.QueryMgsApipageResponseBodyResultContentListMockRule = None,
        need_etag: str = None,
        need_encrypt: str = None,
        need_jsonp: str = None,
        need_sign: str = None,
        operation_type: str = None,
        param_get_method: str = None,
        path: str = None,
        request_body_model: str = None,
        request_params: List[main_models.QueryMgsApipageResponseBodyResultContentListRequestParams] = None,
        response_body_model: str = None,
        sys_id: int = None,
        sys_name: str = None,
        timeout: str = None,
        workspace_id: str = None,
    ):
        self.api_invoker = api_invoker
        self.api_name = api_name
        self.api_status = api_status
        self.api_type = api_type
        self.app_id = app_id
        self.auth_rule_name = auth_rule_name
        self.cache_rule = cache_rule
        self.charset = charset
        self.circuit_breaker_rule = circuit_breaker_rule
        self.content_type = content_type
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.header_rule = header_rule
        self.header_rules = header_rules
        self.host = host
        self.id = id
        self.interface_type = interface_type
        self.limit_rule = limit_rule
        self.method = method
        self.method_name = method_name
        self.migrate_rule = migrate_rule
        self.mock_rule = mock_rule
        self.need_etag = need_etag
        self.need_encrypt = need_encrypt
        self.need_jsonp = need_jsonp
        self.need_sign = need_sign
        self.operation_type = operation_type
        self.param_get_method = param_get_method
        self.path = path
        self.request_body_model = request_body_model
        self.request_params = request_params
        self.response_body_model = response_body_model
        self.sys_id = sys_id
        self.sys_name = sys_name
        self.timeout = timeout
        self.workspace_id = workspace_id

    def validate(self):
        if self.api_invoker:
            self.api_invoker.validate()
        if self.cache_rule:
            self.cache_rule.validate()
        if self.circuit_breaker_rule:
            self.circuit_breaker_rule.validate()
        if self.header_rule:
            for v1 in self.header_rule:
                 if v1:
                    v1.validate()
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
        if self.api_invoker is not None:
            result['ApiInvoker'] = self.api_invoker.to_map()

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.api_status is not None:
            result['ApiStatus'] = self.api_status

        if self.api_type is not None:
            result['ApiType'] = self.api_type

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.auth_rule_name is not None:
            result['AuthRuleName'] = self.auth_rule_name

        if self.cache_rule is not None:
            result['CacheRule'] = self.cache_rule.to_map()

        if self.charset is not None:
            result['Charset'] = self.charset

        if self.circuit_breaker_rule is not None:
            result['CircuitBreakerRule'] = self.circuit_breaker_rule.to_map()

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        result['HeaderRule'] = []
        if self.header_rule is not None:
            for k1 in self.header_rule:
                result['HeaderRule'].append(k1.to_map() if k1 else None)

        result['HeaderRules'] = []
        if self.header_rules is not None:
            for k1 in self.header_rules:
                result['HeaderRules'].append(k1.to_map() if k1 else None)

        if self.host is not None:
            result['Host'] = self.host

        if self.id is not None:
            result['Id'] = self.id

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

        if self.need_etag is not None:
            result['NeedETag'] = self.need_etag

        if self.need_encrypt is not None:
            result['NeedEncrypt'] = self.need_encrypt

        if self.need_jsonp is not None:
            result['NeedJsonp'] = self.need_jsonp

        if self.need_sign is not None:
            result['NeedSign'] = self.need_sign

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.param_get_method is not None:
            result['ParamGetMethod'] = self.param_get_method

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

        if self.sys_id is not None:
            result['SysId'] = self.sys_id

        if self.sys_name is not None:
            result['SysName'] = self.sys_name

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiInvoker') is not None:
            temp_model = main_models.QueryMgsApipageResponseBodyResultContentListApiInvoker()
            self.api_invoker = temp_model.from_map(m.get('ApiInvoker'))

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('ApiStatus') is not None:
            self.api_status = m.get('ApiStatus')

        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AuthRuleName') is not None:
            self.auth_rule_name = m.get('AuthRuleName')

        if m.get('CacheRule') is not None:
            temp_model = main_models.QueryMgsApipageResponseBodyResultContentListCacheRule()
            self.cache_rule = temp_model.from_map(m.get('CacheRule'))

        if m.get('Charset') is not None:
            self.charset = m.get('Charset')

        if m.get('CircuitBreakerRule') is not None:
            temp_model = main_models.QueryMgsApipageResponseBodyResultContentListCircuitBreakerRule()
            self.circuit_breaker_rule = temp_model.from_map(m.get('CircuitBreakerRule'))

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        self.header_rule = []
        if m.get('HeaderRule') is not None:
            for k1 in m.get('HeaderRule'):
                temp_model = main_models.QueryMgsApipageResponseBodyResultContentListHeaderRule()
                self.header_rule.append(temp_model.from_map(k1))

        self.header_rules = []
        if m.get('HeaderRules') is not None:
            for k1 in m.get('HeaderRules'):
                temp_model = main_models.QueryMgsApipageResponseBodyResultContentListHeaderRules()
                self.header_rules.append(temp_model.from_map(k1))

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InterfaceType') is not None:
            self.interface_type = m.get('InterfaceType')

        if m.get('LimitRule') is not None:
            temp_model = main_models.QueryMgsApipageResponseBodyResultContentListLimitRule()
            self.limit_rule = temp_model.from_map(m.get('LimitRule'))

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')

        if m.get('MigrateRule') is not None:
            temp_model = main_models.QueryMgsApipageResponseBodyResultContentListMigrateRule()
            self.migrate_rule = temp_model.from_map(m.get('MigrateRule'))

        if m.get('MockRule') is not None:
            temp_model = main_models.QueryMgsApipageResponseBodyResultContentListMockRule()
            self.mock_rule = temp_model.from_map(m.get('MockRule'))

        if m.get('NeedETag') is not None:
            self.need_etag = m.get('NeedETag')

        if m.get('NeedEncrypt') is not None:
            self.need_encrypt = m.get('NeedEncrypt')

        if m.get('NeedJsonp') is not None:
            self.need_jsonp = m.get('NeedJsonp')

        if m.get('NeedSign') is not None:
            self.need_sign = m.get('NeedSign')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('ParamGetMethod') is not None:
            self.param_get_method = m.get('ParamGetMethod')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('RequestBodyModel') is not None:
            self.request_body_model = m.get('RequestBodyModel')

        self.request_params = []
        if m.get('RequestParams') is not None:
            for k1 in m.get('RequestParams'):
                temp_model = main_models.QueryMgsApipageResponseBodyResultContentListRequestParams()
                self.request_params.append(temp_model.from_map(k1))

        if m.get('ResponseBodyModel') is not None:
            self.response_body_model = m.get('ResponseBodyModel')

        if m.get('SysId') is not None:
            self.sys_id = m.get('SysId')

        if m.get('SysName') is not None:
            self.sys_name = m.get('SysName')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class QueryMgsApipageResponseBodyResultContentListRequestParams(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        app_id: str = None,
        default_value: str = None,
        description: str = None,
        id: int = None,
        location: str = None,
        name: str = None,
        ref_type: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        self.api_id = api_id
        self.app_id = app_id
        self.default_value = default_value
        self.description = description
        self.id = id
        self.location = location
        self.name = name
        self.ref_type = ref_type
        self.type = type
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.location is not None:
            result['Location'] = self.location

        if self.name is not None:
            result['Name'] = self.name

        if self.ref_type is not None:
            result['RefType'] = self.ref_type

        if self.type is not None:
            result['Type'] = self.type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RefType') is not None:
            self.ref_type = m.get('RefType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class QueryMgsApipageResponseBodyResultContentListMockRule(DaraModel):
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

class QueryMgsApipageResponseBodyResultContentListMigrateRule(DaraModel):
    def __init__(
        self,
        flow_percent: int = None,
        need_migrate: bool = None,
        need_switch_completely: bool = None,
        sys_id: int = None,
        sys_name: str = None,
        upstream_type: str = None,
    ):
        self.flow_percent = flow_percent
        self.need_migrate = need_migrate
        self.need_switch_completely = need_switch_completely
        self.sys_id = sys_id
        self.sys_name = sys_name
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

        if self.need_migrate is not None:
            result['NeedMigrate'] = self.need_migrate

        if self.need_switch_completely is not None:
            result['NeedSwitchCompletely'] = self.need_switch_completely

        if self.sys_id is not None:
            result['SysId'] = self.sys_id

        if self.sys_name is not None:
            result['SysName'] = self.sys_name

        if self.upstream_type is not None:
            result['UpstreamType'] = self.upstream_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')

        if m.get('NeedMigrate') is not None:
            self.need_migrate = m.get('NeedMigrate')

        if m.get('NeedSwitchCompletely') is not None:
            self.need_switch_completely = m.get('NeedSwitchCompletely')

        if m.get('SysId') is not None:
            self.sys_id = m.get('SysId')

        if m.get('SysName') is not None:
            self.sys_name = m.get('SysName')

        if m.get('UpstreamType') is not None:
            self.upstream_type = m.get('UpstreamType')

        return self

class QueryMgsApipageResponseBodyResultContentListLimitRule(DaraModel):
    def __init__(
        self,
        default_response: str = None,
        i_18n_response: str = None,
        interval: int = None,
        limit: int = None,
        mode: str = None,
    ):
        self.default_response = default_response
        self.i_18n_response = i_18n_response
        self.interval = interval
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

        if self.i_18n_response is not None:
            result['I18nResponse'] = self.i_18n_response

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultResponse') is not None:
            self.default_response = m.get('DefaultResponse')

        if m.get('I18nResponse') is not None:
            self.i_18n_response = m.get('I18nResponse')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

class QueryMgsApipageResponseBodyResultContentListHeaderRules(DaraModel):
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

class QueryMgsApipageResponseBodyResultContentListHeaderRule(DaraModel):
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

class QueryMgsApipageResponseBodyResultContentListCircuitBreakerRule(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        default_response: str = None,
        error_threshold: int = None,
        id: int = None,
        model: str = None,
        open_timeout_seconds: int = None,
        slow_ratio_threshold: float = None,
        switch_status: str = None,
        windows_in_seconds: int = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.default_response = default_response
        self.error_threshold = error_threshold
        self.id = id
        self.model = model
        self.open_timeout_seconds = open_timeout_seconds
        self.slow_ratio_threshold = slow_ratio_threshold
        self.switch_status = switch_status
        self.windows_in_seconds = windows_in_seconds
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.default_response is not None:
            result['DefaultResponse'] = self.default_response

        if self.error_threshold is not None:
            result['ErrorThreshold'] = self.error_threshold

        if self.id is not None:
            result['Id'] = self.id

        if self.model is not None:
            result['Model'] = self.model

        if self.open_timeout_seconds is not None:
            result['OpenTimeoutSeconds'] = self.open_timeout_seconds

        if self.slow_ratio_threshold is not None:
            result['SlowRatioThreshold'] = self.slow_ratio_threshold

        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status

        if self.windows_in_seconds is not None:
            result['WindowsInSeconds'] = self.windows_in_seconds

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DefaultResponse') is not None:
            self.default_response = m.get('DefaultResponse')

        if m.get('ErrorThreshold') is not None:
            self.error_threshold = m.get('ErrorThreshold')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('OpenTimeoutSeconds') is not None:
            self.open_timeout_seconds = m.get('OpenTimeoutSeconds')

        if m.get('SlowRatioThreshold') is not None:
            self.slow_ratio_threshold = m.get('SlowRatioThreshold')

        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')

        if m.get('WindowsInSeconds') is not None:
            self.windows_in_seconds = m.get('WindowsInSeconds')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class QueryMgsApipageResponseBodyResultContentListCacheRule(DaraModel):
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

class QueryMgsApipageResponseBodyResultContentListApiInvoker(DaraModel):
    def __init__(
        self,
        http_invoker: main_models.QueryMgsApipageResponseBodyResultContentListApiInvokerHttpInvoker = None,
        rpc_invoker: str = None,
    ):
        self.http_invoker = http_invoker
        self.rpc_invoker = rpc_invoker

    def validate(self):
        if self.http_invoker:
            self.http_invoker.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_invoker is not None:
            result['HttpInvoker'] = self.http_invoker.to_map()

        if self.rpc_invoker is not None:
            result['RpcInvoker'] = self.rpc_invoker

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpInvoker') is not None:
            temp_model = main_models.QueryMgsApipageResponseBodyResultContentListApiInvokerHttpInvoker()
            self.http_invoker = temp_model.from_map(m.get('HttpInvoker'))

        if m.get('RpcInvoker') is not None:
            self.rpc_invoker = m.get('RpcInvoker')

        return self

class QueryMgsApipageResponseBodyResultContentListApiInvokerHttpInvoker(DaraModel):
    def __init__(
        self,
        charset: str = None,
        content_type: str = None,
        host: str = None,
        method: str = None,
        path: str = None,
    ):
        self.charset = charset
        self.content_type = content_type
        self.host = host
        self.method = method
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charset is not None:
            result['Charset'] = self.charset

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.host is not None:
            result['Host'] = self.host

        if self.method is not None:
            result['Method'] = self.method

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

