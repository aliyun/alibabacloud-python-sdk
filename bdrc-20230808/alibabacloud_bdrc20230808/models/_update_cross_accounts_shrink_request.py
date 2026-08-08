# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCrossAccountsShrinkRequest(DaraModel):
    def __init__(
        self,
        create_targets_shrink: str = None,
        delete_targets_shrink: str = None,
    ):
        self.create_targets_shrink = create_targets_shrink
        self.delete_targets_shrink = delete_targets_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_targets_shrink is not None:
            result['CreateTargets'] = self.create_targets_shrink

        if self.delete_targets_shrink is not None:
            result['DeleteTargets'] = self.delete_targets_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTargets') is not None:
            self.create_targets_shrink = m.get('CreateTargets')

        if m.get('DeleteTargets') is not None:
            self.delete_targets_shrink = m.get('DeleteTargets')

        return self

