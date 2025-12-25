# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class PolicyInfo(DaraModel):
    def __init__(
        self,
        attachments: List[main_models.Attachment] = None,
        class_alias: str = None,
        class_name: str = None,
        config: str = None,
        direction: str = None,
        execute_priority: str = None,
        execute_stage: str = None,
        name: str = None,
        policy_id: str = None,
        type: str = None,
    ):
        self.attachments = attachments
        self.class_alias = class_alias
        self.class_name = class_name
        self.config = config
        self.direction = direction
        self.execute_priority = execute_priority
        self.execute_stage = execute_stage
        self.name = name
        self.policy_id = policy_id
        self.type = type

    def validate(self):
        if self.attachments:
            for v1 in self.attachments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['attachments'] = []
        if self.attachments is not None:
            for k1 in self.attachments:
                result['attachments'].append(k1.to_map() if k1 else None)

        if self.class_alias is not None:
            result['classAlias'] = self.class_alias

        if self.class_name is not None:
            result['className'] = self.class_name

        if self.config is not None:
            result['config'] = self.config

        if self.direction is not None:
            result['direction'] = self.direction

        if self.execute_priority is not None:
            result['executePriority'] = self.execute_priority

        if self.execute_stage is not None:
            result['executeStage'] = self.execute_stage

        if self.name is not None:
            result['name'] = self.name

        if self.policy_id is not None:
            result['policyId'] = self.policy_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('attachments') is not None:
            for k1 in m.get('attachments'):
                temp_model = main_models.Attachment()
                self.attachments.append(temp_model.from_map(k1))

        if m.get('classAlias') is not None:
            self.class_alias = m.get('classAlias')

        if m.get('className') is not None:
            self.class_name = m.get('className')

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('executePriority') is not None:
            self.execute_priority = m.get('executePriority')

        if m.get('executeStage') is not None:
            self.execute_stage = m.get('executeStage')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

