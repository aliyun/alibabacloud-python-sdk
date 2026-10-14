# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWatermarkExtractTaskResultRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        task_id: str = None,
    ):
        # A reserved idempotence field. This field is not supported. Passing in a value does not cause an error, but it does not produce an idempotence effect.
        self.client_token = client_token
        # The dark watermark task ID returned by the CreateWatermarkExtractTask operation.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

