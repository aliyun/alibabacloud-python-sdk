# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListInstanceNodesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        message: str = None,
        nodes: List[main_models.ListInstanceNodesResponseBodyNodes] = None,
        request_id: str = None,
        state_version: int = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The physical instance ID.
        self.instance_id = instance_id
        # The error description.
        self.message = message
        # The visible nodes arranged in topological order. The number of nodes is determined by the actual dynamic graph.
        self.nodes = nodes
        # The request tracking ID.
        self.request_id = request_id
        # The state version.
        self.state_version = state_version

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
        if self.code is not None:
            result['code'] = self.code

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.message is not None:
            result['message'] = self.message

        result['nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['nodes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.state_version is not None:
            result['stateVersion'] = self.state_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('message') is not None:
            self.message = m.get('message')

        self.nodes = []
        if m.get('nodes') is not None:
            for k1 in m.get('nodes'):
                temp_model = main_models.ListInstanceNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('stateVersion') is not None:
            self.state_version = m.get('stateVersion')

        return self

class ListInstanceNodesResponseBodyNodes(DaraModel):
    def __init__(
        self,
        conclusion: str = None,
        duration: int = None,
        entered_at: str = None,
        finished_at: str = None,
        handler: str = None,
        lane: int = None,
        node_id: str = None,
        node_name: str = None,
        node_order: int = None,
        node_type: str = None,
        rank: int = None,
        status: str = None,
        wait_type: str = None,
    ):
        # The conclusion of the node result. This field is empty if there is no conclusion.
        self.conclusion = conclusion
        # The total number of seconds from the first run to the desired state. This field is empty if the time is missing.
        self.duration = duration
        # The time when the node was first run. This field is empty for historical or unrun nodes.
        self.entered_at = entered_at
        # The time when the node actually entered the desired state. This field is empty if the node has not finished.
        self.finished_at = finished_at
        # The display name of the node assignee. This field is empty if the assignee is unknown.
        self.handler = handler
        # The lane position of the node in the workflow graph.
        self.lane = lane
        # The key of the node (nodeKey). This is not the session ID.
        self.node_id = node_id
        # The display name of the node.
        self.node_name = node_name
        # The display sequence number of the node in the returned topology list, starting from 1.
        self.node_order = node_order
        # The actual node type, such as AGENT or HUMAN.
        self.node_type = node_type
        # The level of the node in the workflow graph, starting from 0.
        self.rank = rank
        # The original running status of the node, such as READY, RUNNING, WAITING, SUCCEEDED, or FAILED.
        self.status = status
        # The reason for waiting, such as HUMAN_INPUT, HUMAN_STEP, REVIEW, MANUAL_PAUSE, or UNBLOCK. This field is empty if the node is not waiting.
        self.wait_type = wait_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conclusion is not None:
            result['conclusion'] = self.conclusion

        if self.duration is not None:
            result['duration'] = self.duration

        if self.entered_at is not None:
            result['enteredAt'] = self.entered_at

        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at

        if self.handler is not None:
            result['handler'] = self.handler

        if self.lane is not None:
            result['lane'] = self.lane

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.node_name is not None:
            result['nodeName'] = self.node_name

        if self.node_order is not None:
            result['nodeOrder'] = self.node_order

        if self.node_type is not None:
            result['nodeType'] = self.node_type

        if self.rank is not None:
            result['rank'] = self.rank

        if self.status is not None:
            result['status'] = self.status

        if self.wait_type is not None:
            result['waitType'] = self.wait_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conclusion') is not None:
            self.conclusion = m.get('conclusion')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('enteredAt') is not None:
            self.entered_at = m.get('enteredAt')

        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        if m.get('handler') is not None:
            self.handler = m.get('handler')

        if m.get('lane') is not None:
            self.lane = m.get('lane')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')

        if m.get('nodeOrder') is not None:
            self.node_order = m.get('nodeOrder')

        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')

        if m.get('rank') is not None:
            self.rank = m.get('rank')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('waitType') is not None:
            self.wait_type = m.get('waitType')

        return self

