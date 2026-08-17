# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListNodeGroupDriftedNodesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        nodes: List[main_models.ListNodeGroupDriftedNodesResponseBodyNodes] = None,
        request_id: str = None,
    ):
        # The maximum number of entries per page for a single query.
        self.max_results = max_results
        # The pagination token returned by this call. An empty value indicates that no more pages are available.
        self.next_token = next_token
        # The list of nodes that are inconsistent with the node group configuration (paginated).
        self.nodes = nodes
        # Id of the request
        self.request_id = request_id

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.ListNodeGroupDriftedNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListNodeGroupDriftedNodesResponseBodyNodes(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        property_drifts: List[main_models.ListNodeGroupDriftedNodesResponseBodyNodesPropertyDrifts] = None,
    ):
        # The ID of the node.
        self.node_id = node_id
        # The list of inconsistent properties for this node.
        self.property_drifts = property_drifts

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
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        result['PropertyDrifts'] = []
        if self.property_drifts is not None:
            for k1 in self.property_drifts:
                result['PropertyDrifts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        self.property_drifts = []
        if m.get('PropertyDrifts') is not None:
            for k1 in m.get('PropertyDrifts'):
                temp_model = main_models.ListNodeGroupDriftedNodesResponseBodyNodesPropertyDrifts()
                self.property_drifts.append(temp_model.from_map(k1))

        return self

class ListNodeGroupDriftedNodesResponseBodyNodesPropertyDrifts(DaraModel):
    def __init__(
        self,
        actual_value: str = None,
        min_required_action: str = None,
        property_path: str = None,
        target_value: str = None,
    ):
        # The current value of the node property. Complex types are serialized as JSON strings.
        self.actual_value = actual_value
        # The minimum action required to apply the TargetValue: Refresh / Reboot / Reimage. For more information, refer to the MaxDisruptiveAction parameter description in the RefreshNodeGroupNodes operation.
        self.min_required_action = min_required_action
        # The property path in dot notation (such as a.b.c), compatible with both flat and nested properties.
        self.property_path = property_path
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

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        return self

