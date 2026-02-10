# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class VerifyCheckInstanceResultResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.VerifyCheckInstanceResultResponseBodyData = None,
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
            temp_model = main_models.VerifyCheckInstanceResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class VerifyCheckInstanceResultResponseBodyData(DaraModel):
    def __init__(
        self,
        fail_instances: List[str] = None,
        operate_code: str = None,
        task_id: str = None,
    ):
        # An array consisting of instances that failed the check.
        self.fail_instances = fail_instances
        # The operation code of the task that checks the configurations of cloud services. Valid values:
        # 
        # *   **Throttling**
        # *   **ActionTrialUnauthorized**
        self.operate_code = operate_code
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_instances is not None:
            result['FailInstances'] = self.fail_instances

        if self.operate_code is not None:
            result['OperateCode'] = self.operate_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailInstances') is not None:
            self.fail_instances = m.get('FailInstances')

        if m.get('OperateCode') is not None:
            self.operate_code = m.get('OperateCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

