# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceJobResponseBody(DaraModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        instance_id: str = None,
        instance_job_id: str = None,
        reason_message: str = None,
        request_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The creation time in UTC, in ISO 8601 format.
        self.gmt_create_time = gmt_create_time
        # The instance ID. For example, if a job creates a custom role, this parameter returns the corresponding role ID.
        self.instance_id = instance_id
        # The job ID.
        self.instance_job_id = instance_job_id
        # A message providing details about the job.
        self.reason_message = reason_message
        # The request ID.
        self.request_id = request_id
        # The status of the job. Valid values:
        # 
        # - Creating: The job is being created.
        # 
        # - Updating: The job is being updated.
        # 
        # - Deleting: The job is being deleted.
        # 
        # - Successful: The job completed successfully (a final state).
        # 
        # - Failed: The job failed (a final state).
        self.status = status
        # The job type. Valid values:
        # 
        # - CreateWorkspaceCustomRole
        # 
        # - UpdateWorkspaceCustomRole
        # 
        # - DeleteWorkspaceCustomRole
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_job_id is not None:
            result['InstanceJobId'] = self.instance_job_id

        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceJobId') is not None:
            self.instance_job_id = m.get('InstanceJobId')

        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

