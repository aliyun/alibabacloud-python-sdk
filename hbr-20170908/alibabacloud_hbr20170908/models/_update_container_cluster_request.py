# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateContainerClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        description: str = None,
        name: str = None,
        network_type: str = None,
        renew_token: bool = None,
    ):
        # Cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Cluster description.
        self.description = description
        # Cluster name.
        self.name = name
        # Network type, with possible values including:
        # * **CLASSIC**: Classic Network.
        # * **VPC**: Virtual Private Cloud.
        self.network_type = network_type
        # Whether to regenerate the token.
        self.renew_token = renew_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.renew_token is not None:
            result['RenewToken'] = self.renew_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('RenewToken') is not None:
            self.renew_token = m.get('RenewToken')

        return self

