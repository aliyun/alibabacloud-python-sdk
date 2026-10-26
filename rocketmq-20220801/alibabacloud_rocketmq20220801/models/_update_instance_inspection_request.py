# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class UpdateInstanceInspectionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        items: List[main_models.UpdateInstanceInspectionRequestItems] = None,
        resource_scope: main_models.UpdateInstanceInspectionRequestResourceScope = None,
        revision: int = None,
        schedule: main_models.UpdateInstanceInspectionRequestSchedule = None,
        region_id: str = None,
    ):
        # 同一实例配置生命周期内有效 24 小时；同 token 同请求返回首次成功结果，不同请求返回冲突。新请求仍须携带当前 revision。
        # 
        # This parameter is required.
        self.client_token = client_token
        self.items = items
        self.resource_scope = resource_scope
        # This parameter is required.
        self.revision = revision
        self.schedule = schedule
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()
        if self.resource_scope:
            self.resource_scope.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.resource_scope is not None:
            result['resourceScope'] = self.resource_scope.to_map()

        if self.revision is not None:
            result['revision'] = self.revision

        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.UpdateInstanceInspectionRequestItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('resourceScope') is not None:
            temp_model = main_models.UpdateInstanceInspectionRequestResourceScope()
            self.resource_scope = temp_model.from_map(m.get('resourceScope'))

        if m.get('revision') is not None:
            self.revision = m.get('revision')

        if m.get('schedule') is not None:
            temp_model = main_models.UpdateInstanceInspectionRequestSchedule()
            self.schedule = temp_model.from_map(m.get('schedule'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class UpdateInstanceInspectionRequestSchedule(DaraModel):
    def __init__(
        self,
        cron: str = None,
        enabled: bool = None,
    ):
        self.cron = cron
        # This parameter is required.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron is not None:
            result['cron'] = self.cron

        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cron') is not None:
            self.cron = m.get('cron')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

class UpdateInstanceInspectionRequestResourceScope(DaraModel):
    def __init__(
        self,
        consumer_groups: List[str] = None,
        mode: str = None,
        topics: List[str] = None,
    ):
        self.consumer_groups = consumer_groups
        # This parameter is required.
        self.mode = mode
        self.topics = topics

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_groups is not None:
            result['consumerGroups'] = self.consumer_groups

        if self.mode is not None:
            result['mode'] = self.mode

        if self.topics is not None:
            result['topics'] = self.topics

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroups') is not None:
            self.consumer_groups = m.get('consumerGroups')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('topics') is not None:
            self.topics = m.get('topics')

        return self

class UpdateInstanceInspectionRequestItems(DaraModel):
    def __init__(
        self,
        parameters: Any = None,
        template_code: str = None,
    ):
        # This parameter is required.
        self.parameters = parameters
        # This parameter is required.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        return self

