# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class ReleaseInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ReleaseInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # data
        self.data = data
        # The description of the execution result.
        self.message = message
        # The ID of the request, which can be used for troubleshooting.
        self.request_id = request_id
        # A value of true indicates that the execution is complete.
        # 
        # A value of false indicates that an error occurs during the execution.
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
            temp_model = main_models.ReleaseInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ReleaseInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        host_id: str = None,
        release_result: bool = None,
    ):
        # The site of the execution host.
        self.host_id = host_id
        # Indicates whether the instance is released.
        self.release_result = release_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.release_result is not None:
            result['ReleaseResult'] = self.release_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('ReleaseResult') is not None:
            self.release_result = m.get('ReleaseResult')

        return self

