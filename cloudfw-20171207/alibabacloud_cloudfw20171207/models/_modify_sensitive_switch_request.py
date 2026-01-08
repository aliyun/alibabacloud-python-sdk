# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySensitiveSwitchRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        sensitive_category: str = None,
        switch_status: str = None,
    ):
        self.lang = lang
        self.sensitive_category = sensitive_category
        self.switch_status = switch_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.sensitive_category is not None:
            result['SensitiveCategory'] = self.sensitive_category

        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SensitiveCategory') is not None:
            self.sensitive_category = m.get('SensitiveCategory')

        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')

        return self

