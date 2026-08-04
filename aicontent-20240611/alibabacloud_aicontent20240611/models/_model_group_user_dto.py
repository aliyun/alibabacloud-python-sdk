# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ModelGroupUserDTO(DaraModel):
    def __init__(
        self,
        api_keys: List[main_models.ModelGroupClientKeyItemDTO] = None,
        user_id: int = None,
        user_name: str = None,
    ):
        self.api_keys = api_keys
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.api_keys:
            for v1 in self.api_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['apiKeys'] = []
        if self.api_keys is not None:
            for k1 in self.api_keys:
                result['apiKeys'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_keys = []
        if m.get('apiKeys') is not None:
            for k1 in m.get('apiKeys'):
                temp_model = main_models.ModelGroupClientKeyItemDTO()
                self.api_keys.append(temp_model.from_map(k1))

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

