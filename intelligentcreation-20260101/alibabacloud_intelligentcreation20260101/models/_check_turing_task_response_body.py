# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_intelligentcreation20260101 import models as main_models
from darabonba.model import DaraModel

class CheckTuringTaskResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        result: main_models.CheckTuringTaskResponseBodyResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.CheckTuringTaskResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('success') is not None:
            self.success = m.get('success')

        return self



class CheckTuringTaskResponseBodyResult(DaraModel):
    def __init__(
        self,
        fail_code: str = None,
        fail_msg: str = None,
        status: str = None,
        task_id: str = None,
        video_url: str = None,
    ):
        self.fail_code = fail_code
        self.fail_msg = fail_msg
        self.status = status
        self.task_id = task_id
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_code is not None:
            result['failCode'] = self.fail_code

        if self.fail_msg is not None:
            result['failMsg'] = self.fail_msg

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.video_url is not None:
            result['videoUrl'] = self.video_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failCode') is not None:
            self.fail_code = m.get('failCode')

        if m.get('failMsg') is not None:
            self.fail_msg = m.get('failMsg')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('videoUrl') is not None:
            self.video_url = m.get('videoUrl')

        return self

