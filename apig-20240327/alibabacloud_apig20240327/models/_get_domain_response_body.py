# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetDomainResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDomainResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The response message returned.
        self.message = message
        # The request ID, which is used to trace the API call link.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetDomainResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetDomainResponseBodyData(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        ca_cert_identifier: str = None,
        cert_identifier: str = None,
        cert_name: str = None,
        client_cacert: str = None,
        create_from: str = None,
        create_timestamp: int = None,
        default: bool = None,
        domain_id: str = None,
        force_https: bool = None,
        http_2option: str = None,
        issuer: str = None,
        m_tlsenabled: bool = None,
        name: str = None,
        not_after_timstamp: int = None,
        not_before_timestamp: int = None,
        protocol: str = None,
        resource_group_id: str = None,
        sans: str = None,
        statistics_info: main_models.GetDomainResponseBodyDataStatisticsInfo = None,
        tls_cipher_suites_config: main_models.TlsCipherSuitesConfig = None,
        tls_max: str = None,
        tls_min: str = None,
        updatetimestamp: int = None,
    ):
        # The encryption algorithm.
        self.algorithm = algorithm
        # The CA certificate ID.
        self.ca_cert_identifier = ca_cert_identifier
        # The certificate ID.
        self.cert_identifier = cert_identifier
        # The certificate name.
        self.cert_name = cert_name
        # The client CA certificate.
        self.client_cacert = client_cacert
        # The creation source.
        # 
        # Valid values:
        # 
        # *   Console
        # *   Ingress
        self.create_from = create_from
        # The creation timestamp.
        self.create_timestamp = create_timestamp
        # Indicates whether the domain name is the default domain name.
        self.default = default
        # The ID of the domain name.
        self.domain_id = domain_id
        # Indicates whether forcible HTTPS redirection is enabled.
        self.force_https = force_https
        # The HTTP/2 configuration.
        # 
        # Valid values:
        # 
        # *   GlobalConfig
        # *   Close
        # *   Open
        self.http_2option = http_2option
        # The certificate issuer.
        self.issuer = issuer
        # Indicates whether mutual authentication is enabled.
        # 
        # Valid values:
        # 
        # *   false
        # *   true
        self.m_tlsenabled = m_tlsenabled
        # The domain name.
        self.name = name
        # The expiration time of the certificate.
        self.not_after_timstamp = not_after_timstamp
        # The time when the certificate started to take effect.
        self.not_before_timestamp = not_before_timestamp
        # The supported protocol. Valid values:
        # 
        # *   HTTP: Only HTTP is supported.
        # *   HTTPS: Only HTTPS is supported.
        self.protocol = protocol
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # All domain names that are bound to the certificate.
        self.sans = sans
        # The information about online resources.
        self.statistics_info = statistics_info
        # The cipher suite configuration.
        self.tls_cipher_suites_config = tls_cipher_suites_config
        # The maximum version of the TLS protocol. Up to TLS 1.3 is supported.
        self.tls_max = tls_max
        # The minimum version of the TLS protocol. Down to TLS 1.0 is supported.
        self.tls_min = tls_min
        # The update timestamp.
        self.updatetimestamp = updatetimestamp

    def validate(self):
        if self.statistics_info:
            self.statistics_info.validate()
        if self.tls_cipher_suites_config:
            self.tls_cipher_suites_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm

        if self.ca_cert_identifier is not None:
            result['caCertIdentifier'] = self.ca_cert_identifier

        if self.cert_identifier is not None:
            result['certIdentifier'] = self.cert_identifier

        if self.cert_name is not None:
            result['certName'] = self.cert_name

        if self.client_cacert is not None:
            result['clientCACert'] = self.client_cacert

        if self.create_from is not None:
            result['createFrom'] = self.create_from

        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.default is not None:
            result['default'] = self.default

        if self.domain_id is not None:
            result['domainId'] = self.domain_id

        if self.force_https is not None:
            result['forceHttps'] = self.force_https

        if self.http_2option is not None:
            result['http2Option'] = self.http_2option

        if self.issuer is not None:
            result['issuer'] = self.issuer

        if self.m_tlsenabled is not None:
            result['mTLSEnabled'] = self.m_tlsenabled

        if self.name is not None:
            result['name'] = self.name

        if self.not_after_timstamp is not None:
            result['notAfterTimstamp'] = self.not_after_timstamp

        if self.not_before_timestamp is not None:
            result['notBeforeTimestamp'] = self.not_before_timestamp

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.sans is not None:
            result['sans'] = self.sans

        if self.statistics_info is not None:
            result['statisticsInfo'] = self.statistics_info.to_map()

        if self.tls_cipher_suites_config is not None:
            result['tlsCipherSuitesConfig'] = self.tls_cipher_suites_config.to_map()

        if self.tls_max is not None:
            result['tlsMax'] = self.tls_max

        if self.tls_min is not None:
            result['tlsMin'] = self.tls_min

        if self.updatetimestamp is not None:
            result['updatetimestamp'] = self.updatetimestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')

        if m.get('caCertIdentifier') is not None:
            self.ca_cert_identifier = m.get('caCertIdentifier')

        if m.get('certIdentifier') is not None:
            self.cert_identifier = m.get('certIdentifier')

        if m.get('certName') is not None:
            self.cert_name = m.get('certName')

        if m.get('clientCACert') is not None:
            self.client_cacert = m.get('clientCACert')

        if m.get('createFrom') is not None:
            self.create_from = m.get('createFrom')

        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('default') is not None:
            self.default = m.get('default')

        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')

        if m.get('forceHttps') is not None:
            self.force_https = m.get('forceHttps')

        if m.get('http2Option') is not None:
            self.http_2option = m.get('http2Option')

        if m.get('issuer') is not None:
            self.issuer = m.get('issuer')

        if m.get('mTLSEnabled') is not None:
            self.m_tlsenabled = m.get('mTLSEnabled')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('notAfterTimstamp') is not None:
            self.not_after_timstamp = m.get('notAfterTimstamp')

        if m.get('notBeforeTimestamp') is not None:
            self.not_before_timestamp = m.get('notBeforeTimestamp')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('sans') is not None:
            self.sans = m.get('sans')

        if m.get('statisticsInfo') is not None:
            temp_model = main_models.GetDomainResponseBodyDataStatisticsInfo()
            self.statistics_info = temp_model.from_map(m.get('statisticsInfo'))

        if m.get('tlsCipherSuitesConfig') is not None:
            temp_model = main_models.TlsCipherSuitesConfig()
            self.tls_cipher_suites_config = temp_model.from_map(m.get('tlsCipherSuitesConfig'))

        if m.get('tlsMax') is not None:
            self.tls_max = m.get('tlsMax')

        if m.get('tlsMin') is not None:
            self.tls_min = m.get('tlsMin')

        if m.get('updatetimestamp') is not None:
            self.updatetimestamp = m.get('updatetimestamp')

        return self

class GetDomainResponseBodyDataStatisticsInfo(DaraModel):
    def __init__(
        self,
        resource_statistics: List[main_models.ResourceStatistic] = None,
        total_count: str = None,
    ):
        # The resource statistics.
        self.resource_statistics = resource_statistics
        # The total number of resources.
        self.total_count = total_count

    def validate(self):
        if self.resource_statistics:
            for v1 in self.resource_statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['resourceStatistics'] = []
        if self.resource_statistics is not None:
            for k1 in self.resource_statistics:
                result['resourceStatistics'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_statistics = []
        if m.get('resourceStatistics') is not None:
            for k1 in m.get('resourceStatistics'):
                temp_model = main_models.ResourceStatistic()
                self.resource_statistics.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

