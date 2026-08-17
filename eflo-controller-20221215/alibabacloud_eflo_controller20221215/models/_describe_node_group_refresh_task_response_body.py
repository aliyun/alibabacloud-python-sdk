# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class DescribeNodeGroupRefreshTaskResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        failed_count: int = None,
        finished_count: int = None,
        max_disruptive_action: str = None,
        max_results: int = None,
        next_token: str = None,
        node_group_id: str = None,
        node_group_refresh_task_id: str = None,
        nodes: List[main_models.DescribeNodeGroupRefreshTaskResponseBodyNodes] = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        total_node_count: int = None,
    ):
        # The end time of the refresh task in ISO 8601 format.
        self.end_time = end_time
        # The number of failed nodes.
        self.failed_count = failed_count
        # The number of finished nodes, including succeeded, failed, and skipped nodes.
        self.finished_count = finished_count
        # The maximum disruptive action level allowed for the refresh operation.
        self.max_disruptive_action = max_disruptive_action
        # The maximum number of entries per page.
        self.max_results = max_results
        # The token for the next query. An empty value of NextToken indicates that no more results exist.
        self.next_token = next_token
        # The ID of the node group.
        self.node_group_id = node_group_id
        # The ID of the refresh task.
        self.node_group_refresh_task_id = node_group_refresh_task_id
        # The list of nodes.
        self.nodes = nodes
        # Id of the request
        self.request_id = request_id
        # The start time of the refresh task in ISO 8601 format.
        self.start_time = start_time
        # The task status. Valid values:
        # - Pending: the refresh task is created and waiting to be executed.
        # - InProgress: the refresh task is being processed.
        # - Success: the refresh task is executed.
        # - Failed: the refresh task failed to be executed.
        self.status = status
        # The total number of nodes to be refreshed in the task.
        self.total_node_count = total_node_count

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.finished_count is not None:
            result['FinishedCount'] = self.finished_count

        if self.max_disruptive_action is not None:
            result['MaxDisruptiveAction'] = self.max_disruptive_action

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_refresh_task_id is not None:
            result['NodeGroupRefreshTaskId'] = self.node_group_refresh_task_id

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.total_node_count is not None:
            result['TotalNodeCount'] = self.total_node_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('FinishedCount') is not None:
            self.finished_count = m.get('FinishedCount')

        if m.get('MaxDisruptiveAction') is not None:
            self.max_disruptive_action = m.get('MaxDisruptiveAction')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupRefreshTaskId') is not None:
            self.node_group_refresh_task_id = m.get('NodeGroupRefreshTaskId')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeNodeGroupRefreshTaskResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalNodeCount') is not None:
            self.total_node_count = m.get('TotalNodeCount')

        return self

class DescribeNodeGroupRefreshTaskResponseBodyNodes(DaraModel):
    def __init__(
        self,
        action: str = None,
        error_code: str = None,
        error_message: str = None,
        node_id: str = None,
        property_drifts: List[main_models.DescribeNodeGroupRefreshTaskResponseBodyNodesPropertyDrifts] = None,
        status: str = None,
    ):
        # The action level actually executed on the node. If multiple properties are refreshed on the node, the highest required action level is used. Valid values:
        # - Refresh: in-place refresh.
        # - Reboot: restart.
        # - Reimage: reimage.
        # If the entire node is skipped, this value is empty.
        self.action = action
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the node.
        self.node_id = node_id
        # The list of property drifts for the node, including both executed and skipped properties.
        self.property_drifts = property_drifts
        # The node refresh status. Valid values:
        # - Pending: the node is waiting to be refreshed.
        # - InProgress: the node is being refreshed.
        # - Success: the node is refreshed.
        # - Failed: the node failed to be refreshed.
        # - Skipped: all properties to be refreshed on the node exceeded the MaxDisruptiveAction constraint and were skipped.
        self.status = status

    def validate(self):
        if self.property_drifts:
            for v1 in self.property_drifts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        result['PropertyDrifts'] = []
        if self.property_drifts is not None:
            for k1 in self.property_drifts:
                result['PropertyDrifts'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        self.property_drifts = []
        if m.get('PropertyDrifts') is not None:
            for k1 in m.get('PropertyDrifts'):
                temp_model = main_models.DescribeNodeGroupRefreshTaskResponseBodyNodesPropertyDrifts()
                self.property_drifts.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeNodeGroupRefreshTaskResponseBodyNodesPropertyDrifts(DaraModel):
    def __init__(
        self,
        actual_value: str = None,
        min_required_action: str = None,
        property_path: str = None,
        skipped: bool = None,
        target_value: str = None,
    ):
        # The current value of the node property. Complex types are serialized as JSON strings.
        self.actual_value = actual_value
        # The minimum action required to apply the target value: Refresh / Reboot / Reimage. For more information, see the MaxDisruptiveAction parameter description in the RefreshNodeGroupNodes operation.
        self.min_required_action = min_required_action
        # The property path in dot notation.
        self.property_path = property_path
        # Indicates whether the property was skipped because it exceeded the MaxDisruptiveAction constraint.
        self.skipped = skipped
        # The target value of the node property. Complex types are serialized as JSON strings.
        self.target_value = target_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value

        if self.min_required_action is not None:
            result['MinRequiredAction'] = self.min_required_action

        if self.property_path is not None:
            result['PropertyPath'] = self.property_path

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.target_value is not None:
            result['TargetValue'] = self.target_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')

        if m.get('MinRequiredAction') is not None:
            self.min_required_action = m.get('MinRequiredAction')

        if m.get('PropertyPath') is not None:
            self.property_path = m.get('PropertyPath')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        return self

