# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddContainerClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        description: str = None,
        identifier: str = None,
        name: str = None,
        network_type: str = None,
    ):
        # The type of the cluster. Only Container Service for Kubernetes (ACK) clusters are supported.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # The description of the cluster.
        self.description = description
        # The ID of the cluster that you want to register.
        # 
        # This parameter is required.
        self.identifier = identifier
        # The name of the cluster.
        self.name = name
        # The network type of the cluster. Valid values:
        # 
        # *   **CLASSIC**: the classic network
        # *   **VPC**: a virtual private cloud (VPC)
        # 
        # This parameter is required.
        self.network_type = network_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.description is not None:
            result['Description'] = self.description

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.name is not None:
            result['Name'] = self.name

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        return self

