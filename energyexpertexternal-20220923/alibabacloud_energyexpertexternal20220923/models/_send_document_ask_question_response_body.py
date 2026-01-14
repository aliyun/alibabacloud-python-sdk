# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class SendDocumentAskQuestionResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SendDocumentAskQuestionResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned data
        self.data = data
        # Request ID
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.SendDocumentAskQuestionResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class SendDocumentAskQuestionResponseBodyData(DaraModel):
    def __init__(
        self,
        answer: str = None,
        document: List[str] = None,
    ):
        # Q&A result
        self.answer = answer
        # Documents associated with the answer returned by the query
        self.document = document

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['answer'] = self.answer

        if self.document is not None:
            result['document'] = self.document

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answer') is not None:
            self.answer = m.get('answer')

        if m.get('document') is not None:
            self.document = m.get('document')

        return self

