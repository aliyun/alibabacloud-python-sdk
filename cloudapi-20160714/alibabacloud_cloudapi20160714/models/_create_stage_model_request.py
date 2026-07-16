# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateStageModelRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        security_token: str = None,
        stage_alias: str = None,
        stage_name: str = None,
    ):
        self.description = description
        self.security_token = security_token
        # This parameter is required.
        self.stage_alias = stage_alias
        # This parameter is required.
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.stage_alias is not None:
            result['StageAlias'] = self.stage_alias

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StageAlias') is not None:
            self.stage_alias = m.get('StageAlias')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        return self

