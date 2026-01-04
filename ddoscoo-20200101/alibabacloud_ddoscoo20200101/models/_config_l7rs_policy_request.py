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
        # The domain name of the website.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query the domain names for which forwarding rules are configured.
        # 
        # This parameter is required.
        self.domain = domain
        # The back-to-origin policy. The value is a string that consists of a JSON struct. The JSON struct contains the following fields:
        # 
        # *   **ProxyMode**: The load balancing algorithm for back-to-origin traffic. This field is required and must be a string. Valid values:
        # 
        #     *   **ip_hash**: the IP hash algorithm. This algorithm is used to redirect requests from the same IP address to the same origin server.
        #     *   **rr**: the round-robin algorithm. This algorithm is used to redirect requests to origin servers in turn. If you use this algorithm, you can specify a weight for each server based on server performance.
        #     *   **least_time**: the least response time algorithm. This algorithm is used to minimize the latency when requests are forwarded from the instance to origin servers based on the intelligent DNS resolution feature.
        # 
        # *   **Attributes**: the parameters for back-to-origin processing. This field is optional and must be a JSON array. Each element in the array contains the following fields:
        # 
        #     *   **RealServer**: the address of the origin server. This field is optional and must be a string.
        # 
        #     *   **Attribute**: the parameter for back-to-origin processing. This field is optional and must be a JSON object. Valid values:
        # 
        #         *   **Weight**: the weight of the server. This field is optional and must be an integer. This field takes effect only when **ProxyMode** is set to **rr**. Valid values: **1** to **100**. Default value: **100**. An origin server with a higher weight receives more requests.
        #         *   **ConnectTimeout**: the timeout period for new connections. This field is optional and must be an integer. Valid values: **1** to **10**. Unit: seconds. Default value: **5**.
        #         *   **FailTimeout**: the period after which a connection is considered to have failed. This field is optional and must be an integer. Valid values: **1** to **3600**. Unit: seconds. Default value: **10**.
        #         *   **MaxFails**: the maximum number of failures allowed. This field is related to health checks. This field is optional and must be an integer. Valid values: **1** to **10**. Unit: seconds. Default value: **3**.
        #         *   **Mode**: the primary/secondary attribute flag. This parameter is optional and must be a string. Valid values: **active** (primary) and **backup** (secondary).
        #         *   **ReadTimeout**: the read timeout period. This field is optional and must be an integer. Valid values: **10** to **300**. Unit: seconds. Default value: **120**.
        #         *   **SendTimeout**: the write timeout period. This field is optional and must be an integer. Valid values: **10** to **300**. Unit: seconds. Default value: **120**.
        # 
        # This parameter is required.
        self.policy = policy
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id
        # The retry switch. Valid values:
        # 
        # *   **1**: on
        # *   **0**: off
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

