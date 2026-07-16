# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAddonRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_spec: str = None,
        cluster_type: str = None,
        cluster_version: str = None,
        profile: str = None,
        region_id: str = None,
        version: str = None,
    ):
        # Cluster ID.
        # When a cluster ID is specified, the list of available components for the cluster is queried, and other parameters are ignored.
        self.cluster_id = cluster_id
        # Cluster specification.
        # If cluster_id is specified, this parameter is ignored.
        # The five parameters region_id, cluster_type, profile, cluster_spec, and cluster_version must be specified together.
        self.cluster_spec = cluster_spec
        # Cluster type.
        # If cluster_id is specified, this parameter is ignored.
        # The five parameters region_id, cluster_type, profile, cluster_spec, and cluster_version must be specified together.
        self.cluster_type = cluster_type
        # Cluster version.
        # If cluster_id is specified, this parameter is ignored.
        # The five parameters region_id, cluster_type, profile, cluster_spec, and cluster_version must be specified together.
        self.cluster_version = cluster_version
        # Cluster subtype.
        # If cluster_id is specified, this parameter is ignored.
        # The five parameters region_id, cluster_type, profile, cluster_spec, and cluster_version must be specified together.
        self.profile = profile
        # Region.
        # If cluster_id is specified, this parameter is ignored.
        # The five parameters region_id, cluster_type, profile, cluster_spec, and cluster_version must be specified together.
        self.region_id = region_id
        # Component version. If not specified, the latest available version of the component is queried.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec

        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type

        if self.cluster_version is not None:
            result['cluster_version'] = self.cluster_version

        if self.profile is not None:
            result['profile'] = self.profile

        if self.region_id is not None:
            result['region_id'] = self.region_id

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')

        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')

        if m.get('cluster_version') is not None:
            self.cluster_version = m.get('cluster_version')

        if m.get('profile') is not None:
            self.profile = m.get('profile')

        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

