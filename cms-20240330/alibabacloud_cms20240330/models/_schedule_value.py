# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScheduleValue(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        end: str = None,
        start: str = None,
        contact_name: str = None,
    ):
        # The ID of the on-call contact.
        self.contact_id = contact_id
        # The end time. Format: yyyy-MM-dd HH:mm:ss.
        self.end = end
        # The start time. Format: yyyy-MM-dd HH:mm:ss.
        self.start = start
        # The name of the on-call contact.
        self.contact_name = contact_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['contactId'] = self.contact_id

        if self.end is not None:
            result['end'] = self.end

        if self.start is not None:
            result['start'] = self.start

        if self.contact_name is not None:
            result['contactName'] = self.contact_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactId') is not None:
            self.contact_id = m.get('contactId')

        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('start') is not None:
            self.start = m.get('start')

        if m.get('contactName') is not None:
            self.contact_name = m.get('contactName')

        return self

