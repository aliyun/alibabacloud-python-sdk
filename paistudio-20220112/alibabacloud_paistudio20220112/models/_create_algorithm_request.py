# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAlgorithmRequest(DaraModel):
    def __init__(
        self,
        algorithm_description: str = None,
        algorithm_name: str = None,
        display_name: str = None,
        workspace_id: str = None,
    ):
        self.algorithm_description = algorithm_description
        self.algorithm_name = algorithm_name
        self.display_name = display_name
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm_description is not None:
            result['AlgorithmDescription'] = self.algorithm_description

        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmDescription') is not None:
            self.algorithm_description = m.get('AlgorithmDescription')

        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

