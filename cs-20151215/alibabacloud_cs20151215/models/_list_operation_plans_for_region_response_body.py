# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ListOperationPlansForRegionResponseBody(DaraModel):
    def __init__(
        self,
        plans: List[main_models.ListOperationPlansForRegionResponseBodyPlans] = None,
    ):
        self.plans = plans

    def validate(self):
        if self.plans:
            for v1 in self.plans:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['plans'] = []
        if self.plans is not None:
            for k1 in self.plans:
                result['plans'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plans = []
        if m.get('plans') is not None:
            for k1 in m.get('plans'):
                temp_model = main_models.ListOperationPlansForRegionResponseBodyPlans()
                self.plans.append(temp_model.from_map(k1))

        return self

class ListOperationPlansForRegionResponseBodyPlans(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        created: str = None,
        end_time: str = None,
        plan_id: str = None,
        start_time: str = None,
        state: str = None,
        state_reason: main_models.ListOperationPlansForRegionResponseBodyPlansStateReason = None,
        target_id: str = None,
        target_type: str = None,
        task_id: str = None,
        type: str = None,
    ):
        self.cluster_id = cluster_id
        self.created = created
        self.end_time = end_time
        self.plan_id = plan_id
        self.start_time = start_time
        self.state = state
        self.state_reason = state_reason
        self.target_id = target_id
        self.target_type = target_type
        self.task_id = task_id
        self.type = type

    def validate(self):
        if self.state_reason:
            self.state_reason.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.created is not None:
            result['created'] = self.created

        if self.end_time is not None:
            result['end_time'] = self.end_time

        if self.plan_id is not None:
            result['plan_id'] = self.plan_id

        if self.start_time is not None:
            result['start_time'] = self.start_time

        if self.state is not None:
            result['state'] = self.state

        if self.state_reason is not None:
            result['state_reason'] = self.state_reason.to_map()

        if self.target_id is not None:
            result['target_id'] = self.target_id

        if self.target_type is not None:
            result['target_type'] = self.target_type

        if self.task_id is not None:
            result['task_id'] = self.task_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')

        if m.get('plan_id') is not None:
            self.plan_id = m.get('plan_id')

        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('state_reason') is not None:
            temp_model = main_models.ListOperationPlansForRegionResponseBodyPlansStateReason()
            self.state_reason = temp_model.from_map(m.get('state_reason'))

        if m.get('target_id') is not None:
            self.target_id = m.get('target_id')

        if m.get('target_type') is not None:
            self.target_type = m.get('target_type')

        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListOperationPlansForRegionResponseBodyPlansStateReason(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

