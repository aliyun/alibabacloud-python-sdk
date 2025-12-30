# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListDiagnosticResultsResponseBody(DaraModel):
    def __init__(
        self,
        diagnostic_results: List[main_models.ListDiagnosticResultsResponseBodyDiagnosticResults] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The diagnostic information.
        self.diagnostic_results = diagnostic_results
        # Number of items per page in a paginated query. The maximum value is 100.
        # 
        # Default value:
        # 
        # - If no value is set or the set value is less than 20, the default value is 20.
        # - If the set value is greater than 100, the default value is 100.
        self.max_results = max_results
        # NextToken for the next page. Include this value when requesting the next page.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.diagnostic_results:
            for v1 in self.diagnostic_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DiagnosticResults'] = []
        if self.diagnostic_results is not None:
            for k1 in self.diagnostic_results:
                result['DiagnosticResults'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.diagnostic_results = []
        if m.get('DiagnosticResults') is not None:
            for k1 in m.get('DiagnosticResults'):
                temp_model = main_models.ListDiagnosticResultsResponseBodyDiagnosticResults()
                self.diagnostic_results.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDiagnosticResultsResponseBodyDiagnosticResults(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        creation_time: str = None,
        diag_content: str = None,
        diag_id: str = None,
        diag_result: str = None,
        finished_time: str = None,
        resource_id: str = None,
        server_name: str = None,
        status: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # Cluster Name
        self.cluster_name = cluster_name
        # Creation time of the diagnostic task.
        self.creation_time = creation_time
        # Diagnostic content. For example, in network diagnostics, there are static configuration checks, dynamic operation checks, and other diagnostic contents.
        self.diag_content = diag_content
        # Diagnosis ID
        self.diag_id = diag_id
        # Diagnostic result, either success or failure.
        self.diag_result = diag_result
        # Completion time of the diagnostic task.
        self.finished_time = finished_time
        # The resource ID.
        self.resource_id = resource_id
        # Server name.
        self.server_name = server_name
        # Status of the diagnostic task. Possible values:
        # - InProgress: Diagnosing.
        # - Finished: Diagnosis completed.
        # - Failed: Diagnosis failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.diag_content is not None:
            result['DiagContent'] = self.diag_content

        if self.diag_id is not None:
            result['DiagId'] = self.diag_id

        if self.diag_result is not None:
            result['DiagResult'] = self.diag_result

        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.server_name is not None:
            result['ServerName'] = self.server_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DiagContent') is not None:
            self.diag_content = m.get('DiagContent')

        if m.get('DiagId') is not None:
            self.diag_id = m.get('DiagId')

        if m.get('DiagResult') is not None:
            self.diag_result = m.get('DiagResult')

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

