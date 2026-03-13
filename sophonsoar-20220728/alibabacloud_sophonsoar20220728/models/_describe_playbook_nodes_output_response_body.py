# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribePlaybookNodesOutputResponseBody(DaraModel):
    def __init__(
        self,
        playbook_nodes_output: main_models.DescribePlaybookNodesOutputResponseBodyPlaybookNodesOutput = None,
        request_id: str = None,
    ):
        # The output data of the component node.
        self.playbook_nodes_output = playbook_nodes_output
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.playbook_nodes_output:
            self.playbook_nodes_output.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.playbook_nodes_output is not None:
            result['PlaybookNodesOutput'] = self.playbook_nodes_output.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlaybookNodesOutput') is not None:
            temp_model = main_models.DescribePlaybookNodesOutputResponseBodyPlaybookNodesOutput()
            self.playbook_nodes_output = temp_model.from_map(m.get('PlaybookNodesOutput'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePlaybookNodesOutputResponseBodyPlaybookNodesOutput(DaraModel):
    def __init__(
        self,
        node_name: str = None,
        node_output: str = None,
    ):
        # The name of the component node.
        self.node_name = node_name
        # The historical output data of the component node. The value is in the JSON string format. If no data is found, the parameter is left empty.
        self.node_output = node_output

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_output is not None:
            result['NodeOutput'] = self.node_output

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeOutput') is not None:
            self.node_output = m.get('NodeOutput')

        return self

