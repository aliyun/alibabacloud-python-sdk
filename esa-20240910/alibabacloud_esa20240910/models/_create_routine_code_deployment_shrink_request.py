# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRoutineCodeDeploymentShrinkRequest(DaraModel):
    def __init__(
        self,
        code_versions_shrink: str = None,
        env: str = None,
        name: str = None,
        strategy: str = None,
    ):
        # The configuration list of phased release version numbers. A maximum of two versions are supported, and the sum of the total proportions is equal to 100.
        # 
        # This parameter is required.
        self.code_versions_shrink = code_versions_shrink
        # The name of the environment. Only supports test environment `staging` or production environment `production`.
        # 
        # This parameter is required.
        self.env = env
        # The function name.
        # 
        # This parameter is required.
        self.name = name
        # The deployment policy. Valid value: percentage.
        # 
        # This parameter is required.
        self.strategy = strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_versions_shrink is not None:
            result['CodeVersions'] = self.code_versions_shrink

        if self.env is not None:
            result['Env'] = self.env

        if self.name is not None:
            result['Name'] = self.name

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVersions') is not None:
            self.code_versions_shrink = m.get('CodeVersions')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

