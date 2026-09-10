# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class GetSqlConversionProgressResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetSqlConversionProgressResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data body returned by the operation. For the field structure, see the child field descriptions.
        self.data = data
        # The error code. An empty string is returned if the call is successful.
        self.err_code = err_code
        # The error message. An empty string is returned if the call is successful.
        self.err_message = err_message
        # The request ID, which is used to locate and troubleshoot issues with this call.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # - true: The call is successful.
        # - false: The call failed. Check errCode and errMessage for troubleshooting.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetSqlConversionProgressResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetSqlConversionProgressResponseBodyData(DaraModel):
    def __init__(
        self,
        fail: int = None,
        finish: int = None,
        percent: float = None,
        running: int = None,
        total: int = None,
    ):
        # The number of failed scripts.
        self.fail = fail
        # The number of completed scripts.
        self.finish = finish
        # The completion percentage.
        self.percent = percent
        # The number of scripts being converted.
        self.running = running
        # The total number of scripts.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail is not None:
            result['fail'] = self.fail

        if self.finish is not None:
            result['finish'] = self.finish

        if self.percent is not None:
            result['percent'] = self.percent

        if self.running is not None:
            result['running'] = self.running

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fail') is not None:
            self.fail = m.get('fail')

        if m.get('finish') is not None:
            self.finish = m.get('finish')

        if m.get('percent') is not None:
            self.percent = m.get('percent')

        if m.get('running') is not None:
            self.running = m.get('running')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

