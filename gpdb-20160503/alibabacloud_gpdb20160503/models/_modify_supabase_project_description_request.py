# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySupabaseProjectDescriptionRequest(DaraModel):
    def __init__(
        self,
        project_description: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        self.project_description = project_description
        self.project_id = project_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_description is not None:
            result['ProjectDescription'] = self.project_description

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectDescription') is not None:
            self.project_description = m.get('ProjectDescription')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

