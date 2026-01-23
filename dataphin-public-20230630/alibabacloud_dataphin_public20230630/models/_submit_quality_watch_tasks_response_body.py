# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class SubmitQualityWatchTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        submit_result: main_models.SubmitQualityWatchTasksResponseBodySubmitResult = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.submit_result = submit_result
        self.success = success

    def validate(self):
        if self.submit_result:
            self.submit_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.submit_result is not None:
            result['SubmitResult'] = self.submit_result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubmitResult') is not None:
            temp_model = main_models.SubmitQualityWatchTasksResponseBodySubmitResult()
            self.submit_result = temp_model.from_map(m.get('SubmitResult'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SubmitQualityWatchTasksResponseBodySubmitResult(DaraModel):
    def __init__(
        self,
        watch_task_id_list: List[int] = None,
    ):
        self.watch_task_id_list = watch_task_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.watch_task_id_list is not None:
            result['WatchTaskIdList'] = self.watch_task_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WatchTaskIdList') is not None:
            self.watch_task_id_list = m.get('WatchTaskIdList')

        return self

