# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClustersV1Request(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        ens_region_id: str = None,
        name: str = None,
        profile: str = None,
    ):
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The cluster type. Valid values: Kubernetes and ManagedKubernetes. A value of Kubernetes indicates an ECK cluster. A value of ManagedKubernetes indicates a serverless virtual cluster. This parameter must be used together with the profile parameter.
        self.cluster_type = cluster_type
        # The ENS region ID of the cluster.
        self.ens_region_id = ens_region_id
        # The name of the cluster.
        self.name = name
        # The cluster profile. Valid values: Default and Serverless. A value of Default indicates an ECK cluster. A value of Serverless indicates a serverless virtual cluster. This parameter must be used together with the cluster_type parameter.
        self.profile = profile

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.name is not None:
            result['Name'] = self.name

        if self.profile is not None:
            result['Profile'] = self.profile

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        return self

