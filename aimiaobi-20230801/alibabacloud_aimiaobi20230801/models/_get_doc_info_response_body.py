# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetDocInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDocInfoResponseBodyData = None,
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
            temp_model = main_models.GetDocInfoResponseBodyData()
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

class GetDocInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        doc_name: str = None,
        doc_type: str = None,
        file_url: str = None,
        status: int = None,
        status_message: str = None,
        video_contents: List[str] = None,
    ):
        self.category_id = category_id
        self.doc_name = doc_name
        self.doc_type = doc_type
        self.file_url = file_url
        self.status = status
        self.status_message = status_message
        self.video_contents = video_contents

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.doc_name is not None:
            result['DocName'] = self.doc_name

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.status is not None:
            result['Status'] = self.status

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        if self.video_contents is not None:
            result['VideoContents'] = self.video_contents

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        if m.get('VideoContents') is not None:
            self.video_contents = m.get('VideoContents')

        return self

