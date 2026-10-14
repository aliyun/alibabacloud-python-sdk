# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aideepsign20260511 import models as main_models
from darabonba.model import DaraModel

class GetVideoTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
        task_id: str = None,
        videos: List[main_models.GetVideoTaskResultResponseBodyVideos] = None,
    ):
        # **Business error code.** Returns "OK" if the request succeeds.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The cause of the failure. This field is returned only when the task status is failed.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The task status. Valid values: running, succeeded, and failed. Set the polling interval to at least 5 seconds.
        self.status = status
        # Indicates whether the request is successful.
        self.success = success
        # The task ID.
        self.task_id = task_id
        # The list of video information.
        self.videos = videos

    def validate(self):
        if self.videos:
            for v1 in self.videos:
                 if v1:
                    v1.validate()

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

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        result['Videos'] = []
        if self.videos is not None:
            for k1 in self.videos:
                result['Videos'].append(k1.to_map() if k1 else None)

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        self.videos = []
        if m.get('Videos') is not None:
            for k1 in m.get('Videos'):
                temp_model = main_models.GetVideoTaskResultResponseBodyVideos()
                self.videos.append(temp_model.from_map(k1))

        return self

class GetVideoTaskResultResponseBodyVideos(DaraModel):
    def __init__(
        self,
        object_key: str = None,
        url: str = None,
    ):
        # The OSS key of the output object.
        self.object_key = object_key
        # The presigned download URL of the video stored in OSS after C2PA signing.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

