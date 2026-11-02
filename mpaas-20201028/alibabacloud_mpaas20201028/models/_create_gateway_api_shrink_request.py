# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGatewayApiShrinkRequest(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        api_status: str = None,
        api_type: str = None,
        app_id: str = None,
        auth_rule_name: str = None,
        cache_rule_shrink: str = None,
        charset: str = None,
        content_type: str = None,
        default_limit_rule_shrink: str = None,
        description: str = None,
        group_id: int = None,
        header_rules_shrink: str = None,
        interface_type: str = None,
        limit_rule_shrink: str = None,
        method: str = None,
        method_name: str = None,
        migrate_rule_shrink: str = None,
        mock_rule_shrink: str = None,
        need_encrypt: bool = None,
        need_jsonp: bool = None,
        need_sign: bool = None,
        operation_type: str = None,
        path: str = None,
        request_body_model: str = None,
        request_params_shrink: str = None,
        response_body_model: str = None,
        rpc_parameter_types_shrink: str = None,
        serialization: str = None,
        tenant_id: str = None,
        timeout: int = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.api_name = api_name
        self.api_status = api_status
        # This parameter is required.
        self.api_type = api_type
        # This parameter is required.
        self.app_id = app_id
        self.auth_rule_name = auth_rule_name
        self.cache_rule_shrink = cache_rule_shrink
        self.charset = charset
        self.content_type = content_type
        self.default_limit_rule_shrink = default_limit_rule_shrink
        self.description = description
        # This parameter is required.
        self.group_id = group_id
        self.header_rules_shrink = header_rules_shrink
        self.interface_type = interface_type
        self.limit_rule_shrink = limit_rule_shrink
        self.method = method
        self.method_name = method_name
        self.migrate_rule_shrink = migrate_rule_shrink
        self.mock_rule_shrink = mock_rule_shrink
        self.need_encrypt = need_encrypt
        self.need_jsonp = need_jsonp
        self.need_sign = need_sign
        # This parameter is required.
        self.operation_type = operation_type
        self.path = path
        self.request_body_model = request_body_model
        self.request_params_shrink = request_params_shrink
        self.response_body_model = response_body_model
        self.rpc_parameter_types_shrink = rpc_parameter_types_shrink
        self.serialization = serialization
        # This parameter is required.
        self.tenant_id = tenant_id
        self.timeout = timeout
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.cache_rule_shrink is not None:
            result['CacheRule'] = self.cache_rule_shrink

        if self.charset is not None:
            result['Charset'] = self.charset

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.default_limit_rule_shrink is not None:
            result['DefaultLimitRule'] = self.default_limit_rule_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.header_rules_shrink is not None:
            result['HeaderRules'] = self.header_rules_shrink

        if self.interface_type is not None:
            result['InterfaceType'] = self.interface_type

        if self.limit_rule_shrink is not None:
            result['LimitRule'] = self.limit_rule_shrink

        if self.method is not None:
            result['Method'] = self.method

        if self.method_name is not None:
            result['MethodName'] = self.method_name

        if self.migrate_rule_shrink is not None:
            result['MigrateRule'] = self.migrate_rule_shrink

        if self.mock_rule_shrink is not None:
            result['MockRule'] = self.mock_rule_shrink

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

        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink

        if self.response_body_model is not None:
            result['ResponseBodyModel'] = self.response_body_model

        if self.rpc_parameter_types_shrink is not None:
            result['RpcParameterTypes'] = self.rpc_parameter_types_shrink

        if self.serialization is not None:
            result['Serialization'] = self.serialization

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
            self.cache_rule_shrink = m.get('CacheRule')

        if m.get('Charset') is not None:
            self.charset = m.get('Charset')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('DefaultLimitRule') is not None:
            self.default_limit_rule_shrink = m.get('DefaultLimitRule')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HeaderRules') is not None:
            self.header_rules_shrink = m.get('HeaderRules')

        if m.get('InterfaceType') is not None:
            self.interface_type = m.get('InterfaceType')

        if m.get('LimitRule') is not None:
            self.limit_rule_shrink = m.get('LimitRule')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')

        if m.get('MigrateRule') is not None:
            self.migrate_rule_shrink = m.get('MigrateRule')

        if m.get('MockRule') is not None:
            self.mock_rule_shrink = m.get('MockRule')

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

        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')

        if m.get('ResponseBodyModel') is not None:
            self.response_body_model = m.get('ResponseBodyModel')

        if m.get('RpcParameterTypes') is not None:
            self.rpc_parameter_types_shrink = m.get('RpcParameterTypes')

        if m.get('Serialization') is not None:
            self.serialization = m.get('Serialization')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

