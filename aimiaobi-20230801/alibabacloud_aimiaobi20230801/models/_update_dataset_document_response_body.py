# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class UpdateDatasetDocumentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateDatasetDocumentResponseBodyData = None,
        http_status_code: int = None,
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
            temp_model = main_models.UpdateDatasetDocumentResponseBodyData()
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

class UpdateDatasetDocumentResponseBodyData(DaraModel):
    def __init__(
        self,
        category_uuid: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        extend_1: str = None,
        extend_2: str = None,
        extend_3: str = None,
        tags: List[str] = None,
        title: str = None,
    ):
        self.category_uuid = category_uuid
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.extend_1 = extend_1
        self.extend_2 = extend_2
        self.extend_3 = extend_3
        self.tags = tags
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_uuid is not None:
            result['CategoryUuid'] = self.category_uuid

        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.extend_1 is not None:
            result['Extend1'] = self.extend_1

        if self.extend_2 is not None:
            result['Extend2'] = self.extend_2

        if self.extend_3 is not None:
            result['Extend3'] = self.extend_3

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryUuid') is not None:
            self.category_uuid = m.get('CategoryUuid')

        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('Extend1') is not None:
            self.extend_1 = m.get('Extend1')

        if m.get('Extend2') is not None:
            self.extend_2 = m.get('Extend2')

        if m.get('Extend3') is not None:
            self.extend_3 = m.get('Extend3')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

