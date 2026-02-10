# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddSasModuleTrialRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        module_code: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The code of the feature. Valid values:
        # 
        # *   **vulFix**: vulnerability fixing.
        # *   **cloudSiem**: threat analysis and response.
        self.module_code = module_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        return self

