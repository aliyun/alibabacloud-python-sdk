# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLogstoreStorageRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        lang: str = None,
    ):
        # The identifier of the request source. Set this parameter to **sas**.
        # 
        # This parameter is required.
        self.from_ = from_
        # The language type of the request and response messages. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

