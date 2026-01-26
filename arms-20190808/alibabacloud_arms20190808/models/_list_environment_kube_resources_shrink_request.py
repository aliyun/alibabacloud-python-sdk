# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEnvironmentKubeResourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        environment_id: str = None,
        kind: str = None,
        label_selectors_shrink: str = None,
        namespace: str = None,
        region_id: str = None,
    ):
        # The environment ID.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # The resource type. Valid values: Pod, Deployment, and Service.
        # 
        # This parameter is required.
        self.kind = kind
        # The tags.
        self.label_selectors_shrink = label_selectors_shrink
        # The namespace.
        self.namespace = namespace
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.label_selectors_shrink is not None:
            result['LabelSelectors'] = self.label_selectors_shrink

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('LabelSelectors') is not None:
            self.label_selectors_shrink = m.get('LabelSelectors')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

