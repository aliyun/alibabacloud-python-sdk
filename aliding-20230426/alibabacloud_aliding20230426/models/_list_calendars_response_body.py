# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class ListCalendarsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        response: main_models.ListCalendarsResponseBodyResponse = None,
    ):
        # requestId
        self.request_id = request_id
        self.response = response

    def validate(self):
        if self.response:
            self.response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.response is not None:
            result['response'] = self.response.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('response') is not None:
            temp_model = main_models.ListCalendarsResponseBodyResponse()
            self.response = temp_model.from_map(m.get('response'))

        return self

class ListCalendarsResponseBodyResponse(DaraModel):
    def __init__(
        self,
        calendars: List[main_models.ListCalendarsResponseBodyResponseCalendars] = None,
    ):
        self.calendars = calendars

    def validate(self):
        if self.calendars:
            for v1 in self.calendars:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Calendars'] = []
        if self.calendars is not None:
            for k1 in self.calendars:
                result['Calendars'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.calendars = []
        if m.get('Calendars') is not None:
            for k1 in m.get('Calendars'):
                temp_model = main_models.ListCalendarsResponseBodyResponseCalendars()
                self.calendars.append(temp_model.from_map(k1))

        return self

class ListCalendarsResponseBodyResponseCalendars(DaraModel):
    def __init__(
        self,
        description: str = None,
        etag: str = None,
        id: str = None,
        privilege: str = None,
        summary: str = None,
        time_zone: str = None,
        type: str = None,
    ):
        self.description = description
        self.etag = etag
        self.id = id
        self.privilege = privilege
        self.summary = summary
        self.time_zone = time_zone
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.etag is not None:
            result['ETag'] = self.etag

        if self.id is not None:
            result['Id'] = self.id

        if self.privilege is not None:
            result['Privilege'] = self.privilege

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ETag') is not None:
            self.etag = m.get('ETag')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Privilege') is not None:
            self.privilege = m.get('Privilege')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

