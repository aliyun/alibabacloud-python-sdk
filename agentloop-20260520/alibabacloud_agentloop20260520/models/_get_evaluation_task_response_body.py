# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class GetEvaluationTaskResponseBody(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        channel: str = None,
        config: Dict[str, str] = None,
        created_at: int = None,
        data_filter: str = None,
        data_type: str = None,
        description: str = None,
        evaluators: List[main_models.Evaluator] = None,
        region_id: str = None,
        request_id: str = None,
        run_strategy_config: main_models.RunStrategies = None,
        status: str = None,
        tags: Dict[str, str] = None,
        task_id: str = None,
        task_mode: str = None,
        task_name: str = None,
        updated_at: int = None,
    ):
        # The AgentSpace name.
        self.agent_space = agent_space
        # The task source.
        self.channel = channel
        # The data source and execution configuration. Tasks with `dataType=trace` typically include `project`, `storeName`, and `dataScope` fields populated by the backend.
        self.config = config
        # The creation time, in seconds-level UNIX timestamp.
        self.created_at = created_at
        # The filter conditions for evaluation data, returned by the backend as a JSON string.
        self.data_filter = data_filter
        # The data source type of the evaluation object.
        self.data_type = data_type
        # The evaluation task description.
        self.description = description
        # The list of evaluator configurations.
        self.evaluators = evaluators
        # The region to which the task belongs.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The structured configuration of the run strategy, including the parsed backfill strategy and continuous evaluation strategy.
        self.run_strategy_config = run_strategy_config
        # The evaluation task status.
        self.status = status
        # The key-value pairs of task tags. Empty if not set.
        self.tags = tags
        # The evaluation task ID.
        self.task_id = task_id
        # The evaluation task mode.
        self.task_mode = task_mode
        # The task name.
        self.task_name = task_name
        # The last update time, in seconds-level UNIX timestamp.
        self.updated_at = updated_at

    def validate(self):
        if self.evaluators:
            for v1 in self.evaluators:
                 if v1:
                    v1.validate()
        if self.run_strategy_config:
            self.run_strategy_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.channel is not None:
            result['channel'] = self.channel

        if self.config is not None:
            result['config'] = self.config

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.data_filter is not None:
            result['dataFilter'] = self.data_filter

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.description is not None:
            result['description'] = self.description

        result['evaluators'] = []
        if self.evaluators is not None:
            for k1 in self.evaluators:
                result['evaluators'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.run_strategy_config is not None:
            result['runStrategyConfig'] = self.run_strategy_config.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.tags is not None:
            result['tags'] = self.tags

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_mode is not None:
            result['taskMode'] = self.task_mode

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('dataFilter') is not None:
            self.data_filter = m.get('dataFilter')

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('description') is not None:
            self.description = m.get('description')

        self.evaluators = []
        if m.get('evaluators') is not None:
            for k1 in m.get('evaluators'):
                temp_model = main_models.Evaluator()
                self.evaluators.append(temp_model.from_map(k1))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('runStrategyConfig') is not None:
            temp_model = main_models.RunStrategies()
            self.run_strategy_config = temp_model.from_map(m.get('runStrategyConfig'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskMode') is not None:
            self.task_mode = m.get('taskMode')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

