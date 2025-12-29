# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeEventsResponseBody(DaraModel):
    def __init__(
        self,
        events: List[main_models.DescribeEventsResponseBodyEvents] = None,
        page_info: main_models.DescribeEventsResponseBodyPageInfo = None,
    ):
        # The details of the events.
        self.events = events
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

        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('events') is not None:
            for k1 in m.get('events'):
                temp_model = main_models.DescribeEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('page_info') is not None:
            temp_model = main_models.DescribeEventsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('page_info'))

        return self

class DescribeEventsResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
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

class DescribeEventsResponseBodyEvents(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        data: main_models.DescribeEventsResponseBodyEventsData = None,
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
        # The event ID.
        self.event_id = event_id
        # The source of the event.
        self.source = source
        # The subject of the event.
        self.subject = subject
        # The time when the event started.
        self.time = time
        # The event type. Valid values:
        # 
        # *   `cluster_create`: cluster creation.
        # *   `cluster_scaleout`: cluster scale-out.
        # *   `cluster_attach`: node addition.
        # *   `cluster_delete`: cluster deletion.
        # *   `cluster_upgrade`: cluster upgrades.
        # *   `cluster_migrate`: cluster migration.
        # *   `cluster_node_delete`: node removal.
        # *   `cluster_node_drain`: node draining.
        # *   `cluster_modify`: cluster modifications.
        # *   `cluster_configuration_modify`: modifications of control plane configurations.
        # *   `cluster_addon_install`: component installation.
        # *   `cluster_addon_upgrade`: component updates.
        # *   `cluster_addon_uninstall`: component uninstallation.
        # *   `runtime_upgrade`: runtime updates.
        # *   `nodepool_upgrade`: node pool upgrades.
        # *   `nodepool_update`: node pool updates.
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
            temp_model = main_models.DescribeEventsResponseBodyEventsData()
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

class DescribeEventsResponseBodyEventsData(DaraModel):
    def __init__(
        self,
        level: str = None,
        message: str = None,
        reason: str = None,
    ):
        # The severity level of the event. Valid values:
        # 
        # *   info
        # *   warning
        # *   error
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

