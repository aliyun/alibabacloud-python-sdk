# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class GetExperimentPlanResponseBody(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        dataset_id: str = None,
        description: str = None,
        evaluators: List[main_models.Evaluator] = None,
        experiment_type: str = None,
        experiments: List[main_models.ExperimentConfig] = None,
        input: Dict[str, Any] = None,
        plan_id: str = None,
        plan_name: str = None,
        query_sql: str = None,
        request_id: str = None,
        selected_item_ids: List[str] = None,
        status: str = None,
        updated_at: int = None,
    ):
        # The creation time, in millisecond Unix timestamp.
        self.created_at = created_at
        # The associated dataset ID.
        self.dataset_id = dataset_id
        # The description.
        self.description = description
        # The list of evaluators.
        self.evaluators = evaluators
        # The experiment type.
        self.experiment_type = experiment_type
        # The list of experiment configurations.
        self.experiments = experiments
        # Optional.
        self.input = input
        # The experiment plan ID.
        self.plan_id = plan_id
        # The experiment plan name.
        self.plan_name = plan_name
        # The custom query SQL clause in partial dataset mode.
        self.query_sql = query_sql
        # The request ID.
        self.request_id = request_id
        # The list of selected data item IDs in partial dataset mode.
        self.selected_item_ids = selected_item_ids
        # The plan status.
        self.status = status
        # The update time, in millisecond Unix timestamp.
        self.updated_at = updated_at

    def validate(self):
        if self.evaluators:
            for v1 in self.evaluators:
                 if v1:
                    v1.validate()
        if self.experiments:
            for v1 in self.experiments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id

        if self.description is not None:
            result['description'] = self.description

        result['evaluators'] = []
        if self.evaluators is not None:
            for k1 in self.evaluators:
                result['evaluators'].append(k1.to_map() if k1 else None)

        if self.experiment_type is not None:
            result['experimentType'] = self.experiment_type

        result['experiments'] = []
        if self.experiments is not None:
            for k1 in self.experiments:
                result['experiments'].append(k1.to_map() if k1 else None)

        if self.input is not None:
            result['input'] = self.input

        if self.plan_id is not None:
            result['planId'] = self.plan_id

        if self.plan_name is not None:
            result['planName'] = self.plan_name

        if self.query_sql is not None:
            result['querySql'] = self.query_sql

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.selected_item_ids is not None:
            result['selectedItemIds'] = self.selected_item_ids

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')

        if m.get('description') is not None:
            self.description = m.get('description')

        self.evaluators = []
        if m.get('evaluators') is not None:
            for k1 in m.get('evaluators'):
                temp_model = main_models.Evaluator()
                self.evaluators.append(temp_model.from_map(k1))

        if m.get('experimentType') is not None:
            self.experiment_type = m.get('experimentType')

        self.experiments = []
        if m.get('experiments') is not None:
            for k1 in m.get('experiments'):
                temp_model = main_models.ExperimentConfig()
                self.experiments.append(temp_model.from_map(k1))

        if m.get('input') is not None:
            self.input = m.get('input')

        if m.get('planId') is not None:
            self.plan_id = m.get('planId')

        if m.get('planName') is not None:
            self.plan_name = m.get('planName')

        if m.get('querySql') is not None:
            self.query_sql = m.get('querySql')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('selectedItemIds') is not None:
            self.selected_item_ids = m.get('selectedItemIds')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

