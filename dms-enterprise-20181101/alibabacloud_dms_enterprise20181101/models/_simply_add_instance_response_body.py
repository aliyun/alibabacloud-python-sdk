# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class SimplyAddInstanceResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        instance: main_models.SimplyAddInstanceResponseBodyInstance = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.instance = instance
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.instance is not None:
            result['Instance'] = self.instance.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Instance') is not None:
            temp_model = main_models.SimplyAddInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m.get('Instance'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SimplyAddInstanceResponseBodyInstance(DaraModel):
    def __init__(
        self,
        host: str = None,
        instance_id: str = None,
        port: str = None,
    ):
        self.host = host
        self.instance_id = instance_id
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['Host'] = self.host

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

