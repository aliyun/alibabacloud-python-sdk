# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAICoachTaskSessionHistoryRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        session_id: str = None,
        uid: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.session_id = session_id
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.uid is not None:
            result['uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        return self

