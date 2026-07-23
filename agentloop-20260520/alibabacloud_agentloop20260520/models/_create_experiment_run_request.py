# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class CreateExperimentRunRequest(DaraModel):
    def __init__(
        self,
        completed_at: int = None,
        completed_tasks: int = None,
        executed_at: int = None,
        experiment_plan_id: str = None,
        failed_tasks: int = None,
        offline_experiments: List[main_models.OfflineExperimentConfig] = None,
        record_name: str = None,
        status: str = None,
        total_tasks: int = None,
        client_token: str = None,
    ):
        # The completion time, in millisecond-level UNIX timestamp.
        self.completed_at = completed_at
        # The number of completed tasks. If not specified, the default value is 0.
        self.completed_tasks = completed_tasks
        # The execution time, in millisecond-level UNIX timestamp.
        self.executed_at = executed_at
        # The experiment plan ID.
        # 
        # This parameter is required.
        self.experiment_plan_id = experiment_plan_id
        # The number of failed tasks. If not specified, the default value is 0.
        self.failed_tasks = failed_tasks
        # The list of offline experiment configurations. Required when the plan type is offline. The number of items ranges from 1 to 5.
        self.offline_experiments = offline_experiments
        # The experiment record name. If not specified, the default value is the plan name plus a timestamp.
        self.record_name = record_name
        # The initial status. If not specified, the default value is `pending`.
        self.status = status
        # The total number of tasks. For online experiments, if not specified, the value is calculated based on the number of generated tasks.
        self.total_tasks = total_tasks
        # Optional.
        self.client_token = client_token

    def validate(self):
        if self.offline_experiments:
            for v1 in self.offline_experiments:
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

        if self.executed_at is not None:
            result['executedAt'] = self.executed_at

        if self.experiment_plan_id is not None:
            result['experimentPlanId'] = self.experiment_plan_id

        if self.failed_tasks is not None:
            result['failedTasks'] = self.failed_tasks

        result['offlineExperiments'] = []
        if self.offline_experiments is not None:
            for k1 in self.offline_experiments:
                result['offlineExperiments'].append(k1.to_map() if k1 else None)

        if self.record_name is not None:
            result['recordName'] = self.record_name

        if self.status is not None:
            result['status'] = self.status

        if self.total_tasks is not None:
            result['totalTasks'] = self.total_tasks

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completedAt') is not None:
            self.completed_at = m.get('completedAt')

        if m.get('completedTasks') is not None:
            self.completed_tasks = m.get('completedTasks')

        if m.get('executedAt') is not None:
            self.executed_at = m.get('executedAt')

        if m.get('experimentPlanId') is not None:
            self.experiment_plan_id = m.get('experimentPlanId')

        if m.get('failedTasks') is not None:
            self.failed_tasks = m.get('failedTasks')

        self.offline_experiments = []
        if m.get('offlineExperiments') is not None:
            for k1 in m.get('offlineExperiments'):
                temp_model = main_models.OfflineExperimentConfig()
                self.offline_experiments.append(temp_model.from_map(k1))

        if m.get('recordName') is not None:
            self.record_name = m.get('recordName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('totalTasks') is not None:
            self.total_tasks = m.get('totalTasks')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

