# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_anytrans20250707 import models as main_models
from darabonba.model import DaraModel

class TermQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.TermQueryResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.TermQueryResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class TermQueryResponseBodyData(DaraModel):
    def __init__(
        self,
        fail_count: int = None,
        terms: List[main_models.TermQueryResponseBodyDataTerms] = None,
    ):
        self.fail_count = fail_count
        self.terms = terms

    def validate(self):
        if self.terms:
            for v1 in self.terms:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_count is not None:
            result['failCount'] = self.fail_count

        result['terms'] = []
        if self.terms is not None:
            for k1 in self.terms:
                result['terms'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failCount') is not None:
            self.fail_count = m.get('failCount')

        self.terms = []
        if m.get('terms') is not None:
            for k1 in m.get('terms'):
                temp_model = main_models.TermQueryResponseBodyDataTerms()
                self.terms.append(temp_model.from_map(k1))

        return self

class TermQueryResponseBodyDataTerms(DaraModel):
    def __init__(
        self,
        src: str = None,
        term_id: str = None,
        tgt: str = None,
    ):
        self.src = src
        self.term_id = term_id
        self.tgt = tgt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.src is not None:
            result['src'] = self.src

        if self.term_id is not None:
            result['termId'] = self.term_id

        if self.tgt is not None:
            result['tgt'] = self.tgt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('src') is not None:
            self.src = m.get('src')

        if m.get('termId') is not None:
            self.term_id = m.get('termId')

        if m.get('tgt') is not None:
            self.tgt = m.get('tgt')

        return self

