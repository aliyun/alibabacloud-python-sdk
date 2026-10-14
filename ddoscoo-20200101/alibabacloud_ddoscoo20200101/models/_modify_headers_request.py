# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyHeadersRequest(DaraModel):
    def __init__(
        self,
        custom_headers: str = None,
        domain: str = None,
        embedded_headers: str = None,
        resource_group_id: str = None,
    ):
        # The custom header, specified as a key-value pair. The key is the header name and the value is the header value. You can specify up to 5 key-value pairs. The total length cannot exceed 200 characters.
        # 
        # Important:
        # 
        # - - X-Forwarded-ClientSrcPort: Used by default to retrieve the client port that accesses the Layer 7 engine of Anti-DDoS Pro.
        # 
        #   - X-Forwarded-ProxyPort: Used by default to retrieve the listening port of the Layer 7 engine of Anti-DDoS Pro.
        # 
        #   - X-Forwarded-For: Used by default to retrieve the client IP address that accesses the Layer 7 engine of Anti-DDoS Pro.
        # 
        # - Do not use standard HTTP header fields (such as `host`, `user-agent`, `connection`, and `upgrade`) or common custom HTTP header fields (such as `x-real-ip`, `x-true-ip`, `x-client-ip`, `web-server-type`, `wl-proxy-client-ip`, `eagleeye-rpcid`, `eagleeye-traceid`, `x-forwarded-cluster`, and `x-forwarded-proto`) as they will overwrite the original header values in requests.
        # 
        # > To use the `X-Forwarded-ClientSrcPort` key to retrieve the client port that accesses the Layer 7 engine of Anti-DDoS Pro, set the value to `""`.
        # 
        # This parameter is required.
        self.custom_headers = custom_headers
        # The domain of the website.
        # 
        # > A website service forwarding rule must be configured for the domain. You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query all your domains.
        # 
        # This parameter is required.
        self.domain = domain
        # The forwarding configuration for request headers. This parameter is a JSON string of key-value pairs where the key is the header field name and the value is a boolean. Set the value to `true` to enable forwarding or `false` to disable it.
        # 
        # Field description:
        # 
        # `X-Client-IP`: Forwards the client\\"s real IP address.
        # 
        # `X-True-IP`: Forwards the client\\"s connection IP address.
        # 
        # `Web-Server-Type`: Informs the back-end server about the type of front-end web server or proxy that is handling the request.
        # 
        # `WL-Proxy-Client-IP`: A request header specific to Oracle WebLogic Server that provides the same functionality as `X-Client-IP`.
        # 
        # `X-Forwarded-Proto`: Indicates the protocol used for the connection between the client and the first proxy.
        # 
        # Important:
        # 
        # - **Supported Headers**: The configuration supports only the five preset header fields listed above.
        # 
        # - **Default settings**: All the listed header fields are enabled by default. To make changes, you must explicitly set the corresponding value to `false`.
        self.embedded_headers = embedded_headers
        # The ID of the resource group.
        # 
        # > - You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation or use the console to obtain a list of resource group IDs. For more information, see [View basic information about a resource group](https://help.aliyun.com/document_detail/151181.html).
        # 
        # - To find the current resource group of an instance before changing it, call the [ListResources](https://help.aliyun.com/document_detail/158866.html) operation.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_headers is not None:
            result['CustomHeaders'] = self.custom_headers

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.embedded_headers is not None:
            result['EmbeddedHeaders'] = self.embedded_headers

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomHeaders') is not None:
            self.custom_headers = m.get('CustomHeaders')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EmbeddedHeaders') is not None:
            self.embedded_headers = m.get('EmbeddedHeaders')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

