# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class ListAliyunOfficialEventSourcesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListAliyunOfficialEventSourcesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For a list of error codes, see Error codes.
        self.code = code
        # The data returned.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. If the operation is successful, the value true is returned.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListAliyunOfficialEventSourcesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAliyunOfficialEventSourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        event_source_list: List[main_models.ListAliyunOfficialEventSourcesResponseBodyDataEventSourceList] = None,
    ):
        # The event sources.
        self.event_source_list = event_source_list

    def validate(self):
        if self.event_source_list:
            for v1 in self.event_source_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventSourceList'] = []
        if self.event_source_list is not None:
            for k1 in self.event_source_list:
                result['EventSourceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_source_list = []
        if m.get('EventSourceList') is not None:
            for k1 in m.get('EventSourceList'):
                temp_model = main_models.ListAliyunOfficialEventSourcesResponseBodyDataEventSourceList()
                self.event_source_list.append(temp_model.from_map(k1))

        return self

class ListAliyunOfficialEventSourcesResponseBodyDataEventSourceList(DaraModel):
    def __init__(
        self,
        arn: str = None,
        ctime: float = None,
        description: str = None,
        event_bus_name: str = None,
        event_types: List[main_models.ListAliyunOfficialEventSourcesResponseBodyDataEventSourceListEventTypes] = None,
        full_name: str = None,
        name: str = None,
        status: str = None,
        type: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the event bus.
        self.arn = arn
        # The time when the event source was created. Unit: milliseconds.
        self.ctime = ctime
        # The description of the event source.
        self.description = description
        # The name of the event source to which the event type belongs.
        self.event_bus_name = event_bus_name
        # The event types.
        self.event_types = event_types
        # The full name of the event source.
        self.full_name = full_name
        # The name of the event source.
        self.name = name
        # The status of the event source. Valid value: Activated.
        self.status = status
        # The type of the event source.
        self.type = type

    def validate(self):
        if self.event_types:
            for v1 in self.event_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.ctime is not None:
            result['Ctime'] = self.ctime

        if self.description is not None:
            result['Description'] = self.description

        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        result['EventTypes'] = []
        if self.event_types is not None:
            for k1 in self.event_types:
                result['EventTypes'].append(k1.to_map() if k1 else None)

        if self.full_name is not None:
            result['FullName'] = self.full_name

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        self.event_types = []
        if m.get('EventTypes') is not None:
            for k1 in m.get('EventTypes'):
                temp_model = main_models.ListAliyunOfficialEventSourcesResponseBodyDataEventSourceListEventTypes()
                self.event_types.append(temp_model.from_map(k1))

        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListAliyunOfficialEventSourcesResponseBodyDataEventSourceListEventTypes(DaraModel):
    def __init__(
        self,
        event_source_name: str = None,
        group_name: str = None,
        name: str = None,
        short_name: str = None,
    ):
        # The name of the event source.
        self.event_source_name = event_source_name
        # The name of the group to which the event type belongs.
        self.group_name = group_name
        # The full name of the event type.
        self.name = name
        # The short name of the event type.
        self.short_name = short_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.name is not None:
            result['Name'] = self.name

        if self.short_name is not None:
            result['ShortName'] = self.short_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ShortName') is not None:
            self.short_name = m.get('ShortName')

        return self

