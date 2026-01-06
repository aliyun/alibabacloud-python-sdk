# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Detail(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        dbcluster_id: str = None,
        data: str = None,
        duration_in_millis: int = None,
        estimate_execution_cpu_time_in_seconds: int = None,
        execution_duration_in_millis: int = None,
        last_attempt_id: str = None,
        last_updated_time_in_millis: int = None,
        log_root_path: str = None,
        resource_group_name: str = None,
        resource_provisioning_duration_in_millis: int = None,
        running_start_time_in_millis: int = None,
        started_time_in_millis: int = None,
        submitted_time_in_millis: int = None,
        terminated_time_in_millis: int = None,
        web_ui_address: str = None,
    ):
        self.app_type = app_type
        self.dbcluster_id = dbcluster_id
        self.data = data
        self.duration_in_millis = duration_in_millis
        self.estimate_execution_cpu_time_in_seconds = estimate_execution_cpu_time_in_seconds
        self.execution_duration_in_millis = execution_duration_in_millis
        self.last_attempt_id = last_attempt_id
        self.last_updated_time_in_millis = last_updated_time_in_millis
        self.log_root_path = log_root_path
        self.resource_group_name = resource_group_name
        self.resource_provisioning_duration_in_millis = resource_provisioning_duration_in_millis
        self.running_start_time_in_millis = running_start_time_in_millis
        self.started_time_in_millis = started_time_in_millis
        self.submitted_time_in_millis = submitted_time_in_millis
        self.terminated_time_in_millis = terminated_time_in_millis
        self.web_ui_address = web_ui_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.data is not None:
            result['Data'] = self.data

        if self.duration_in_millis is not None:
            result['DurationInMillis'] = self.duration_in_millis

        if self.estimate_execution_cpu_time_in_seconds is not None:
            result['EstimateExecutionCpuTimeInSeconds'] = self.estimate_execution_cpu_time_in_seconds

        if self.execution_duration_in_millis is not None:
            result['ExecutionDurationInMillis'] = self.execution_duration_in_millis

        if self.last_attempt_id is not None:
            result['LastAttemptId'] = self.last_attempt_id

        if self.last_updated_time_in_millis is not None:
            result['LastUpdatedTimeInMillis'] = self.last_updated_time_in_millis

        if self.log_root_path is not None:
            result['LogRootPath'] = self.log_root_path

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.resource_provisioning_duration_in_millis is not None:
            result['ResourceProvisioningDurationInMillis'] = self.resource_provisioning_duration_in_millis

        if self.running_start_time_in_millis is not None:
            result['RunningStartTimeInMillis'] = self.running_start_time_in_millis

        if self.started_time_in_millis is not None:
            result['StartedTimeInMillis'] = self.started_time_in_millis

        if self.submitted_time_in_millis is not None:
            result['SubmittedTimeInMillis'] = self.submitted_time_in_millis

        if self.terminated_time_in_millis is not None:
            result['TerminatedTimeInMillis'] = self.terminated_time_in_millis

        if self.web_ui_address is not None:
            result['WebUiAddress'] = self.web_ui_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('DurationInMillis') is not None:
            self.duration_in_millis = m.get('DurationInMillis')

        if m.get('EstimateExecutionCpuTimeInSeconds') is not None:
            self.estimate_execution_cpu_time_in_seconds = m.get('EstimateExecutionCpuTimeInSeconds')

        if m.get('ExecutionDurationInMillis') is not None:
            self.execution_duration_in_millis = m.get('ExecutionDurationInMillis')

        if m.get('LastAttemptId') is not None:
            self.last_attempt_id = m.get('LastAttemptId')

        if m.get('LastUpdatedTimeInMillis') is not None:
            self.last_updated_time_in_millis = m.get('LastUpdatedTimeInMillis')

        if m.get('LogRootPath') is not None:
            self.log_root_path = m.get('LogRootPath')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('ResourceProvisioningDurationInMillis') is not None:
            self.resource_provisioning_duration_in_millis = m.get('ResourceProvisioningDurationInMillis')

        if m.get('RunningStartTimeInMillis') is not None:
            self.running_start_time_in_millis = m.get('RunningStartTimeInMillis')

        if m.get('StartedTimeInMillis') is not None:
            self.started_time_in_millis = m.get('StartedTimeInMillis')

        if m.get('SubmittedTimeInMillis') is not None:
            self.submitted_time_in_millis = m.get('SubmittedTimeInMillis')

        if m.get('TerminatedTimeInMillis') is not None:
            self.terminated_time_in_millis = m.get('TerminatedTimeInMillis')

        if m.get('WebUiAddress') is not None:
            self.web_ui_address = m.get('WebUiAddress')

        return self

