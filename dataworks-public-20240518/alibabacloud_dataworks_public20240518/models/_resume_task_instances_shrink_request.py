# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResumeTaskInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        ids_shrink: str = None,
    ):
        # Remarks.
        self.comment = comment
        # The ID list of the task instance.
        self.ids_shrink = ids_shrink

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Ids') is not None:
            self.ids_shrink = m.get('Ids')

        return self

