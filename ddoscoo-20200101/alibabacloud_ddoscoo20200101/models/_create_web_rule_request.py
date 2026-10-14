# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateWebRuleRequest(DaraModel):
    def __init__(
        self,
        defense_id: str = None,
        domain: str = None,
        https_ext: str = None,
        instance_ids: List[str] = None,
        resource_group_id: str = None,
        rs_type: int = None,
        rules: str = None,
    ):
        # The ID of the protection rule to associate. This parameter is used when an Alibaba Cloud service, such as Object Storage Service (OSS), is integrated with an Anti-DDoS instance.
        # 
        # > This parameter is for internal use. Do not use this parameter.
        # 
        # For example, if your OSS is integrated with an Anti-DDoS Proxy instance, the instance allocates a resource pool of IP addresses to the OSS tenant account. Each IP address has a unique protection ID. The protection ID is a CNAME that resolves to the IP address of the Anti-DDoS instance by default. You can resolve the CNAME to an IP address. This lets you reuse the IP address for flexible scheduling.
        # 
        # > You cannot specify both **InstanceIds** and **DefenseId**.
        self.defense_id = defense_id
        # The domain name of the website to add to the Anti-DDoS Proxy instance for protection.
        # 
        # This parameter is required.
        self.domain = domain
        # The advanced HTTPS settings. This parameter takes effect only when the value of **ProxyType** includes **https**. This parameter is a JSON string. The value is a JSON object that contains the following fields:
        # 
        # - **Http2https**: This field is an integer. Optional. Specifies whether to forcibly redirect HTTP requests to HTTPS requests. Valid values: **0** (disabled) and **1** (enabled). The default value is 0.
        # 
        #   This setting is available when your website supports both HTTP and HTTPS. If you enable this setting, all HTTP requests are redirected to HTTPS requests over port 443.
        # 
        # - **Https2http**: This field is an integer. Optional. Specifies whether to enable HTTP back-to-origin. Valid values: **0** (disabled) and **1** (enabled). The default value is 0.
        # 
        #   This setting applies to websites that do not support HTTPS back-to-origin. If you enable this setting, all HTTPS requests are sent to the origin server over HTTP on port 80 by default. All WebSockets requests are sent to the origin server over WebSocket.
        # 
        # - **Http2**: This field is an integer. Optional. Specifies whether to enable HTTP/2. Valid values: **0** (disabled) and **1** (enabled). The default value is 0.
        # 
        #   If you enable this setting, HTTP/2 is used.
        self.https_ext = https_ext
        # The IDs of the Anti-DDoS Proxy instances to associate.
        self.instance_ids = instance_ids
        # The ID of the resource group to which the Anti-DDoS Proxy instance belongs in Resource Management. If you leave this parameter empty, the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id
        # The address type of the origin server. Valid values:
        # 
        # - **0**: IP address.
        # 
        # - **1**: domain name. This value is typically used when a proxy service, such as Web Application Firewall (WAF), is deployed between the origin server and the Anti-DDoS Proxy instance. The domain name is the back-to-origin address of the proxy service, such as the canonical name (CNAME) of WAF.
        # 
        # This parameter is required.
        self.rs_type = rs_type
        # The details of the forwarding rule, in a JSON string format. The value is an array of objects. Each object contains the following fields:
        # 
        # - **ProxyRules**: This field is a JSON array. Required. The information about the origin server, including the port number and server address. Each object in the array contains the following fields:
        # 
        #   - **ProxyPort**: This field is an integer. Required. The port number that is used by the protocol.
        # 
        #   - **RealServers**: This field is a string array. Required. The addresses of the origin servers.
        # 
        # - **ProxyType**: This field is a string. Required. The protocol of the website. Valid values: **http**, **https**, **websocket**, and **websockets**.
        # 
        # This parameter is required.
        self.rules = rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_id is not None:
            result['DefenseId'] = self.defense_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.https_ext is not None:
            result['HttpsExt'] = self.https_ext

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.rs_type is not None:
            result['RsType'] = self.rs_type

        if self.rules is not None:
            result['Rules'] = self.rules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseId') is not None:
            self.defense_id = m.get('DefenseId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('HttpsExt') is not None:
            self.https_ext = m.get('HttpsExt')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        return self

