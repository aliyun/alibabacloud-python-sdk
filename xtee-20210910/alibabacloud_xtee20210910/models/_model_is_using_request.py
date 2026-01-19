# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelIsUsingRequest(DaraModel):
    def __init__(
        self,
        model_code: str = None,
        model_id: str = None,
        model_name: str = None,
        reg_id: str = None,
        status: str = None,
    ):
        # Model code.
        # 
        # This parameter is required.
        self.model_code = model_code
        # Model ID.
        # 
        # This parameter is required.
        self.model_id = model_id
        # Model name.
        # 
        # This parameter is required.
        self.model_name = model_name
        # Region code.
        self.reg_id = reg_id
        # Model status.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_code is not None:
            result['ModelCode'] = self.model_code

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelCode') is not None:
            self.model_code = m.get('ModelCode')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

