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
        # The request ID.
        self.request_id = request_id
        # The total number of web rules returned.
        self.total_count = total_count
        # An array of web rule configurations.
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
        # An array of IP addresses on the blocklist for the domain.
        self.black_list = black_list
        # Whether CC protection is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.cc_enabled = cc_enabled
        # Whether custom CC protection rules are enabled. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.cc_rule_enabled = cc_rule_enabled
        # The CC protection mode. Valid values:
        # 
        # - **default**: normal mode
        # 
        # - **gf_under_attack**: Emergency mode
        # 
        # - **gf_sos_verify**: Strict mode
        # 
        # - **gf_sos_enhance**: Super Strict mode
        self.cc_template = cc_template
        # The name of the SSL certificate used by the domain.
        self.cert_name = cert_name
        # The CNAME assigned to the domain by Anti-DDoS Pro.
        self.cname = cname
        # An array of custom cipher suites.
        self.custom_ciphers = custom_ciphers
        # The domain name.
        self.domain = domain
        # Whether HTTP/2 is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.http_2enable = http_2enable
        # Whether forced HTTPS redirect is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.http_2https_enable = http_2https_enable
        # Whether HTTP back-to-source is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.https_2http_enable = https_2http_enable
        # The advanced HTTPS settings, formatted as a JSON string. These settings apply only when the domain uses HTTPS (the `ProxyType` value includes `https`). The string contains the following fields:
        # 
        # - **Http2https**: integer. Specifies whether to enable forced HTTPS redirect. Valid values: **0** (disabled) and **1** (enabled).
        # 
        # - **Https2http**: integer. Specifies whether to enable HTTP back-to-source. Valid values: **0** (disabled) and **1** (enabled).
        # 
        # - **Http2**: integer. Specifies whether to enable HTTP/2. Valid values: **0** (disabled) and **1** (enabled).
        self.https_ext = https_ext
        # An array of IDs for the Anti-DDoS Pro instances associated with the domain.
        self.instance_ids = instance_ids
        # Whether Online Certificate Status Protocol (OCSP) is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.ocsp_enabled = ocsp_enabled
        # The back-to-source load balancing algorithm. This algorithm determines how traffic is distributed to origin servers. Valid values:
        # 
        # - **ip_hash**: IP Hash. This algorithm hashes the source IP address and routes all requests from the same IP address to the same origin server.
        # 
        # - **rr**: Round Robin. This algorithm distributes requests across origin servers in turn.
        # 
        # - **least_time**: Least Time. This algorithm uses intelligent DNS resolution to minimize end-to-end latency from the protection node to the origin server.
        self.policy_mode = policy_mode
        # Whether Anti-DDoS Pro forwards traffic for the domain. Valid values:
        # 
        # - **true**: Forwarding is enabled.
        # 
        # - **false**: Forwarding is disabled.
        self.proxy_enabled = proxy_enabled
        # An array of proxy configurations for the domain, each specifying a protocol and its associated ports.
        self.proxy_types = proxy_types
        # The reason the domain is penalized. Valid values:
        # 
        # - **1**: The domain does not have an ICP filing.
        # 
        # - **2**: The business hosted on the domain does not meet regulatory requirements.
        # 
        # If both reasons apply, this parameter returns **2**.
        self.punish_reason = punish_reason
        # Whether the domain is penalized. Valid values:
        # 
        # - **true**: The domain is penalized. For more information, see the `PunishReason` parameter.
        # 
        # - **false**: The domain is not penalized.
        self.punish_status = punish_status
        # An array of origin server addresses.
        self.real_servers = real_servers
        # The address type of the origin server. Valid values:
        # 
        # - **0**: IP address
        # 
        # - **1**: domain
        self.rs_type = rs_type
        # Whether TLS 1.3 is enabled. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.ssl_13enabled = ssl_13enabled
        # The cipher suite configuration type. Valid values:
        # 
        # - **default**: Custom
        # 
        # - **all**: All
        # 
        # - **strong**: Strong
        # 
        # - **improved**: Improved
        self.ssl_ciphers = ssl_ciphers
        # The minimum TLS protocol version. Valid values:
        # 
        # - **tls1.0**: TLS 1.0 and later versions.
        # 
        # - **tls1.1**: TLS 1.1 and later versions.
        # 
        # - **tls1.2**: TLS 1.2 and later versions.
        self.ssl_protocols = ssl_protocols
        # An array of IP addresses on the allowlist for the domain.
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
        # The array of ports associated with the protocol.
        self.proxy_ports = proxy_ports
        # The proxy protocol. Valid values:
        # 
        # - **http**: HTTP
        # 
        # - **https**: HTTPS
        # 
        # - **websocket**: WebSocket
        # 
        # - **websockets**: WebSockets
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

