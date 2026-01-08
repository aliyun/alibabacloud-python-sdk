# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dsw20220101 import models as main_models
from darabonba.model import DaraModel

class GetLifecycleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        lifecycle: List[List[main_models.GetLifecycleResponseBodyLifecycle]] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: All errors, except for parameter validation errors, are internal errors.
        # *   ValidationError: A parameter validation error.
        self.code = code
        # The lifecycle details.
        self.lifecycle = lifecycle
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of queried sessions.
        self.total_count = total_count

    def validate(self):
        if self.lifecycle:
            for v1 in self.lifecycle:
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Lifecycle'] = []
        if self.lifecycle is not None:
            for k1 in self.lifecycle:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['Lifecycle'].append(l1)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.lifecycle = []
        if m.get('Lifecycle') is not None:
            for k1 in m.get('Lifecycle'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.GetLifecycleResponseBodyLifecycle()
                    l1.append(temp_model.from_map(k2))
                self.lifecycle.append(l1)

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetLifecycleResponseBodyLifecycle(DaraModel):
    def __init__(
        self,
        status: str = None,
        reason_code: str = None,
        reason_message: str = None,
        gmt_create_time: str = None,
        gmt_end_time: str = None,
        lifecycle_id: str = None,
    ):
        # The status of the instance. Valid values:
        # 
        # *   Creating
        # *   SaveFailed: The instance image failed to be saved.
        # *   Stopped
        # *   Failed
        # *   ResourceAllocating
        # *   Stopping
        # *   Updating
        # *   Saving
        # *   Starting
        # *   Running
        # *   Saved
        # *   EnvPreparing: Preparing environment.
        # *   ArrearStopping: The service is being stopped due to overdue payments.
        # *   Arrearge: The service is stopped due to overdue payments.
        # *   Queuing
        # *   Recovering
        self.status = status
        # The reason code that corresponds to an event.
        self.reason_code = reason_code
        # The reason message that corresponds to an event.
        self.reason_message = reason_message
        # The time the status was created, specifically the time the instance transitioned to this status (in GMT).
        self.gmt_create_time = gmt_create_time
        self.gmt_end_time = gmt_end_time
        self.lifecycle_id = lifecycle_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time

        if self.lifecycle_id is not None:
            result['LifecycleId'] = self.lifecycle_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')

        if m.get('LifecycleId') is not None:
            self.lifecycle_id = m.get('LifecycleId')

        return self

