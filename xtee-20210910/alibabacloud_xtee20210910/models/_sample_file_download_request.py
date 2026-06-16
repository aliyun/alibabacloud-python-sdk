# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SampleFileDownloadRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        reg_id: str = None,
        tab: str = None,
    ):
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The region ID.
        self.reg_id = reg_id
        # The scenario.
        self.tab = tab

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        if self.tab is not None:
            result['Tab'] = self.tab

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        return self

