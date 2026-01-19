# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAnalysisConditionFavoriteRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        condition: str = None,
        event_begin_time: int = None,
        event_code: str = None,
        event_end_time: int = None,
        field_name: str = None,
        field_value: str = None,
        id: int = None,
        name: str = None,
        reg_id: str = None,
        type: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Condition value.
        self.condition = condition
        # Start time, accurate to milliseconds (ms).
        self.event_begin_time = event_begin_time
        # Event code
        self.event_code = event_code
        # End time, accurate to milliseconds (ms).
        self.event_end_time = event_end_time
        # Field name
        self.field_name = field_name
        # Field value
        self.field_value = field_value
        # Primary key ID
        # 
        # This parameter is required.
        self.id = id
        # Condition name
        self.name = name
        # Region code
        # 
        # This parameter is required.
        self.reg_id = reg_id
        # Type, BASIC: Basic query, ADVANCE: Advanced query, BATCH: Batch query
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.condition is not None:
            result['condition'] = self.condition

        if self.event_begin_time is not None:
            result['eventBeginTime'] = self.event_begin_time

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.event_end_time is not None:
            result['eventEndTime'] = self.event_end_time

        if self.field_name is not None:
            result['fieldName'] = self.field_name

        if self.field_value is not None:
            result['fieldValue'] = self.field_value

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('eventBeginTime') is not None:
            self.event_begin_time = m.get('eventBeginTime')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventEndTime') is not None:
            self.event_end_time = m.get('eventEndTime')

        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')

        if m.get('fieldValue') is not None:
            self.field_value = m.get('fieldValue')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

