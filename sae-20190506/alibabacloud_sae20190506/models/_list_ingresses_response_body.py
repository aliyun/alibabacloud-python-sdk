# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListIngressesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListIngressesResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The request was successful.
        # *   **3xx**: The request was redirected.
        # *   **4xx**: The request failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The result returned.
        self.data = data
        # The error code returned if the request failed. Valid values:
        # 
        # *   **ErrorCode** is not returned if a request is successful.
        # *   **ErrorCode** is returned if a request failed. For more information, see **Error codes**.
        self.error_code = error_code
        # The message returned. Valid values:
        # 
        # *   **success** is returned when a request is successful.
        # *   An error code is returned when a request failed.
        self.message = message
        # The ID of a request.
        self.request_id = request_id
        # Indicates whether the list of Ingresses was obtained. Valid values:
        # 
        # *   **true**: The list were obtained.
        # *   **false**: The list failed to be queried.
        self.success = success
        # The ID of a trace. The ID is used to query the details of a request.
        self.trace_id = trace_id

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListIngressesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class ListIngressesResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        ingress_list: List[main_models.ListIngressesResponseBodyDataIngressList] = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.current_page = current_page
        # The list of routing rules.
        self.ingress_list = ingress_list
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.ingress_list:
            for v1 in self.ingress_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['IngressList'] = []
        if self.ingress_list is not None:
            for k1 in self.ingress_list:
                result['IngressList'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.ingress_list = []
        if m.get('IngressList') is not None:
            for k1 in m.get('IngressList'):
                temp_model = main_models.ListIngressesResponseBodyDataIngressList()
                self.ingress_list.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListIngressesResponseBodyDataIngressList(DaraModel):
    def __init__(
        self,
        cert_id: str = None,
        cert_ids: str = None,
        cors_config: main_models.ListIngressesResponseBodyDataIngressListCorsConfig = None,
        create_time: int = None,
        default_rule: main_models.ListIngressesResponseBodyDataIngressListDefaultRule = None,
        description: str = None,
        id: int = None,
        idle_timeout: int = None,
        listener_port: str = None,
        listener_protocol: str = None,
        load_balance_type: str = None,
        mse_gateway_id: str = None,
        mse_gateway_port: str = None,
        mse_gateway_protocol: str = None,
        name: str = None,
        namespace_id: str = None,
        request_timeout: int = None,
        rules: List[main_models.ListIngressesResponseBodyDataIngressListRules] = None,
        slb_id: str = None,
        slb_type: str = None,
    ):
        # The ID of the certificate that is associated with a Classic Load Balancer (**CLB**) instance.
        self.cert_id = cert_id
        # The ID of the certificate that is associated with an Application Load Balancer **ALB** instance.
        self.cert_ids = cert_ids
        self.cors_config = cors_config
        self.create_time = create_time
        self.default_rule = default_rule
        # The name of a routing rule.
        self.description = description
        # The ID of a routing rule.
        self.id = id
        self.idle_timeout = idle_timeout
        # The listener ports for an SLB instance.
        self.listener_port = listener_port
        # The protocol that is supported by SLB to forward requests. Valid values:
        # 
        # *   **HTTP**: HTTP is suitable for applications that need to identify the transmitted data.
        # *   **HTTPS**: HTTPS is suitable for applications that require encrypted data transmission.
        # 
        # This parameter is optional in the **CreateIngress** and **UpadateIngress** operations. If you do not configure this parameter when you call the CreateIngress or UpdateIngress operation to create or update a gateway routing rule, this parameter is not returned for the corresponding response.
        self.listener_protocol = listener_protocol
        # The type of SLB instances. Valid values:
        # 
        # *   **clb**: Classic Load Balancer (formerly known as SLB).
        # *   **alb**: Application Load Balancer.
        self.load_balance_type = load_balance_type
        # The ID of an MSE cloud-native gateway.
        self.mse_gateway_id = mse_gateway_id
        # The port of a service.
        self.mse_gateway_port = mse_gateway_port
        # The protocol that is supported by an MSE cloud-native gateway to forward requests. Valid values:
        # 
        # *   **HTTP**: HTTP is suitable for applications that need to identify transmitted data.
        # *   **HTTPS**: HTTPS is suitable for applications that require encrypted data transmission.
        self.mse_gateway_protocol = mse_gateway_protocol
        # The name of a routing rule.
        self.name = name
        # The ID of a namespace.
        self.namespace_id = namespace_id
        self.request_timeout = request_timeout
        self.rules = rules
        # The ID of a Server Load Balancer (SLB) instance.
        self.slb_id = slb_id
        # The type of SLB instances. Valid values:
        # 
        # *   **internet**: an Internet-facing SLB instance
        # *   **intranet**: an Intranet-facing SLB instance
        self.slb_type = slb_type

    def validate(self):
        if self.cors_config:
            self.cors_config.validate()
        if self.default_rule:
            self.default_rule.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_ids is not None:
            result['CertIds'] = self.cert_ids

        if self.cors_config is not None:
            result['CorsConfig'] = self.cors_config.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol

        if self.load_balance_type is not None:
            result['LoadBalanceType'] = self.load_balance_type

        if self.mse_gateway_id is not None:
            result['MseGatewayId'] = self.mse_gateway_id

        if self.mse_gateway_port is not None:
            result['MseGatewayPort'] = self.mse_gateway_port

        if self.mse_gateway_protocol is not None:
            result['MseGatewayProtocol'] = self.mse_gateway_protocol

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.slb_type is not None:
            result['SlbType'] = self.slb_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertIds') is not None:
            self.cert_ids = m.get('CertIds')

        if m.get('CorsConfig') is not None:
            temp_model = main_models.ListIngressesResponseBodyDataIngressListCorsConfig()
            self.cors_config = temp_model.from_map(m.get('CorsConfig'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultRule') is not None:
            temp_model = main_models.ListIngressesResponseBodyDataIngressListDefaultRule()
            self.default_rule = temp_model.from_map(m.get('DefaultRule'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')

        if m.get('LoadBalanceType') is not None:
            self.load_balance_type = m.get('LoadBalanceType')

        if m.get('MseGatewayId') is not None:
            self.mse_gateway_id = m.get('MseGatewayId')

        if m.get('MseGatewayPort') is not None:
            self.mse_gateway_port = m.get('MseGatewayPort')

        if m.get('MseGatewayProtocol') is not None:
            self.mse_gateway_protocol = m.get('MseGatewayProtocol')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.ListIngressesResponseBodyDataIngressListRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('SlbType') is not None:
            self.slb_type = m.get('SlbType')

        return self

class ListIngressesResponseBodyDataIngressListRules(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        backend_protocol: str = None,
        container_port: int = None,
        domain: str = None,
        path: str = None,
        rewrite_path: str = None,
        rule_actions: List[main_models.ListIngressesResponseBodyDataIngressListRulesRuleActions] = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.backend_protocol = backend_protocol
        self.container_port = container_port
        self.domain = domain
        self.path = path
        self.rewrite_path = rewrite_path
        self.rule_actions = rule_actions

    def validate(self):
        if self.rule_actions:
            for v1 in self.rule_actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.backend_protocol is not None:
            result['BackendProtocol'] = self.backend_protocol

        if self.container_port is not None:
            result['ContainerPort'] = self.container_port

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.path is not None:
            result['Path'] = self.path

        if self.rewrite_path is not None:
            result['RewritePath'] = self.rewrite_path

        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k1 in self.rule_actions:
                result['RuleActions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BackendProtocol') is not None:
            self.backend_protocol = m.get('BackendProtocol')

        if m.get('ContainerPort') is not None:
            self.container_port = m.get('ContainerPort')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('RewritePath') is not None:
            self.rewrite_path = m.get('RewritePath')

        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k1 in m.get('RuleActions'):
                temp_model = main_models.ListIngressesResponseBodyDataIngressListRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k1))

        return self

class ListIngressesResponseBodyDataIngressListRulesRuleActions(DaraModel):
    def __init__(
        self,
        action_config: str = None,
        action_type: str = None,
    ):
        self.action_config = action_config
        self.action_type = action_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_config is not None:
            result['ActionConfig'] = self.action_config

        if self.action_type is not None:
            result['ActionType'] = self.action_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionConfig') is not None:
            self.action_config = m.get('ActionConfig')

        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        return self

class ListIngressesResponseBodyDataIngressListDefaultRule(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        backend_protocol: str = None,
        container_port: int = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.backend_protocol = backend_protocol
        self.container_port = container_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.backend_protocol is not None:
            result['BackendProtocol'] = self.backend_protocol

        if self.container_port is not None:
            result['ContainerPort'] = self.container_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BackendProtocol') is not None:
            self.backend_protocol = m.get('BackendProtocol')

        if m.get('ContainerPort') is not None:
            self.container_port = m.get('ContainerPort')

        return self

class ListIngressesResponseBodyDataIngressListCorsConfig(DaraModel):
    def __init__(
        self,
        allow_credentials: str = None,
        allow_headers: str = None,
        allow_methods: str = None,
        allow_origin: str = None,
        enable: str = None,
        expose_headers: str = None,
        max_age: str = None,
    ):
        self.allow_credentials = allow_credentials
        self.allow_headers = allow_headers
        self.allow_methods = allow_methods
        self.allow_origin = allow_origin
        self.enable = enable
        self.expose_headers = expose_headers
        self.max_age = max_age

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_credentials is not None:
            result['AllowCredentials'] = self.allow_credentials

        if self.allow_headers is not None:
            result['AllowHeaders'] = self.allow_headers

        if self.allow_methods is not None:
            result['AllowMethods'] = self.allow_methods

        if self.allow_origin is not None:
            result['AllowOrigin'] = self.allow_origin

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.expose_headers is not None:
            result['ExposeHeaders'] = self.expose_headers

        if self.max_age is not None:
            result['MaxAge'] = self.max_age

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCredentials') is not None:
            self.allow_credentials = m.get('AllowCredentials')

        if m.get('AllowHeaders') is not None:
            self.allow_headers = m.get('AllowHeaders')

        if m.get('AllowMethods') is not None:
            self.allow_methods = m.get('AllowMethods')

        if m.get('AllowOrigin') is not None:
            self.allow_origin = m.get('AllowOrigin')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('ExposeHeaders') is not None:
            self.expose_headers = m.get('ExposeHeaders')

        if m.get('MaxAge') is not None:
            self.max_age = m.get('MaxAge')

        return self

