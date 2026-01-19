# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeModelDetailsByIdRequest(DaraModel):
    def __init__(
        self,
        model_id: str = None,
        reg_id: str = None,
    ):
        # Model ID.
        # 
        # This parameter is required.
        self.model_id = model_id
        # Region code.
        self.reg_id = reg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        return self

