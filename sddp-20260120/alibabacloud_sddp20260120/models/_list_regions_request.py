# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRegionsRequest(DaraModel):
    def __init__(
        self,
        audited: bool = None,
        identified: bool = None,
        lang: str = None,
    ):
        # Specifies whether to filter regions by assets that have audit enabled. A value of true indicates that audit is enabled. A value of false indicates that audit is not enabled. If you do not specify this parameter, this filter condition is not applied.
        self.audited = audited
        # Specifies whether to filter regions by assets that have detection enabled. A value of true indicates that detection is enabled. A value of false indicates that detection is not enabled. If you do not specify this parameter, this filter condition is not applied.
        self.identified = identified
        # The language of the response description. Valid values:
        # 
        # - zh: Chinese.
        # - en: English.
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audited is not None:
            result['Audited'] = self.audited

        if self.identified is not None:
            result['Identified'] = self.identified

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audited') is not None:
            self.audited = m.get('Audited')

        if m.get('Identified') is not None:
            self.identified = m.get('Identified')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

