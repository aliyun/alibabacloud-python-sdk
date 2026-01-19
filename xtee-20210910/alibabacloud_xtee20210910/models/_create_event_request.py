# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEventRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        create_type: str = None,
        event_name: str = None,
        input_fields_str: str = None,
        memo: str = None,
        reg_id: str = None,
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Creation type
        self.create_type = create_type
        # Event name.
        self.event_name = event_name
        # Input parameters, JSON string.
        self.input_fields_str = input_fields_str
        # Memo information
        self.memo = memo
        # Region code
        self.reg_id = reg_id
        # Input field template type
        self.template_code = template_code
        # Published template name.
        self.template_name = template_name
        # Template type.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.create_type is not None:
            result['createType'] = self.create_type

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.input_fields_str is not None:
            result['inputFieldsStr'] = self.input_fields_str

        if self.memo is not None:
            result['memo'] = self.memo

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.template_type is not None:
            result['templateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('createType') is not None:
            self.create_type = m.get('createType')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('inputFieldsStr') is not None:
            self.input_fields_str = m.get('inputFieldsStr')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')

        return self

