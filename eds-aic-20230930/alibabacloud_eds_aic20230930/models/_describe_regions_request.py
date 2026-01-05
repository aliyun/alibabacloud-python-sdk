# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRegionsRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        sale_mode: str = None,
    ):
        # The display language of the console. Valid values:
        # 
        # *   cn: Simplified Chinese
        # *   en: English
        self.accept_language = accept_language
        # The sales mode.
        # 
        # Valid values:
        # 
        # *   Instance: the instance group mode. [Default]
        # *   Node: the matrix mode. [Whitelist required]
        self.sale_mode = sale_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')

        return self

