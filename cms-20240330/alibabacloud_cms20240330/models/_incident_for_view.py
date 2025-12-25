# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IncidentForView(DaraModel):
    def __init__(
        self,
        content: str = None,
        escalations: List[main_models.IncidentEscalationPolicyForView] = None,
        group_uuid: str = None,
        grouping_keys: Dict[str, str] = None,
        incident_id: str = None,
        notify_strategy_name: str = None,
        notify_strategy_uuid: str = None,
        operator: main_models.ContactForIncidentView = None,
        owners: List[main_models.ContactForIncidentView] = None,
        participants: List[main_models.ContactForIncidentView] = None,
        plan: main_models.IncidentResponsePlanForView = None,
        related_resources: List[main_models.EventResourceForIncidentView] = None,
        root_cause_category: str = None,
        severity: str = None,
        solution: str = None,
        state: str = None,
        subscription_name: str = None,
        subscription_uuid: str = None,
        time: int = None,
        title: str = None,
        user_id: str = None,
        workspace: str = None,
    ):
        self.content = content
        self.escalations = escalations
        self.group_uuid = group_uuid
        self.grouping_keys = grouping_keys
        self.incident_id = incident_id
        self.notify_strategy_name = notify_strategy_name
        self.notify_strategy_uuid = notify_strategy_uuid
        self.operator = operator
        self.owners = owners
        self.participants = participants
        self.plan = plan
        self.related_resources = related_resources
        self.root_cause_category = root_cause_category
        self.severity = severity
        self.solution = solution
        self.state = state
        self.subscription_name = subscription_name
        self.subscription_uuid = subscription_uuid
        self.time = time
        self.title = title
        self.user_id = user_id
        self.workspace = workspace

    def validate(self):
        if self.escalations:
            for v1 in self.escalations:
                 if v1:
                    v1.validate()
        if self.operator:
            self.operator.validate()
        if self.owners:
            for v1 in self.owners:
                 if v1:
                    v1.validate()
        if self.participants:
            for v1 in self.participants:
                 if v1:
                    v1.validate()
        if self.plan:
            self.plan.validate()
        if self.related_resources:
            for v1 in self.related_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        result['escalations'] = []
        if self.escalations is not None:
            for k1 in self.escalations:
                result['escalations'].append(k1.to_map() if k1 else None)

        if self.group_uuid is not None:
            result['groupUuid'] = self.group_uuid

        if self.grouping_keys is not None:
            result['groupingKeys'] = self.grouping_keys

        if self.incident_id is not None:
            result['incidentId'] = self.incident_id

        if self.notify_strategy_name is not None:
            result['notifyStrategyName'] = self.notify_strategy_name

        if self.notify_strategy_uuid is not None:
            result['notifyStrategyUuid'] = self.notify_strategy_uuid

        if self.operator is not None:
            result['operator'] = self.operator.to_map()

        result['owners'] = []
        if self.owners is not None:
            for k1 in self.owners:
                result['owners'].append(k1.to_map() if k1 else None)

        result['participants'] = []
        if self.participants is not None:
            for k1 in self.participants:
                result['participants'].append(k1.to_map() if k1 else None)

        if self.plan is not None:
            result['plan'] = self.plan.to_map()

        result['relatedResources'] = []
        if self.related_resources is not None:
            for k1 in self.related_resources:
                result['relatedResources'].append(k1.to_map() if k1 else None)

        if self.root_cause_category is not None:
            result['rootCauseCategory'] = self.root_cause_category

        if self.severity is not None:
            result['severity'] = self.severity

        if self.solution is not None:
            result['solution'] = self.solution

        if self.state is not None:
            result['state'] = self.state

        if self.subscription_name is not None:
            result['subscriptionName'] = self.subscription_name

        if self.subscription_uuid is not None:
            result['subscriptionUuid'] = self.subscription_uuid

        if self.time is not None:
            result['time'] = self.time

        if self.title is not None:
            result['title'] = self.title

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        self.escalations = []
        if m.get('escalations') is not None:
            for k1 in m.get('escalations'):
                temp_model = main_models.IncidentEscalationPolicyForView()
                self.escalations.append(temp_model.from_map(k1))

        if m.get('groupUuid') is not None:
            self.group_uuid = m.get('groupUuid')

        if m.get('groupingKeys') is not None:
            self.grouping_keys = m.get('groupingKeys')

        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')

        if m.get('notifyStrategyName') is not None:
            self.notify_strategy_name = m.get('notifyStrategyName')

        if m.get('notifyStrategyUuid') is not None:
            self.notify_strategy_uuid = m.get('notifyStrategyUuid')

        if m.get('operator') is not None:
            temp_model = main_models.ContactForIncidentView()
            self.operator = temp_model.from_map(m.get('operator'))

        self.owners = []
        if m.get('owners') is not None:
            for k1 in m.get('owners'):
                temp_model = main_models.ContactForIncidentView()
                self.owners.append(temp_model.from_map(k1))

        self.participants = []
        if m.get('participants') is not None:
            for k1 in m.get('participants'):
                temp_model = main_models.ContactForIncidentView()
                self.participants.append(temp_model.from_map(k1))

        if m.get('plan') is not None:
            temp_model = main_models.IncidentResponsePlanForView()
            self.plan = temp_model.from_map(m.get('plan'))

        self.related_resources = []
        if m.get('relatedResources') is not None:
            for k1 in m.get('relatedResources'):
                temp_model = main_models.EventResourceForIncidentView()
                self.related_resources.append(temp_model.from_map(k1))

        if m.get('rootCauseCategory') is not None:
            self.root_cause_category = m.get('rootCauseCategory')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('solution') is not None:
            self.solution = m.get('solution')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('subscriptionName') is not None:
            self.subscription_name = m.get('subscriptionName')

        if m.get('subscriptionUuid') is not None:
            self.subscription_uuid = m.get('subscriptionUuid')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

