# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAnalysisExportTaskRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        columns: str = None,
        conditions: str = None,
        event_begin_time: int = None,
        event_codes: str = None,
        event_end_time: int = None,
        field_name: str = None,
        field_value: str = None,
        file_format: str = None,
        reg_id: str = None,
        scope: str = None,
        type: str = None,
    ):
        # Sets the language type for the request and response messages, with a default value of **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Custom columns
        self.columns = columns
        # Query expression
        self.conditions = conditions
        # Start time, accurate to milliseconds (ms).
        # 
        # This parameter is required.
        self.event_begin_time = event_begin_time
        # Event code.
        # 
        # This parameter is required.
        self.event_codes = event_codes
        # End time, accurate to milliseconds (ms).
        # 
        # This parameter is required.
        self.event_end_time = event_end_time
        # Field name
        self.field_name = field_name
        # Field value
        self.field_value = field_value
        # File format, Excel, CSV
        # 
        # This parameter is required.
        self.file_format = file_format
        # Region code
        # 
        # This parameter is required.
        self.reg_id = reg_id
        # Export scope: ALL: All, SELECT: Selected rows
        # 
        # This parameter is required.
        self.scope = scope
        # Type, BASIC: Basic query, ADVANCE: Advanced query, BATCH: Batch query
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
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.columns is not None:
            result['columns'] = self.columns

        if self.conditions is not None:
            result['conditions'] = self.conditions

        if self.event_begin_time is not None:
            result['eventBeginTime'] = self.event_begin_time

        if self.event_codes is not None:
            result['eventCodes'] = self.event_codes

        if self.event_end_time is not None:
            result['eventEndTime'] = self.event_end_time

        if self.field_name is not None:
            result['fieldName'] = self.field_name

        if self.field_value is not None:
            result['fieldValue'] = self.field_value

        if self.file_format is not None:
            result['fileFormat'] = self.file_format

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.scope is not None:
            result['scope'] = self.scope

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('columns') is not None:
            self.columns = m.get('columns')

        if m.get('conditions') is not None:
            self.conditions = m.get('conditions')

        if m.get('eventBeginTime') is not None:
            self.event_begin_time = m.get('eventBeginTime')

        if m.get('eventCodes') is not None:
            self.event_codes = m.get('eventCodes')

        if m.get('eventEndTime') is not None:
            self.event_end_time = m.get('eventEndTime')

        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')

        if m.get('fieldValue') is not None:
            self.field_value = m.get('fieldValue')

        if m.get('fileFormat') is not None:
            self.file_format = m.get('fileFormat')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

