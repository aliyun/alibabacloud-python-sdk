# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyClusterAddonShrinkRequest(DaraModel):
    def __init__(
        self,
        addon_shrink: str = None,
        cluster_id: str = None,
        component_name: str = None,
    ):
        self.addon_shrink = addon_shrink
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.component_name = component_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_shrink is not None:
            result['Addon'] = self.addon_shrink

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addon') is not None:
            self.addon_shrink = m.get('Addon')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        return self

