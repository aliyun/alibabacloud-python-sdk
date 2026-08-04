# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class CheckAuthCodeBindForExtResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.CheckAuthCodeBindForExtResponseBodyResult = None,
    ):
        # The returned error code. The value 200 indicates that the invocation succeeded.
        self.code = code
        # Return Result of invoking this API.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Detailed information
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.CheckAuthCodeBindForExtResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class CheckAuthCodeBindForExtResponseBodyResult(DaraModel):
    def __init__(
        self,
        device_open_info: main_models.CheckAuthCodeBindForExtResponseBodyResultDeviceOpenInfo = None,
        user_open_info: main_models.CheckAuthCodeBindForExtResponseBodyResultUserOpenInfo = None,
    ):
        # Device open information
        self.device_open_info = device_open_info
        # User open information
        self.user_open_info = user_open_info

    def validate(self):
        if self.device_open_info:
            self.device_open_info.validate()
        if self.user_open_info:
            self.user_open_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_open_info is not None:
            result['DeviceOpenInfo'] = self.device_open_info.to_map()

        if self.user_open_info is not None:
            result['UserOpenInfo'] = self.user_open_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceOpenInfo') is not None:
            temp_model = main_models.CheckAuthCodeBindForExtResponseBodyResultDeviceOpenInfo()
            self.device_open_info = temp_model.from_map(m.get('DeviceOpenInfo'))

        if m.get('UserOpenInfo') is not None:
            temp_model = main_models.CheckAuthCodeBindForExtResponseBodyResultUserOpenInfo()
            self.user_open_info = temp_model.from_map(m.get('UserOpenInfo'))

        return self

class CheckAuthCodeBindForExtResponseBodyResultUserOpenInfo(DaraModel):
    def __init__(
        self,
        id: str = None,
        id_type: str = None,
    ):
        # External user ID
        self.id = id
        # USER_ID
        self.id_type = id_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.id_type is not None:
            result['IdType'] = self.id_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')

        return self

class CheckAuthCodeBindForExtResponseBodyResultDeviceOpenInfo(DaraModel):
    def __init__(
        self,
        id: str = None,
        id_type: str = None,
    ):
        # External device ID
        self.id = id
        # DEVICE_ID
        self.id_type = id_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.id_type is not None:
            result['IdType'] = self.id_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')

        return self

