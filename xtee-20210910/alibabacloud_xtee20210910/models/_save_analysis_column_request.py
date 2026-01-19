# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveAnalysisColumnRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        columns: str = None,
        reg_id: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Custom columns
        # 
        # This parameter is required.
        self.columns = columns
        # Region code
        # 
        # This parameter is required.
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

        if self.columns is not None:
            result['columns'] = self.columns

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('columns') is not None:
            self.columns = m.get('columns')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

