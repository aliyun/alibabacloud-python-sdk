# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class UpdateQaLibraryRequest(DaraModel):
    def __init__(
        self,
        parse_qa_results: List[main_models.UpdateQaLibraryRequestParseQaResults] = None,
        qa_library_id: str = None,
        request_id: str = None,
    ):
        # This parameter is required.
        self.parse_qa_results = parse_qa_results
        self.qa_library_id = qa_library_id
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        if self.parse_qa_results:
            for v1 in self.parse_qa_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['parseQaResults'] = []
        if self.parse_qa_results is not None:
            for k1 in self.parse_qa_results:
                result['parseQaResults'].append(k1.to_map() if k1 else None)

        if self.qa_library_id is not None:
            result['qaLibraryId'] = self.qa_library_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parse_qa_results = []
        if m.get('parseQaResults') is not None:
            for k1 in m.get('parseQaResults'):
                temp_model = main_models.UpdateQaLibraryRequestParseQaResults()
                self.parse_qa_results.append(temp_model.from_map(k1))

        if m.get('qaLibraryId') is not None:
            self.qa_library_id = m.get('qaLibraryId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class UpdateQaLibraryRequestParseQaResults(DaraModel):
    def __init__(
        self,
        answer: str = None,
        question: str = None,
    ):
        # This parameter is required.
        self.answer = answer
        # This parameter is required.
        self.question = question

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['answer'] = self.answer

        if self.question is not None:
            result['question'] = self.question

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answer') is not None:
            self.answer = m.get('answer')

        if m.get('question') is not None:
            self.question = m.get('question')

        return self

