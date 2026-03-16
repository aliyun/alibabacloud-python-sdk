# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListExecutionsRequest(DaraModel):
    def __init__(
        self,
        execution_name_prefix: str = None,
        flow_name: str = None,
        limit: int = None,
        map_run_name: str = None,
        metadata_only: bool = None,
        next_token: str = None,
        qualifier: str = None,
        started_time_begin: str = None,
        started_time_end: str = None,
        status: str = None,
    ):
        # The name prefix of the execution.
        self.execution_name_prefix = execution_name_prefix
        # The name of the flow. The name must be unique within the region and cannot be modified after the flow is created. The name must meet the following conventions:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a letter or an underscore (_).
        # *   The name is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The number of executions that you want to query. Valid values: 1-99. Default value: 60.
        self.limit = limit
        self.map_run_name = map_run_name
        self.metadata_only = metadata_only
        # The name of the execution to start the query. You can obtain the value from the response data. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        self.qualifier = qualifier
        # The beginning of the time range to query executions. Specify the value in the UTC RFC3339 format.
        self.started_time_begin = started_time_begin
        # The end of the time range to query executions. Specify the value in the UTC RFC3339 format.
        self.started_time_end = started_time_end
        # The status of the execution that you want to filter. Valid values:
        # 
        # *   **Starting**
        # *   **Running**
        # *   **Stopped**
        # *   **Succeeded**
        # *   **Failed**
        # *   **TimedOut**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_name_prefix is not None:
            result['ExecutionNamePrefix'] = self.execution_name_prefix

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.map_run_name is not None:
            result['MapRunName'] = self.map_run_name

        if self.metadata_only is not None:
            result['MetadataOnly'] = self.metadata_only

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier

        if self.started_time_begin is not None:
            result['StartedTimeBegin'] = self.started_time_begin

        if self.started_time_end is not None:
            result['StartedTimeEnd'] = self.started_time_end

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionNamePrefix') is not None:
            self.execution_name_prefix = m.get('ExecutionNamePrefix')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('MapRunName') is not None:
            self.map_run_name = m.get('MapRunName')

        if m.get('MetadataOnly') is not None:
            self.metadata_only = m.get('MetadataOnly')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Qualifier') is not None:
            self.qualifier = m.get('Qualifier')

        if m.get('StartedTimeBegin') is not None:
            self.started_time_begin = m.get('StartedTimeBegin')

        if m.get('StartedTimeEnd') is not None:
            self.started_time_end = m.get('StartedTimeEnd')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

