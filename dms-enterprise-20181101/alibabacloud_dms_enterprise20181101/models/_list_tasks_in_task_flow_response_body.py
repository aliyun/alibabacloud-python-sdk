# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListTasksInTaskFlowResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        tasks: main_models.ListTasksInTaskFlowResponseBodyTasks = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request. You can use the ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The tasks in the task flow.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Tasks') is not None:
            temp_model = main_models.ListTasksInTaskFlowResponseBodyTasks()
            self.tasks = temp_model.from_map(m.get('Tasks'))

        return self

class ListTasksInTaskFlowResponseBodyTasks(DaraModel):
    def __init__(
        self,
        task: List[main_models.ListTasksInTaskFlowResponseBodyTasksTask] = None,
    ):
        self.task = task

    def validate(self):
        if self.task:
            for v1 in self.task:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Task'] = []
        if self.task is not None:
            for k1 in self.task:
                result['Task'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task = []
        if m.get('Task') is not None:
            for k1 in m.get('Task'):
                temp_model = main_models.ListTasksInTaskFlowResponseBodyTasksTask()
                self.task.append(temp_model.from_map(k1))

        return self

class ListTasksInTaskFlowResponseBodyTasksTask(DaraModel):
    def __init__(
        self,
        graph_param: str = None,
        node_config: str = None,
        node_content: str = None,
        node_id: str = None,
        node_name: str = None,
        node_output: str = None,
        node_type: str = None,
        time_variables: str = None,
    ):
        # The position of the node on the Directed Acyclic Graph (DAG).
        self.graph_param = graph_param
        # The advanced configuration for the node.
        self.node_config = node_config
        # The configuration for the node.
        self.node_content = node_content
        # The ID of the node.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The output variables for the task.
        self.node_output = node_output
        # The type of the node. For more information about the valid values for this parameter, see [NodeType parameter](https://help.aliyun.com/document_detail/424705.html).
        self.node_type = node_type
        # The time variables configured for the node.
        self.time_variables = time_variables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.graph_param is not None:
            result['GraphParam'] = self.graph_param

        if self.node_config is not None:
            result['NodeConfig'] = self.node_config

        if self.node_content is not None:
            result['NodeContent'] = self.node_content

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_output is not None:
            result['NodeOutput'] = self.node_output

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.time_variables is not None:
            result['TimeVariables'] = self.time_variables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GraphParam') is not None:
            self.graph_param = m.get('GraphParam')

        if m.get('NodeConfig') is not None:
            self.node_config = m.get('NodeConfig')

        if m.get('NodeContent') is not None:
            self.node_content = m.get('NodeContent')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeOutput') is not None:
            self.node_output = m.get('NodeOutput')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('TimeVariables') is not None:
            self.time_variables = m.get('TimeVariables')

        return self

