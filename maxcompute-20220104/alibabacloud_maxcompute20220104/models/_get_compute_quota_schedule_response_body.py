# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetComputeQuotaScheduleResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetComputeQuotaScheduleResponseBodyData] = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: informational response. The request is received and is being processed.
        # - 2xx: success. The request is successfully received, understood, and accepted by the server.
        # - 3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # - 4xx: client error. The request contains invalid request parameters or syntaxes, or specific request conditions cannot be met.
        # - 5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
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
                temp_model = main_models.GetComputeQuotaScheduleResponseBodyData()
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

class GetComputeQuotaScheduleResponseBodyData(DaraModel):
    def __init__(
        self,
        condition: main_models.GetComputeQuotaScheduleResponseBodyDataCondition = None,
        id: str = None,
        plan: str = None,
        timezone: str = None,
        type: str = None,
    ):
        # The value of effective condition.
        self.condition = condition
        # The ID of the quota plan.
        self.id = id
        # The name of the quota plan.
        self.plan = plan
        # The time zone property.
        self.timezone = timezone
        # The type of the quota plan.
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
            temp_model = main_models.GetComputeQuotaScheduleResponseBodyDataCondition()
            self.condition = temp_model.from_map(m.get('condition'))

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('plan') is not None:
            self.plan = m.get('plan')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetComputeQuotaScheduleResponseBodyDataCondition(DaraModel):
    def __init__(
        self,
        at: str = None,
    ):
        # The start time when the quota plan takes effect.
        self.at = at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.at is not None:
            result['at'] = self.at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('at') is not None:
            self.at = m.get('at')

        return self

