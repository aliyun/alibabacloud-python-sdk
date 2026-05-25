# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyStageModelRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        security_token: str = None,
        stage_alias: str = None,
        stage_model_id: str = None,
    ):
        self.description = description
        self.security_token = security_token
        self.stage_alias = stage_alias
        # This parameter is required.
        self.stage_model_id = stage_model_id

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

        if self.stage_model_id is not None:
            result['StageModelId'] = self.stage_model_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StageAlias') is not None:
            self.stage_alias = m.get('StageAlias')

        if m.get('StageModelId') is not None:
            self.stage_model_id = m.get('StageModelId')

        return self

