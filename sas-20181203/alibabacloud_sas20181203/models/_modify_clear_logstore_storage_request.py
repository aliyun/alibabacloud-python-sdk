# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyClearLogstoreStorageRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        lang: str = None,
        user_log_store: str = None,
        user_project: str = None,
    ):
        # The ID of the request source. Set the value to **sas**.
        self.from_ = from_
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English.
        self.lang = lang
        # The name of the Logstore that stores logs.
        self.user_log_store = user_log_store
        # The name of the project.
        self.user_project = user_project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_log_store is not None:
            result['UserLogStore'] = self.user_log_store

        if self.user_project is not None:
            result['UserProject'] = self.user_project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserLogStore') is not None:
            self.user_log_store = m.get('UserLogStore')

        if m.get('UserProject') is not None:
            self.user_project = m.get('UserProject')

        return self

