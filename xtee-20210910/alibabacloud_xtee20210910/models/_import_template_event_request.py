# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportTemplateEventRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        event_template_ids: str = None,
        reg_id: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The template ID of the event.
        self.event_template_ids = event_template_ids
        # Region code
        self.reg_id = reg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.event_template_ids is not None:
            result['eventTemplateIds'] = self.event_template_ids

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('eventTemplateIds') is not None:
            self.event_template_ids = m.get('eventTemplateIds')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

