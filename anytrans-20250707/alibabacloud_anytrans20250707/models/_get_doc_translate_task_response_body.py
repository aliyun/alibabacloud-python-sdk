# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_anytrans20250707 import models as main_models
from darabonba.model import DaraModel

class GetDocTranslateTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDocTranslateTaskResponseBodyData = None,
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
            temp_model = main_models.GetDocTranslateTaskResponseBodyData()
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

class GetDocTranslateTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        characters_count: int = None,
        page_count: int = None,
        status: str = None,
        task_id: str = None,
        translate_file_url: str = None,
    ):
        self.characters_count = characters_count
        self.page_count = page_count
        self.status = status
        self.task_id = task_id
        self.translate_file_url = translate_file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.characters_count is not None:
            result['charactersCount'] = self.characters_count

        if self.page_count is not None:
            result['pageCount'] = self.page_count

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.translate_file_url is not None:
            result['translateFileUrl'] = self.translate_file_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('charactersCount') is not None:
            self.characters_count = m.get('charactersCount')

        if m.get('pageCount') is not None:
            self.page_count = m.get('pageCount')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('translateFileUrl') is not None:
            self.translate_file_url = m.get('translateFileUrl')

        return self

