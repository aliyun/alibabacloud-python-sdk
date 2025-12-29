# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ListServiceQAResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        page: main_models.ListServiceQAResponseBodyPage = None,
        request_id: str = None,
        result: List[main_models.ListServiceQAResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.message = message
        self.page = page
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.page:
            self.page.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Page') is not None:
            temp_model = main_models.ListServiceQAResponseBodyPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListServiceQAResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class ListServiceQAResponseBodyResult(DaraModel):
    def __init__(
        self,
        active: bool = None,
        answer: str = None,
        gmt_modified: str = None,
        question: str = None,
        service_qaid: int = None,
        templates: str = None,
    ):
        self.active = active
        self.answer = answer
        self.gmt_modified = gmt_modified
        self.question = question
        self.service_qaid = service_qaid
        self.templates = templates

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.answer is not None:
            result['Answer'] = self.answer

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.question is not None:
            result['Question'] = self.question

        if self.service_qaid is not None:
            result['ServiceQAId'] = self.service_qaid

        if self.templates is not None:
            result['Templates'] = self.templates

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        if m.get('ServiceQAId') is not None:
            self.service_qaid = m.get('ServiceQAId')

        if m.get('Templates') is not None:
            self.templates = m.get('Templates')

        return self

class ListServiceQAResponseBodyPage(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

