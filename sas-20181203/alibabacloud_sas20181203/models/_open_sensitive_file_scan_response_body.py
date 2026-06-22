# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class OpenSensitiveFileScanResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.OpenSensitiveFileScanResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result code. A value of **200** indicates success. Any other value indicates failure. You can use this field to determine the cause of the failure.
        self.code = code
        # The data returned for modifying the sensitive file scan switch.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The detailed information of the error code.
        self.message = message
        # The ID of the request. Alibaba Cloud generates a unique identifier for each request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The result status of the API call. Valid values:
        # - **true**: The API call was successful.
        # - **false**: The API call failed.
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
            temp_model = main_models.OpenSensitiveFileScanResponseBodyData()
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

class OpenSensitiveFileScanResponseBodyData(DaraModel):
    def __init__(
        self,
        switch_on: str = None,
    ):
        # The switch operation. Valid values:
        # 
        # - **on**: Enable.
        # - **off**: Disable.
        self.switch_on = switch_on

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.switch_on is not None:
            result['SwitchOn'] = self.switch_on

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SwitchOn') is not None:
            self.switch_on = m.get('SwitchOn')

        return self

