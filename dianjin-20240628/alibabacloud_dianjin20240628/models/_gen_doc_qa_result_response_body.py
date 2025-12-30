# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class GenDocQaResultResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: main_models.GenDocQaResultResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['cost'] = self.cost

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('data') is not None:
            temp_model = main_models.GenDocQaResultResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

class GenDocQaResultResponseBodyData(DaraModel):
    def __init__(
        self,
        current_status: str = None,
        doc_id: str = None,
        library_id: str = None,
        parse_qa_results: List[main_models.GenDocQaResultResponseBodyDataParseQaResults] = None,
    ):
        self.current_status = current_status
        self.doc_id = doc_id
        self.library_id = library_id
        self.parse_qa_results = parse_qa_results

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
        if self.current_status is not None:
            result['currentStatus'] = self.current_status

        if self.doc_id is not None:
            result['docId'] = self.doc_id

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        result['parseQaResults'] = []
        if self.parse_qa_results is not None:
            for k1 in self.parse_qa_results:
                result['parseQaResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentStatus') is not None:
            self.current_status = m.get('currentStatus')

        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        self.parse_qa_results = []
        if m.get('parseQaResults') is not None:
            for k1 in m.get('parseQaResults'):
                temp_model = main_models.GenDocQaResultResponseBodyDataParseQaResults()
                self.parse_qa_results.append(temp_model.from_map(k1))

        return self

class GenDocQaResultResponseBodyDataParseQaResults(DaraModel):
    def __init__(
        self,
        answer: str = None,
        question: str = None,
    ):
        self.answer = answer
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

