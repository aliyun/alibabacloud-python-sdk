# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class CreateMcubeVhostResponseBody(DaraModel):
    def __init__(
        self,
        create_vhost_result: main_models.CreateMcubeVhostResponseBodyCreateVhostResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.create_vhost_result = create_vhost_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.create_vhost_result:
            self.create_vhost_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_vhost_result is not None:
            result['CreateVhostResult'] = self.create_vhost_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateVhostResult') is not None:
            temp_model = main_models.CreateMcubeVhostResponseBodyCreateVhostResult()
            self.create_vhost_result = temp_model.from_map(m.get('CreateVhostResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class CreateMcubeVhostResponseBodyCreateVhostResult(DaraModel):
    def __init__(
        self,
        data: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

