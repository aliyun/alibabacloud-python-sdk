# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModelRouterCreateModelGroupRequest(DaraModel):
    def __init__(
        self,
        model_list: List[int] = None,
        name: str = None,
    ):
        # The array of model IDs. At least one element is required. Each element must be the numeric model ID, not the model identifier.
        # 
        # This parameter is required.
        self.model_list = model_list
        # The group name. The name must be 1 to 50 characters in length and must be unique within the tenant (case-insensitive).
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_list is not None:
            result['modelList'] = self.model_list

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelList') is not None:
            self.model_list = m.get('modelList')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

