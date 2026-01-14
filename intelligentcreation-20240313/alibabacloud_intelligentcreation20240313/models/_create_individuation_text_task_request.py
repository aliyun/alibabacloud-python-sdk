# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateIndividuationTextTaskRequest(DaraModel):
    def __init__(
        self,
        crowd_pack: List[List[str]] = None,
        project_id: str = None,
        task_name: str = None,
    ):
        self.crowd_pack = crowd_pack
        self.project_id = project_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.crowd_pack is not None:
            result['crowdPack'] = self.crowd_pack

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.task_name is not None:
            result['taskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('crowdPack') is not None:
            self.crowd_pack = m.get('crowdPack')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        return self

