# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchNodesByOutputRequest(DaraModel):
    def __init__(
        self,
        outputs: str = None,
        project_env: str = None,
    ):
        # The output strings of the node. You can specify multiple values. Separate multiple values with commas (,).
        # 
        # This parameter is required.
        self.outputs = outputs
        # The environment identifier in Operation Center. Valid values:
        # 
        # - PROD: production environment.
        # - DEV: development environment.
        # 
        # This parameter is required.
        self.project_env = project_env

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.outputs is not None:
            result['Outputs'] = self.outputs

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        return self

