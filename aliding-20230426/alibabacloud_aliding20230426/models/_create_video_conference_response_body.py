# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateVideoConferenceResponseBody(DaraModel):
    def __init__(
        self,
        conference_id: str = None,
        conference_password: str = None,
        external_link_url: str = None,
        host_password: str = None,
        phone_numbers: List[str] = None,
        request_id: str = None,
        room_code: str = None,
    ):
        self.conference_id = conference_id
        self.conference_password = conference_password
        self.external_link_url = external_link_url
        self.host_password = host_password
        self.phone_numbers = phone_numbers
        # requestId
        self.request_id = request_id
        self.room_code = room_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conference_id is not None:
            result['conferenceId'] = self.conference_id

        if self.conference_password is not None:
            result['conferencePassword'] = self.conference_password

        if self.external_link_url is not None:
            result['externalLinkUrl'] = self.external_link_url

        if self.host_password is not None:
            result['hostPassword'] = self.host_password

        if self.phone_numbers is not None:
            result['phoneNumbers'] = self.phone_numbers

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.room_code is not None:
            result['roomCode'] = self.room_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conferenceId') is not None:
            self.conference_id = m.get('conferenceId')

        if m.get('conferencePassword') is not None:
            self.conference_password = m.get('conferencePassword')

        if m.get('externalLinkUrl') is not None:
            self.external_link_url = m.get('externalLinkUrl')

        if m.get('hostPassword') is not None:
            self.host_password = m.get('hostPassword')

        if m.get('phoneNumbers') is not None:
            self.phone_numbers = m.get('phoneNumbers')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('roomCode') is not None:
            self.room_code = m.get('roomCode')

        return self

