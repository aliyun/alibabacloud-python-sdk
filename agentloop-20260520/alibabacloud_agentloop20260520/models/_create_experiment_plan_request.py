# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class CreateExperimentPlanRequest(DaraModel):
    def __init__(
        self,
        dataset_id: str = None,
        description: str = None,
        evaluators: List[main_models.Evaluator] = None,
        experiment_type: str = None,
        experiments: List[main_models.ExperimentConfig] = None,
        input: Dict[str, Any] = None,
        pipeline_name: str = None,
        plan_name: str = None,
        query_sql: str = None,
        selected_item_ids: List[str] = None,
    ):
        # The ID of the associated dataset. If this parameter is not specified, the execution phase processes in simple mode.
        self.dataset_id = dataset_id
        # The description of the experiment plan.
        self.description = description
        # The list of evaluators. When configured, evaluation can be automatically triggered upon experiment completion.
        self.evaluators = evaluators
        # The experiment type. Set this parameter to `OFFLINE` or `ONLINE`.
        # 
        # This parameter is required.
        self.experiment_type = experiment_type
        # The list of experiment configurations. A maximum of five configurations are supported. For offline experiments, this parameter can be omitted or set to an empty array. For online experiments, at least one configuration is required.
        # 
        # This parameter is required.
        self.experiments = experiments
        # Optional.
        self.input = input
        # The name of the associated data processing pipeline (optional). After association, when the experiment execution under this plan writes results to the experiment result Logstore, the system filters by the traceId of the experiment trace, calls PreviewPipeline, and writes the pipeline-processed results together.
        self.pipeline_name = pipeline_name
        # The experiment plan name. The name must be unique within the same AgentSpace under the same account.
        # 
        # This parameter is required.
        self.plan_name = plan_name
        # The custom query SQL clause in partial dataset mode. This parameter can be used when `selectedItemIds` is empty.
        self.query_sql = query_sql
        # The list of selected data item IDs in partial dataset mode. Use this parameter together with `datasetId`.
        self.selected_item_ids = selected_item_ids

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

        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name

        if self.plan_name is not None:
            result['planName'] = self.plan_name

        if self.query_sql is not None:
            result['querySql'] = self.query_sql

        if self.selected_item_ids is not None:
            result['selectedItemIds'] = self.selected_item_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')

        if m.get('planName') is not None:
            self.plan_name = m.get('planName')

        if m.get('querySql') is not None:
            self.query_sql = m.get('querySql')

        if m.get('selectedItemIds') is not None:
            self.selected_item_ids = m.get('selectedItemIds')

        return self

