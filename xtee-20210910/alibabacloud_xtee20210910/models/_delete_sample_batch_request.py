# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSampleBatchRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        ids: str = None,
        reg_id: str = None,
        versions: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # IDs for batch deletion operations.
        self.ids = ids
        # Region code.
        self.reg_id = reg_id
        # List of versions.
        # 
        # This parameter is required.
        self.versions = versions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.ids is not None:
            result['ids'] = self.ids

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.versions is not None:
            result['versions'] = self.versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ids') is not None:
            self.ids = m.get('ids')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('versions') is not None:
            self.versions = m.get('versions')

        return self

