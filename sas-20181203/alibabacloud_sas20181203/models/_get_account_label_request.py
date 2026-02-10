# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetAccountLabelRequest(DaraModel):
    def __init__(
        self,
        label_list: List[str] = None,
        lang: str = None,
    ):
        # The tags.
        # 
        # This parameter is required.
        self.label_list = label_list
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_list is not None:
            result['LabelList'] = self.label_list

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelList') is not None:
            self.label_list = m.get('LabelList')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

