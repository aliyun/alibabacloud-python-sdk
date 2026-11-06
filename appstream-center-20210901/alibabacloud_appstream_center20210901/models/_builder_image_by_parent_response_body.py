# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class BuilderImageByParentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.BuilderImageByParentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. This parameter is returned when the request fails. A successful response may not contain this parameter.
        self.code = code
        # The business data returned by this operation.
        self.data = data
        # The error or result message. This parameter describes the cause when the request fails. A successful response may not contain this parameter.
        self.message = message
        # The unique identifier of the request. You can provide this value for troubleshooting.
        self.request_id = request_id
        # Indicates whether the request is processed successfully. A value of true indicates that the request is processed successfully. To check whether the asynchronous task is completed, you must query the task status separately.
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
            temp_model = main_models.BuilderImageByParentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class BuilderImageByParentResponseBodyData(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        task_id: str = None,
        version_id: str = None,
    ):
        # The image ID, which is used for subsequent queries or modifications of the image.
        self.image_id = image_id
        # The task ID, which can be used to call GetTask to query the task status.
        self.task_id = task_id
        # The image version ID, which is used to query or manage the specified version of the image.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

