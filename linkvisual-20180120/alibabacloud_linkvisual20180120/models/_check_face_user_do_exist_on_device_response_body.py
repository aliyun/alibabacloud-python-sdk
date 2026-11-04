# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class CheckFaceUserDoExistOnDeviceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CheckFaceUserDoExistOnDeviceResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned check information.
        self.data = data
        # The error message.
        self.error_message = error_message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

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
            temp_model = main_models.CheckFaceUserDoExistOnDeviceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CheckFaceUserDoExistOnDeviceResponseBodyData(DaraModel):
    def __init__(
        self,
        do_exist: bool = None,
    ):
        # Indicates whether the face of the specified user is successfully synchronized.
        self.do_exist = do_exist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.do_exist is not None:
            result['DoExist'] = self.do_exist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DoExist') is not None:
            self.do_exist = m.get('DoExist')

        return self

