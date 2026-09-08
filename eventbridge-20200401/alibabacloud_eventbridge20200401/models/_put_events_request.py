# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class PutEventsRequest(DaraModel):
    def __init__(
        self,
        event_bus_name: str = None,
        event_list: List[main_models.PutEventsRequestEventList] = None,
    ):
        # The name of the event bus.
        # 
        # This parameter is required.
        self.event_bus_name = event_bus_name
        # The list of events.
        self.event_list = event_list

    def validate(self):
        if self.event_list:
            for v1 in self.event_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        result['EventList'] = []
        if self.event_list is not None:
            for k1 in self.event_list:
                result['EventList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        self.event_list = []
        if m.get('EventList') is not None:
            for k1 in m.get('EventList'):
                temp_model = main_models.PutEventsRequestEventList()
                self.event_list.append(temp_model.from_map(k1))

        return self

class PutEventsRequestEventList(DaraModel):
    def __init__(
        self,
        data: Any = None,
        data_content_type: str = None,
        data_schema: str = None,
        id: str = None,
        source: str = None,
        spec_version: str = None,
        subject: str = None,
        time: str = None,
        type: str = None,
    ):
        # The event payload.
        self.data = data
        # The data format.
        self.data_content_type = data_content_type
        # The data schema address.
        self.data_schema = data_schema
        # The event ID.
        # 
        # This parameter is required.
        self.id = id
        # The event source.
        # 
        # This parameter is required.
        self.source = source
        # The protocol version.
        self.spec_version = spec_version
        # The event subject.
        self.subject = subject
        # The event time.
        self.time = time
        # The event type.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.data_content_type is not None:
            result['DataContentType'] = self.data_content_type

        if self.data_schema is not None:
            result['DataSchema'] = self.data_schema

        if self.id is not None:
            result['Id'] = self.id

        if self.source is not None:
            result['Source'] = self.source

        if self.spec_version is not None:
            result['SpecVersion'] = self.spec_version

        if self.subject is not None:
            result['Subject'] = self.subject

        if self.time is not None:
            result['Time'] = self.time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('DataContentType') is not None:
            self.data_content_type = m.get('DataContentType')

        if m.get('DataSchema') is not None:
            self.data_schema = m.get('DataSchema')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SpecVersion') is not None:
            self.spec_version = m.get('SpecVersion')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

