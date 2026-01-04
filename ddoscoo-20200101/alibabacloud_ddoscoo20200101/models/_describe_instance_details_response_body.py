# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceDetailsResponseBody(DaraModel):
    def __init__(
        self,
        instance_details: List[main_models.DescribeInstanceDetailsResponseBodyInstanceDetails] = None,
        request_id: str = None,
    ):
        # The IP address and ISP line information about the Anti-DDoS Proxy instance.
        self.instance_details = instance_details
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_details:
            for v1 in self.instance_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceDetails'] = []
        if self.instance_details is not None:
            for k1 in self.instance_details:
                result['InstanceDetails'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_details = []
        if m.get('InstanceDetails') is not None:
            for k1 in m.get('InstanceDetails'):
                temp_model = main_models.DescribeInstanceDetailsResponseBodyInstanceDetails()
                self.instance_details.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceDetailsResponseBodyInstanceDetails(DaraModel):
    def __init__(
        self,
        eip_infos: List[main_models.DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfos] = None,
        instance_id: str = None,
        line: str = None,
    ):
        # The IP address information about the Anti-DDoS Proxy instance.
        self.eip_infos = eip_infos
        # The ID of the instance.
        self.instance_id = instance_id
        # The protection line of the instance.
        self.line = line

    def validate(self):
        if self.eip_infos:
            for v1 in self.eip_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EipInfos'] = []
        if self.eip_infos is not None:
            for k1 in self.eip_infos:
                result['EipInfos'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.line is not None:
            result['Line'] = self.line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eip_infos = []
        if m.get('EipInfos') is not None:
            for k1 in m.get('EipInfos'):
                temp_model = main_models.DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfos()
                self.eip_infos.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        return self

class DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfos(DaraModel):
    def __init__(
        self,
        cert_configured: bool = None,
        eip: str = None,
        function_version: str = None,
        ip_mode: str = None,
        ip_version: str = None,
        ssl_13enabled: bool = None,
        status: str = None,
        tls_version: str = None,
    ):
        # Indicates whether a custom certificate is configured.
        self.cert_configured = cert_configured
        # The IP address of the instance.
        self.eip = eip
        # The type of the instance.
        self.function_version = function_version
        # The IP address-based forwarding mode of the instance. Valid values:
        # 
        # *   **fnat**: Requests from IPv4 addresses are forwarded to origin servers that use IPv4 addresses and requests from IPv6 addresses are forwarded to origin servers that use IPv6 addresses.
        # *   **v6tov4**: All requests are forwarded to origin servers that use IPv4 addresses.
        self.ip_mode = ip_mode
        # The IP version of the protocol. Valid values:
        # 
        # *   **Ipv4**: IPv4
        # *   **Ipv6**: IPv6
        self.ip_version = ip_version
        # Indicates whether the TLS 1.3 version is supported.
        self.ssl_13enabled = ssl_13enabled
        # The status of the instance. Valid values:
        # 
        # *   **normal**: indicates that the instance is normal.
        # *   **expired**: indicates that the instance expired.
        # *   **defense**: indicates that traffic scrubbing is performed on the asset that is protected by the instance.
        # *   **blackhole**: indicates that blackhole filtering is triggered for the asset that is protected by the instance.
        # *   **punished**: indicates that the instance is in penalty.
        self.status = status
        # The Transport Layer Security (TLS) version that is configured.
        self.tls_version = tls_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_configured is not None:
            result['CertConfigured'] = self.cert_configured

        if self.eip is not None:
            result['Eip'] = self.eip

        if self.function_version is not None:
            result['FunctionVersion'] = self.function_version

        if self.ip_mode is not None:
            result['IpMode'] = self.ip_mode

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.ssl_13enabled is not None:
            result['Ssl13Enabled'] = self.ssl_13enabled

        if self.status is not None:
            result['Status'] = self.status

        if self.tls_version is not None:
            result['TlsVersion'] = self.tls_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertConfigured') is not None:
            self.cert_configured = m.get('CertConfigured')

        if m.get('Eip') is not None:
            self.eip = m.get('Eip')

        if m.get('FunctionVersion') is not None:
            self.function_version = m.get('FunctionVersion')

        if m.get('IpMode') is not None:
            self.ip_mode = m.get('IpMode')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Ssl13Enabled') is not None:
            self.ssl_13enabled = m.get('Ssl13Enabled')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TlsVersion') is not None:
            self.tls_version = m.get('TlsVersion')

        return self

