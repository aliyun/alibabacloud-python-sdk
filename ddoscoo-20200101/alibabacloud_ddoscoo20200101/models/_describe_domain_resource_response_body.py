# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainResourceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        web_rules: List[main_models.DescribeDomainResourceResponseBodyWebRules] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of forwarding rules.
        self.total_count = total_count
        # The configurations of the forwarding rule.
        self.web_rules = web_rules

    def validate(self):
        if self.web_rules:
            for v1 in self.web_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['WebRules'] = []
        if self.web_rules is not None:
            for k1 in self.web_rules:
                result['WebRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.web_rules = []
        if m.get('WebRules') is not None:
            for k1 in m.get('WebRules'):
                temp_model = main_models.DescribeDomainResourceResponseBodyWebRules()
                self.web_rules.append(temp_model.from_map(k1))

        return self

class DescribeDomainResourceResponseBodyWebRules(DaraModel):
    def __init__(
        self,
        black_list: List[str] = None,
        cc_enabled: bool = None,
        cc_rule_enabled: bool = None,
        cc_template: str = None,
        cert_name: str = None,
        cname: str = None,
        custom_ciphers: List[str] = None,
        domain: str = None,
        http_2enable: bool = None,
        http_2https_enable: bool = None,
        https_2http_enable: bool = None,
        https_ext: str = None,
        instance_ids: List[str] = None,
        ocsp_enabled: bool = None,
        policy_mode: str = None,
        proxy_enabled: bool = None,
        proxy_types: List[main_models.DescribeDomainResourceResponseBodyWebRulesProxyTypes] = None,
        punish_reason: int = None,
        punish_status: bool = None,
        real_servers: List[str] = None,
        rs_type: int = None,
        ssl_13enabled: bool = None,
        ssl_ciphers: str = None,
        ssl_protocols: str = None,
        white_list: List[str] = None,
    ):
        # The IP addresses that are included in the blacklist of the domain name.
        self.black_list = black_list
        # Indicates whether Frequency Control is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.cc_enabled = cc_enabled
        # Indicates whether the Custom Rules switch of Frequency Control is turned on. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.cc_rule_enabled = cc_rule_enabled
        # The mode of Frequency Control. Valid values:
        # 
        # *   **default**: the Normal mode
        # *   **gf_under_attack**: the Emergency mode
        # *   **gf_sos_verify**: the Strict mode
        # *   **gf_sos_verify**: the Super Strict mode
        self.cc_template = cc_template
        # The name of the SSL certificate used by the domain name.
        self.cert_name = cert_name
        # The CNAME provided by the instance to which the domain name is added.
        self.cname = cname
        # The custom cipher suites.
        self.custom_ciphers = custom_ciphers
        # The domain name of the website.
        self.domain = domain
        # Indicates whether Enable HTTP/2 is turned on. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.http_2enable = http_2enable
        # Indicates whether Enable HTTPS Redirection is turned on. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.http_2https_enable = http_2https_enable
        # Indicates whether Enable HTTP Redirection of Back-to-origin Requests is turned on. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.https_2http_enable = https_2http_enable
        # The advanced HTTPS settings. This parameter takes effect only when the value of the **ProxyType** parameter includes **https**. The value is a string that consists of a JSON struct. The JSON struct contains the following fields:
        # 
        # *   **Http2https**: indicates whether Enable HTTPS Redirection is turned on. Data type: integer. Valid values: **0** and **1**. The value 0 indicates that Enable HTTPS Redirection is turned on. The value 1 indicates that Enable HTTPS Redirection is turned off.
        # *   **Https2http**: indicates whether Enable HTTP Redirection of Back-to-origin Requests is turned on. Data type: integer. Valid values: **0** and **1**. The value 0 indicates that the feature is turned on. The value 1 indicates that the feature is turned off.
        # *   **Http2**: indicates whether Enable HTTP/2 is turned on. Data type: integer. Valid values: **0** and **1**. The value 0 indicates that Enable HTTP/2 is turned off. The value 1 indicates that Enable HTTP/2 is turned on.
        self.https_ext = https_ext
        # The IDs of the instances to which the domain name is added.
        self.instance_ids = instance_ids
        # Indicates whether the Online Certificate Status Protocol (OCSP) feature is turned on. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.ocsp_enabled = ocsp_enabled
        # The scheduling algorithm for back-to-origin traffic. Valid values:
        # 
        # *   **ip_hash**: the IP hash algorithm. This algorithm is used to redirect the requests from the same IP address to the same origin server.
        # *   **rr**: the round-robin algorithm. This algorithm is used to redirect requests to origin servers in turn.
        # *   **least_time**: the least response time algorithm. This algorithm is used to minimize the latency when requests are forwarded from the instance to origin servers based on the intelligent DNS resolution feature.
        self.policy_mode = policy_mode
        # Indicates whether the instance forwards the traffic that is destined for the website. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.proxy_enabled = proxy_enabled
        # The details about the protocol type and port number.
        self.proxy_types = proxy_types
        # The reason why the domain name is invalid. Valid values:
        # 
        # *   **1**: No Content Provider (ICP) filing is completed for the domain name.
        # *   **2**: The business for which you registered the domain name does not meet regulatory requirements.
        # 
        # If the two reasons are both involved, the value **2** is returned.
        self.punish_reason = punish_reason
        # Indicates whether the domain name is invalid. Valid values:
        # 
        # *   **true**: The domain name is invalid. You can view the specific reasons from the **PunishReason** parameter.
        # *   **false**: The domain name is valid.
        self.punish_status = punish_status
        # The addresses of origin servers.
        self.real_servers = real_servers
        # The address type of the origin server. Valid values:
        # 
        # *   **0**: IP address
        # *   **1**: domain name
        self.rs_type = rs_type
        # Indicates whether TLS 1.3 is supported. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.ssl_13enabled = ssl_13enabled
        # The type of the cipher suite. Valid values:
        # 
        # *   **default**: custom cipher suite
        # *   **all**: all cipher suites
        # *   **strong**: strong cipher suites
        self.ssl_ciphers = ssl_ciphers
        # The version of the TLS protocol. Valid values:
        # 
        # *   **tls1.0**: TLS 1.0 or later
        # *   **tls1.1**: TLS 1.1 or later
        # *   **tls1.2**: TLS 1.2 or later
        self.ssl_protocols = ssl_protocols
        # The IP addresses that are included in the whitelist of the domain name.
        self.white_list = white_list

    def validate(self):
        if self.proxy_types:
            for v1 in self.proxy_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.black_list is not None:
            result['BlackList'] = self.black_list

        if self.cc_enabled is not None:
            result['CcEnabled'] = self.cc_enabled

        if self.cc_rule_enabled is not None:
            result['CcRuleEnabled'] = self.cc_rule_enabled

        if self.cc_template is not None:
            result['CcTemplate'] = self.cc_template

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.cname is not None:
            result['Cname'] = self.cname

        if self.custom_ciphers is not None:
            result['CustomCiphers'] = self.custom_ciphers

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.http_2enable is not None:
            result['Http2Enable'] = self.http_2enable

        if self.http_2https_enable is not None:
            result['Http2HttpsEnable'] = self.http_2https_enable

        if self.https_2http_enable is not None:
            result['Https2HttpEnable'] = self.https_2http_enable

        if self.https_ext is not None:
            result['HttpsExt'] = self.https_ext

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.ocsp_enabled is not None:
            result['OcspEnabled'] = self.ocsp_enabled

        if self.policy_mode is not None:
            result['PolicyMode'] = self.policy_mode

        if self.proxy_enabled is not None:
            result['ProxyEnabled'] = self.proxy_enabled

        result['ProxyTypes'] = []
        if self.proxy_types is not None:
            for k1 in self.proxy_types:
                result['ProxyTypes'].append(k1.to_map() if k1 else None)

        if self.punish_reason is not None:
            result['PunishReason'] = self.punish_reason

        if self.punish_status is not None:
            result['PunishStatus'] = self.punish_status

        if self.real_servers is not None:
            result['RealServers'] = self.real_servers

        if self.rs_type is not None:
            result['RsType'] = self.rs_type

        if self.ssl_13enabled is not None:
            result['Ssl13Enabled'] = self.ssl_13enabled

        if self.ssl_ciphers is not None:
            result['SslCiphers'] = self.ssl_ciphers

        if self.ssl_protocols is not None:
            result['SslProtocols'] = self.ssl_protocols

        if self.white_list is not None:
            result['WhiteList'] = self.white_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')

        if m.get('CcEnabled') is not None:
            self.cc_enabled = m.get('CcEnabled')

        if m.get('CcRuleEnabled') is not None:
            self.cc_rule_enabled = m.get('CcRuleEnabled')

        if m.get('CcTemplate') is not None:
            self.cc_template = m.get('CcTemplate')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('CustomCiphers') is not None:
            self.custom_ciphers = m.get('CustomCiphers')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Http2Enable') is not None:
            self.http_2enable = m.get('Http2Enable')

        if m.get('Http2HttpsEnable') is not None:
            self.http_2https_enable = m.get('Http2HttpsEnable')

        if m.get('Https2HttpEnable') is not None:
            self.https_2http_enable = m.get('Https2HttpEnable')

        if m.get('HttpsExt') is not None:
            self.https_ext = m.get('HttpsExt')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('OcspEnabled') is not None:
            self.ocsp_enabled = m.get('OcspEnabled')

        if m.get('PolicyMode') is not None:
            self.policy_mode = m.get('PolicyMode')

        if m.get('ProxyEnabled') is not None:
            self.proxy_enabled = m.get('ProxyEnabled')

        self.proxy_types = []
        if m.get('ProxyTypes') is not None:
            for k1 in m.get('ProxyTypes'):
                temp_model = main_models.DescribeDomainResourceResponseBodyWebRulesProxyTypes()
                self.proxy_types.append(temp_model.from_map(k1))

        if m.get('PunishReason') is not None:
            self.punish_reason = m.get('PunishReason')

        if m.get('PunishStatus') is not None:
            self.punish_status = m.get('PunishStatus')

        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')

        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')

        if m.get('Ssl13Enabled') is not None:
            self.ssl_13enabled = m.get('Ssl13Enabled')

        if m.get('SslCiphers') is not None:
            self.ssl_ciphers = m.get('SslCiphers')

        if m.get('SslProtocols') is not None:
            self.ssl_protocols = m.get('SslProtocols')

        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')

        return self

class DescribeDomainResourceResponseBodyWebRulesProxyTypes(DaraModel):
    def __init__(
        self,
        proxy_ports: List[str] = None,
        proxy_type: str = None,
    ):
        # The port numbers.
        self.proxy_ports = proxy_ports
        # The type of the protocol. Valid values:
        # 
        # *   **http**
        # *   **https**
        # *   **websocket**
        # *   **websockets**
        self.proxy_type = proxy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.proxy_ports is not None:
            result['ProxyPorts'] = self.proxy_ports

        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyPorts') is not None:
            self.proxy_ports = m.get('ProxyPorts')

        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')

        return self

