# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class VerifyCheckResultResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.VerifyCheckResultResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.VerifyCheckResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class VerifyCheckResultResponseBodyData(DaraModel):
    def __init__(
        self,
        operate_code: str = None,
        task_id: str = None,
        throttling_time_second: int = None,
    ):
        # The operation code of the cloud service configuration task. Valid values:
        # 
        # *   **Throttling**: frequency limit
        # *   **ActionTrialUnauthorized**: an error that is related to unauthorized operations
        self.operate_code = operate_code
        # The task ID.
        self.task_id = task_id
        # The throttling duration. Unit: seconds
        self.throttling_time_second = throttling_time_second

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operate_code is not None:
            result['OperateCode'] = self.operate_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.throttling_time_second is not None:
            result['ThrottlingTimeSecond'] = self.throttling_time_second

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateCode') is not None:
            self.operate_code = m.get('OperateCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('ThrottlingTimeSecond') is not None:
            self.throttling_time_second = m.get('ThrottlingTimeSecond')

        return self

