# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RerunTaskInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        ids_shrink: str = None,
        use_latest_config: bool = None,
    ):
        # The remarks.
        self.comment = comment
        # The list of node instance IDs.
        self.ids_shrink = ids_shrink
        self.use_latest_config = use_latest_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.ids_shrink is not None:
            result['Ids'] = self.ids_shrink

        if self.use_latest_config is not None:
            result['UseLatestConfig'] = self.use_latest_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Ids') is not None:
            self.ids_shrink = m.get('Ids')

        if m.get('UseLatestConfig') is not None:
            self.use_latest_config = m.get('UseLatestConfig')

        return self

