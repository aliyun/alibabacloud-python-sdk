# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCustomLineRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        line_id: int = None,
    ):
        # The language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The unique ID of the custom line.<props="china"> Call [DescribeCustomLines](https://help.aliyun.com/en/dns/api-alidns-2015-01-09-describecustomlines?spm=a2c4g.11186623.help-menu-search-29697.d_0) to obtain this ID.
        # <props="intl">Call [DescribeCustomLines](https://www.alibabacloud.com/help/en/dns/api-alidns-2015-01-09-describecustomlines?spm=a2c63.p38356.help-menu-search-29697.d_0) to obtain this ID.
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

