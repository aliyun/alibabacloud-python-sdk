# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDiagnosticRequest(DaraModel):
    def __init__(
        self,
        diagnostic_key: str = None,
        diagnostic_type: str = None,
        lang: str = None,
        product: str = None,
    ):
        # The keyword in the diagnosis.
        # 
        # You can specify the ID of the stack that you want to diagnose.
        # 
        # This parameter is required.
        self.diagnostic_key = diagnostic_key
        # The type of the item that is diagnosed. Set the value to Stack, which specifies that the stack is diagnosed.
        self.diagnostic_type = diagnostic_type
        # The language of the diagnostic report to be generated. Only Chinese and English are supported.
        # 
        # Valid values:
        # 
        # *   zh-cn
        # *   en
        self.lang = lang
        # The name of the product that is diagonosed.
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnostic_key is not None:
            result['DiagnosticKey'] = self.diagnostic_key

        if self.diagnostic_type is not None:
            result['DiagnosticType'] = self.diagnostic_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.product is not None:
            result['Product'] = self.product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnosticKey') is not None:
            self.diagnostic_key = m.get('DiagnosticKey')

        if m.get('DiagnosticType') is not None:
            self.diagnostic_type = m.get('DiagnosticType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        return self

