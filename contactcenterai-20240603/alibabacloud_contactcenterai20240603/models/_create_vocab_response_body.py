# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_contactcenterai20240603 import models as main_models
from darabonba.model import DaraModel

class CreateVocabResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateVocabResponseBodyData = None,
        request_id: str = None,
        success: str = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.CreateVocabResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateVocabResponseBodyData(DaraModel):
    def __init__(
        self,
        vocabulary_id: str = None,
    ):
        self.vocabulary_id = vocabulary_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vocabulary_id is not None:
            result['vocabularyId'] = self.vocabulary_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vocabularyId') is not None:
            self.vocabulary_id = m.get('vocabularyId')

        return self

