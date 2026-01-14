# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class BatchGetProjectTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_list: List[main_models.BatchGetProjectTaskResponseBodyResultList] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result_list = result_list

    def validate(self):
        if self.result_list:
            for v1 in self.result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['resultList'] = []
        if self.result_list is not None:
            for k1 in self.result_list:
                result['resultList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result_list = []
        if m.get('resultList') is not None:
            for k1 in m.get('resultList'):
                temp_model = main_models.BatchGetProjectTaskResponseBodyResultList()
                self.result_list.append(temp_model.from_map(k1))

        return self

class BatchGetProjectTaskResponseBodyResultList(DaraModel):
    def __init__(
        self,
        error_msg: str = None,
        status: str = None,
        task_id: str = None,
        video_download_url: str = None,
        video_duration: int = None,
        video_url: str = None,
    ):
        self.error_msg = error_msg
        self.status = status
        self.task_id = task_id
        self.video_download_url = video_download_url
        self.video_duration = video_duration
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.video_download_url is not None:
            result['videoDownloadUrl'] = self.video_download_url

        if self.video_duration is not None:
            result['videoDuration'] = self.video_duration

        if self.video_url is not None:
            result['videoUrl'] = self.video_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('videoDownloadUrl') is not None:
            self.video_download_url = m.get('videoDownloadUrl')

        if m.get('videoDuration') is not None:
            self.video_duration = m.get('videoDuration')

        if m.get('videoUrl') is not None:
            self.video_url = m.get('videoUrl')

        return self

