# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ModelGroupClientDTO(DaraModel):
    def __init__(
        self,
        api_keys: List[main_models.ModelGroupClientKeyItemDTO] = None,
        client_id: int = None,
        client_name: str = None,
    ):
        self.api_keys = api_keys
        self.client_id = client_id
        self.client_name = client_name

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

        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.client_name is not None:
            result['clientName'] = self.client_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_keys = []
        if m.get('apiKeys') is not None:
            for k1 in m.get('apiKeys'):
                temp_model = main_models.ModelGroupClientKeyItemDTO()
                self.api_keys.append(temp_model.from_map(k1))

        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('clientName') is not None:
            self.client_name = m.get('clientName')

        return self

