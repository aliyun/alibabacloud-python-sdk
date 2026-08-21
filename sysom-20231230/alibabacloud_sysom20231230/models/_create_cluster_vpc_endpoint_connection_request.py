# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateClusterVpcEndpointConnectionRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        cluster_id: str = None,
        dry_run: bool = None,
        region: str = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # The ID of the ACK cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Specifies whether to perform a dry run.
        self.dry_run = dry_run
        # The region to which the cluster belongs.
        # 
        # This parameter is required.
        self.region = region
        self.x_sysom_invoke_source = x_sysom_invoke_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_debug_id is not None:
            result['X-Debug-Id'] = self.x_debug_id

        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.region is not None:
            result['region'] = self.region

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

