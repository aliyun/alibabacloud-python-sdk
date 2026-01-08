# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePageDocumentsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        page_name: str = None,
        source_code: str = None,
        source_ip: str = None,
        tab_name: str = None,
    ):
        self.lang = lang
        # This parameter is required.
        self.page_name = page_name
        # This parameter is required.
        self.source_code = source_code
        self.source_ip = source_ip
        # This parameter is required.
        self.tab_name = tab_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_name is not None:
            result['PageName'] = self.page_name

        if self.source_code is not None:
            result['SourceCode'] = self.source_code

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.tab_name is not None:
            result['TabName'] = self.tab_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageName') is not None:
            self.page_name = m.get('PageName')

        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('TabName') is not None:
            self.tab_name = m.get('TabName')

        return self

