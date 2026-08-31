# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class UpdateEvaluationTaskRequest(DaraModel):
    def __init__(
        self,
        config: Dict[str, str] = None,
        data_filter: str = None,
        description: str = None,
        evaluators: List[main_models.Evaluator] = None,
        run_strategies: main_models.RunStrategies = None,
        status: str = None,
        tags: Dict[str, str] = None,
        client_token: str = None,
    ):
        # The new task configuration. Some fields that are set during creation cannot be modified.
        self.config = config
        # The filter conditions for evaluation data. JSON objects and JSON strings are supported.
        self.data_filter = data_filter
        # The description of the evaluation task.
        self.description = description
        # The new list of evaluator configurations. When specified, this list entirely replaces the existing evaluator list of the task, and the system re-validates evaluator uniqueness and variable mappings.
        self.evaluators = evaluators
        # The new task execution strategies. JSON objects and JSON strings are supported. If the task is in the `Completed`, `Terminated`, or `Failed` state and the new strategy enables backfill or continuous mode, the backend restores the task to the `Pending` state and triggers orchestration.
        self.run_strategies = run_strategies
        # The task status. Currently, the backend only allows users to manually set this to `Terminated`. Other statuses are managed by the system.
        self.status = status
        # The key-value pairs of task tags. You do not need to specify this parameter by default. Specify this parameter only when you want to associate or filter tasks by business tags.
        self.tags = tags
        # The idempotency token. CloudSpec declares this query parameter, but the backend does not currently perform idempotency checks.
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
        if self.config is not None:
            result['config'] = self.config

        if self.data_filter is not None:
            result['dataFilter'] = self.data_filter

        if self.description is not None:
            result['description'] = self.description

        result['evaluators'] = []
        if self.evaluators is not None:
            for k1 in self.evaluators:
                result['evaluators'].append(k1.to_map() if k1 else None)

        if self.run_strategies is not None:
            result['runStrategies'] = self.run_strategies.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.tags is not None:
            result['tags'] = self.tags

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('dataFilter') is not None:
            self.data_filter = m.get('dataFilter')

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

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

