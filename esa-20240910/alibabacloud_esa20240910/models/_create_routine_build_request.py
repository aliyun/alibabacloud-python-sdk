# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRoutineBuildRequest(DaraModel):
    def __init__(
        self,
        artifact_url: str = None,
        branch: str = None,
        routine_name: str = None,
    ):
        # The OSS object URL. This parameter is required in upload mode but is not required in git mode.
        self.artifact_url = artifact_url
        # The name of the branch to build. This parameter is not required in upload mode but is required in git mode.
        self.branch = branch
        # The ER name.
        # 
        # This parameter is required.
        self.routine_name = routine_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_url is not None:
            result['ArtifactUrl'] = self.artifact_url

        if self.branch is not None:
            result['Branch'] = self.branch

        if self.routine_name is not None:
            result['RoutineName'] = self.routine_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactUrl') is not None:
            self.artifact_url = m.get('ArtifactUrl')

        if m.get('Branch') is not None:
            self.branch = m.get('Branch')

        if m.get('RoutineName') is not None:
            self.routine_name = m.get('RoutineName')

        return self

