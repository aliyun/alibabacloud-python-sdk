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
        # -
        self.address_type = address_type
        # The ID of the **CLB** certificate. Valid values:
        # 
        # *   If you set **LoadBalanceType** to **clb**, you can use CertId to configure a certificate for the HTTPS listener.
        # 
        # For more information about how to use SSL certificate IDs for CLB, see [Manage certificates (CLB)](https://help.aliyun.com/document_detail/90792.html).
        self.cert_id = cert_id
        # The ID of the multi-certificate **ALB**. Valid values:
        # 
        # *   If the **LoadBalanceType** is **alb**, use this field to configure multiple certificates for HTTPS listeners. Separate multiple certificate IDs with commas (,).
        # *   The ID of the SSL certificate used by ALB must be obtained from the digital certificate product. For example, in the configuration `756***-cn-hangzhou`, the `756***` is the certificate ID obtained from the product page, and the `-cn-hangzhou` is a fixed suffix. For more information, see [Manage certificates](https://help.aliyun.com/document_detail/209076.html).
        self.cert_ids = cert_ids
        # -
        self.cors_config = cors_config
        # The default forwarding rule. Forwards traffic to a specified application through a specified port based on the IP address. The following table describes the parameters.
        # 
        # *   **appId**: the ID of the application.
        # *   **containerPort**: The port of the application instance.
        # 
        # >  All requests that do not match or satisfy **Rules** forwarding rules are forwarded to the specified application.
        # 
        # This parameter is required.
        self.default_rule = default_rule
        # The name of the routing rule.
        self.description = description
        # -
        self.enable_gzip = enable_gzip
        # -
        self.enable_xforwarded_for = enable_xforwarded_for
        # -
        self.enable_xforwarded_for_client_src_port = enable_xforwarded_for_client_src_port
        # -
        self.enable_xforwarded_for_proto = enable_xforwarded_for_proto
        # -
        self.enable_xforwarded_for_slb_id = enable_xforwarded_for_slb_id
        # -
        self.enable_xforwarded_for_slb_port = enable_xforwarded_for_slb_port
        # Specifies the connection idle timeout period. Unit: seconds. Valid values: 1 to 60. If there is no access request within the timeout period, the SLB will temporarily interrupt the current connection until the next request comes to re-establish a new connection.
        self.idle_timeout = idle_timeout
        # The SLB listening port. This port cannot be occupied.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The request forwarding protocol. Valid values:
        # 
        # *   **HTTP**: suitable for applications that need to identify data content.
        # *   **HTTPS**: suitable for applications that require encrypted transmission.
        self.listener_protocol = listener_protocol
        # SLB the type of the SLB instance. It depends on the type that you entered when you created the routing rule and cannot be changed when you update it. Valid values:
        # 
        # *   **clb**: traditional SLB CLB (formerly SLB).
        # *   **alb**: Applied SLB ALB.
        self.load_balance_type = load_balance_type
        # -
        self.load_balancer_edition = load_balancer_edition
        # The ID of the namespace where the application resides. Currently, cross-namespace applications are not supported.
        # 
        # This parameter is required.
        self.namespace_id = namespace_id
        # Specifies the request timeout period. Unit: seconds. Valid values: 1 to 180. If the backend server does not respond within the timeout period, the SLB abandons the wait and returns an HTTP 504 error code to the client.
        self.request_timeout = request_timeout
        # The forwarding rule. Forwards traffic to a specified application through a specified port based on the domain name and request path. The following table describes the parameters.
        # 
        # *   **appId**: the ID of the application.
        # *   **containerPort**: The port of the application instance.
        # *   **domain**: the domain name.
        # *   **path**: the request path.
        # *   **backendProtocol**: The backend service protocol. Valid values: http, https, and grpc. Default value: http.
        # *   **rewritePath**: Rewrite the path.
        # 
        # >  Only ALB allows you to set the RewritePath feature. CLB does not support this feature.
        # 
        # This parameter is required.
        self.rules = rules
        # The ID of the security policy instance.
        self.security_policy_id = security_policy_id
        # The Server Load Balancer (SLB) instance that is used by the routing rule.
        # 
        # >  SLB SLB instances include CLB instances and ALB instances.
        self.slb_id = slb_id
        # -
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

