# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class AppendInstancesToPrometheusGlobalViewResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.AppendInstancesToPrometheusGlobalViewResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Status code. 200 means success, other status codes are exceptions.
        self.code = code
        # The information about the array object.
        self.data = data
        # Additional message.
        self.message = message
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.AppendInstancesToPrometheusGlobalViewResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AppendInstancesToPrometheusGlobalViewResponseBodyData(DaraModel):
    def __init__(
        self,
        info: str = None,
        msg: str = None,
        success: bool = None,
    ):
        # The Info-level information.
        self.info = info
        # The additional information.
        self.msg = msg
        # Indicates whether the call was successful. Valid values:
        # 
        # *   `true`: The call was successful.
        # *   `false`: The call failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info is not None:
            result['Info'] = self.info

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

