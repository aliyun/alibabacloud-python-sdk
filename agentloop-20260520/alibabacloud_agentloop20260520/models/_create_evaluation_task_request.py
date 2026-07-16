# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class CreateEvaluationTaskRequest(DaraModel):
    def __init__(
        self,
        channel: str = None,
        config: Dict[str, str] = None,
        data_filter: str = None,
        data_type: str = None,
        description: str = None,
        evaluators: List[main_models.Evaluator] = None,
        run_strategies: main_models.RunStrategies = None,
        tags: Dict[str, str] = None,
        task_mode: str = None,
        task_name: str = None,
        client_token: str = None,
    ):
        # The task source. If this parameter is not specified, the backend uses `default`.
        self.channel = channel
        # The data source and execution configuration. When `dataType` is set to `trace`, the backend automatically populates the SLS Project and sets `storeName` to `logstore-tracing`. For trace-level evaluation, set `dataScope` to `trace`.
        self.config = config
        # The filter conditions for evaluation data. This parameter supports a JSON object or a JSON string. Common fields include `query`, `provided`, `maxRecords`, and `samplingRate`.
        self.data_filter = data_filter
        # The data source type of the evaluation object. Set this parameter to `trace` for trace-based evaluation.
        self.data_type = data_type
        # The description of the evaluation task.
        self.description = description
        # The list of evaluator configurations. This parameter cannot be empty. Within the same task, `evaluatorRef` takes precedence as the unique identifier. Otherwise, `name` is used.
        self.evaluators = evaluators
        # The task execution strategy. This parameter supports a JSON object or a JSON string. Set this parameter to `backfill` for historical data backfill or `continuous` for continuous evaluation of new data.
        self.run_strategies = run_strategies
        # The key-value pairs of task tags. You do not need to specify this parameter by default. Specify this parameter only when you want to associate or filter tasks by business tags.
        self.tags = tags
        # The evaluation task mode. Set this parameter to `batch` to create a persistent evaluation task.
        self.task_mode = task_mode
        # The task name. The name must be unique among non-deleted tasks within the same user and AgentSpace. The name can be up to 256 characters in length.
        self.task_name = task_name
        # The idempotency token. This query parameter is declared in CloudSpec, but the backend does not currently perform idempotency comparison.
        self.client_token = client_token

    def validate(self):
        if self.evaluators:
            for v1 in self.evaluators:
                 if v1:
                    v1.validate()
        if self.run_strategies:
            self.run_strategies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['channel'] = self.channel

        if self.config is not None:
            result['config'] = self.config

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

        if self.run_strategies is not None:
            result['runStrategies'] = self.run_strategies.to_map()

        if self.tags is not None:
            result['tags'] = self.tags

        if self.task_mode is not None:
            result['taskMode'] = self.task_mode

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('config') is not None:
            self.config = m.get('config')

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

        if m.get('runStrategies') is not None:
            temp_model = main_models.RunStrategies()
            self.run_strategies = temp_model.from_map(m.get('runStrategies'))

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('taskMode') is not None:
            self.task_mode = m.get('taskMode')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

