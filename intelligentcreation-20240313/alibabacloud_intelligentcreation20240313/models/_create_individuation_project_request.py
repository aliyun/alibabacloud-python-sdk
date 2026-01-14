# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIndividuationProjectRequest(DaraModel):
    def __init__(
        self,
        project_info: str = None,
        project_name: str = None,
        purpose: str = None,
        scene_id: str = None,
    ):
        self.project_info = project_info
        self.project_name = project_name
        self.purpose = purpose
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_info is not None:
            result['projectInfo'] = self.project_info

        if self.project_name is not None:
            result['projectName'] = self.project_name

        if self.purpose is not None:
            result['purpose'] = self.purpose

        if self.scene_id is not None:
            result['sceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectInfo') is not None:
            self.project_info = m.get('projectInfo')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        if m.get('purpose') is not None:
            self.purpose = m.get('purpose')

        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')

        return self

