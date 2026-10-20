# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterEventsResponseBody(DaraModel):
    def __init__(
        self,
        events: List[main_models.DescribeClusterEventsResponseBodyEvents] = None,
        next_token: str = None,
        page_info: main_models.DescribeClusterEventsResponseBodyPageInfo = None,
    ):
        # The list of events.
        self.events = events
        # The pagination token.
        self.next_token = next_token
        # The pagination information.
        self.page_info = page_info

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['events'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['next_token'] = self.next_token

        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('events') is not None:
            for k1 in m.get('events'):
                temp_model = main_models.DescribeClusterEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')

        if m.get('page_info') is not None:
            temp_model = main_models.DescribeClusterEventsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('page_info'))

        return self

class DescribeClusterEventsResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The maximum number of results to return per page.
        self.page_size = page_size
        # The total number of results.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['page_number'] = self.page_number

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.total_count is not None:
            result['total_count'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')

        return self

class DescribeClusterEventsResponseBodyEvents(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        data: main_models.DescribeClusterEventsResponseBodyEventsData = None,
        event_id: str = None,
        source: str = None,
        subject: str = None,
        time: str = None,
        type: str = None,
    ):
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The description of the event.
        self.data = data
        # The ID of the event.
        self.event_id = event_id
        # The source of the event.
        self.source = source
        # The operation object associated with the event.
        self.subject = subject
        # The start time of the event. The time is in ISO 8601 format and includes time zone information.
        self.time = time
        # The event type. Valid values:
        # 
        # - cluster_create: Creates a cluster.
        # - cluster_scaleout: Scales out a cluster.
        # - cluster_attach: Adds existing nodes.
        # - cluster_delete: Deletes a cluster.
        # - cluster_upgrade: Upgrades a cluster.
        # - cluster_migrate: Migrates a cluster.
        # - cluster_node_delete: Removes a node.
        # - cluster_node_drain: Drains a node.
        # - cluster_modify: Modifies a cluster.
        # - cluster_configuration_modify: Modifies the control configurations of a cluster.
        # - cluster_addon_install: Installs a component.
        # - cluster_addon_upgrade: Upgrades a component.
        # - cluster_addon_uninstall: Uninstalls a component.
        # - runtime_upgrade: Upgrades the runtime.
        # - nodepool_upgrade: Upgrades a node pool.
        # - nodepool_update: Updates a node pool.
        self.type = type

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.event_id is not None:
            result['event_id'] = self.event_id

        if self.source is not None:
            result['source'] = self.source

        if self.subject is not None:
            result['subject'] = self.subject

        if self.time is not None:
            result['time'] = self.time

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('data') is not None:
            temp_model = main_models.DescribeClusterEventsResponseBodyEventsData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class DescribeClusterEventsResponseBodyEventsData(DaraModel):
    def __init__(
        self,
        level: str = None,
        message: str = None,
        reason: str = None,
    ):
        # The event level.
        self.level = level
        # The details of the event.
        self.message = message
        # The status of the event.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['level'] = self.level

        if self.message is not None:
            result['message'] = self.message

        if self.reason is not None:
            result['reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        return self

