# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchModelErrorDTO(DaraModel):
    def __init__(
        self,
        error_msg: str = None,
        model_id: str = None,
        name: str = None,
    ):
        self.error_msg = error_msg
        self.model_id = model_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

