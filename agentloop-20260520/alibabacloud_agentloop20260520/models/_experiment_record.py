# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class ExperimentRecord(DaraModel):
    def __init__(
        self,
        completed_at: int = None,
        completed_tasks: int = None,
        data_source_type: str = None,
        dataset_id: str = None,
        dataset_project: str = None,
        error_message: str = None,
        evaluation_task_id: str = None,
        evaluators: List[main_models.Evaluator] = None,
        executed_at: int = None,
        experiment_config: List[main_models.ExperimentConfig] = None,
        experiment_plan_id: str = None,
        failed_tasks: int = None,
        input: Dict[str, Any] = None,
        model_names: List[str] = None,
        plan_name: str = None,
        progress: float = None,
        query_sql: str = None,
        record_id: str = None,
        record_name: str = None,
        selected_item_ids: List[str] = None,
        status: str = None,
        total_tasks: int = None,
    ):
        self.completed_at = completed_at
        self.completed_tasks = completed_tasks
        self.data_source_type = data_source_type
        self.dataset_id = dataset_id
        self.dataset_project = dataset_project
        self.error_message = error_message
        self.evaluation_task_id = evaluation_task_id
        self.evaluators = evaluators
        self.executed_at = executed_at
        self.experiment_config = experiment_config
        self.experiment_plan_id = experiment_plan_id
        self.failed_tasks = failed_tasks
        self.input = input
        self.model_names = model_names
        self.plan_name = plan_name
        self.progress = progress
        self.query_sql = query_sql
        self.record_id = record_id
        self.record_name = record_name
        self.selected_item_ids = selected_item_ids
        self.status = status
        self.total_tasks = total_tasks

    def validate(self):
        if self.evaluators:
            for v1 in self.evaluators:
                 if v1:
                    v1.validate()
        if self.experiment_config:
            for v1 in self.experiment_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed_at is not None:
            result['completedAt'] = self.completed_at

        if self.completed_tasks is not None:
            result['completedTasks'] = self.completed_tasks

        if self.data_source_type is not None:
            result['dataSourceType'] = self.data_source_type

        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id

        if self.dataset_project is not None:
            result['datasetProject'] = self.dataset_project

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.evaluation_task_id is not None:
            result['evaluationTaskId'] = self.evaluation_task_id

        result['evaluators'] = []
        if self.evaluators is not None:
            for k1 in self.evaluators:
                result['evaluators'].append(k1.to_map() if k1 else None)

        if self.executed_at is not None:
            result['executedAt'] = self.executed_at

        result['experimentConfig'] = []
        if self.experiment_config is not None:
            for k1 in self.experiment_config:
                result['experimentConfig'].append(k1.to_map() if k1 else None)

        if self.experiment_plan_id is not None:
            result['experimentPlanId'] = self.experiment_plan_id

        if self.failed_tasks is not None:
            result['failedTasks'] = self.failed_tasks

        if self.input is not None:
            result['input'] = self.input

        if self.model_names is not None:
            result['modelNames'] = self.model_names

        if self.plan_name is not None:
            result['planName'] = self.plan_name

        if self.progress is not None:
            result['progress'] = self.progress

        if self.query_sql is not None:
            result['querySql'] = self.query_sql

        if self.record_id is not None:
            result['recordId'] = self.record_id

        if self.record_name is not None:
            result['recordName'] = self.record_name

        if self.selected_item_ids is not None:
            result['selectedItemIds'] = self.selected_item_ids

        if self.status is not None:
            result['status'] = self.status

        if self.total_tasks is not None:
            result['totalTasks'] = self.total_tasks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completedAt') is not None:
            self.completed_at = m.get('completedAt')

        if m.get('completedTasks') is not None:
            self.completed_tasks = m.get('completedTasks')

        if m.get('dataSourceType') is not None:
            self.data_source_type = m.get('dataSourceType')

        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')

        if m.get('datasetProject') is not None:
            self.dataset_project = m.get('datasetProject')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('evaluationTaskId') is not None:
            self.evaluation_task_id = m.get('evaluationTaskId')

        self.evaluators = []
        if m.get('evaluators') is not None:
            for k1 in m.get('evaluators'):
                temp_model = main_models.Evaluator()
                self.evaluators.append(temp_model.from_map(k1))

        if m.get('executedAt') is not None:
            self.executed_at = m.get('executedAt')

        self.experiment_config = []
        if m.get('experimentConfig') is not None:
            for k1 in m.get('experimentConfig'):
                temp_model = main_models.ExperimentConfig()
                self.experiment_config.append(temp_model.from_map(k1))

        if m.get('experimentPlanId') is not None:
            self.experiment_plan_id = m.get('experimentPlanId')

        if m.get('failedTasks') is not None:
            self.failed_tasks = m.get('failedTasks')

        if m.get('input') is not None:
            self.input = m.get('input')

        if m.get('modelNames') is not None:
            self.model_names = m.get('modelNames')

        if m.get('planName') is not None:
            self.plan_name = m.get('planName')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('querySql') is not None:
            self.query_sql = m.get('querySql')

        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')

        if m.get('recordName') is not None:
            self.record_name = m.get('recordName')

        if m.get('selectedItemIds') is not None:
            self.selected_item_ids = m.get('selectedItemIds')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('totalTasks') is not None:
            self.total_tasks = m.get('totalTasks')

        return self

