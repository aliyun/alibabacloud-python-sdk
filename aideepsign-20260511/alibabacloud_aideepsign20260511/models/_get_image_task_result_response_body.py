# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aideepsign20260511 import models as main_models
from darabonba.model import DaraModel

class GetImageTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        images: List[main_models.GetImageTaskResultResponseBodyImages] = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # The business error code. The value `OK` is returned if the request succeeds.
        self.code = code
        # The error message. This parameter is returned only when the task status is `failed`.
        self.error_message = error_message
        # The HTTP status code. The value `200` is returned if the request succeeds.
        self.http_status_code = http_status_code
        # The list of generated images. This parameter is returned only when `Status` is `succeeded`.
        self.images = images
        # The additional information. The value `success` is returned if the request succeeds. An error message is returned if the task fails. This parameter is returned only when `Status` is `failed`.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The task status. Valid values: `pending` (waiting), `running` (in progress), `succeeded` (completed), `failed` (failed).
        self.status = status
        # Indicates whether the request was successful.
        self.success = success
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['Images'].append(k1.to_map() if k1 else None)

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.GetImageTaskResultResponseBodyImages()
                self.images.append(temp_model.from_map(k1))

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

        return self

class GetImageTaskResultResponseBodyImages(DaraModel):
    def __init__(
        self,
        object_key: str = None,
        url: str = None,
    ):
        # The `ObjectKey` of the image in OSS. You can use this value in subsequent API calls.
        self.object_key = object_key
        # The pre-signed download URL of the image. The URL is valid for 1 hour.
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

