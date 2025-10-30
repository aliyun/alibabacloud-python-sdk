# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListSupportModelsResponseBody(DaraModel):
    def __init__(
        self,
        model_names: main_models.ListSupportModelsResponseBodyModelNames = None,
        request_id: str = None,
    ):
        self.model_names = model_names
        self.request_id = request_id

    def validate(self):
        if self.model_names:
            self.model_names.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_names is not None:
            result['ModelNames'] = self.model_names.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelNames') is not None:
            temp_model = main_models.ListSupportModelsResponseBodyModelNames()
            self.model_names = temp_model.from_map(m.get('ModelNames'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSupportModelsResponseBodyModelNames(DaraModel):
    def __init__(
        self,
        model_names: List[str] = None,
    ):
        self.model_names = model_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_names is not None:
            result['modelNames'] = self.model_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelNames') is not None:
            self.model_names = m.get('modelNames')

        return self

