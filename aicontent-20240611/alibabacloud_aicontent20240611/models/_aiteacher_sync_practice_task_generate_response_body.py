# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class AITeacherSyncPracticeTaskGenerateResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.AITeacherSyncPracticeTaskGenerateResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.AITeacherSyncPracticeTaskGenerateResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class AITeacherSyncPracticeTaskGenerateResponseBodyData(DaraModel):
    def __init__(
        self,
        task_content: List[main_models.AITeacherSyncPracticeTaskGenerateResponseBodyDataTaskContent] = None,
        task_type: str = None,
    ):
        self.task_content = task_content
        self.task_type = task_type

    def validate(self):
        if self.task_content:
            for v1 in self.task_content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['taskContent'] = []
        if self.task_content is not None:
            for k1 in self.task_content:
                result['taskContent'].append(k1.to_map() if k1 else None)

        if self.task_type is not None:
            result['taskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_content = []
        if m.get('taskContent') is not None:
            for k1 in m.get('taskContent'):
                temp_model = main_models.AITeacherSyncPracticeTaskGenerateResponseBodyDataTaskContent()
                self.task_content.append(temp_model.from_map(k1))

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        return self

class AITeacherSyncPracticeTaskGenerateResponseBodyDataTaskContent(DaraModel):
    def __init__(
        self,
        assistant: str = None,
        user: str = None,
    ):
        self.assistant = assistant
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assistant is not None:
            result['assistant'] = self.assistant

        if self.user is not None:
            result['user'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')

        if m.get('user') is not None:
            self.user = m.get('user')

        return self

