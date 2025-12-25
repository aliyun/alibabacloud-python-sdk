# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class AsyncUploadVideoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.AsyncUploadVideoResponseBodyData = None,
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
            temp_model = main_models.AsyncUploadVideoResponseBodyData()
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

class AsyncUploadVideoResponseBodyData(DaraModel):
    def __init__(
        self,
        task_id: str = None,
        video_infos: List[main_models.AsyncUploadVideoResponseBodyDataVideoInfos] = None,
    ):
        self.task_id = task_id
        self.video_infos = video_infos

    def validate(self):
        if self.video_infos:
            for v1 in self.video_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        result['VideoInfos'] = []
        if self.video_infos is not None:
            for k1 in self.video_infos:
                result['VideoInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        self.video_infos = []
        if m.get('VideoInfos') is not None:
            for k1 in m.get('VideoInfos'):
                temp_model = main_models.AsyncUploadVideoResponseBodyDataVideoInfos()
                self.video_infos.append(temp_model.from_map(k1))

        return self

class AsyncUploadVideoResponseBodyDataVideoInfos(DaraModel):
    def __init__(
        self,
        video_extra_info: str = None,
        video_id: str = None,
        video_name: str = None,
        video_url: str = None,
    ):
        self.video_extra_info = video_extra_info
        self.video_id = video_id
        self.video_name = video_name
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.video_extra_info is not None:
            result['VideoExtraInfo'] = self.video_extra_info

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        if self.video_name is not None:
            result['VideoName'] = self.video_name

        if self.video_url is not None:
            result['VideoUrl'] = self.video_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoExtraInfo') is not None:
            self.video_extra_info = m.get('VideoExtraInfo')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')

        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')

        return self

