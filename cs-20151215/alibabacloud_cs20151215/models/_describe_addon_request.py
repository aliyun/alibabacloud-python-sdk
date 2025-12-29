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
        # The ID of the cluster. If you specify a cluster ID, only components used in the cluster are queried. Other parameters are ignored.
        self.cluster_id = cluster_id
        # The specifications of the cluster. If cluster_id is specified, this parameter is ignored. You must specify the region_id, cluster_type, profile, cluster_spec, and cluster_version parameters at the same time.
        self.cluster_spec = cluster_spec
        # The type of the cluster. If cluster_id is specified, this parameter is ignored. You must specify the region_id, cluster_type, profile, cluster_spec, and cluster_version parameters at the same time.
        self.cluster_type = cluster_type
        # The version of the cluster. If cluster_id is specified, this parameter is ignored. You must specify the region_id, cluster_type, profile, cluster_spec, and cluster_version parameters at the same time.
        self.cluster_version = cluster_version
        # The subtype of the cluster. If cluster_id is specified, this parameter is ignored. You must specify the region_id, cluster_type, profile, cluster_spec, and cluster_version parameters at the same time.
        self.profile = profile
        # The region ID. If cluster_id is specified, this parameter is ignored. You must specify the region_id, cluster_type, profile, cluster_spec, and cluster_version parameters at the same time.
        self.region_id = region_id
        # The version of the component. If you do not specify this parameter, the latest version of the component is queried.
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

