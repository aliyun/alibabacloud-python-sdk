# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelFileUploadRequest(DaraModel):
    def __init__(
        self,
        object_name: str = None,
        reg_id: str = None,
    ):
        # File name.
        # 
        # This parameter is required.
        self.object_name = object_name
        # Region code.
        self.reg_id = reg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        return self

