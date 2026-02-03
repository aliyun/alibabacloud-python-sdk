# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNetworkReachableAnalysisResponseBody(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        create_time: str = None,
        network_path_id: str = None,
        network_path_parameter: str = None,
        network_reachable_analysis_id: str = None,
        network_reachable_analysis_result: str = None,
        network_reachable_analysis_status: str = None,
        reachable: bool = None,
        request_id: str = None,
    ):
        # The unique ID (UID) of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The time when the network path was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The network path ID.
        self.network_path_id = network_path_id
        # The parameters of the network path.
        self.network_path_parameter = network_path_parameter
        # The ID of the task for analyzing network reachability.
        self.network_reachable_analysis_id = network_reachable_analysis_id
        # The result of network reachability analysis, which includes the network topology, error codes of network unreachability, and rules of network unreachability.
        self.network_reachable_analysis_result = network_reachable_analysis_result
        # The state of the task for analyzing network reachability. Valid values:
        # 
        # *   **init**: The task is in progress.
        # *   **finish**: The task is complete.
        # *   **error**: An analysis error occurred.
        # *   **timeout**: The task timed out.
        self.network_reachable_analysis_status = network_reachable_analysis_status
        # Indicates whether the network path is reachable. Valid values:
        # 
        # *   **true**: The network path is reachable.
        # *   **false**: The network path is unreachable.
        self.reachable = reachable
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.network_path_id is not None:
            result['NetworkPathId'] = self.network_path_id

        if self.network_path_parameter is not None:
            result['NetworkPathParameter'] = self.network_path_parameter

        if self.network_reachable_analysis_id is not None:
            result['NetworkReachableAnalysisId'] = self.network_reachable_analysis_id

        if self.network_reachable_analysis_result is not None:
            result['NetworkReachableAnalysisResult'] = self.network_reachable_analysis_result

        if self.network_reachable_analysis_status is not None:
            result['NetworkReachableAnalysisStatus'] = self.network_reachable_analysis_status

        if self.reachable is not None:
            result['Reachable'] = self.reachable

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('NetworkPathId') is not None:
            self.network_path_id = m.get('NetworkPathId')

        if m.get('NetworkPathParameter') is not None:
            self.network_path_parameter = m.get('NetworkPathParameter')

        if m.get('NetworkReachableAnalysisId') is not None:
            self.network_reachable_analysis_id = m.get('NetworkReachableAnalysisId')

        if m.get('NetworkReachableAnalysisResult') is not None:
            self.network_reachable_analysis_result = m.get('NetworkReachableAnalysisResult')

        if m.get('NetworkReachableAnalysisStatus') is not None:
            self.network_reachable_analysis_status = m.get('NetworkReachableAnalysisStatus')

        if m.get('Reachable') is not None:
            self.reachable = m.get('Reachable')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

