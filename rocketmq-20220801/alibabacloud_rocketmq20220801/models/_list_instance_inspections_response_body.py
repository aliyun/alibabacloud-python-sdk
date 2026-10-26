# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ListInstanceInspectionsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListInstanceInspectionsResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.data = data
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListInstanceInspectionsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

class ListInstanceInspectionsResponseBodyData(DaraModel):
    def __init__(
        self,
        config: main_models.ListInstanceInspectionsResponseBodyDataConfig = None,
        configured: bool = None,
        instance_id: str = None,
        items: List[main_models.ListInstanceInspectionsResponseBodyDataItems] = None,
        next_run_at: str = None,
        region_id: str = None,
        revision: int = None,
    ):
        self.config = config
        self.configured = configured
        self.instance_id = instance_id
        self.items = items
        self.next_run_at = next_run_at
        self.region_id = region_id
        self.revision = revision

    def validate(self):
        if self.config:
            self.config.validate()
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.configured is not None:
            result['configured'] = self.configured

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.next_run_at is not None:
            result['nextRunAt'] = self.next_run_at

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.revision is not None:
            result['revision'] = self.revision

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.ListInstanceInspectionsResponseBodyDataConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('configured') is not None:
            self.configured = m.get('configured')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListInstanceInspectionsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('nextRunAt') is not None:
            self.next_run_at = m.get('nextRunAt')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('revision') is not None:
            self.revision = m.get('revision')

        return self

class ListInstanceInspectionsResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        resource_count: int = None,
        resource_types: List[str] = None,
        template_code: str = None,
    ):
        self.description = description
        self.name = name
        self.resource_count = resource_count
        self.resource_types = resource_types
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.resource_count is not None:
            result['resourceCount'] = self.resource_count

        if self.resource_types is not None:
            result['resourceTypes'] = self.resource_types

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceCount') is not None:
            self.resource_count = m.get('resourceCount')

        if m.get('resourceTypes') is not None:
            self.resource_types = m.get('resourceTypes')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        return self

class ListInstanceInspectionsResponseBodyDataConfig(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListInstanceInspectionsResponseBodyDataConfigItems] = None,
        resource_scope: main_models.ListInstanceInspectionsResponseBodyDataConfigResourceScope = None,
        schedule: main_models.ListInstanceInspectionsResponseBodyDataConfigSchedule = None,
    ):
        # This parameter is required.
        self.items = items
        # This parameter is required.
        self.resource_scope = resource_scope
        # This parameter is required.
        self.schedule = schedule

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
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.resource_scope is not None:
            result['resourceScope'] = self.resource_scope.to_map()

        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListInstanceInspectionsResponseBodyDataConfigItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('resourceScope') is not None:
            temp_model = main_models.ListInstanceInspectionsResponseBodyDataConfigResourceScope()
            self.resource_scope = temp_model.from_map(m.get('resourceScope'))

        if m.get('schedule') is not None:
            temp_model = main_models.ListInstanceInspectionsResponseBodyDataConfigSchedule()
            self.schedule = temp_model.from_map(m.get('schedule'))

        return self

class ListInstanceInspectionsResponseBodyDataConfigSchedule(DaraModel):
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

class ListInstanceInspectionsResponseBodyDataConfigResourceScope(DaraModel):
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

class ListInstanceInspectionsResponseBodyDataConfigItems(DaraModel):
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

