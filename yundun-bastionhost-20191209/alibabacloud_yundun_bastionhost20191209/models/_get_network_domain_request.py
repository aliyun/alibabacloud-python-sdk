# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNetworkDomainRequest(DaraModel):
    def __init__(
        self,
        check_proxy_state: str = None,
        instance_id: str = None,
        network_domain_id: str = None,
        project_id: int = None,
        region_id: str = None,
    ):
        # Specifies whether to immediately re-check the proxy server status. Valid values:
        # 
        # - **true**: Immediately re-checks the proxy server status and returns the latest ProxyState/ProxyStateErrorCode.
        # 
        # - **false**: Default value. Does not re-check the proxy server status and directly returns the currently recorded status.
        self.check_proxy_state = check_proxy_state
        # The instance ID of the bastion host.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the network domain to query.
        # > You can call the [ListNetworkDomains](https://help.aliyun.com/document_detail/2758827.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.network_domain_id = network_domain_id
        # The project ID.
        self.project_id = project_id
        # The region ID of the bastion host.
        # 
        # > For the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_proxy_state is not None:
            result['CheckProxyState'] = self.check_proxy_state

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckProxyState') is not None:
            self.check_proxy_state = m.get('CheckProxyState')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

