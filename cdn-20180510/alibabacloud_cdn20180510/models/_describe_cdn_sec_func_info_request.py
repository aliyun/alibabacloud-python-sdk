# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCdnSecFuncInfoRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        sec_func_type: str = None,
    ):
        # The language.
        # 
        # *   en: English
        # *   zh: Chinese
        # 
        # This parameter is required.
        self.lang = lang
        # The type of the security feature. Valid values:
        # 
        # *   CipherSuiteGroupCustomize: custom cipher suite.
        # *   CipherSuiteGroupStrict: dustom cipher suite.
        # 
        # This parameter is required.
        self.sec_func_type = sec_func_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.sec_func_type is not None:
            result['SecFuncType'] = self.sec_func_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SecFuncType') is not None:
            self.sec_func_type = m.get('SecFuncType')

        return self

