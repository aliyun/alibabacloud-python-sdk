# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyApplicationPromptResponseBody(DaraModel):
    def __init__(
        self,
        prompt_id: str = None,
        request_id: str = None,
    ):
        self.prompt_id = prompt_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prompt_id is not None:
            result['PromptId'] = self.prompt_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromptId') is not None:
            self.prompt_id = m.get('PromptId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

