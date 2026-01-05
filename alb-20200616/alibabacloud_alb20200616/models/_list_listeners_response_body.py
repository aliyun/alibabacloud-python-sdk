# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class ListListenersResponseBody(DaraModel):
    def __init__(
        self,
        listeners: List[main_models.ListListenersResponseBodyListeners] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The listeners.
        self.listeners = listeners
        # The maximum number of entries returned.
        self.max_results = max_results
        # The position where the query stopped. If this parameter is not returned, all data is queried.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.listeners:
            for v1 in self.listeners:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Listeners'] = []
        if self.listeners is not None:
            for k1 in self.listeners:
                result['Listeners'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listeners = []
        if m.get('Listeners') is not None:
            for k1 in m.get('Listeners'):
                temp_model = main_models.ListListenersResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListListenersResponseBodyListeners(DaraModel):
    def __init__(
        self,
        default_actions: List[main_models.ListListenersResponseBodyListenersDefaultActions] = None,
        gzip_enabled: bool = None,
        http_2enabled: bool = None,
        idle_timeout: int = None,
        listener_description: str = None,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        listener_status: str = None,
        load_balancer_id: str = None,
        log_config: main_models.ListListenersResponseBodyListenersLogConfig = None,
        quic_config: main_models.ListListenersResponseBodyListenersQuicConfig = None,
        request_timeout: int = None,
        security_policy_id: str = None,
        tags: List[main_models.ListListenersResponseBodyListenersTags] = None,
        xforwarded_for_config: main_models.ListListenersResponseBodyListenersXForwardedForConfig = None,
    ):
        # The default actions in the forwarding rules.
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
        # >  Only HTTPS listeners support this parameter.
        self.http_2enabled = http_2enabled
        # The timeout period of an idle connection. Unit: seconds. Valid values: **1 to 60**.
        # 
        # If no request is received within the specified timeout period, ALB closes the connection. ALB establishes the connection again when a new connection request is received.
        self.idle_timeout = idle_timeout
        # The name of the listener.
        self.listener_description = listener_description
        # The listener ID.
        self.listener_id = listener_id
        # The frontend port that is used by the ALB instance. Valid values: **1 to 65535**.
        self.listener_port = listener_port
        # The listener protocol of the instance. Valid values:
        # 
        # *   **HTTP**
        # *   **HTTPS**
        # *   **QUIC**
        self.listener_protocol = listener_protocol
        # The status of the listener. Valid values:
        # 
        # *   **Provisioning**: The listener is being created.
        # *   **Running**: The listener is running.
        # *   **Configuring**: The listener is being configured.
        # *   **Stopped**: The listener is disabled.
        self.listener_status = listener_status
        # The ALB instance ID.
        self.load_balancer_id = load_balancer_id
        # The logging configurations.
        self.log_config = log_config
        # The configurations of the QUIC listener associated with the ALB instance.
        self.quic_config = quic_config
        # The timeout period of a request. Unit: seconds. Valid values: **1 to 180**.
        # 
        # If no responses are received from the backend server within the specified timeout period, ALB returns an `HTTP 504` error code to the client.
        self.request_timeout = request_timeout
        # The security policy.
        # 
        # >  Only HTTPS listeners support this parameter.
        self.security_policy_id = security_policy_id
        # The tags.
        self.tags = tags
        # The configuration of the `XForward` header.
        self.xforwarded_for_config = xforwarded_for_config

    def validate(self):
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
        self.default_actions = []
        if m.get('DefaultActions') is not None:
            for k1 in m.get('DefaultActions'):
                temp_model = main_models.ListListenersResponseBodyListenersDefaultActions()
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
            temp_model = main_models.ListListenersResponseBodyListenersLogConfig()
            self.log_config = temp_model.from_map(m.get('LogConfig'))

        if m.get('QuicConfig') is not None:
            temp_model = main_models.ListListenersResponseBodyListenersQuicConfig()
            self.quic_config = temp_model.from_map(m.get('QuicConfig'))

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListListenersResponseBodyListenersTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('XForwardedForConfig') is not None:
            temp_model = main_models.ListListenersResponseBodyListenersXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m.get('XForwardedForConfig'))

        return self

class ListListenersResponseBodyListenersXForwardedForConfig(DaraModel):
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
        # The name must be 1 to 40 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores (_).
        # 
        # >  Only HTTPS listeners support this parameter.
        self.xforwarded_for_client_cert_client_verify_alias = xforwarded_for_client_cert_client_verify_alias
        # Indicates whether the `X-Forwarded-Clientcert-clientverify` header is used to obtain the verification result of the client certificate. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  Only HTTPS listeners support this parameter.
        self.xforwarded_for_client_cert_client_verify_enabled = xforwarded_for_client_cert_client_verify_enabled
        # The name of the custom header. This parameter takes effect only when **XForwardedForClientCertFingerprintEnabled** is set to **true**.
        # 
        # The name must be 1 to 40 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores (_).
        # 
        # >  Only HTTPS listeners support this parameter.
        self.xforwarded_for_client_cert_fingerprint_alias = xforwarded_for_client_cert_fingerprint_alias
        # Indicates whether the `X-Forwarded-Clientcert-fingerprint` header is used to retrieve the fingerprint of the client certificate. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  Only HTTPS listeners support this parameter.
        self.xforwarded_for_client_cert_fingerprint_enabled = xforwarded_for_client_cert_fingerprint_enabled
        # The name of the custom header. This parameter takes effect only when **XForwardedForClientCertIssuerDNEnabled** is set to **true**.
        # 
        # The name must be 1 to 40 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores (_).
        # 
        # >  Only HTTPS listeners support this parameter.
        self.xforwarded_for_client_cert_issuer_dnalias = xforwarded_for_client_cert_issuer_dnalias
        # Indicates whether the `X-Forwarded-Clientcert-issuerdn` header is used to retrieve information about the authority that issues the client certificate. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  Only HTTPS listeners support this parameter.
        self.xforwarded_for_client_cert_issuer_dnenabled = xforwarded_for_client_cert_issuer_dnenabled
        # The name of the custom header. This parameter takes effect only when **XForwardedForClientCertSubjectDNEnabled** is set to **true**.
        # 
        # The name must be 1 to 40 characters in length, and can contain lowercase letters, digits, hyphens (-), and underscores (_).
        # 
        # >  Only HTTPS listeners support this parameter.
        self.xforwarded_for_client_cert_subject_dnalias = xforwarded_for_client_cert_subject_dnalias
        # Indicates whether the `X-Forwarded-Clientcert-subjectdn` header is used to retrieve information about the owner of the client certificate. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  Only HTTPS listeners support this parameter.
        self.xforwarded_for_client_cert_subject_dnenabled = xforwarded_for_client_cert_subject_dnenabled
        # Indicates whether the X-Forwarded-For header is used to preserver client IP addresses for the ALB instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is returned only for HTTP and HTTPS listeners.
        self.xforwarded_for_client_source_ips_enabled = xforwarded_for_client_source_ips_enabled
        # The trusted proxy IP address.
        # 
        # ALB instances traverse the IP addresses in the `X-Forwarded-For` header from the rightmost IP address to the leftmost IP address. The first IP address that is not on the trusted IP address list is considered the client IP address. Requests from the client IP address are throttled.
        self.xforwarded_for_client_source_ips_trusted = xforwarded_for_client_source_ips_trusted
        # Indicates whether the `X-Forwarded-Client-Port` header is used to retrieve the client port. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is returned only for HTTP and HTTPS listeners.
        self.xforwarded_for_client_src_port_enabled = xforwarded_for_client_src_port_enabled
        # Specifies whether to use the `X-Forwarded-For` header to retrieve client IP addresses. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        # 
        # > *   If this parameter is set to **true**, the default value of the **XForwardedForProcessingMode** parameter is **append**. You can change it to **remove**.
        # > *   If this parameter is set to **false**, the `X-Forwarded-For` header in the request is not modified in any way before the request is sent to backend servers.
        # > *   Both HTTP and HTTPS listeners support this parameter.
        self.xforwarded_for_enabled = xforwarded_for_enabled
        # Specifies whether to use the `X-Forwarded-Host` header to retrieve client domain names. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # >  HTTP, HTTPS, and QUIC listeners all support this parameter.
        self.xforwarded_for_host_enabled = xforwarded_for_host_enabled
        # Specifies how the `X-Forwarded-For` header is processed. This parameter takes effect only when **XForwardedForEnabled** is set to **true**. Valid values:
        # 
        # *   **append** (default)
        # *   **remove**
        # 
        # > *   If this parameter is set to **append**, ALB appends the IP address of the last hop to the existing `X-Forwarded-For` header in the request before the request is sent to backend servers.
        # > *   If this parameter is set to **remove**, ALB removes the `X-Forwarded-For` header in the request before the request is sent to backend servers, no matter whether the request carries the `X-Forwarded-For` header.
        # > *   Both HTTP and HTTPS listeners support this parameter.
        self.xforwarded_for_processing_mode = xforwarded_for_processing_mode
        # Indicates whether the `X-Forwarded-Proto` header is used to retrieve the listener protocol. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is supported by HTTP, HTTPS, and QUIC listeners.
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled
        # Specifies whether to use the `SLB-ID` header to retrieve the ID of the ALB instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is supported by HTTP, HTTPS, and QUIC listeners.
        self.xforwarded_for_slbid_enabled = xforwarded_for_slbid_enabled
        # Indicates whether the `X-Forwarded-Port` header is used to retrieve the listener port of the ALB instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter is supported by HTTP, HTTPS, and QUIC listeners.
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

class ListListenersResponseBodyListenersTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://.
        self.key = key
        # The tag value. The tag value can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://.
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

class ListListenersResponseBodyListenersQuicConfig(DaraModel):
    def __init__(
        self,
        quic_listener_id: str = None,
        quic_upgrade_enabled: bool = None,
    ):
        # The ID of the QUIC listener associated with the ALB instance. This parameter is required if the **QuicUpgradeEnabled** parameter is set to **true**. Only HTTPS listeners support this parameter.
        # 
        # >  The existing listener and QUIC listener must be to the same ALB instance, and the QUIC listener has not been associated with an ALB instance.
        self.quic_listener_id = quic_listener_id
        # Indicates whether QUIC upgrade is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  Only HTTPS listeners support this parameter.
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

class ListListenersResponseBodyListenersLogConfig(DaraModel):
    def __init__(
        self,
        access_log_record_customized_headers_enabled: bool = None,
        access_log_tracing_config: main_models.ListListenersResponseBodyListenersLogConfigAccessLogTracingConfig = None,
    ):
        # Indicates whether custom headers are carried in the access log. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.access_log_record_customized_headers_enabled = access_log_record_customized_headers_enabled
        # The configurations of xtrace.
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
            temp_model = main_models.ListListenersResponseBodyListenersLogConfigAccessLogTracingConfig()
            self.access_log_tracing_config = temp_model.from_map(m.get('AccessLogTracingConfig'))

        return self

class ListListenersResponseBodyListenersLogConfigAccessLogTracingConfig(DaraModel):
    def __init__(
        self,
        tracing_enabled: bool = None,
        tracing_sample: int = None,
        tracing_type: str = None,
    ):
        # Indicates whether xtrace is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter can be set to **true** only when the access log feature of ALB is enabled by setting **AccessLogEnabled** to true.
        self.tracing_enabled = tracing_enabled
        # The sampling rate of xtrace. Valid values: **1 to 10000**.
        # 
        # >  This parameter takes effect when **TracingEnabled** is set to **true**.
        self.tracing_sample = tracing_sample
        # The type of xtrace. The value is set to **Zipkin**.
        # 
        # >  This parameter takes effect when **TracingEnabled** is set to **true**.
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

class ListListenersResponseBodyListenersDefaultActions(DaraModel):
    def __init__(
        self,
        forward_group_config: main_models.ListListenersResponseBodyListenersDefaultActionsForwardGroupConfig = None,
        type: str = None,
    ):
        # The configuration of the forwarding rule action. This parameter takes effect only when the action is **ForwardGroup**.
        self.forward_group_config = forward_group_config
        # The action. **ForwardGroup**: forwards requests to multiple server groups.
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
            temp_model = main_models.ListListenersResponseBodyListenersDefaultActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m.get('ForwardGroupConfig'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListListenersResponseBodyListenersDefaultActionsForwardGroupConfig(DaraModel):
    def __init__(
        self,
        server_group_tuples: List[main_models.ListListenersResponseBodyListenersDefaultActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # The server groups to which requests are forwarded.
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
                temp_model = main_models.ListListenersResponseBodyListenersDefaultActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k1))

        return self

class ListListenersResponseBodyListenersDefaultActionsForwardGroupConfigServerGroupTuples(DaraModel):
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

