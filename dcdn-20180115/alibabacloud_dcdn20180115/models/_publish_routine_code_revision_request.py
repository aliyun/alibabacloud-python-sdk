# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class PublishRoutineCodeRevisionRequest(DaraModel):
    def __init__(
        self,
        envs: Dict[str, Any] = None,
        name: str = None,
        select_code_revision: str = None,
    ):
        # The environment to which you want to publish the code.
        # 
        # > 
        # 
        # *   production: the name of the environment, including the environment name (SpecName) and the domain name whitelist (AllowedHosts).
        # 
        # *   presetCanary: You can add canary release environments based on your business requirements. This parameter is optional.
        # 
        # This parameter is required.
        self.envs = envs
        # The name of the routine. The name must be unique among the routines that belong to the same Alibaba Cloud account.
        # 
        # This parameter is required.
        self.name = name
        # The version of the routine code that you want to publish.
        # 
        # This parameter is required.
        self.select_code_revision = select_code_revision

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.envs is not None:
            result['Envs'] = self.envs

        if self.name is not None:
            result['Name'] = self.name

        if self.select_code_revision is not None:
            result['SelectCodeRevision'] = self.select_code_revision

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SelectCodeRevision') is not None:
            self.select_code_revision = m.get('SelectCodeRevision')

        return self

