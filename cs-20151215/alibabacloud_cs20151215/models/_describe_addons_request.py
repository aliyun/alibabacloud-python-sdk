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
        # 
        # *   `Default`: ACK managed cluster
        # *   `Serverless`: ACK Serverless cluster
        # *   `Edge`: ACK Edge cluster
        self.cluster_profile = cluster_profile
        # If you set `cluster_type` to `ManagedKubernetes` and specify `profile`, you can further specify the edition of the cluster. Valid values:
        # 
        # *   `ack.pro.small`: creates an ACK Pro cluster.
        # *   `ack.standard`: creates an ACK Basic cluster. If you leave the parameter empty, an ACK Basic cluster is created.
        self.cluster_spec = cluster_spec
        # *   `Kubernetes`: ACK dedicated cluster.
        # *   `ManagedKubernetes`: ACK managed cluster. ACK managed clusters include ACK Basic clusters, ACK Pro clusters, ACK Serverless Basic clusters, ACK Serverless Pro clusters, ACK Edge Basic clusters, ACK Edge Pro clusters, and ACK Lingjun Pro clusters.
        # *   `ExternalKubernetes`: registered cluster.
        self.cluster_type = cluster_type
        # The cluster version.
        self.cluster_version = cluster_version
        # The region ID of the cluster.
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

