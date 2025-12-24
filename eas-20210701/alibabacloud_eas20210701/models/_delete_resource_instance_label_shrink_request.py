# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteResourceInstanceLabelShrinkRequest(DaraModel):
    def __init__(
        self,
        all_instances: bool = None,
        instance_ids_shrink: str = None,
        keys_shrink: str = None,
        label_keys_shrink: str = None,
    ):
        # Specifies whether the delete operation takes effect on all instances in the resource group. If you set this parameter to true, the InstanceIds parameter does not take effect.
        self.all_instances = all_instances
        # The instance IDs.
        self.instance_ids_shrink = instance_ids_shrink
        # The keys of the tags that you want to delete.
        self.keys_shrink = keys_shrink
        self.label_keys_shrink = label_keys_shrink

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

        if self.keys_shrink is not None:
            result['Keys'] = self.keys_shrink

        if self.label_keys_shrink is not None:
            result['LabelKeys'] = self.label_keys_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllInstances') is not None:
            self.all_instances = m.get('AllInstances')

        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        if m.get('Keys') is not None:
            self.keys_shrink = m.get('Keys')

        if m.get('LabelKeys') is not None:
            self.label_keys_shrink = m.get('LabelKeys')

        return self

