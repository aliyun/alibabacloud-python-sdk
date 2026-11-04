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
        # The ID of the Classic Load Balancer (CLB) certificate. Valid values:
        # 
        # - If **LoadBalanceType** is set to **clb**, use this field to configure the certificate for the HTTPS listener.
        # 
        # For more information about using SSL certificate IDs in CLB, see [Manage certificates (CLB)](https://help.aliyun.com/document_detail/90792.html).
        self.cert_id = cert_id
        # The IDs of multiple Application Load Balancer (ALB) certificates. Valid values:
        # 
        # - If **LoadBalanceType** is set to **alb**, use this field to configure multiple certificates for the HTTPS listener. Separate multiple certificate IDs with commas (,).
        # 
        # - You must obtain the SSL certificate IDs used by ALB from the Certificate Management Service. For example, if you configure `756***-cn-hangzhou`, `756***` is the certificate ID obtained from the product page, and `-cn-hangzhou` is a fixed suffix. For more information, see [Manage certificates (ALB)](https://help.aliyun.com/document_detail/209076.html).
        self.cert_ids = cert_ids
        # The cross-origin resource sharing (CORS) configuration.
        self.cors_config = cors_config
        # The default forwarding rule. Traffic is forwarded to a specified application through a specified port based on the IP address. The parameters are described as follows:
        # 
        # - **appId**: the ID of the application.
        # - **containerPort**: the port of the application instance.
        # 
        # > All requests that do not match or meet the forwarding rules in **Rules** are forwarded to the specified application.
        self.default_rule = default_rule
        # The name of the routing rule.
        self.description = description
        # Specifies whether to enable data compression.
        self.enable_gzip = enable_gzip
        # Specifies whether to enable the retrieval of the client IP address through the X-Forwarded-For header field.
        self.enable_xforwarded_for = enable_xforwarded_for
        # Specifies whether to retrieve the listening port of the load balancing instance through the X-Forwarded-Port header field.
        self.enable_xforwarded_for_client_src_port = enable_xforwarded_for_client_src_port
        # Specifies whether to retrieve the listening protocol of the load balancing instance through the X-Forwarded-Proto header field.
        self.enable_xforwarded_for_proto = enable_xforwarded_for_proto
        # Specifies whether to retrieve the instance ID of the load balancing instance through the SLB-ID header field.
        self.enable_xforwarded_for_slb_id = enable_xforwarded_for_slb_id
        # Specifies whether to retrieve the listening port of the load balancing instance through the X-Forwarded-Port header field.
        self.enable_xforwarded_for_slb_port = enable_xforwarded_for_slb_port
        # The idle connection timeout period, in seconds.
        # > A value of 0 indicates that the default idle timeout value is used.
        self.idle_timeout = idle_timeout
        # The ID of the routing rule.
        # 
        # This parameter is required.
        self.ingress_id = ingress_id
        # The listening port of the Server Load Balancer (SLB) instance. The port must not be occupied.
        self.listener_port = listener_port
        # The request forwarding protocol. Valid values:
        # 
        # - **HTTP**: applicable to applications that need to identify data content.
        # - **HTTPS**: applicable to applications that require encrypted transmission.
        self.listener_protocol = listener_protocol
        # **[Deprecated]** This parameter is deprecated and updates are no longer supported.
        self.load_balance_type = load_balance_type
        # The request timeout period, in seconds.
        self.request_timeout = request_timeout
        # The forwarding rules. Traffic is forwarded to a specified application through a specified port based on the domain name and request path. The parameters are described as follows:
        # 
        # - **appId**: the ID of the application.
        # - **containerPort**: the port of the application instance.
        # - **domain**: the domain name.
        # - **path**: the request path.
        self.rules = rules
        # The ID of the security policy instance.
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

