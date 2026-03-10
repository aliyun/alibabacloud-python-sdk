# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cms20240330 import models as main_models
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
        evaluators: List[main_models.Evaluator] = None,
        executed_at: int = None,
        experiment_config: main_models.ExperimentConfig = None,
        experiment_name: str = None,
        failed_tasks: int = None,
        input: Dict[str, Any] = None,
        model_name: str = None,
        plan_id: str = None,
        plan_name: str = None,
        progress: float = None,
        record_id: str = None,
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
        self.evaluators = evaluators
        self.executed_at = executed_at
        self.experiment_config = experiment_config
        self.experiment_name = experiment_name
        self.failed_tasks = failed_tasks
        self.input = input
        self.model_name = model_name
        self.plan_id = plan_id
        self.plan_name = plan_name
        self.progress = progress
        self.record_id = record_id
        self.selected_item_ids = selected_item_ids
        self.status = status
        self.total_tasks = total_tasks

    def validate(self):
        if self.evaluators:
            for v1 in self.evaluators:
                 if v1:
                    v1.validate()
        if self.experiment_config:
            self.experiment_config.validate()

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

        result['evaluators'] = []
        if self.evaluators is not None:
            for k1 in self.evaluators:
                result['evaluators'].append(k1.to_map() if k1 else None)

        if self.executed_at is not None:
            result['executedAt'] = self.executed_at

        if self.experiment_config is not None:
            result['experimentConfig'] = self.experiment_config.to_map()

        if self.experiment_name is not None:
            result['experimentName'] = self.experiment_name

        if self.failed_tasks is not None:
            result['failedTasks'] = self.failed_tasks

        if self.input is not None:
            result['input'] = self.input

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.plan_id is not None:
            result['planId'] = self.plan_id

        if self.plan_name is not None:
            result['planName'] = self.plan_name

        if self.progress is not None:
            result['progress'] = self.progress

        if self.record_id is not None:
            result['recordId'] = self.record_id

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

        self.evaluators = []
        if m.get('evaluators') is not None:
            for k1 in m.get('evaluators'):
                temp_model = main_models.Evaluator()
                self.evaluators.append(temp_model.from_map(k1))

        if m.get('executedAt') is not None:
            self.executed_at = m.get('executedAt')

        if m.get('experimentConfig') is not None:
            temp_model = main_models.ExperimentConfig()
            self.experiment_config = temp_model.from_map(m.get('experimentConfig'))

        if m.get('experimentName') is not None:
            self.experiment_name = m.get('experimentName')

        if m.get('failedTasks') is not None:
            self.failed_tasks = m.get('failedTasks')

        if m.get('input') is not None:
            self.input = m.get('input')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('planId') is not None:
            self.plan_id = m.get('planId')

        if m.get('planName') is not None:
            self.plan_name = m.get('planName')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')

        if m.get('selectedItemIds') is not None:
            self.selected_item_ids = m.get('selectedItemIds')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('totalTasks') is not None:
            self.total_tasks = m.get('totalTasks')

        return self

