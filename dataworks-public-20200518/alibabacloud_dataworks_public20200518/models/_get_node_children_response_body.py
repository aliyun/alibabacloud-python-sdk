# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetNodeChildrenResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetNodeChildrenResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the descendant nodes.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetNodeChildrenResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetNodeChildrenResponseBodyData(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.GetNodeChildrenResponseBodyDataNodes] = None,
    ):
        # The descendant nodes.
        self.nodes = nodes

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
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.GetNodeChildrenResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k1))

        return self

class GetNodeChildrenResponseBodyDataNodes(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        cron_express: str = None,
        node_id: int = None,
        node_name: str = None,
        owner_id: str = None,
        priority: int = None,
        program_type: str = None,
        project_id: int = None,
        repeatability: bool = None,
        scheduler_type: str = None,
        step_type: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The CRON expression. CRON expressions are used to run auto triggered nodes.
        self.cron_express = cron_express
        # The node ID.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The ID of the Alibaba Cloud account used by the node owner.
        self.owner_id = owner_id
        # The priority. Valid values: 1 to 8. A large value indicates a high priority.
        self.priority = priority
        # The type of the node.
        self.program_type = program_type
        # The ID of the workspace to which the node belongs.
        self.project_id = project_id
        # Indicates whether the node can be rerun if the node fails to run. Valid values:
        # 
        # *   true
        # *   false
        self.repeatability = repeatability
        # The scheduling type of the node. Valid values:
        # 
        # *   NORMAL: The node is an auto triggered node.
        # *   MANUAL: The node is a manually triggered node. Manually triggered nodes cannot be automatically triggered.
        # *   PAUSE: The node is a paused node. Paused nodes are started as scheduled but the system sets the status of the nodes to failed when it starts to run them.
        # *   SKIP: The node is a dry-run node. Dry-run nodes are started as scheduled but the system sets the status of the nodes to successful when it starts to run them.
        self.scheduler_type = scheduler_type
        # The scheduling dependency type. Valid values:
        # 
        # *   **0**: same-cycle scheduling dependency
        # *   **3**: cross-cycle scheduling dependency
        self.step_type = step_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.cron_express is not None:
            result['CronExpress'] = self.cron_express

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.program_type is not None:
            result['ProgramType'] = self.program_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.repeatability is not None:
            result['Repeatability'] = self.repeatability

        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type

        if self.step_type is not None:
            result['StepType'] = self.step_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('CronExpress') is not None:
            self.cron_express = m.get('CronExpress')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProgramType') is not None:
            self.program_type = m.get('ProgramType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Repeatability') is not None:
            self.repeatability = m.get('Repeatability')

        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')

        if m.get('StepType') is not None:
            self.step_type = m.get('StepType')

        return self

