# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCustomLineInfoRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        line_id: str = None,
    ):
        # The language of the response.
        self.lang = lang
        # The unique ID of the custom line.
        # 
        # This parameter is required.
        self.line_id = line_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.line_id is not None:
            result['LineId'] = self.line_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')

        return self

