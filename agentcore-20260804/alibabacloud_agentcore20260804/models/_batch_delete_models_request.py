# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class BatchDeleteModelsRequest(DaraModel):
    def __init__(
        self,
        body: main_models.BatchDeleteModelsRequestBody = None,
        client_token: str = None,
    ):
        self.body = body
        self.client_token = client_token

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.BatchDeleteModelsRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self



class BatchDeleteModelsRequestBody(DaraModel):
    def __init__(
        self,
        model_ids: List[str] = None,
    ):
        # This parameter is required.
        self.model_ids = model_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_ids is not None:
            result['modelIds'] = self.model_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelIds') is not None:
            self.model_ids = m.get('modelIds')

        return self

