# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeIngressResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeIngressResponseBodyData = None,
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
        # The error codes. Valid values:
        # 
        # *   **ErrorCode** is not returned if a request is successful.
        # *   **ErrorCode** is returned if a request failed. For more information, see **Error code** section of this topic.
        self.error_code = error_code
        # The message returned. Valid values:
        # 
        # *   **success** is returned when a request is successful.
        # *   An error code is returned when the request failed.
        self.message = message
        # The ID of a request.
        self.request_id = request_id
        # Indicates whether the configurations of Ingresses were queried successfully. Valid values:
        # 
        # *   **true**: The information was queried.
        # *   **false**: The information failed to be queried.
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
            temp_model = main_models.DescribeIngressResponseBodyData()
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

class DescribeIngressResponseBodyData(DaraModel):
    def __init__(
        self,
        cert_id: str = None,
        cert_ids: str = None,
        cors_config: main_models.DescribeIngressResponseBodyDataCorsConfig = None,
        created_by_sae: bool = None,
        default_rule: main_models.DescribeIngressResponseBodyDataDefaultRule = None,
        description: str = None,
        enable_gzip: bool = None,
        enable_xforwarded_for: bool = None,
        enable_xforwarded_for_client_src_port: bool = None,
        enable_xforwarded_for_proto: bool = None,
        enable_xforwarded_for_slb_id: bool = None,
        enable_xforwarded_for_slb_port: bool = None,
        id: int = None,
        idle_timeout: int = None,
        listener_port: int = None,
        listener_protocol: str = None,
        load_balance_type: str = None,
        name: str = None,
        namespace_id: str = None,
        request_timeout: int = None,
        rules: List[main_models.DescribeIngressResponseBodyDataRules] = None,
        security_policy_id: str = None,
        slb_id: str = None,
        slb_type: str = None,
    ):
        # The ID of the certificate that is associated with a Classic Load Balancer (**CLB**) instance.
        self.cert_id = cert_id
        # The ID of the certificate that is associated with an Application Load Balancer **ALB** instance.
        self.cert_ids = cert_ids
        self.cors_config = cors_config
        self.created_by_sae = created_by_sae
        # The default rule.
        self.default_rule = default_rule
        # The name of a routing rule.
        self.description = description
        self.enable_gzip = enable_gzip
        self.enable_xforwarded_for = enable_xforwarded_for
        self.enable_xforwarded_for_client_src_port = enable_xforwarded_for_client_src_port
        self.enable_xforwarded_for_proto = enable_xforwarded_for_proto
        self.enable_xforwarded_for_slb_id = enable_xforwarded_for_slb_id
        self.enable_xforwarded_for_slb_port = enable_xforwarded_for_slb_port
        # The ID of a routing rule.
        self.id = id
        self.idle_timeout = idle_timeout
        # The listener ports for an SLB instance.
        self.listener_port = listener_port
        # The protocol used to forward requests. Valid values:
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
        # The name of a routing rule.
        self.name = name
        # The ID of a namespace.
        self.namespace_id = namespace_id
        self.request_timeout = request_timeout
        # The forwarding rules.
        self.rules = rules
        self.security_policy_id = security_policy_id
        # The ID of a Server Load Balancer (SLB) instance.
        self.slb_id = slb_id
        # The type of an SLB instance. Valid values:
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

        if self.created_by_sae is not None:
            result['CreatedBySae'] = self.created_by_sae

        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_gzip is not None:
            result['EnableGzip'] = self.enable_gzip

        if self.enable_xforwarded_for is not None:
            result['EnableXForwardedFor'] = self.enable_xforwarded_for

        if self.enable_xforwarded_for_client_src_port is not None:
            result['EnableXForwardedForClientSrcPort'] = self.enable_xforwarded_for_client_src_port

        if self.enable_xforwarded_for_proto is not None:
            result['EnableXForwardedForProto'] = self.enable_xforwarded_for_proto

        if self.enable_xforwarded_for_slb_id is not None:
            result['EnableXForwardedForSlbId'] = self.enable_xforwarded_for_slb_id

        if self.enable_xforwarded_for_slb_port is not None:
            result['EnableXForwardedForSlbPort'] = self.enable_xforwarded_for_slb_port

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

        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id

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
            temp_model = main_models.DescribeIngressResponseBodyDataCorsConfig()
            self.cors_config = temp_model.from_map(m.get('CorsConfig'))

        if m.get('CreatedBySae') is not None:
            self.created_by_sae = m.get('CreatedBySae')

        if m.get('DefaultRule') is not None:
            temp_model = main_models.DescribeIngressResponseBodyDataDefaultRule()
            self.default_rule = temp_model.from_map(m.get('DefaultRule'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableGzip') is not None:
            self.enable_gzip = m.get('EnableGzip')

        if m.get('EnableXForwardedFor') is not None:
            self.enable_xforwarded_for = m.get('EnableXForwardedFor')

        if m.get('EnableXForwardedForClientSrcPort') is not None:
            self.enable_xforwarded_for_client_src_port = m.get('EnableXForwardedForClientSrcPort')

        if m.get('EnableXForwardedForProto') is not None:
            self.enable_xforwarded_for_proto = m.get('EnableXForwardedForProto')

        if m.get('EnableXForwardedForSlbId') is not None:
            self.enable_xforwarded_for_slb_id = m.get('EnableXForwardedForSlbId')

        if m.get('EnableXForwardedForSlbPort') is not None:
            self.enable_xforwarded_for_slb_port = m.get('EnableXForwardedForSlbPort')

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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeIngressResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('SlbType') is not None:
            self.slb_type = m.get('SlbType')

        return self

class DescribeIngressResponseBodyDataRules(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        backend_protocol: str = None,
        container_port: int = None,
        domain: str = None,
        path: str = None,
        rewrite_path: str = None,
        rule_actions: List[main_models.DescribeIngressResponseBodyDataRulesRuleActions] = None,
    ):
        # The ID of the application specified in the forwarding rule.
        self.app_id = app_id
        # The name of the application specified in the forwarding rules.
        self.app_name = app_name
        # The backend protocol. Valid values:
        # 
        # *   **http**: HTTP is suitable for applications that need to identify the transmitted data.
        # *   **https**: HTTPS is suitable for applications that require encrypted data transmission.
        # *   **grpc**: GRPC is suitable for load balancing scenarios in which you want to deploy services in multi-language frameworks, such as the .NET framework.
        # 
        # This parameter is returned only if the **LoadBalanceType** parameter is set to **ALB** and the **ListenerProtocol** parameter is set to **HTTPS**.
        self.backend_protocol = backend_protocol
        # Tthe container port of the application specified in the forwarding rules.
        self.container_port = container_port
        # The domain name of the application specified in the forwarding rules.
        self.domain = domain
        # The path of a URL.
        self.path = path
        # The path that is used to rewrite the original path.
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
                temp_model = main_models.DescribeIngressResponseBodyDataRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k1))

        return self

class DescribeIngressResponseBodyDataRulesRuleActions(DaraModel):
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

class DescribeIngressResponseBodyDataDefaultRule(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        backend_protocol: str = None,
        container_port: int = None,
    ):
        # The ID of the application that is specified in the default rule.
        self.app_id = app_id
        # The name of the application that is specified in the default rule.
        self.app_name = app_name
        # The backend protocol. Valid values:
        # 
        # *   **http**: HTTP is suitable for applications that need to identify the transmitted data.
        # *   **https**: HTTP is suitable for applications that require encrypted data transmission.
        # *   **grpc**: GRPC is suitable for load balancing scenarios in which you want to deploy services in multi-language frameworks, such as the .NET framework.
        # 
        # This parameter is returned only if the**LoadBalanceType** parameter is set to **ALB** and the **ListenerProtocol** parameter **is set to HTTPS**.
        self.backend_protocol = backend_protocol
        # The container port of the application that is specified in the default rule.
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

class DescribeIngressResponseBodyDataCorsConfig(DaraModel):
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

