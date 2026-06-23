# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAddonsRequest(DaraModel):
    def __init__(
        self,
        cluster_profile: str = None,
        cluster_spec: str = None,
        cluster_type: str = None,
        cluster_version: str = None,
        region: str = None,
    ):
        # The cluster type. Valid values:
        # - `Default`: managed cluster.
        # - `Serverless`: serverless cluster.
        # - `Edge`: edge cluster.
        self.cluster_profile = cluster_profile
        # After you set `cluster_type` to `ManagedKubernetes` and configure `profile`, you can further specify the cluster specification.
        # 
        # - `ack.pro.small`: Pro cluster.
        # 
        # - `ack.standard`: Basic cluster (selected by default if this parameter is left empty).
        self.cluster_spec = cluster_spec
        # - `Kubernetes`: ACK dedicated cluster.
        # 
        # - `ManagedKubernetes`: ACK managed cluster types, including ACK managed clusters (ACK Pro and ACK Basic), ACK Serverless clusters (Pro and Basic), ACK Edge clusters (Pro and Basic), and ACK Lingjun clusters (Pro).
        # 
        # - `ExternalKubernetes`: registered cluster.
        self.cluster_type = cluster_type
        # The cluster version.
        self.cluster_version = cluster_version
        # The ID of the region where the cluster resides.
        # 
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_profile is not None:
            result['cluster_profile'] = self.cluster_profile

        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec

        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type

        if self.cluster_version is not None:
            result['cluster_version'] = self.cluster_version

        if self.region is not None:
            result['region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_profile') is not None:
            self.cluster_profile = m.get('cluster_profile')

        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')

        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')

        if m.get('cluster_version') is not None:
            self.cluster_version = m.get('cluster_version')

        if m.get('region') is not None:
            self.region = m.get('region')

        return self

