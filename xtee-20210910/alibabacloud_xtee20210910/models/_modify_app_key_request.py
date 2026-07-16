# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAppKeyRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        app_key: str = None,
        memo: str = None,
        reg_id: str = None,
    ):
        # Specifies the language type of the request and response messages. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The AppKey information.
        self.app_key = app_key
        # The memo information of the application.
        self.memo = memo
        # The region ID.
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

        if self.app_key is not None:
            result['appKey'] = self.app_key

        if self.memo is not None:
            result['memo'] = self.memo

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('appKey') is not None:
            self.app_key = m.get('appKey')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

