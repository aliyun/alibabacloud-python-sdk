# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dsw20220101 import models as main_models
from darabonba.model import DaraModel

class GetSanityCheckTaskResponseBody(DaraModel):
    def __init__(
        self,
        check_details: List[main_models.GetSanityCheckTaskResponseBodyCheckDetails] = None,
        check_type: str = None,
        end_time: str = None,
        instance_id: str = None,
        issues: List[str] = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
        request_id: str = None,
    ):
        self.check_details = check_details
        self.check_type = check_type
        self.end_time = end_time
        self.instance_id = instance_id
        self.issues = issues
        self.start_time = start_time
        self.status = status
        self.task_id = task_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.check_details:
            for v1 in self.check_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckDetails'] = []
        if self.check_details is not None:
            for k1 in self.check_details:
                result['CheckDetails'].append(k1.to_map() if k1 else None)

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.issues is not None:
            result['Issues'] = self.issues

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_details = []
        if m.get('CheckDetails') is not None:
            for k1 in m.get('CheckDetails'):
                temp_model = main_models.GetSanityCheckTaskResponseBodyCheckDetails()
                self.check_details.append(temp_model.from_map(k1))

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Issues') is not None:
            self.issues = m.get('Issues')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetSanityCheckTaskResponseBodyCheckDetails(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        reason: str = None,
        result: str = None,
    ):
        self.description = description
        self.name = name
        self.reason = reason
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

