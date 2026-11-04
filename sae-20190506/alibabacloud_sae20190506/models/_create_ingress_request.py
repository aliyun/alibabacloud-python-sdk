# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIngressRequest(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        cert_id: str = None,
        cert_ids: str = None,
        cors_config: str = None,
        default_rule: str = None,
        description: str = None,
        enable_gzip: bool = None,
        enable_xforwarded_for: bool = None,
        enable_xforwarded_for_client_src_port: bool = None,
        enable_xforwarded_for_proto: bool = None,
        enable_xforwarded_for_slb_id: bool = None,
        enable_xforwarded_for_slb_port: bool = None,
        idle_timeout: int = None,
        listener_port: int = None,
        listener_protocol: str = None,
        load_balance_type: str = None,
        load_balancer_edition: str = None,
        namespace_id: str = None,
        request_timeout: int = None,
        rules: str = None,
        security_policy_id: str = None,
        slb_id: str = None,
        zone_mappings: str = None,
    ):
        # The address type. Valid values:
        # - Internet: public network address.
        # - Intranet: private network address.
        self.address_type = address_type
        # The ID of the **CLB** certificate. Valid values:
        # 
        # - If **LoadBalanceType** is set to **clb**, use this field to configure the certificate for the HTTPS listener.
        # 
        # For more information about how to use SSL certificate IDs in CLB, see [Manage certificates (CLB)](https://help.aliyun.com/document_detail/90792.html).
        self.cert_id = cert_id
        # The IDs of the **ALB** certificates. Valid values:
        # 
        # - If **LoadBalanceType** is set to **alb**, use this field to configure multiple certificates for the HTTPS listener. Separate multiple certificate IDs with commas (,).
        # 
        # - You must obtain the SSL certificate IDs used by ALB from the Certificate Management Service. For example, if you configure `756***-cn-hangzhou`, `756***` is the certificate ID obtained from the product page, and `-cn-hangzhou` is a fixed suffix. For more information, see [Manage certificates (ALB)](https://help.aliyun.com/document_detail/209076.html).
        self.cert_ids = cert_ids
        # The cross-origin resource sharing (CORS) configuration.
        self.cors_config = cors_config
        # The default forwarding rule. Traffic is forwarded to the specified application based on the IP address through the specified port. The parameters are as follows:
        # 
        # - **appId**: the ID of the application.
        # - **containerPort**: the port of the application instance.
        # 
        # > All requests that do not match or meet the forwarding rules in **Rules** are forwarded to the specified application.
        # 
        # This parameter is required.
        self.default_rule = default_rule
        # The name of the routing rule.
        self.description = description
        # Specifies whether to enable data compression.
        self.enable_gzip = enable_gzip
        # Specifies whether to enable the feature to obtain the client IP address of the visitor through the X-Forwarded-For header field.
        self.enable_xforwarded_for = enable_xforwarded_for
        # Specifies whether to obtain the listening port of the load balancing instance through the X-Forwarded-Port header field.
        self.enable_xforwarded_for_client_src_port = enable_xforwarded_for_client_src_port
        # Specifies whether to obtain the listening protocol of the load balancing instance through the X-Forwarded-Proto header field.
        self.enable_xforwarded_for_proto = enable_xforwarded_for_proto
        # Specifies whether to obtain the load balancing instance ID through the SLB-ID header field.
        self.enable_xforwarded_for_slb_id = enable_xforwarded_for_slb_id
        # Specifies whether to obtain the listening port of the load balancing instance through the X-Forwarded-Port header field.
        self.enable_xforwarded_for_slb_port = enable_xforwarded_for_slb_port
        # Specifies the connection idle timeout period. Unit: seconds. Valid values: 1 to 60. If no access request is received within the timeout period, load balancing temporarily breaks the current connection until a new connection is established when the next request arrives.
        self.idle_timeout = idle_timeout
        # The listening port of the SLB instance. The port must not be occupied.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The request forwarding protocol. Valid values:
        # 
        # - **HTTP**: applicable to applications that need to identify data content.
        # - **HTTPS**: applicable to applications that require encrypted transmission.
        self.listener_protocol = listener_protocol
        # The type of the SLB instance. The type depends on the value specified when the routing rule is created and cannot be changed during updates. Valid values:
        # 
        # - **clb**: Classic Load Balancer (CLB).
        # - **alb**: Application Load Balancer (ALB).
        self.load_balance_type = load_balance_type
        # The edition of the Application Load Balancer (ALB). Different editions have different feature limits and billing policy. Valid values:
        # 
        # - **Standard**: Standard Edition.
        # 
        # - **StandardWithWaf**: WAF-enhanced Edition.
        self.load_balancer_edition = load_balancer_edition
        # The ID of the namespace where the application resides. Cross-namespace applications are not supported.
        # 
        # This parameter is required.
        self.namespace_id = namespace_id
        # Specifies the request timeout period. Unit: seconds. Valid values: 1 to 180. If the backend server does not send a response within the timeout period, load balancing stops waiting and returns an HTTP 504 error code to the client.
        self.request_timeout = request_timeout
        # The forwarding rules. Traffic is forwarded to the specified application based on the domain name and the request path through the specified port. The parameters are as follows:
        # 
        # - **appId**: the ID of the application.
        # - **containerPort**: the port of the application instance.
        # - **domain**: the domain name.
        # - **path**: the URI of the request.
        # - **backendProtocol**: the backend service Terms of Service. Valid values: http, https, and grpc. Default value: http.
        # - **rewritePath**: the rewrite path.
        # 
        # > Currently, only ALB supports the URL path rewrite (RewritePath) feature. CLB does not support this feature.
        # 
        # This parameter is required.
        self.rules = rules
        # The ID of the security policy instance.
        self.security_policy_id = security_policy_id
        # The SLB instance ID used by the routing rule.
        # 
        # > Server Load Balancer (SLB) includes CLB and ALB instances.
        self.slb_id = slb_id
        # The JSON string of the zone and vSwitch mapping list. If the current region supports two or more zones, you must add at least two zones. A ZoneMapping structure includes:
        # 
        # - VSwitchId: the vSwitch corresponding to the zone. Data type: String. Only one vSwitch and one subnet can be used in each zone.
        # 
        # - ZoneId: the zone ID of the Network Load Balancer (NLB) instance. Data type: String.
        self.zone_mappings = zone_mappings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_ids is not None:
            result['CertIds'] = self.cert_ids

        if self.cors_config is not None:
            result['CorsConfig'] = self.cors_config

        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule

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

        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol

        if self.load_balance_type is not None:
            result['LoadBalanceType'] = self.load_balance_type

        if self.load_balancer_edition is not None:
            result['LoadBalancerEdition'] = self.load_balancer_edition

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        if self.rules is not None:
            result['Rules'] = self.rules

        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.zone_mappings is not None:
            result['ZoneMappings'] = self.zone_mappings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertIds') is not None:
            self.cert_ids = m.get('CertIds')

        if m.get('CorsConfig') is not None:
            self.cors_config = m.get('CorsConfig')

        if m.get('DefaultRule') is not None:
            self.default_rule = m.get('DefaultRule')

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

        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')

        if m.get('LoadBalanceType') is not None:
            self.load_balance_type = m.get('LoadBalanceType')

        if m.get('LoadBalancerEdition') is not None:
            self.load_balancer_edition = m.get('LoadBalancerEdition')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('ZoneMappings') is not None:
            self.zone_mappings = m.get('ZoneMappings')

        return self

