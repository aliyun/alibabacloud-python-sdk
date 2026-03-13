# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IntlFlightSegmentAvailableCertRequest(DaraModel):
    def __init__(
        self,
        isv_name: str = None,
        language: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.isv_name = isv_name
        self.language = language
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.language is not None:
            result['language'] = self.language

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

