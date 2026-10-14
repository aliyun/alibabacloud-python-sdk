# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigL7RsPolicyRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        policy: str = None,
        resource_group_id: str = None,
        upstream_retry: int = None,
    ):
        # The domain name of the website whose forwarding rules you want to manage.
        # 
        # > The domain name must have website forwarding rules configured. You can call [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) to query all domain names that have website forwarding rules configured.
        # 
        # This parameter is required.
        self.domain = domain
        # The back-to-origin policy. The value is a character string that represents a JSON structure. The JSON structure contains the following fields:
        # 
        #  - **ProxyMode**: String | Required | The load balancing algorithm for back-to-origin. Valid values:
        #     - **ip_hash**: IP Hash algorithm. Requests from the same source IP address are directed to the same origin server based on hash mapping.
        #     - **rr**: Polling algorithm. All requests are allocated to different origin servers in turn. When you use this algorithm, you can set weights for servers based on their performance.
        #      - **least_time**: Least Time algorithm. This algorithm uses intelligent DNS resolution to ensure the lowest latency for service traffic across the entire path from the protection node to forward back to the origin server.
        # - **Attributes**: JSONArray | Optional | The back-to-origin parameter information. Each element in the array contains the following fields:
        #     - **RealServer**: String | Optional | The address of the origin server.
        #     - **Attribute**: JSONObject | Optional | The back-to-origin parameters. This field contains the following fields:
        #         - **Weight**: Integer | Optional | The weight of the server. This property takes effect only when the polling algorithm is used (**ProxyMode** is set to **rr**). Valid values: **1** to **100**. Default value: **100**. A server with a higher weight receives more requests.
        #         - **ConnectTimeout**: Integer | Optional | The timeout period for new connections. Valid values: **1** to **10**. Unit: seconds. Default value: **5**.
        #         - **FailTimeout**: Integer | Optional | The failed timeout period. Valid values: **1** to **3600**. Unit: seconds. Default value: **10**.
        #         - **MaxFails**: Integer | Optional | The maximum number of failures for health checks. Valid values: **1** to **10**. Default value: **3**.
        #         - **Mode**: String | Optional | The primary/secondary property flag. Valid values: **active** indicates primary. **backup** indicates secondary.
        #         - **ReadTimeout**: Integer | Optional | The read timeout period. Valid values: **10** to **300**. Unit: seconds. Default value: **120**.
        #         - **SendTimeout**: Integer | Optional | The write timeout period. Valid values: **10** to **300**. Unit: seconds. Default value: **120**.
        # 
        # This parameter is required.
        self.policy = policy
        # The ID of the resource group to which the Anti-DDoS Pro or Anti-DDoS Premium instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id
        # Specifies whether to enable back-to-origin retry. Valid values:
        # 
        # - **1**: Enabled.
        # - **0**: Disabled.
        self.upstream_retry = upstream_retry

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.upstream_retry is not None:
            result['UpstreamRetry'] = self.upstream_retry

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('UpstreamRetry') is not None:
            self.upstream_retry = m.get('UpstreamRetry')

        return self

