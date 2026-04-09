# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RollbackParameterRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        rollback_version: int = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.rollback_version = rollback_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.rollback_version is not None:
            result['RollbackVersion'] = self.rollback_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RollbackVersion') is not None:
            self.rollback_version = m.get('RollbackVersion')

        return self

