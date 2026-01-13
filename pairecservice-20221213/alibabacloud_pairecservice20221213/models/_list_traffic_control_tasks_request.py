# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTrafficControlTasksRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        control_target_filter: str = None,
        environment: str = None,
        instance_id: str = None,
        name: str = None,
        order: str = None,
        page_number: str = None,
        page_size: str = None,
        scene_id: str = None,
        sort_by: str = None,
        status: str = None,
        traffic_control_task_id: str = None,
        version: str = None,
    ):
        self.all = all
        self.control_target_filter = control_target_filter
        self.environment = environment
        self.instance_id = instance_id
        self.name = name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.scene_id = scene_id
        self.sort_by = sort_by
        self.status = status
        self.traffic_control_task_id = traffic_control_task_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.control_target_filter is not None:
            result['ControlTargetFilter'] = self.control_target_filter

        if self.environment is not None:
            result['Environment'] = self.environment

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.status is not None:
            result['Status'] = self.status

        if self.traffic_control_task_id is not None:
            result['TrafficControlTaskId'] = self.traffic_control_task_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('ControlTargetFilter') is not None:
            self.control_target_filter = m.get('ControlTargetFilter')

        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TrafficControlTaskId') is not None:
            self.traffic_control_task_id = m.get('TrafficControlTaskId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

