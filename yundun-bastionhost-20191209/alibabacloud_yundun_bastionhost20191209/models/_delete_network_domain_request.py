# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteNetworkDomainRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        network_domain_id: str = None,
        region_id: str = None,
    ):
        # The ID of the bastion host whose network domain you want to delete.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the network domain to be deleted.
        # 
        # This parameter is required.
        self.network_domain_id = network_domain_id
        # The region ID of the bastion host whose network domain you want to delete.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

