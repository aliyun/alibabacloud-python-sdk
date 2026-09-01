# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFieldRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        query_key: str = None,
    ):
        # The language of the request and response messages. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The key of the global configuration. Valid value:
        # 
        # - **soar_filed_tags**: Obtains the input field template for a playbook.
        # 
        # This parameter is required.
        self.query_key = query_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.query_key is not None:
            result['QueryKey'] = self.query_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('QueryKey') is not None:
            self.query_key = m.get('QueryKey')

        return self

