# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExperimentPlanData(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        dataset_id: str = None,
        description: str = None,
        experiment_count: int = None,
        plan_id: str = None,
        plan_name: str = None,
        status: str = None,
        updated_at: int = None,
    ):
        self.created_at = created_at
        self.dataset_id = dataset_id
        self.description = description
        self.experiment_count = experiment_count
        self.plan_id = plan_id
        self.plan_name = plan_name
        self.status = status
        self.updated_at = updated_at

    def validate(self):
        pass

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

        if self.experiment_count is not None:
            result['experimentCount'] = self.experiment_count

        if self.plan_id is not None:
            result['planId'] = self.plan_id

        if self.plan_name is not None:
            result['planName'] = self.plan_name

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

        if m.get('experimentCount') is not None:
            self.experiment_count = m.get('experimentCount')

        if m.get('planId') is not None:
            self.plan_id = m.get('planId')

        if m.get('planName') is not None:
            self.plan_name = m.get('planName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

