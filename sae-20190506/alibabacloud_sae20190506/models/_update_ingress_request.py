# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateIngressRequest(DaraModel):
    def __init__(
        self,
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
        ingress_id: int = None,
        listener_port: str = None,
        listener_protocol: str = None,
        load_balance_type: str = None,
        request_timeout: int = None,
        rules: str = None,
        security_policy_id: str = None,
    ):
        # **CLB** certificate ID. Details are as follows:
        # 
        # - If **LoadBalanceType** is **clb**, use this field to configure the HTTPS listener certificate.
        # 
        # For more information about using SSL certificate IDs with CLB, see [Manage Certificates (CLB)]().
        self.cert_id = cert_id
        # **ALB** multiple certificate IDs. Details are as follows:
        # 
        # - If **LoadBalanceType** is **alb**, use this field to configure multiple HTTPS listener certificates. Separate multiple certificate IDs with commas.
        # 
        # - Obtain the SSL certificate ID used by ALB from the digital certificate product. For example, configure `756***-cn-hangzhou`, where `756***` is the certificate ID obtained from the product page, and `-cn-hangzhou` is a fixed suffix. For more information, see [Manage Certificates (ALB)]().
        self.cert_ids = cert_ids
        # Cross-domain configuration.
        self.cors_config = cors_config
        # Default forwarding rule. Forward traffic to the specified application by IP address through the specified port. Parameter description:
        # 
        # - **appId**: Application ID.
        # 
        # - **containerPort**: Application instance port.
        # 
        # > All requests that do not match or satisfy the **Rules** forwarding rule are forwarded to this specified application.
        self.default_rule = default_rule
        # Routing rule name.
        self.description = description
        # Enable or disable data compression.
        self.enable_gzip = enable_gzip
        # Enable or disable obtaining the client IP address of the visitor through the X-Forwarded-For header field.
        self.enable_xforwarded_for = enable_xforwarded_for
        # Obtain the listening port of the SLB instance through the X-Forwarded-Port header field.
        self.enable_xforwarded_for_client_src_port = enable_xforwarded_for_client_src_port
        # Specifies whether to determine the listener protocol of the SLB instance from the X-Forwarded-Proto header field.
        self.enable_xforwarded_for_proto = enable_xforwarded_for_proto
        # Obtain the SLB instance ID through the SLB-ID header field.
        self.enable_xforwarded_for_slb_id = enable_xforwarded_for_slb_id
        # Whether to obtain the listening port of the Server Load Balancer instance from the X-Forwarded-Port header field.
        self.enable_xforwarded_for_slb_port = enable_xforwarded_for_slb_port
        # Idle connection timeout, in seconds (s).
        # 
        # > A value of 0 indicates that the default idle timeout is used.
        self.idle_timeout = idle_timeout
        # Routing rule ID.
        # 
        # This parameter is required.
        self.ingress_id = ingress_id
        # SLB listening port. This port must not be occupied.
        self.listener_port = listener_port
        # Forwarding Protocol. Details are as follows:
        # 
        # - **HTTP**: Applies to applications that need to identify data content.
        # 
        # - **HTTPS**: Applies to applications that need encrypted transmission.
        self.listener_protocol = listener_protocol
        # Deprecated parameter. Updates are no longer supported.
        self.load_balance_type = load_balance_type
        # Request timeout, in seconds (s).
        self.request_timeout = request_timeout
        # Forwarding rules. Forward traffic to the specified application by domain name and URI of the request through the specified port. Parameter description:
        # 
        # - **appId**: Application ID.
        # 
        # - **containerPort**: Application instance port.
        # 
        # - **domain**: Domain name.
        # 
        # - **path**: URI of the request.
        self.rules = rules
        # Security policy instance ID.
        self.security_policy_id = security_policy_id

    def validate(self):
        pass

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

        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol

        if self.load_balance_type is not None:
            result['LoadBalanceType'] = self.load_balance_type

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        if self.rules is not None:
            result['Rules'] = self.rules

        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')

        if m.get('LoadBalanceType') is not None:
            self.load_balance_type = m.get('LoadBalanceType')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        return self

