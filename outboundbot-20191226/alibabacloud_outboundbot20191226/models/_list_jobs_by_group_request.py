# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListJobsByGroupRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        job_failure_reason: str = None,
        job_group_id: str = None,
        job_status: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.job_failure_reason = job_failure_reason
        # This parameter is required.
        self.job_group_id = job_group_id
        self.job_status = job_status
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_failure_reason is not None:
            result['JobFailureReason'] = self.job_failure_reason

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobFailureReason') is not None:
            self.job_failure_reason = m.get('JobFailureReason')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

