# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class DescribeTaskResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        create_time: str = None,
        message: str = None,
        node_ids: List[str] = None,
        request_id: str = None,
        steps: List[main_models.DescribeTaskResponseBodySteps] = None,
        task_state: str = None,
        task_type: str = None,
        update_time: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The start time. The value is in ISO 8601 format. Z in the example indicates UTC.
        self.create_time = create_time
        # The task failure message.
        self.message = message
        # The list of node IDs.
        self.node_ids = node_ids
        # The request ID.
        self.request_id = request_id
        # The execution steps.
        self.steps = steps
        # The task state.
        self.task_state = task_state
        # The task type.
        self.task_type = task_type
        # The update time. Uses ISO 8601 format. The Z in the example indicates UTC.
        self.update_time = update_time

    def validate(self):
        if self.steps:
            for v1 in self.steps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.message is not None:
            result['Message'] = self.message

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Steps'] = []
        if self.steps is not None:
            for k1 in self.steps:
                result['Steps'].append(k1.to_map() if k1 else None)

        if self.task_state is not None:
            result['TaskState'] = self.task_state

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.steps = []
        if m.get('Steps') is not None:
            for k1 in m.get('Steps'):
                temp_model = main_models.DescribeTaskResponseBodySteps()
                self.steps.append(temp_model.from_map(k1))

        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeTaskResponseBodySteps(DaraModel):
    def __init__(
        self,
        message: str = None,
        stage_tag: str = None,
        start_time: str = None,
        step_name: str = None,
        step_state: str = None,
        step_type: str = None,
        sub_tasks: List[main_models.DescribeTaskResponseBodyStepsSubTasks] = None,
        update_time: str = None,
    ):
        # The step failure message.
        self.message = message
        # The stage tag.
        self.stage_tag = stage_tag
        # The start time. Z in the example indicates UTC.
        self.start_time = start_time
        # The step name.
        self.step_name = step_name
        # The step execution state.
        self.step_state = step_state
        # The step type.
        self.step_type = step_type
        # The subtasks.
        self.sub_tasks = sub_tasks
        # The update time. Uses ISO 8601 format. The Z in the example indicates UTC.
        self.update_time = update_time

    def validate(self):
        if self.sub_tasks:
            for v1 in self.sub_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.stage_tag is not None:
            result['StageTag'] = self.stage_tag

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.step_name is not None:
            result['StepName'] = self.step_name

        if self.step_state is not None:
            result['StepState'] = self.step_state

        if self.step_type is not None:
            result['StepType'] = self.step_type

        result['SubTasks'] = []
        if self.sub_tasks is not None:
            for k1 in self.sub_tasks:
                result['SubTasks'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('StageTag') is not None:
            self.stage_tag = m.get('StageTag')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        if m.get('StepState') is not None:
            self.step_state = m.get('StepState')

        if m.get('StepType') is not None:
            self.step_type = m.get('StepType')

        self.sub_tasks = []
        if m.get('SubTasks') is not None:
            for k1 in m.get('SubTasks'):
                temp_model = main_models.DescribeTaskResponseBodyStepsSubTasks()
                self.sub_tasks.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeTaskResponseBodyStepsSubTasks(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        message: str = None,
        task_id: str = None,
        task_state: str = None,
        task_type: str = None,
        update_time: str = None,
    ):
        # The creation time. The Z in the example indicates UTC.
        self.create_time = create_time
        # The subtask failure message.
        self.message = message
        # The node ID.
        self.task_id = task_id
        # The task execution state.
        self.task_state = task_state
        # The task type.
        self.task_type = task_type
        # The update time. Uses ISO 8601 format. The Z in the example indicates UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.message is not None:
            result['Message'] = self.message

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_state is not None:
            result['TaskState'] = self.task_state

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

