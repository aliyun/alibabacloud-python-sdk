# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddProjectManagerShrinkRequest(DaraModel):
    def __init__(
        self,
        org_entities_shrink: str = None,
        out_project_id: str = None,
        project_id: int = None,
    ):
        self.org_entities_shrink = org_entities_shrink
        self.out_project_id = out_project_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.org_entities_shrink is not None:
            result['org_entities'] = self.org_entities_shrink

        if self.out_project_id is not None:
            result['out_project_id'] = self.out_project_id

        if self.project_id is not None:
            result['project_id'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('org_entities') is not None:
            self.org_entities_shrink = m.get('org_entities')

        if m.get('out_project_id') is not None:
            self.out_project_id = m.get('out_project_id')

        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')

        return self

