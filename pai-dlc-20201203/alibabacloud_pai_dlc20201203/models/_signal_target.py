# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SignalTarget(DaraModel):
    def __init__(
        self,
        pod_names: List[str] = None,
        roles: List[str] = None,
        scope: str = None,
    ):
        self.pod_names = pod_names
        self.roles = roles
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pod_names is not None:
            result['PodNames'] = self.pod_names

        if self.roles is not None:
            result['Roles'] = self.roles

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PodNames') is not None:
            self.pod_names = m.get('PodNames')

        if m.get('Roles') is not None:
            self.roles = m.get('Roles')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

