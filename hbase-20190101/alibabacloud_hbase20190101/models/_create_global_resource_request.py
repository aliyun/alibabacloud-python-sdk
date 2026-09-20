# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGlobalResourceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        cluster_id: str = None,
        region_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # This parameter is automatically populated when the request is sent. You do not need to specify this parameter.
        self.client_token = client_token
        # The ID of the target instance. You can call the DescribeInstances operation to obtain the instance ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The region ID of the instance.
        self.region_id = region_id
        # The resource name. Valid values:
        # 
        # - HbaseSLBThriftVip: Thrift SLB EPS resource.
        # 
        # - SolrSlbVip: Solr SLB EPS resource.
        # 
        # - PhoenixSLBQueryServerVip: Phoenix SLB EPS resource.
        # 
        # - PubHbaseSLBThriftVip: Thrift SLB public network resource.
        # 
        # - PubPhoenixSLBQueryServerVip: Phoenix SLB public network resource.
        # 
        # This parameter is required.
        self.resource_name = resource_name
        # The resource type. Set the value to **GLOBAL_VIP**.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

