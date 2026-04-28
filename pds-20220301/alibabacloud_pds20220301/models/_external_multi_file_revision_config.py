# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExternalMultiFileRevisionConfig(DaraModel):
    def __init__(
        self,
        revision_count: int = None,
        revision_merge_enabled: bool = None,
        revision_recycle_period: int = None,
    ):
        self.revision_count = revision_count
        self.revision_merge_enabled = revision_merge_enabled
        self.revision_recycle_period = revision_recycle_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.revision_count is not None:
            result['revision_count'] = self.revision_count

        if self.revision_merge_enabled is not None:
            result['revision_merge_enabled'] = self.revision_merge_enabled

        if self.revision_recycle_period is not None:
            result['revision_recycle_period'] = self.revision_recycle_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('revision_count') is not None:
            self.revision_count = m.get('revision_count')

        if m.get('revision_merge_enabled') is not None:
            self.revision_merge_enabled = m.get('revision_merge_enabled')

        if m.get('revision_recycle_period') is not None:
            self.revision_recycle_period = m.get('revision_recycle_period')

        return self

