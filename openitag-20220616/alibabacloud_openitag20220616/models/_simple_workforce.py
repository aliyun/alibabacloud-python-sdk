# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SimpleWorkforce(DaraModel):
    def __init__(
        self,
        user_ids: List[int] = None,
        work_node_id: int = None,
    ):
        # List of personnel information.
        self.user_ids = user_ids
        # Node ID. For more information, see [GetTaskWorkforce](https://help.aliyun.com/document_detail/454697.html).
        self.work_node_id = work_node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        if self.work_node_id is not None:
            result['WorkNodeId'] = self.work_node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        if m.get('WorkNodeId') is not None:
            self.work_node_id = m.get('WorkNodeId')

        return self

