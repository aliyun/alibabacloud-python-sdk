# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetInstanceStatusCountResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        status_count: main_models.GetInstanceStatusCountResponseBodyStatusCount = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The statistics of instances.
        self.status_count = status_count

    def validate(self):
        if self.status_count:
            self.status_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status_count is not None:
            result['StatusCount'] = self.status_count.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StatusCount') is not None:
            temp_model = main_models.GetInstanceStatusCountResponseBodyStatusCount()
            self.status_count = temp_model.from_map(m.get('StatusCount'))

        return self

class GetInstanceStatusCountResponseBodyStatusCount(DaraModel):
    def __init__(
        self,
        failure_count: int = None,
        not_run_count: int = None,
        running_count: int = None,
        success_count: int = None,
        total_count: int = None,
        wait_res_count: int = None,
        wait_time_count: int = None,
    ):
        # The number of instances that failed.
        self.failure_count = failure_count
        # The number of instances that are not run.
        self.not_run_count = not_run_count
        # The number of instances that are running.
        self.running_count = running_count
        # The number of instances that are successfully run.
        self.success_count = success_count
        # The total number of instances returned.
        self.total_count = total_count
        # The number of instances that are waiting for resources.
        self.wait_res_count = wait_res_count
        # The number of instances that are waiting for their scheduling time to arrive.
        self.wait_time_count = wait_time_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failure_count is not None:
            result['FailureCount'] = self.failure_count

        if self.not_run_count is not None:
            result['NotRunCount'] = self.not_run_count

        if self.running_count is not None:
            result['RunningCount'] = self.running_count

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.wait_res_count is not None:
            result['WaitResCount'] = self.wait_res_count

        if self.wait_time_count is not None:
            result['WaitTimeCount'] = self.wait_time_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailureCount') is not None:
            self.failure_count = m.get('FailureCount')

        if m.get('NotRunCount') is not None:
            self.not_run_count = m.get('NotRunCount')

        if m.get('RunningCount') is not None:
            self.running_count = m.get('RunningCount')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('WaitResCount') is not None:
            self.wait_res_count = m.get('WaitResCount')

        if m.get('WaitTimeCount') is not None:
            self.wait_time_count = m.get('WaitTimeCount')

        return self

