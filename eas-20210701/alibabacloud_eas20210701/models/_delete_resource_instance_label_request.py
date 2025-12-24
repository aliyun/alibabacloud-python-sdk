# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteResourceInstanceLabelRequest(DaraModel):
    def __init__(
        self,
        all_instances: bool = None,
        instance_ids: List[str] = None,
        keys: List[str] = None,
        label_keys: List[str] = None,
    ):
        # Specifies whether the delete operation takes effect on all instances in the resource group. If you set this parameter to true, the InstanceIds parameter does not take effect.
        self.all_instances = all_instances
        # The instance IDs.
        self.instance_ids = instance_ids
        # The keys of the tags that you want to delete.
        self.keys = keys
        self.label_keys = label_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_instances is not None:
            result['AllInstances'] = self.all_instances

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.keys is not None:
            result['Keys'] = self.keys

        if self.label_keys is not None:
            result['LabelKeys'] = self.label_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllInstances') is not None:
            self.all_instances = m.get('AllInstances')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Keys') is not None:
            self.keys = m.get('Keys')

        if m.get('LabelKeys') is not None:
            self.label_keys = m.get('LabelKeys')

        return self

