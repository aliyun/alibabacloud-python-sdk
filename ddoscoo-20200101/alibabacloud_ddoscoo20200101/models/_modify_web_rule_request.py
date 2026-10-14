# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyWebRuleRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        https_ext: str = None,
        instance_ids: List[str] = None,
        proxy_types: str = None,
        real_servers: List[str] = None,
        resource_group_id: str = None,
        rs_type: int = None,
    ):
        # The domain name of the website business to operate.
        # 
        # > The domain name must have a website forwarding rule configured. You can call [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) to query all domain names that have website forwarding rules configured.
        # 
        # This parameter is required.
        self.domain = domain
        # The HTTPS advanced settings, which take effect only when the website protocol type supports HTTPS (**ProxyType** includes **https**). This parameter is a string converted from a JSON struct that contains the following fields:
        # 
        # - **Http2https**: Integer type | Optional | Specifies whether to enable the HTTPS force redirect feature. Valid values: **0** (disabled) | **1** (enabled). Default value: 0 (disabled).
        # 
        #   This is applicable when your website supports both HTTP and HTTPS protocols. After this setting is enabled, all HTTP requests will be forcibly converted to HTTPS requests and redirected to port 443 by default.
        # 
        # - **Https2http**: Integer type | Optional | Specifies whether to enable the HTTP back-to-origin feature. Valid values: **0** (disabled) | **1** (enabled). Default value: 0 (disabled).
        # 
        #   This is applicable when your website does not support HTTPS back-to-origin. After this setting is enabled, all HTTPS protocol requests will be forwarded to the origin through HTTP (Websockets protocol requests will be forwarded through Websocket), and the default back-to-origin port is 80.
        # 
        # - **Http2**: Integer type | Optional | Specifies whether to enable the HTTP2.0 protocol type. Valid values: **0** (disabled) | **1** (enabled). Default value: 0 (disabled).
        # 
        #   After this setting is enabled, the protocol version is HTTP2.0.
        self.https_ext = https_ext
        # The list of Anti-DDoS Proxy instance IDs to associate. You can associate up to 100 instances.
        self.instance_ids = instance_ids
        # The protocol information of the website forwarding rule. This parameter is a string converted from a JSON array. Each element in the JSON array is a JSON struct that contains the following fields:
        # 
        # - **ProxyType**: String type | Required | The website protocol type. Valid values: **http** | **https** | **websocket** | **websockets**.
        # 
        # - **ProxyPorts**: array type | Required | The port numbers corresponding to the protocol.
        # 
        # This parameter is required.
        self.proxy_types = proxy_types
        # The list of origin server addresses.
        # 
        # This parameter is required.
        self.real_servers = real_servers
        # The resource group ID of the Anti-DDoS Proxy instance in Resource Management. Default value: empty, which indicates that the instance belongs to the default resource group.
        # 
        # For more information, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id
        # The address type of the origin server. Valid values:
        # 
        # - **0**: indicates the IP address of the origin server.
        # 
        # - **1**: indicates the domain name of the origin server. This is typically applicable to scenarios where other proxy services (such as WAF) are deployed between the origin server and Anti-DDoS Proxy, specifically referring to the redirect address of the proxy service (such as the WAF CNAME address).
        # 
        # This parameter is required.
        self.rs_type = rs_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.https_ext is not None:
            result['HttpsExt'] = self.https_ext

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.proxy_types is not None:
            result['ProxyTypes'] = self.proxy_types

        if self.real_servers is not None:
            result['RealServers'] = self.real_servers

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.rs_type is not None:
            result['RsType'] = self.rs_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('HttpsExt') is not None:
            self.https_ext = m.get('HttpsExt')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('ProxyTypes') is not None:
            self.proxy_types = m.get('ProxyTypes')

        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')

        return self

