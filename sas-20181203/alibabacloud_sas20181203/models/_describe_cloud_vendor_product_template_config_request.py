# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudVendorProductTemplateConfigRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        vendor: str = None,
    ):
        # Set the language type for request and response messages, default is **zh**. Values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Cloud asset vendor. Values:
        # - **CHAITIN**: Chaitin Technology
        # - **FORTINET**: Fortinet
        # - **THREATBOOK**: ThreatBook
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

