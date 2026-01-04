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
        # The ID of the associated defense. This parameter applies to scenarios in which other cloud services, such as Object Storage Service (OSS), are integrated with Anti-DDoS Pro or Anti-DDoS Premium.
        # 
        # > This parameter is in internal preview. Do not use this parameter.
        # 
        # For example, if you integrate OSS with Anti-DDoS Pro or Anti-DDoS Premium, Anti-DDoS Pro or Anti-DDoS Premium allocates an IP address pool for the OSS production account. Each IP address corresponds to a unique defense ID. A defense ID is a CNAME, which is automatically resolved to the IP address of the required Anti-DDoS Pro or Anti-DDoS Premium instance. A defense ID can be resolved to the same IP address to facilitate scheduling.
        # 
        # > You can specify only one of the following parameters: **InstanceIds** and **DefenseId**.
        self.defense_id = defense_id
        # The domain name of the website that you want to add to the instance.
        # 
        # This parameter is required.
        self.domain = domain
        # The advanced HTTPS settings. This parameter takes effect only when the value of the **ProxyType** parameter includes **https**. The value is a string that consists of a JSON struct. The JSON struct contains the following fields:
        # 
        # *   **Http2https**: specifies whether to turn on Enforce HTTPS Routing. This field is optional and must be an integer. Valid values: **0** and **1**. The value 0 indicates that Enforce HTTPS Routing is turned off. The value 1 indicates that Enforce HTTPS Routing is turned on. The default value is 0.
        # 
        #     If your website supports both HTTP and HTTPS, this feature meets your business requirements. If you enable this feature, all HTTP requests to access the website are redirected to HTTPS requests on the standard port 443.
        # 
        # *   **Https2http**: specifies whether to turn on Enable HTTP. This field is optional and must be an integer. Valid values: **0** and **1**. The value 0 indicates that Enable HTTP is turned off. The value 1 indicates that Enable HTTP is turned on. The default value is 0.
        # 
        #     If your website does not support HTTPS, this feature meets your business requirements If this feature is enabled, all HTTPS requests are redirected to HTTP requests and forwarded to origin servers. This feature can redirect WebSockets requests to WebSocket requests. Requests are redirected over the standard port 80.
        # 
        # *   **Http2**: specifies whether to turn on Enable HTTP/2. This field is optional and must be an integer. Valid values: **0** and **1**. The value 0 indicates that Enable HTTP/2 is turned off. The value 1 indicates that Enable HTTP/2 is turned on. The default value is 0.
        # 
        #     After you turn on Enable HTTP/2, the protocol type is HTTP/2.
        self.https_ext = https_ext
        # An array consisting of the IDs of instances that you want to associate.
        self.instance_ids = instance_ids
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id
        # The address type of the origin server. Valid values:
        # 
        # *   **0**: IP address
        # *   **1**: domain name The domain name of the origin server is returned if you deploy proxies, such as Web Application Firewall (WAF), between the origin server and the instance. In this case, the address of the proxy, such as the CNAME provided by WAF, is returned.
        # 
        # This parameter is required.
        self.rs_type = rs_type
        # The details of the forwarding rule. The value is a string that consists of JSON arrays. Each element in a JSON array is a JSON struct that contains the following fields:
        # 
        # *   **ProxyRules**: the information about the origin server. The information includes the port number and IP address. This field is required and must be a JSON array. Each element in a JSON array is a JSON struct that contains the following fields:
        # 
        #     *   **ProxyPort**: the port number. This field is required and must be an integer.
        #     *   **RealServers**: the IP address. This field is required and must be a string array.
        # 
        # *   **ProxyType**: the protocol type. This field is required and must be a string. Valid values: **http**, **https**, **websocket**, and **websockets**.
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

