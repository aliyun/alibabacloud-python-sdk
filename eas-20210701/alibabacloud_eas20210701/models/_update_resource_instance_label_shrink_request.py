# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class UpdateResourceInstanceLabelShrinkRequest(DaraModel):
    def __init__(
        self,
        all_instances: bool = None,
        instance_ids_shrink: str = None,
        labels: Dict[str, str] = None,
    ):
        # Specifies whether the modification takes effect on all instances in the resource group. If you set this parameter to true, the InstanceIds parameter does not take effect.
        self.all_instances = all_instances
        # The instance IDs.
        self.instance_ids_shrink = instance_ids_shrink
        # The custom tag.
        self.labels = labels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_instances is not None:
            result['AllInstances'] = self.all_instances

        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink

        if self.labels is not None:
            result['Labels'] = self.labels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllInstances') is not None:
            self.all_instances = m.get('AllInstances')

        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        return self

