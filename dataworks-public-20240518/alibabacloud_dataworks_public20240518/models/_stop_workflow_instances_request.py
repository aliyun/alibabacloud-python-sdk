# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StopWorkflowInstancesRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        ids: List[int] = None,
    ):
        # The remarks.
        self.comment = comment
        # The workflow instance IDs.
        # 
        # This parameter is required.
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.ids is not None:
            result['Ids'] = self.ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        return self

