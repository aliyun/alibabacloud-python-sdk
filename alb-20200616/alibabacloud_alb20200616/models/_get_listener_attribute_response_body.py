# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class GetListenerAttributeResponseBody(DaraModel):
    def __init__(
        self,
        acl_config: main_models.GetListenerAttributeResponseBodyAclConfig = None,
        ca_certificates: List[main_models.GetListenerAttributeResponseBodyCaCertificates] = None,
        ca_enabled: bool = None,
        certificates: List[main_models.GetListenerAttributeResponseBodyCertificates] = None,
        default_actions: List[main_models.GetListenerAttributeResponseBodyDefaultActions] = None,
        gzip_enabled: bool = None,
        http_2enabled: bool = None,
        idle_timeout: int = None,
        listener_description: str = None,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        listener_status: str = None,
        load_balancer_id: str = None,
        log_config: main_models.GetListenerAttributeResponseBodyLogConfig = None,
        quic_config: main_models.GetListenerAttributeResponseBodyQuicConfig = None,
        request_id: str = None,
        request_timeout: int = None,
        security_policy_id: str = None,
        tags: List[main_models.GetListenerAttributeResponseBodyTags] = None,
        xforwarded_for_config: main_models.GetListenerAttributeResponseBodyXForwardedForConfig = None,
    ):
        # The configurations of the access control lists (ACLs).
        self.acl_config = acl_config
        # A list of default CA certificates.
        self.ca_certificates = ca_certificates
        # Indicates whether mutual authentication is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.ca_enabled = ca_enabled
        # A list of certificates.
        self.certificates = certificates
        # The actions of the default forwarding rule.
        self.default_actions = default_actions
        # Indicates whether GZIP compression is enabled to compress specific types of files. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.gzip_enabled = gzip_enabled
        # Indicates whether HTTP/2 is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > This parameter is available only when you create an HTTPS listener.
        self.http_2enabled = http_2enabled
        # The timeout period of an idle connection. Unit: seconds.
        # 
        # If no requests are received within the specified timeout period, Application Load Balancer (ALB) closes the current connection. When a request is received, ALB establishes a new connection.
        self.idle_timeout = idle_timeout
        # The name of the listener.
        self.listener_description = listener_description
        # The ID of the listener.
        self.listener_id = listener_id
        # The frontend port that is used by the ALB instance.
        self.listener_port = listener_port
        # The listener protocol. Valid values: **HTTP**, **HTTPS**, and **QUIC**.
        self.listener_protocol = listener_protocol
        # The status of the listener. Valid values:
        # 
        # *   **Provisioning**
        # *   **Running**
        # *   **Configuring**
        # *   **Stopped**
        self.listener_status = listener_status
        # The ALB instance ID.
        self.load_balancer_id = load_balancer_id
        # The logging configuration.
        self.log_config = log_config
        # The configuration information when the listener is associated with a QUIC listener.
        self.quic_config = quic_config
        # The request ID.
        self.request_id = request_id
        # The timeout period of a request. Unit: seconds.
        # 
        # If no responses are received from the backend server within the specified timeout period, ALB returns an `HTTP 504` error code to the client.
        self.request_timeout = request_timeout
        # The security policy.
        # 
        # > This parameter is available only when you create an HTTPS listener.
        self.security_policy_id = security_policy_id
        # The tags.
        self.tags = tags
        # The configuration of the XForward headers.
        self.xforwarded_for_config = xforwarded_for_config

    def validate(self):
        if self.acl_config:
            self.acl_config.validate()
        if self.ca_certificates:
            for v1 in self.ca_certificates:
                 if v1:
                    v1.validate()
        if self.certificates:
            for v1 in self.certificates:
                 if v1:
                    v1.validate()
        if self.default_actions:
            for v1 in self.default_actions:
                 if v1:
                    v1.validate()
        if self.log_config:
            self.log_config.validate()
        if self.quic_config:
            self.quic_config.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.xforwarded_for_config:
            self.xforwarded_for_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_config is not None:
            result['AclConfig'] = self.acl_config.to_map()

        result['CaCertificates'] = []
        if self.ca_certificates is not None:
            for k1 in self.ca_certificates:
                result['CaCertificates'].append(k1.to_map() if k1 else None)

        if self.ca_enabled is not None:
            result['CaEnabled'] = self.ca_enabled

        result['Certificates'] = []
        if self.certificates is not None:
            for k1 in self.certificates:
                result['Certificates'].append(k1.to_map() if k1 else None)

        result['DefaultActions'] = []
        if self.default_actions is not None:
            for k1 in self.default_actions:
                result['DefaultActions'].append(k1.to_map() if k1 else None)

        if self.gzip_enabled is not None:
            result['GzipEnabled'] = self.gzip_enabled

        if self.http_2enabled is not None:
            result['Http2Enabled'] = self.http_2enabled

        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout

        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol

        if self.listener_status is not None:
            result['ListenerStatus'] = self.listener_status

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.log_config is not None:
            result['LogConfig'] = self.log_config.to_map()

        if self.quic_config is not None:
            result['QuicConfig'] = self.quic_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclConfig') is not None:
            temp_model = main_models.GetListenerAttributeResponseBodyAclConfig()
            self.acl_config = temp_model.from_map(m.get('AclConfig'))

        self.ca_certificates = []
        if m.get('CaCertificates') is not None:
            for k1 in m.get('CaCertificates'):
                temp_model = main_models.GetListenerAttributeResponseBodyCaCertificates()
                self.ca_certificates.append(temp_model.from_map(k1))

        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')

        self.certificates = []
        if m.get('Certificates') is not None:
            for k1 in m.get('Certificates'):
                temp_model = main_models.GetListenerAttributeResponseBodyCertificates()
                self.certificates.append(temp_model.from_map(k1))

        self.default_actions = []
        if m.get('DefaultActions') is not None:
            for k1 in m.get('DefaultActions'):
                temp_model = main_models.GetListenerAttributeResponseBodyDefaultActions()
                self.default_actions.append(temp_model.from_map(k1))

        if m.get('GzipEnabled') is not None:
            self.gzip_enabled = m.get('GzipEnabled')

        if m.get('Http2Enabled') is not None:
            self.http_2enabled = m.get('Http2Enabled')

        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')

        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')

        if m.get('ListenerStatus') is not None:
            self.listener_status = m.get('ListenerStatus')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LogConfig') is not None:
            temp_model = main_models.GetListenerAttributeResponseBodyLogConfig()
            self.log_config = temp_model.from_map(m.get('LogConfig'))

        if m.get('QuicConfig') is not None:
            temp_model = main_models.GetListenerAttributeResponseBodyQuicConfig()
            self.quic_config = temp_model.from_map(m.get('QuicConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetListenerAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('XForwardedForConfig') is not None:
            temp_model = main_models.GetListenerAttributeResponseBodyXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m.get('XForwardedForConfig'))

        return self

class GetListenerAttributeResponseBodyXForwardedForConfig(DaraModel):
    def __init__(
        self,
        xforwarded_for_client_cert_client_verify_alias: str = None,
        xforwarded_for_client_cert_client_verify_enabled: bool = None,
        xforwarded_for_client_cert_fingerprint_alias: str = None,
        xforwarded_for_client_cert_fingerprint_enabled: bool = None,
        xforwarded_for_client_cert_issuer_dnalias: str = None,
        xforwarded_for_client_cert_issuer_dnenabled: bool = None,
        xforwarded_for_client_cert_subject_dnalias: str = None,
        xforwarded_for_client_cert_subject_dnenabled: bool = None,
        xforwarded_for_client_source_ips_enabled: bool = None,
        xforwarded_for_client_source_ips_trusted: str = None,
        xforwarded_for_client_src_port_enabled: bool = None,
        xforwarded_for_enabled: bool = None,
        xforwarded_for_host_enabled: bool = None,
        xforwarded_for_processing_mode: str = None,
        xforwarded_for_proto_enabled: bool = None,
        xforwarded_for_slbid_enabled: bool = None,
        xforwarded_for_slbport_enabled: bool = None,
    ):
        # The name of the custom header. This parameter takes effect only when **XForwardedForClientCertClientVerifyEnabled** is set to **true**.
        # 
        # The name is 1 to 40 characters in length, and can contain lowercase letters, hyphens (-), underscores (_), and digits.
        # 
        # > This parameter is available only when you create an HTTPS listener.
        self.xforwarded_for_client_cert_client_verify_alias = xforwarded_for_client_cert_client_verify_alias
        # Indicates whether the `X-Forwarded-Clientcert-clientverify` header is used to retrieve the verification result of the client certificate. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > This parameter is available only when you create an HTTPS listener.
        self.xforwarded_for_client_cert_client_verify_enabled = xforwarded_for_client_cert_client_verify_enabled
        # The name of the custom header. This parameter takes effect only when **XForwardedForClientCertFingerprintEnabled** is set to **true**.
        # 
        # The name is 1 to 40 characters in length, and can contain lowercase letters, hyphens (-), underscores (_), and digits.
        # 
        # > This parameter is available only when you create an HTTPS listener.
        self.xforwarded_for_client_cert_fingerprint_alias = xforwarded_for_client_cert_fingerprint_alias
        # Indicates whether the `X-Forwarded-Clientcert-fingerprint` header is used to retrieve the fingerprint of the client certificate. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > This parameter is available only when you create an HTTPS listener.
        self.xforwarded_for_client_cert_fingerprint_enabled = xforwarded_for_client_cert_fingerprint_enabled
        # The name of the custom header. This parameter takes effect only when **XForwardedForClientCertIssuerDNEnabled** is set to **true**.
        # 
        # The name is 1 to 40 characters in length, and can contain lowercase letters, hyphens (-), underscores (_), and digits.
        # 
        # > This parameter is available only when you create an HTTPS listener.
        self.xforwarded_for_client_cert_issuer_dnalias = xforwarded_for_client_cert_issuer_dnalias
        # Indicates whether the `X-Forwarded-Clientcert-issuerdn` header is used to retrieve information about the authority that issues the client certificate. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > This parameter is available only when you create an HTTPS listener.
        self.xforwarded_for_client_cert_issuer_dnenabled = xforwarded_for_client_cert_issuer_dnenabled
        # The name of the custom header. This parameter takes effect only when **XForwardedForClientCertSubjectDNEnabled** is set to **true**.
        # 
        # The name is 1 to 40 characters in length, and can contain lowercase letters, hyphens (-), underscores (_), and digits.
        # 
        # > This parameter is available only when you create an HTTPS listener.
        self.xforwarded_for_client_cert_subject_dnalias = xforwarded_for_client_cert_subject_dnalias
        # Indicates whether the `X-Forwarded-Clientcert-subjectdn` header is used to retrieve information about the owner of the client certificate. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > This parameter is available only when you create an HTTPS listener.
        self.xforwarded_for_client_cert_subject_dnenabled = xforwarded_for_client_cert_subject_dnenabled
        # Indicates whether the `X-Forwarded-Client-Ip` header is used to retrieve the source port of the ALB instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > This parameter is available only when you create an HTTP, HTTPS, or QUIC listener.
        self.xforwarded_for_client_source_ips_enabled = xforwarded_for_client_source_ips_enabled
        # The trusted proxy IP address.
        # 
        # ALB traverses `X-Forwarded-For` backward and selects the first IP address that is not on the trusted IP address list as the real IP address of the client. The IP address is used in source IP address throttling.
        self.xforwarded_for_client_source_ips_trusted = xforwarded_for_client_source_ips_trusted
        # Indicates whether the `X-Forwarded-Client-Port` header is used to retrieve the client port. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > This parameter is available only when you create an HTTP or HTTPS listener.
        self.xforwarded_for_client_src_port_enabled = xforwarded_for_client_src_port_enabled
        # Indicates whether the `X-Forwarded-For` header is used to retrieve the client IP address. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        # 
        # > *   If this parameter is set to **true**, the default value of the **XForwardedForProcessingMode** parameter is **append**. You can change it to **remove**.
        # > *   If this parameter is set to **false**, the `X-Forwarded-For` header in the request is not modified in any way before the request is sent to backend servers.
        # > *   This parameter is only available for HTTP and HTTPS listeners.
        self.xforwarded_for_enabled = xforwarded_for_enabled
        # Specifies whether to use the `X-Forwarded-Host` header to retrieve the client domain name. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # >  This parameter is available for HTTP, HTTPS, and QUIC listeners.
        self.xforwarded_for_host_enabled = xforwarded_for_host_enabled
        # Specifies how the `X-Forwarded-For` header is processed. This parameter takes effect only when **XForwardedForEnabled** is set to **true**. Valid values:
        # 
        # *   **append** (default)
        # *   **remove**
        # 
        # > *   If this parameter is set to **append**, ALB appends the IP address of the last hop to the existing `X-Forwarded-For` header in the request before the request is sent to backend servers.
        # > *   If this parameter is set to **remove**, ALB removes the `X-Forwarded-For` header in the request before the request is sent to backend servers, no matter whether the request carries the `X-Forwarded-For` header.
        # > *   This parameter is only available for HTTP and HTTPS listeners.
        self.xforwarded_for_processing_mode = xforwarded_for_processing_mode
        # Indicates whether the `X-Forwarded-Proto` header is used to retrieve the listening protocol. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > This parameter is available only when you create an HTTP, HTTPS, or QUIC listener.
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled
        # Indicates whether the `SLB-ID` header is used to retrieve the ID of the CLB instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > This parameter is available only when you create an HTTP, HTTPS, or QUIC listener.
        self.xforwarded_for_slbid_enabled = xforwarded_for_slbid_enabled
        # Indicates whether the `X-Forwarded-Port` header is used to retrieve the listening port of the ALB instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > This parameter is available only when you create an HTTP, HTTPS, or QUIC listener.
        self.xforwarded_for_slbport_enabled = xforwarded_for_slbport_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.xforwarded_for_client_cert_client_verify_alias is not None:
            result['XForwardedForClientCertClientVerifyAlias'] = self.xforwarded_for_client_cert_client_verify_alias

        if self.xforwarded_for_client_cert_client_verify_enabled is not None:
            result['XForwardedForClientCertClientVerifyEnabled'] = self.xforwarded_for_client_cert_client_verify_enabled

        if self.xforwarded_for_client_cert_fingerprint_alias is not None:
            result['XForwardedForClientCertFingerprintAlias'] = self.xforwarded_for_client_cert_fingerprint_alias

        if self.xforwarded_for_client_cert_fingerprint_enabled is not None:
            result['XForwardedForClientCertFingerprintEnabled'] = self.xforwarded_for_client_cert_fingerprint_enabled

        if self.xforwarded_for_client_cert_issuer_dnalias is not None:
            result['XForwardedForClientCertIssuerDNAlias'] = self.xforwarded_for_client_cert_issuer_dnalias

        if self.xforwarded_for_client_cert_issuer_dnenabled is not None:
            result['XForwardedForClientCertIssuerDNEnabled'] = self.xforwarded_for_client_cert_issuer_dnenabled

        if self.xforwarded_for_client_cert_subject_dnalias is not None:
            result['XForwardedForClientCertSubjectDNAlias'] = self.xforwarded_for_client_cert_subject_dnalias

        if self.xforwarded_for_client_cert_subject_dnenabled is not None:
            result['XForwardedForClientCertSubjectDNEnabled'] = self.xforwarded_for_client_cert_subject_dnenabled

        if self.xforwarded_for_client_source_ips_enabled is not None:
            result['XForwardedForClientSourceIpsEnabled'] = self.xforwarded_for_client_source_ips_enabled

        if self.xforwarded_for_client_source_ips_trusted is not None:
            result['XForwardedForClientSourceIpsTrusted'] = self.xforwarded_for_client_source_ips_trusted

        if self.xforwarded_for_client_src_port_enabled is not None:
            result['XForwardedForClientSrcPortEnabled'] = self.xforwarded_for_client_src_port_enabled

        if self.xforwarded_for_enabled is not None:
            result['XForwardedForEnabled'] = self.xforwarded_for_enabled

        if self.xforwarded_for_host_enabled is not None:
            result['XForwardedForHostEnabled'] = self.xforwarded_for_host_enabled

        if self.xforwarded_for_processing_mode is not None:
            result['XForwardedForProcessingMode'] = self.xforwarded_for_processing_mode

        if self.xforwarded_for_proto_enabled is not None:
            result['XForwardedForProtoEnabled'] = self.xforwarded_for_proto_enabled

        if self.xforwarded_for_slbid_enabled is not None:
            result['XForwardedForSLBIdEnabled'] = self.xforwarded_for_slbid_enabled

        if self.xforwarded_for_slbport_enabled is not None:
            result['XForwardedForSLBPortEnabled'] = self.xforwarded_for_slbport_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('XForwardedForClientCertClientVerifyAlias') is not None:
            self.xforwarded_for_client_cert_client_verify_alias = m.get('XForwardedForClientCertClientVerifyAlias')

        if m.get('XForwardedForClientCertClientVerifyEnabled') is not None:
            self.xforwarded_for_client_cert_client_verify_enabled = m.get('XForwardedForClientCertClientVerifyEnabled')

        if m.get('XForwardedForClientCertFingerprintAlias') is not None:
            self.xforwarded_for_client_cert_fingerprint_alias = m.get('XForwardedForClientCertFingerprintAlias')

        if m.get('XForwardedForClientCertFingerprintEnabled') is not None:
            self.xforwarded_for_client_cert_fingerprint_enabled = m.get('XForwardedForClientCertFingerprintEnabled')

        if m.get('XForwardedForClientCertIssuerDNAlias') is not None:
            self.xforwarded_for_client_cert_issuer_dnalias = m.get('XForwardedForClientCertIssuerDNAlias')

        if m.get('XForwardedForClientCertIssuerDNEnabled') is not None:
            self.xforwarded_for_client_cert_issuer_dnenabled = m.get('XForwardedForClientCertIssuerDNEnabled')

        if m.get('XForwardedForClientCertSubjectDNAlias') is not None:
            self.xforwarded_for_client_cert_subject_dnalias = m.get('XForwardedForClientCertSubjectDNAlias')

        if m.get('XForwardedForClientCertSubjectDNEnabled') is not None:
            self.xforwarded_for_client_cert_subject_dnenabled = m.get('XForwardedForClientCertSubjectDNEnabled')

        if m.get('XForwardedForClientSourceIpsEnabled') is not None:
            self.xforwarded_for_client_source_ips_enabled = m.get('XForwardedForClientSourceIpsEnabled')

        if m.get('XForwardedForClientSourceIpsTrusted') is not None:
            self.xforwarded_for_client_source_ips_trusted = m.get('XForwardedForClientSourceIpsTrusted')

        if m.get('XForwardedForClientSrcPortEnabled') is not None:
            self.xforwarded_for_client_src_port_enabled = m.get('XForwardedForClientSrcPortEnabled')

        if m.get('XForwardedForEnabled') is not None:
            self.xforwarded_for_enabled = m.get('XForwardedForEnabled')

        if m.get('XForwardedForHostEnabled') is not None:
            self.xforwarded_for_host_enabled = m.get('XForwardedForHostEnabled')

        if m.get('XForwardedForProcessingMode') is not None:
            self.xforwarded_for_processing_mode = m.get('XForwardedForProcessingMode')

        if m.get('XForwardedForProtoEnabled') is not None:
            self.xforwarded_for_proto_enabled = m.get('XForwardedForProtoEnabled')

        if m.get('XForwardedForSLBIdEnabled') is not None:
            self.xforwarded_for_slbid_enabled = m.get('XForwardedForSLBIdEnabled')

        if m.get('XForwardedForSLBPortEnabled') is not None:
            self.xforwarded_for_slbport_enabled = m.get('XForwardedForSLBPortEnabled')

        return self

class GetListenerAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetListenerAttributeResponseBodyQuicConfig(DaraModel):
    def __init__(
        self,
        quic_listener_id: str = None,
        quic_upgrade_enabled: bool = None,
    ):
        # The ID of the QUIC listener. This parameter is returned when **QuicUpgradeEnabled** is set to **true**. Only HTTPS listeners support this parameter.
        # 
        # > You must associate the HTTPS listener and the QUIC listener with the same ALB instance. In addition, make sure that the QUIC listener has never been associated with another listener.
        self.quic_listener_id = quic_listener_id
        # Indicates whether QUIC upgrade is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > Only HTTPS listeners support this parameter.
        self.quic_upgrade_enabled = quic_upgrade_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quic_listener_id is not None:
            result['QuicListenerId'] = self.quic_listener_id

        if self.quic_upgrade_enabled is not None:
            result['QuicUpgradeEnabled'] = self.quic_upgrade_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuicListenerId') is not None:
            self.quic_listener_id = m.get('QuicListenerId')

        if m.get('QuicUpgradeEnabled') is not None:
            self.quic_upgrade_enabled = m.get('QuicUpgradeEnabled')

        return self

class GetListenerAttributeResponseBodyLogConfig(DaraModel):
    def __init__(
        self,
        access_log_record_customized_headers_enabled: bool = None,
        access_log_tracing_config: main_models.GetListenerAttributeResponseBodyLogConfigAccessLogTracingConfig = None,
    ):
        # Indicates whether custom headers are recorded in the access log. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.access_log_record_customized_headers_enabled = access_log_record_customized_headers_enabled
        # The configuration of Xtrace. Xtrace is used to record requests sent to ALB.
        self.access_log_tracing_config = access_log_tracing_config

    def validate(self):
        if self.access_log_tracing_config:
            self.access_log_tracing_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_log_record_customized_headers_enabled is not None:
            result['AccessLogRecordCustomizedHeadersEnabled'] = self.access_log_record_customized_headers_enabled

        if self.access_log_tracing_config is not None:
            result['AccessLogTracingConfig'] = self.access_log_tracing_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogRecordCustomizedHeadersEnabled') is not None:
            self.access_log_record_customized_headers_enabled = m.get('AccessLogRecordCustomizedHeadersEnabled')

        if m.get('AccessLogTracingConfig') is not None:
            temp_model = main_models.GetListenerAttributeResponseBodyLogConfigAccessLogTracingConfig()
            self.access_log_tracing_config = temp_model.from_map(m.get('AccessLogTracingConfig'))

        return self

class GetListenerAttributeResponseBodyLogConfigAccessLogTracingConfig(DaraModel):
    def __init__(
        self,
        tracing_enabled: bool = None,
        tracing_sample: int = None,
        tracing_type: str = None,
    ):
        # Indicates whether Xtrace is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > You can set this parameter to **true** only if the AccessLogEnabled parameter is set to true.
        self.tracing_enabled = tracing_enabled
        # The sampling rate of Xtrace. Valid values: 1 to 10000.
        # 
        # > If **TracingEnabled** is set to **true**, this parameter is valid.
        self.tracing_sample = tracing_sample
        # The Xtrace type. Supported Xtrace type: **Zipkin**.
        # 
        # > If **TracingEnabled** is set to **true**, this parameter is valid.
        self.tracing_type = tracing_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tracing_enabled is not None:
            result['TracingEnabled'] = self.tracing_enabled

        if self.tracing_sample is not None:
            result['TracingSample'] = self.tracing_sample

        if self.tracing_type is not None:
            result['TracingType'] = self.tracing_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TracingEnabled') is not None:
            self.tracing_enabled = m.get('TracingEnabled')

        if m.get('TracingSample') is not None:
            self.tracing_sample = m.get('TracingSample')

        if m.get('TracingType') is not None:
            self.tracing_type = m.get('TracingType')

        return self

class GetListenerAttributeResponseBodyDefaultActions(DaraModel):
    def __init__(
        self,
        forward_group_config: main_models.GetListenerAttributeResponseBodyDefaultActionsForwardGroupConfig = None,
        type: str = None,
    ):
        # The configuration of the ForwardGroup action. This parameter is returned and takes effect when Type is set to **ForwardGroup**.
        self.forward_group_config = forward_group_config
        # The type of the action.
        # 
        # If **ForwardGroup** is returned, requests are forwarded to multiple vServer groups.
        self.type = type

    def validate(self):
        if self.forward_group_config:
            self.forward_group_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardGroupConfig') is not None:
            temp_model = main_models.GetListenerAttributeResponseBodyDefaultActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m.get('ForwardGroupConfig'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetListenerAttributeResponseBodyDefaultActionsForwardGroupConfig(DaraModel):
    def __init__(
        self,
        server_group_tuples: List[main_models.GetListenerAttributeResponseBodyDefaultActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # The server group to which requests are forwarded.
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_tuples:
            for v1 in self.server_group_tuples:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k1 in self.server_group_tuples:
                result['ServerGroupTuples'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k1 in m.get('ServerGroupTuples'):
                temp_model = main_models.GetListenerAttributeResponseBodyDefaultActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k1))

        return self

class GetListenerAttributeResponseBodyDefaultActionsForwardGroupConfigServerGroupTuples(DaraModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        # The ID of the server group to which requests are forwarded.
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        return self

class GetListenerAttributeResponseBodyCertificates(DaraModel):
    def __init__(
        self,
        certificate_id: str = None,
    ):
        # The ID of the certificate. Only server certificates are supported.
        self.certificate_id = certificate_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        return self

class GetListenerAttributeResponseBodyCaCertificates(DaraModel):
    def __init__(
        self,
        certificate_id: str = None,
        is_default: bool = None,
        status: str = None,
    ):
        # The ID of the default CA certificate.
        self.certificate_id = certificate_id
        # Indicates whether the certificate is a default certificate: Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_default = is_default
        # The status of the certificate.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetListenerAttributeResponseBodyAclConfig(DaraModel):
    def __init__(
        self,
        acl_relations: List[main_models.GetListenerAttributeResponseBodyAclConfigAclRelations] = None,
        acl_type: str = None,
    ):
        # The IDs of the ACLs that are associated with the listener.
        self.acl_relations = acl_relations
        # The type of the ACL. Valid values:
        # 
        # *   **White**: a whitelist. Only requests from the IP addresses or CIDR blocks in the network ACL are forwarded. Whitelists are applicable to scenarios in which you want to allow only specific IP addresses to access an application. Your service may be adversely affected if the whitelist is not properly configured. If a whitelist is configured for a listener, only requests from IP addresses that are on the whitelist are forwarded by the listener.
        # 
        #     If you enable a whitelist but do not add an IP address to the whitelist, the listener forwards all requests.
        # 
        # *   **Black**: a blacklist. Requests from the IP addresses or CIDR blocks in the network ACL are denied. Blacklists are suitable for scenarios in which you want to deny access from specific IP addresses or CIDR blocks to an application.
        # 
        #     If a blacklist is configured for a listener but no IP addresses are added to the blacklist, the listener forwards all requests.
        self.acl_type = acl_type

    def validate(self):
        if self.acl_relations:
            for v1 in self.acl_relations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AclRelations'] = []
        if self.acl_relations is not None:
            for k1 in self.acl_relations:
                result['AclRelations'].append(k1.to_map() if k1 else None)

        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_relations = []
        if m.get('AclRelations') is not None:
            for k1 in m.get('AclRelations'):
                temp_model = main_models.GetListenerAttributeResponseBodyAclConfigAclRelations()
                self.acl_relations.append(temp_model.from_map(k1))

        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        return self

class GetListenerAttributeResponseBodyAclConfigAclRelations(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        status: str = None,
    ):
        # The ID of the ACL that is associated with the listener.
        self.acl_id = acl_id
        # Indicates whether the ACL is associated with the listener. Valid values:
        # 
        # *   **Associating**
        # *   **Associated**
        # *   **Dissociating**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

