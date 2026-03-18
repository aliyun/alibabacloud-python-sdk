# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetQuotaScheduleResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetQuotaScheduleResponseBodyData] = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetQuotaScheduleResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetQuotaScheduleResponseBodyData(DaraModel):
    def __init__(
        self,
        condition: main_models.GetQuotaScheduleResponseBodyDataCondition = None,
        id: str = None,
        operator: str = None,
        plan: str = None,
        timezone: str = None,
        type: str = None,
    ):
        self.condition = condition
        self.id = id
        self.operator = operator
        self.plan = plan
        self.timezone = timezone
        self.type = type

    def validate(self):
        if self.condition:
            self.condition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['condition'] = self.condition.to_map()

        if self.id is not None:
            result['id'] = self.id

        if self.operator is not None:
            result['operator'] = self.operator

        if self.plan is not None:
            result['plan'] = self.plan

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            temp_model = main_models.GetQuotaScheduleResponseBodyDataCondition()
            self.condition = temp_model.from_map(m.get('condition'))

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('plan') is not None:
            self.plan = m.get('plan')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetQuotaScheduleResponseBodyDataCondition(DaraModel):
    def __init__(
        self,
        after: str = None,
        at: str = None,
    ):
        self.after = after
        self.at = at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after is not None:
            result['after'] = self.after

        if self.at is not None:
            result['at'] = self.at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('after') is not None:
            self.after = m.get('after')

        if m.get('at') is not None:
            self.at = m.get('at')

        return self

