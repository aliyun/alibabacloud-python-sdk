# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDefaultCollectorConfigurationsRequest(DaraModel):
    def __init__(
        self,
        res_type: str = None,
        res_version: str = None,
        source_type: str = None,
    ):
        # The type of the collector. Valid values:
        # 
        # - fileBeat
        # - metricBeat
        # - heartBeat
        # - auditBeat.
        # 
        # This parameter is required.
        self.res_type = res_type
        # The version of the collector. The available versions vary based on the type of machine on which the collector is deployed. Valid values:
        # 
        # - ECS: 6.8.5_with_community
        # - ACK: 6.8.13_with_community.
        # 
        # This parameter is required.
        self.res_version = res_version
        # The type of machine on which the collector is deployed. If you do not specify this parameter, all types are returned. Valid values:
        # 
        # - ECS: Elastic Compute Service (ECS) instance
        # - ACK: Container Service for Kubernetes (ACK) cluster.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.res_type is not None:
            result['resType'] = self.res_type

        if self.res_version is not None:
            result['resVersion'] = self.res_version

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resType') is not None:
            self.res_type = m.get('resType')

        if m.get('resVersion') is not None:
            self.res_version = m.get('resVersion')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        return self

