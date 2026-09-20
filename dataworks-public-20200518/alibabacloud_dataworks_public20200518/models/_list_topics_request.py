# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTopicsRequest(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        instance_id: int = None,
        node_id: int = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        topic_statuses: str = None,
        topic_types: str = None,
    ):
        # The start time for discovery. Specify the time in UTC format (yyyy-MM-dd\\"T\\"HH:mm:ssZ).
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The end time for discovery. Specify the time in UTC format (yyyy-MM-dd\\"T\\"HH:mm:ssZ).
        # 
        # This parameter is required.
        self.end_time = end_time
        # The instance ID associated with the event. This parameter is mutually exclusive with NodeId.
        self.instance_id = instance_id
        # The ID of the node associated with the event. This parameter is mutually exclusive with InstanceId.
        self.node_id = node_id
        # The Alibaba Cloud UID of the event owner.
        self.owner = owner
        # The page number. Default value: 1. Minimum value: 1. Maximum value: 30.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The status of the event. Valid values: IGNORE (ignored), NEW (newly discovered), FIXING (being processed), and RECOVER (recovered). Separate multiple event statuses with commas (,).
        self.topic_statuses = topic_statuses
        # The type of the event. Valid values: SLOW (slow) and ERROR (error). Separate multiple event types with commas (,).
        self.topic_types = topic_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.topic_statuses is not None:
            result['TopicStatuses'] = self.topic_statuses

        if self.topic_types is not None:
            result['TopicTypes'] = self.topic_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TopicStatuses') is not None:
            self.topic_statuses = m.get('TopicStatuses')

        if m.get('TopicTypes') is not None:
            self.topic_types = m.get('TopicTypes')

        return self

