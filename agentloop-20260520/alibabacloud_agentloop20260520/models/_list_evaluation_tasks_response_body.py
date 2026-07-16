# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class ListEvaluationTasksResponseBody(DaraModel):
    def __init__(
        self,
        evaluation_tasks: List[main_models.ListEvaluationTasksResponseBodyEvaluationTasks] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of evaluation task summaries.
        self.evaluation_tasks = evaluation_tasks
        # The number of entries per page used in this request.
        self.max_results = max_results
        # The pagination token for the next page. An empty value indicates that no more pages are available.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of records. The total count is returned only on the first page. This value may be empty on subsequent pages.
        self.total_count = total_count

    def validate(self):
        if self.evaluation_tasks:
            for v1 in self.evaluation_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['evaluationTasks'] = []
        if self.evaluation_tasks is not None:
            for k1 in self.evaluation_tasks:
                result['evaluationTasks'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.evaluation_tasks = []
        if m.get('evaluationTasks') is not None:
            for k1 in m.get('evaluationTasks'):
                temp_model = main_models.ListEvaluationTasksResponseBodyEvaluationTasks()
                self.evaluation_tasks.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListEvaluationTasksResponseBodyEvaluationTasks(DaraModel):
    def __init__(
        self,
        config: Dict[str, str] = None,
        created_at: int = None,
        data_type: str = None,
        description: str = None,
        evaluators: str = None,
        run_strategy_config: main_models.RunStrategies = None,
        status: str = None,
        tags: Dict[str, str] = None,
        task_id: str = None,
        task_mode: str = None,
        task_name: str = None,
        updated_at: int = None,
    ):
        # The data source and execution configuration summary.
        self.config = config
        # The creation time, in seconds-level UNIX timestamp.
        self.created_at = created_at
        # The data source type of the evaluation object.
        self.data_type = data_type
        # The evaluation task description.
        self.description = description
        # The evaluator configuration summary, in JSON string format.
        self.evaluators = evaluators
        # The structured run strategy configuration, including the parsed backfill strategy and continuous evaluation strategy.
        self.run_strategy_config = run_strategy_config
        # The evaluation task status.
        self.status = status
        # The key-value pairs of task tags. This parameter is empty if no tags are set.
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
        if self.run_strategy_config:
            self.run_strategy_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.description is not None:
            result['description'] = self.description

        if self.evaluators is not None:
            result['evaluators'] = self.evaluators

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
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('evaluators') is not None:
            self.evaluators = m.get('evaluators')

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

