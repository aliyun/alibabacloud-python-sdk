# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class UpdateListenerAttributeRequest(DaraModel):
    def __init__(
        self,
        ca_certificates: List[main_models.UpdateListenerAttributeRequestCaCertificates] = None,
        ca_enabled: bool = None,
        certificates: List[main_models.UpdateListenerAttributeRequestCertificates] = None,
        client_token: str = None,
        default_actions: List[main_models.UpdateListenerAttributeRequestDefaultActions] = None,
        dry_run: bool = None,
        gzip_enabled: bool = None,
        http_2enabled: bool = None,
        idle_timeout: int = None,
        listener_description: str = None,
        listener_id: str = None,
        quic_config: main_models.UpdateListenerAttributeRequestQuicConfig = None,
        request_timeout: int = None,
        security_policy_id: str = None,
        xforwarded_for_config: main_models.UpdateListenerAttributeRequestXForwardedForConfig = None,
    ):
        # The CA certificate. You can specify only one CA certificate.
        self.ca_certificates = ca_certificates
        # Specifies whether to enable mutual authentication. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.ca_enabled = ca_enabled
        # The certificates. You can add at most 20 certificates.
        # 
        # >  Only server certificates are supported.
        self.certificates = certificates
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The actions of the default forwarding rule.
        self.default_actions = default_actions
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a `2xx HTTP` status code is returned and the operation is performed.
        self.dry_run = dry_run
        # Specifies whether to enable GZIP compression for specific types of files. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.gzip_enabled = gzip_enabled
        # Specifies whether to enable HTTP/2. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > This parameter is available only when you create an HTTPS listener.
        self.http_2enabled = http_2enabled
        # The timeout period for idle connections. Unit: seconds. Valid values: **1 to 60**
        # 
        # If no requests are received within the specified timeout period, ALB closes the current connection. When another request is received, ALB establishes a new connection.
        self.idle_timeout = idle_timeout
        # The name of the listener.
        # 
        # The name must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-).
        self.listener_description = listener_description
        # The ID of the Application Load Balancer (ALB) instance.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The configuration information when the listener is associated with a QUIC listener.
        self.quic_config = quic_config
        # The timeout period of a request. Unit: seconds. Valid values: **1 to 180**.
        # 
        # If no response is received from the backend server within the specified timeout period, ALB returns an `HTTP 504` error code to the client.
        self.request_timeout = request_timeout
        # The security policy ID. System security policies and custom security policies are supported.
        # 
        # > This parameter is available only when you create an HTTPS listener.
        self.security_policy_id = security_policy_id
        # The configurations of the X-Forwarded-For header.
        self.xforwarded_for_config = xforwarded_for_config

    def validate(self):
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
        if self.quic_config:
            self.quic_config.validate()
        if self.xforwarded_for_config:
            self.xforwarded_for_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['DefaultActions'] = []
        if self.default_actions is not None:
            for k1 in self.default_actions:
                result['DefaultActions'].append(k1.to_map() if k1 else None)

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

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

        if self.quic_config is not None:
            result['QuicConfig'] = self.quic_config.to_map()

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id

        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ca_certificates = []
        if m.get('CaCertificates') is not None:
            for k1 in m.get('CaCertificates'):
                temp_model = main_models.UpdateListenerAttributeRequestCaCertificates()
                self.ca_certificates.append(temp_model.from_map(k1))

        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')

        self.certificates = []
        if m.get('Certificates') is not None:
            for k1 in m.get('Certificates'):
                temp_model = main_models.UpdateListenerAttributeRequestCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.default_actions = []
        if m.get('DefaultActions') is not None:
            for k1 in m.get('DefaultActions'):
                temp_model = main_models.UpdateListenerAttributeRequestDefaultActions()
                self.default_actions.append(temp_model.from_map(k1))

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

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

        if m.get('QuicConfig') is not None:
            temp_model = main_models.UpdateListenerAttributeRequestQuicConfig()
            self.quic_config = temp_model.from_map(m.get('QuicConfig'))

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        if m.get('XForwardedForConfig') is not None:
            temp_model = main_models.UpdateListenerAttributeRequestXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m.get('XForwardedForConfig'))

        return self

class UpdateListenerAttributeRequestXForwardedForConfig(DaraModel):
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
        # The name of the custom header. The header takes effect only when you set **XForwardedForClientCertClientVerifyEnabled **to **true**.
        # 
        # The name must be 1 to 40 characters in length. It can contain lowercase letters, digits, hyphens (-), and underscores (_).
        # 
        # >  This parameter is only available for HTTPS listeners.
        self.xforwarded_for_client_cert_client_verify_alias = xforwarded_for_client_cert_client_verify_alias
        # Specifies whether to use the `X-Forwarded-Clientcert-clientverify` header to retrieve the verification result of the client certificate. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is only available for HTTPS listeners.
        self.xforwarded_for_client_cert_client_verify_enabled = xforwarded_for_client_cert_client_verify_enabled
        # The name of the custom header. The header takes effect only when you set **XForwardedForClientCertFingerprintEnabled** to **true**.
        # 
        # The name must be 1 to 40 characters in length. It can contain lowercase letters, digits, hyphens (-), and underscores (_).
        # 
        # >  This parameter is only available for HTTPS listeners.
        self.xforwarded_for_client_cert_fingerprint_alias = xforwarded_for_client_cert_fingerprint_alias
        # Specifies whether to use the `X-Forwarded-Clientcert-fingerprint` header to retrieve the fingerprint of the client certificate. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is only available for HTTPS listeners.
        self.xforwarded_for_client_cert_fingerprint_enabled = xforwarded_for_client_cert_fingerprint_enabled
        # The name of the custom header. The header takes effect only when you set **XForwardedForClientCertIssuerDNEnabled** to **true**.
        # 
        # The name must be 1 to 40 characters in length. It can contain lowercase letters, digits, hyphens (-), and underscores (_).
        # 
        # >  This parameter is only available for HTTPS listeners.
        self.xforwarded_for_client_cert_issuer_dnalias = xforwarded_for_client_cert_issuer_dnalias
        # Specifies whether to use the `X-Forwarded-Clientcert-issuerdn` header to retrieve information about the authority that issues the client certificate. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is only available for HTTPS listeners.
        self.xforwarded_for_client_cert_issuer_dnenabled = xforwarded_for_client_cert_issuer_dnenabled
        # The name of the custom header. This parameter is valid only if the **XForwardedForClientCertSubjectDNEnabled** parameter is set to **true**.
        # 
        # The name must be 1 to 40 characters in length. It can contain lowercase letters, digits, hyphens (-), and underscores (_).
        # 
        # >  This parameter is only available for HTTPS listeners.
        self.xforwarded_for_client_cert_subject_dnalias = xforwarded_for_client_cert_subject_dnalias
        # Specifies whether to use the `X-Forwarded-Clientcert-subjectdn` header to retrieve information about the owner of the client certificate. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is only available for HTTPS listeners.
        self.xforwarded_for_client_cert_subject_dnenabled = xforwarded_for_client_cert_subject_dnenabled
        # Specifies whether to use the X-Forwarded-For header to preserve client IP addresses. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is only available for HTTP and HTTPS listeners.
        self.xforwarded_for_client_source_ips_enabled = xforwarded_for_client_source_ips_enabled
        # The trusted proxy IP address.
        # 
        # ALB instances traverse the IP addresses in the `X-Forwarded-For` header from the rightmost IP address to the leftmost IP address. The first IP address that is not on the trusted IP address list is considered the client IP address. Requests from the client IP address are throttled.
        self.xforwarded_for_client_source_ips_trusted = xforwarded_for_client_source_ips_trusted
        # Specifies whether to use the `X-Forwarded-Client-srcport` header to retrieve the client port. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is only available for HTTP and HTTPS listeners.
        self.xforwarded_for_client_src_port_enabled = xforwarded_for_client_src_port_enabled
        # Specifies whether to use the `X-Forwarded-For` header to retrieve the client IP address. Valid values:
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
        # Specifies whether to use the `X-Forwarded-Proto` header to retrieve the listener protocol. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is available for HTTP, HTTPS, and QUIC listeners.
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled
        # Specifies whether to use the `SLB-ID` header to retrieve the ID of the ALB instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is available for HTTP, HTTPS, and QUIC listeners.
        self.xforwarded_for_slbid_enabled = xforwarded_for_slbid_enabled
        # Specifies whether to use the `X-Forwarded-Port` header to retrieve the listener port of the ALB instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is available for HTTP, HTTPS, and QUIC listeners.
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

class UpdateListenerAttributeRequestQuicConfig(DaraModel):
    def __init__(
        self,
        quic_listener_id: str = None,
        quic_upgrade_enabled: bool = None,
    ):
        # The QUIC listener ID. This parameter is required if **QuicUpgradeEnabled** is set to **true**. Only HTTPS listeners support this parameter.
        # 
        # > You must add the HTTPS listener and the QUIC listener to the same ALB instance. In addition, make sure that the QUIC listener has never been associated with another listener.
        self.quic_listener_id = quic_listener_id
        # Specifies whether to enable QUIC upgrade. Valid values:
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

class UpdateListenerAttributeRequestDefaultActions(DaraModel):
    def __init__(
        self,
        forward_group_config: main_models.UpdateListenerAttributeRequestDefaultActionsForwardGroupConfig = None,
        type: str = None,
    ):
        # The forwarding action. This parameter takes effect only when you set **Type** to **ForwardGroup**. You can specify at most 20 actions.
        self.forward_group_config = forward_group_config
        # The action type. You can specify only one type.
        # 
        # Set the value to **ForwardGroup**, which specifies that requests are forwarded to multiple server groups.
        # 
        # This parameter is required.
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
            temp_model = main_models.UpdateListenerAttributeRequestDefaultActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m.get('ForwardGroupConfig'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateListenerAttributeRequestDefaultActionsForwardGroupConfig(DaraModel):
    def __init__(
        self,
        server_group_tuples: List[main_models.UpdateListenerAttributeRequestDefaultActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # The server groups to which requests are forwarded.
        # 
        # This parameter is required.
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
                temp_model = main_models.UpdateListenerAttributeRequestDefaultActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k1))

        return self

class UpdateListenerAttributeRequestDefaultActionsForwardGroupConfigServerGroupTuples(DaraModel):
    def __init__(
        self,
        server_group_id: str = None,
    ):
        # The ID of the server group to which requests are forwarded.
        # 
        # This parameter is required.
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

class UpdateListenerAttributeRequestCertificates(DaraModel):
    def __init__(
        self,
        certificate_id: str = None,
    ):
        # The certificate ID.
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

class UpdateListenerAttributeRequestCaCertificates(DaraModel):
    def __init__(
        self,
        certificate_id: str = None,
    ):
        # The ID of the CA certificate.
        # 
        # >  This parameter is required if **CaEnabled** is set to **true**.
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

