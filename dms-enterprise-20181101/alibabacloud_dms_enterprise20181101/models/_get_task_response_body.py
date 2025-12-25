# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetTaskResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        task: main_models.GetTaskResponseBodyTask = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The task node.
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

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

        if self.task is not None:
            result['Task'] = self.task.to_map()

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

        if m.get('Task') is not None:
            temp_model = main_models.GetTaskResponseBodyTask()
            self.task = temp_model.from_map(m.get('Task'))

        return self

class GetTaskResponseBodyTask(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        graph_param: str = None,
        node_config: str = None,
        node_content: str = None,
        node_name: str = None,
        node_output: str = None,
        node_type: str = None,
        time_variables: str = None,
    ):
        # The ID of the task flow to which the node belongs.
        self.dag_id = dag_id
        # The position of the node on the Directed Acyclic Graph (DAG).
        self.graph_param = graph_param
        # The advanced configuration for the node.
        self.node_config = node_config
        # The configuration for the node.
        self.node_content = node_content
        # The name of the node.
        self.node_name = node_name
        # The output variables for the node. This parameter is available only for some types of nodes.
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
        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.graph_param is not None:
            result['GraphParam'] = self.graph_param

        if self.node_config is not None:
            result['NodeConfig'] = self.node_config

        if self.node_content is not None:
            result['NodeContent'] = self.node_content

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
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('GraphParam') is not None:
            self.graph_param = m.get('GraphParam')

        if m.get('NodeConfig') is not None:
            self.node_config = m.get('NodeConfig')

        if m.get('NodeContent') is not None:
            self.node_content = m.get('NodeContent')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeOutput') is not None:
            self.node_output = m.get('NodeOutput')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('TimeVariables') is not None:
            self.time_variables = m.get('TimeVariables')

        return self

