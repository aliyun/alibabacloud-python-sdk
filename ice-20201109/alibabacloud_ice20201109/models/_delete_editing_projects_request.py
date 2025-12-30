# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEditingProjectsRequest(DaraModel):
    def __init__(
        self,
        project_ids: str = None,
    ):
        # The ID of the online editing project. You can specify multiple IDs separated with commas (,).
        self.project_ids = project_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')

        return self

