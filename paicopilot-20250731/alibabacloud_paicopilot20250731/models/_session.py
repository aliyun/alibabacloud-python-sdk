# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Session(DaraModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        gmt_modified: str = None,
        owner_id: str = None,
        session_id: str = None,
        session_title: str = None,
        user_id: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_create_time = gmt_create_time
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_modified = gmt_modified
        self.owner_id = owner_id
        self.session_id = session_id
        self.session_title = session_title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.session_title is not None:
            result['SessionTitle'] = self.session_title

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SessionTitle') is not None:
            self.session_title = m.get('SessionTitle')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

