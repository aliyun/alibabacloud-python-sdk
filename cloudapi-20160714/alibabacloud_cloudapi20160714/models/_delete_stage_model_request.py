# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteStageModelRequest(DaraModel):
    def __init__(
        self,
        security_token: str = None,
        stage_model_id: str = None,
    ):
        self.security_token = security_token
        # This parameter is required.
        self.stage_model_id = stage_model_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.stage_model_id is not None:
            result['StageModelId'] = self.stage_model_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StageModelId') is not None:
            self.stage_model_id = m.get('StageModelId')

        return self

