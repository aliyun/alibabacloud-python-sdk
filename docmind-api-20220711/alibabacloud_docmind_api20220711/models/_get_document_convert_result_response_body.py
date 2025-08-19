# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_docmind_api20220711 import models as main_models
from darabonba.model import DaraModel

class GetDocumentConvertResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        completed: bool = None,
        data: List[main_models.GetDocumentConvertResultResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.code = code
        # This parameter is required.
        self.completed = completed
        self.data = data
        self.message = message
        self.request_id = request_id
        # This parameter is required.
        self.status = status

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

        if self.completed is not None:
            result['Completed'] = self.completed

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Completed') is not None:
            self.completed = m.get('Completed')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetDocumentConvertResultResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self



class GetDocumentConvertResultResponseBodyData(DaraModel):
    def __init__(
        self,
        md_5: str = None,
        size: int = None,
        type: str = None,
        url: str = None,
    ):
        self.md_5 = md_5
        self.size = size
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.size is not None:
            result['Size'] = self.size

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

