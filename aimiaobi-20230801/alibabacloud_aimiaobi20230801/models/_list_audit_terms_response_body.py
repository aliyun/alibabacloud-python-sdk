# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListAuditTermsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListAuditTermsResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAuditTermsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAuditTermsResponseBodyData(DaraModel):
    def __init__(
        self,
        exception_word: List[str] = None,
        id: str = None,
        keyword: str = None,
        suggest_word: str = None,
        terms_desc: str = None,
        terms_name: str = None,
    ):
        self.exception_word = exception_word
        self.id = id
        self.keyword = keyword
        self.suggest_word = suggest_word
        self.terms_desc = terms_desc
        self.terms_name = terms_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exception_word is not None:
            result['ExceptionWord'] = self.exception_word

        if self.id is not None:
            result['Id'] = self.id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.suggest_word is not None:
            result['SuggestWord'] = self.suggest_word

        if self.terms_desc is not None:
            result['TermsDesc'] = self.terms_desc

        if self.terms_name is not None:
            result['TermsName'] = self.terms_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionWord') is not None:
            self.exception_word = m.get('ExceptionWord')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('SuggestWord') is not None:
            self.suggest_word = m.get('SuggestWord')

        if m.get('TermsDesc') is not None:
            self.terms_desc = m.get('TermsDesc')

        if m.get('TermsName') is not None:
            self.terms_name = m.get('TermsName')

        return self

