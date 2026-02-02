# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteJobRequest(DaraModel):
    def __init__(
        self,
        force_delete: bool = None,
    ):
        # Specifies whether to force delete the subtask. If the task has subtasks and you set this parameter to true, the task and its subtasks are forcibly deleted. If this parameter is set to false, the task and its subtasks fail to be deleted.
        self.force_delete = force_delete

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force_delete is not None:
            result['forceDelete'] = self.force_delete

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('forceDelete') is not None:
            self.force_delete = m.get('forceDelete')

        return self

