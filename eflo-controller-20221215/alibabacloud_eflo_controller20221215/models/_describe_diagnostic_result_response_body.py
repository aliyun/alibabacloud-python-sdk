# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from darabonba.model import DaraModel

class DescribeDiagnosticResultResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        created_time: str = None,
        diagnostic_id: str = None,
        diagnostic_results: List[Any] = None,
        diagnostic_state: str = None,
        diagnostic_type: str = None,
        end_time: str = None,
        node_ids: List[str] = None,
        request_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The creation time.
        self.created_time = created_time
        # The diagnostic task ID.
        self.diagnostic_id = diagnostic_id
        # The diagnostic information.
        self.diagnostic_results = diagnostic_results
        # The diagnostic status.
        self.diagnostic_state = diagnostic_state
        # The type of the diagnostic task.
        self.diagnostic_type = diagnostic_type
        # The end time of the instance exception. The time format with time zone based on the ISO8601 standard. The format is yyyy-MM-ddTHH:mm:ss +0800.
        self.end_time = end_time
        # The node IDs.
        self.node_ids = node_ids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.diagnostic_id is not None:
            result['DiagnosticId'] = self.diagnostic_id

        if self.diagnostic_results is not None:
            result['DiagnosticResults'] = self.diagnostic_results

        if self.diagnostic_state is not None:
            result['DiagnosticState'] = self.diagnostic_state

        if self.diagnostic_type is not None:
            result['DiagnosticType'] = self.diagnostic_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DiagnosticId') is not None:
            self.diagnostic_id = m.get('DiagnosticId')

        if m.get('DiagnosticResults') is not None:
            self.diagnostic_results = m.get('DiagnosticResults')

        if m.get('DiagnosticState') is not None:
            self.diagnostic_state = m.get('DiagnosticState')

        if m.get('DiagnosticType') is not None:
            self.diagnostic_type = m.get('DiagnosticType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

