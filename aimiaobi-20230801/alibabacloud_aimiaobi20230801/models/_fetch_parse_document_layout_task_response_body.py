# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class FetchParseDocumentLayoutTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.FetchParseDocumentLayoutTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.FetchParseDocumentLayoutTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class FetchParseDocumentLayoutTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        layout_result: main_models.FetchParseDocumentLayoutTaskResponseBodyDataLayoutResult = None,
        task_stats: str = None,
    ):
        self.layout_result = layout_result
        self.task_stats = task_stats

    def validate(self):
        if self.layout_result:
            self.layout_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.layout_result is not None:
            result['LayoutResult'] = self.layout_result.to_map()

        if self.task_stats is not None:
            result['TaskStats'] = self.task_stats

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayoutResult') is not None:
            temp_model = main_models.FetchParseDocumentLayoutTaskResponseBodyDataLayoutResult()
            self.layout_result = temp_model.from_map(m.get('LayoutResult'))

        if m.get('TaskStats') is not None:
            self.task_stats = m.get('TaskStats')

        return self

class FetchParseDocumentLayoutTaskResponseBodyDataLayoutResult(DaraModel):
    def __init__(
        self,
        elements: List[main_models.FetchParseDocumentLayoutTaskResponseBodyDataLayoutResultElements] = None,
    ):
        self.elements = elements

    def validate(self):
        if self.elements:
            for v1 in self.elements:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Elements'] = []
        if self.elements is not None:
            for k1 in self.elements:
                result['Elements'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k1 in m.get('Elements'):
                temp_model = main_models.FetchParseDocumentLayoutTaskResponseBodyDataLayoutResultElements()
                self.elements.append(temp_model.from_map(k1))

        return self

class FetchParseDocumentLayoutTaskResponseBodyDataLayoutResultElements(DaraModel):
    def __init__(
        self,
        content: str = None,
        format_content: str = None,
        index: float = None,
        type: str = None,
    ):
        self.content = content
        self.format_content = format_content
        self.index = index
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.format_content is not None:
            result['FormatContent'] = self.format_content

        if self.index is not None:
            result['Index'] = self.index

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FormatContent') is not None:
            self.format_content = m.get('FormatContent')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

