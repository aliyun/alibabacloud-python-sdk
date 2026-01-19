# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteModelRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        model_name: str = None,
    ):
        # The ID of the API group to which the model belongs.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The name of the model.
        # 
        # This parameter is required.
        self.model_name = model_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        return self

