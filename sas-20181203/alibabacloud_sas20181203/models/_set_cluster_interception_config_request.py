# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetClusterInterceptionConfigRequest(DaraModel):
    def __init__(
        self,
        cluster_ids: str = None,
        switch_on: int = None,
        switch_type: int = None,
    ):
        # The ID of the cluster. Separate multiple cluster IDs with commas (,).
        # 
        # > You can call the [ListClusterInterceptionConfig](~~ListClusterInterceptionConfig~~) operation to query the IDs of clusters.
        # 
        # This parameter is required.
        self.cluster_ids = cluster_ids
        # Specifies whether to turn on the switch. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        # 
        # This parameter is required.
        self.switch_on = switch_on
        # The type of the switch that you want to configure. Valid values:
        # 
        # *   **0**: the interception switch
        # *   **1**: the interception type switch
        # *   **2**: the interception history switch
        # 
        # This parameter is required.
        self.switch_type = switch_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids

        if self.switch_on is not None:
            result['SwitchOn'] = self.switch_on

        if self.switch_type is not None:
            result['SwitchType'] = self.switch_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')

        if m.get('SwitchOn') is not None:
            self.switch_on = m.get('SwitchOn')

        if m.get('SwitchType') is not None:
            self.switch_type = m.get('SwitchType')

        return self

