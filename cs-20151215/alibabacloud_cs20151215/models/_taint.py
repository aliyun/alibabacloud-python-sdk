# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Taint(DaraModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        value: str = None,
    ):
        # The scheduling policy. Valid values:
        # 
        # - `NoSchedule`: Not tolerated. This affects only the scheduling process. Already scheduled pods are not affected. This applies only to newly added pods.
        # 
        # - `NoExecute`: Not tolerated. When the taint changes, the pod is evicted.
        # 
        # - `PreferNoSchedule`: Soft constraint. Existing pods on the node are not affected. The scheduler tries to avoid scheduling pods that do not tolerate the taint to the node.
        # 
        # Default value: `NoSchedule`.
        self.effect = effect
        # The key of the taint.
        self.key = key
        # The value of the taint.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effect is not None:
            result['effect'] = self.effect

        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

