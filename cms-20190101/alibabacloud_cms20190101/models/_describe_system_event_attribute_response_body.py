# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeSystemEventAttributeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        system_events: main_models.DescribeSystemEventAttributeResponseBodySystemEvents = None,
    ):
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, `success` is returned. If the call fails, an error message is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values: True: The call is successful. false: The call fails.
        self.success = success
        # The details of the event.
        self.system_events = system_events

    def validate(self):
        if self.system_events:
            self.system_events.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.system_events is not None:
            result['SystemEvents'] = self.system_events.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('SystemEvents') is not None:
            temp_model = main_models.DescribeSystemEventAttributeResponseBodySystemEvents()
            self.system_events = temp_model.from_map(m.get('SystemEvents'))

        return self

class DescribeSystemEventAttributeResponseBodySystemEvents(DaraModel):
    def __init__(
        self,
        system_event: List[main_models.DescribeSystemEventAttributeResponseBodySystemEventsSystemEvent] = None,
    ):
        self.system_event = system_event

    def validate(self):
        if self.system_event:
            for v1 in self.system_event:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SystemEvent'] = []
        if self.system_event is not None:
            for k1 in self.system_event:
                result['SystemEvent'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_event = []
        if m.get('SystemEvent') is not None:
            for k1 in m.get('SystemEvent'):
                temp_model = main_models.DescribeSystemEventAttributeResponseBodySystemEventsSystemEvent()
                self.system_event.append(temp_model.from_map(k1))

        return self

class DescribeSystemEventAttributeResponseBodySystemEventsSystemEvent(DaraModel):
    def __init__(
        self,
        content: str = None,
        group_id: str = None,
        id: str = None,
        instance_name: str = None,
        level: str = None,
        name: str = None,
        product: str = None,
        region_id: str = None,
        resource_id: str = None,
        status: str = None,
        time: int = None,
    ):
        # The details of the event.
        self.content = content
        # The ID of the application group.
        self.group_id = group_id
        # The event ID.
        self.id = id
        # The instance name.
        self.instance_name = instance_name
        # The level of the event. Valid values:
        # 
        # *   CRITICAL
        # *   WARN
        # *   INFO
        self.level = level
        # The event name.
        self.name = name
        # The abbreviation of the service name.
        self.product = product
        # The region ID.
        self.region_id = region_id
        # The resource ID.
        self.resource_id = resource_id
        # The status of the event.
        self.status = status
        # The time when the event occurred. The value is a timestamp.
        # 
        # Unit: milliseconds.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.level is not None:
            result['Level'] = self.level

        if self.name is not None:
            result['Name'] = self.name

        if self.product is not None:
            result['Product'] = self.product

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.status is not None:
            result['Status'] = self.status

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

