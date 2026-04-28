# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class Activity(DaraModel):
    def __init__(
        self,
        activity_id: str = None,
        device: str = None,
        drive_id: str = None,
        event_type: int = None,
        latest_event_time: str = None,
        resource_category: int = None,
        resource_list: List[Dict[str, Any]] = None,
        total_resource_count: int = None,
        user_id: str = None,
    ):
        self.activity_id = activity_id
        self.device = device
        self.drive_id = drive_id
        self.event_type = event_type
        self.latest_event_time = latest_event_time
        self.resource_category = resource_category
        self.resource_list = resource_list
        self.total_resource_count = total_resource_count
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['activity_id'] = self.activity_id

        if self.device is not None:
            result['device'] = self.device

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.event_type is not None:
            result['event_type'] = self.event_type

        if self.latest_event_time is not None:
            result['latest_event_time'] = self.latest_event_time

        if self.resource_category is not None:
            result['resource_category'] = self.resource_category

        if self.resource_list is not None:
            result['resource_list'] = self.resource_list

        if self.total_resource_count is not None:
            result['total_resource_count'] = self.total_resource_count

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activity_id') is not None:
            self.activity_id = m.get('activity_id')

        if m.get('device') is not None:
            self.device = m.get('device')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('event_type') is not None:
            self.event_type = m.get('event_type')

        if m.get('latest_event_time') is not None:
            self.latest_event_time = m.get('latest_event_time')

        if m.get('resource_category') is not None:
            self.resource_category = m.get('resource_category')

        if m.get('resource_list') is not None:
            self.resource_list = m.get('resource_list')

        if m.get('total_resource_count') is not None:
            self.total_resource_count = m.get('total_resource_count')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

