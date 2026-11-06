# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class CreateAndBindAppResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateAndBindAppResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. This field is returned when the request fails. A successful response may not contain this field.
        self.code = code
        # The business data returned by the operation.
        self.data = data
        # The error or result message. This field describes the cause when the request fails. A successful response may not contain this field.
        self.message = message
        # The unique identifier of the request. Provide this value when you troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request is processed successfully. A value of true indicates that the request is processed successfully. To determine whether an asynchronous task is completed, query the task status separately.
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
            temp_model = main_models.CreateAndBindAppResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateAndBindAppResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_version_id: str = None,
        image_id: str = None,
        version_id: str = None,
    ):
        # The application ID, which is used to query the application or dissociate the image later.
        self.app_id = app_id
        # The application version ID, which is used to locate a specified version of the application. This field is not the image version ID.
        self.app_version_id = app_version_id
        # The image ID, which is used to query or modify the image later.
        self.image_id = image_id
        # The image version ID, which is used to query or manage a specified version of the image.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

