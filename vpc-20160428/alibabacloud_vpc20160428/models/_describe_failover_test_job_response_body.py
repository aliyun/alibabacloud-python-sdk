# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeFailoverTestJobResponseBody(DaraModel):
    def __init__(
        self,
        failover_test_job_model: main_models.DescribeFailoverTestJobResponseBodyFailoverTestJobModel = None,
        request_id: str = None,
    ):
        # The failover test.
        self.failover_test_job_model = failover_test_job_model
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.failover_test_job_model:
            self.failover_test_job_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failover_test_job_model is not None:
            result['FailoverTestJobModel'] = self.failover_test_job_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailoverTestJobModel') is not None:
            temp_model = main_models.DescribeFailoverTestJobResponseBodyFailoverTestJobModel()
            self.failover_test_job_model = temp_model.from_map(m.get('FailoverTestJobModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFailoverTestJobResponseBodyFailoverTestJobModel(DaraModel):
    def __init__(
        self,
        description: str = None,
        job_duration: str = None,
        job_id: str = None,
        job_type: str = None,
        name: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        start_time: str = None,
        status: str = None,
        stop_time: str = None,
    ):
        # The description of the failover test.
        # 
        # The description must be 0 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The duration of the failover test. Unit: minutes. Valid values: **1 to 4320**.
        self.job_duration = job_duration
        # The ID of the failover test.
        self.job_id = job_id
        # Indicates whether the failover test is performed immediately. Valid values:
        # 
        # *   **StartNow**
        # *   **StartLater**
        self.job_type = job_type
        # The name of the failover test.
        # 
        # The name must be 0 to 128 characters in length and cannot start with `http://` or `https://`.
        self.name = name
        # The IDs of failover test resources.
        self.resource_id = resource_id
        # The type of failover test resource. Only **PHYSICALCONNECTION** is returned.
        self.resource_type = resource_type
        # The start time of the failover test. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The status of the failover test. Valid values:
        # 
        # *   **Init**
        # *   **Starting**
        # *   **Testing**
        # *   **Stopping**
        # *   **Stopped**
        self.status = status
        # The end time of the failover test. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.stop_time = stop_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.job_duration is not None:
            result['JobDuration'] = self.job_duration

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.stop_time is not None:
            result['StopTime'] = self.stop_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('JobDuration') is not None:
            self.job_duration = m.get('JobDuration')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')

        return self

