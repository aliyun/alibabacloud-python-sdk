# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAppKeyStateRequest(DaraModel):
    def __init__(
        self,
        app_key_id: str = None,
        lang: str = None,
        state: str = None,
    ):
        self.app_key_id = app_key_id
        self.lang = lang
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key_id is not None:
            result['AppKeyId'] = self.app_key_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKeyId') is not None:
            self.app_key_id = m.get('AppKeyId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

