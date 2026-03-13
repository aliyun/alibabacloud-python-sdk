# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeComponentAssetFormRequest(DaraModel):
    def __init__(
        self,
        component_name: str = None,
        lang: str = None,
    ):
        # The component name.
        # 
        # This parameter is required.
        self.component_name = component_name
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

