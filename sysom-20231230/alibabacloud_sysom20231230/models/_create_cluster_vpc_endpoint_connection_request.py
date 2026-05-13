# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateClusterVpcEndpointConnectionRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        dry_run: bool = None,
        region: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        self.dry_run = dry_run
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.region is not None:
            result['region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('region') is not None:
            self.region = m.get('region')

        return self

