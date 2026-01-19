# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustVariableRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        condition: str = None,
        create_type: str = None,
        description: str = None,
        event_codes: str = None,
        history_value_type: str = None,
        object: str = None,
        outputs: str = None,
        reg_id: str = None,
        subject: str = None,
        time_type: str = None,
        title: str = None,
        tw_count: int = None,
        velocity_fc: str = None,
        velocity_tw: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Condition value.
        self.condition = condition
        # Creation type
        self.create_type = create_type
        # Description information.
        self.description = description
        # Event code
        # 
        # This parameter is required.
        self.event_codes = event_codes
        # Value type
        self.history_value_type = history_value_type
        # Accumulative object
        self.object = object
        # Variable return type
        self.outputs = outputs
        # Region code
        self.reg_id = reg_id
        # Primary object
        # 
        # This parameter is required.
        self.subject = subject
        # Time slice type
        # 
        # This parameter is required.
        self.time_type = time_type
        # Title.
        # 
        # This parameter is required.
        self.title = title
        # Number of time units
        self.tw_count = tw_count
        # Variable type
        # 
        # This parameter is required.
        self.velocity_fc = velocity_fc
        # Time slice unit
        # 
        # This parameter is required.
        self.velocity_tw = velocity_tw

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

        if self.create_type is not None:
            result['createType'] = self.create_type

        if self.description is not None:
            result['description'] = self.description

        if self.event_codes is not None:
            result['eventCodes'] = self.event_codes

        if self.history_value_type is not None:
            result['historyValueType'] = self.history_value_type

        if self.object is not None:
            result['object'] = self.object

        if self.outputs is not None:
            result['outputs'] = self.outputs

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.subject is not None:
            result['subject'] = self.subject

        if self.time_type is not None:
            result['timeType'] = self.time_type

        if self.title is not None:
            result['title'] = self.title

        if self.tw_count is not None:
            result['twCount'] = self.tw_count

        if self.velocity_fc is not None:
            result['velocityFC'] = self.velocity_fc

        if self.velocity_tw is not None:
            result['velocityTW'] = self.velocity_tw

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('createType') is not None:
            self.create_type = m.get('createType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('eventCodes') is not None:
            self.event_codes = m.get('eventCodes')

        if m.get('historyValueType') is not None:
            self.history_value_type = m.get('historyValueType')

        if m.get('object') is not None:
            self.object = m.get('object')

        if m.get('outputs') is not None:
            self.outputs = m.get('outputs')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        if m.get('timeType') is not None:
            self.time_type = m.get('timeType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('twCount') is not None:
            self.tw_count = m.get('twCount')

        if m.get('velocityFC') is not None:
            self.velocity_fc = m.get('velocityFC')

        if m.get('velocityTW') is not None:
            self.velocity_tw = m.get('velocityTW')

        return self

