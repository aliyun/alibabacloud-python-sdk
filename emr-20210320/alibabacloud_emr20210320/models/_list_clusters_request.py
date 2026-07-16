# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListClustersRequest(DaraModel):
    def __init__(
        self,
        cluster_ids: List[str] = None,
        cluster_name: str = None,
        cluster_states: List[str] = None,
        cluster_types: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        payment_types: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: List[main_models.Tag] = None,
    ):
        # A list of cluster IDs. The number of array elements N can range from 1 to 100.
        self.cluster_ids = cluster_ids
        # The name of the cluster.
        self.cluster_name = cluster_name
        # An array of cluster states. The number of array elements N can range from 1 to 100.
        self.cluster_states = cluster_states
        # A list of cluster types. The number of array elements N can range from 1 to 100.
        self.cluster_types = cluster_types
        # The maximum number of entries to return on each page. Valid values: 1 to 100.
        self.max_results = max_results
        # The token that specifies the position from which to start the query. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The billing methods. The number of array elements N can be 1 or 2.
        self.payment_types = payment_types
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # A list of tags. The number of array elements N can range from 1 to 20.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_states is not None:
            result['ClusterStates'] = self.cluster_states

        if self.cluster_types is not None:
            result['ClusterTypes'] = self.cluster_types

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.payment_types is not None:
            result['PaymentTypes'] = self.payment_types

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterStates') is not None:
            self.cluster_states = m.get('ClusterStates')

        if m.get('ClusterTypes') is not None:
            self.cluster_types = m.get('ClusterTypes')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PaymentTypes') is not None:
            self.payment_types = m.get('PaymentTypes')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        return self

