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
        load_all: bool = None,
    ):
        # Specifies whether to filter regions based on assets for which auditing is enabled. Valid values: true: Auditing is enabled. false: Auditing is not enabled. If you do not specify this parameter, this condition is not used.
        self.audited = audited
        # Specifies whether to filter regions based on assets for which detection is enabled. Valid values: true: Detection is enabled. false: Detection is not enabled. If you do not specify this parameter, this condition is not used.
        self.identified = identified
        # The language of the response. Valid values: zh: Chinese. en: English.
        self.lang = lang
        # Specifies whether to retrieve all regions.
        self.load_all = load_all

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

        if self.load_all is not None:
            result['LoadAll'] = self.load_all

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audited') is not None:
            self.audited = m.get('Audited')

        if m.get('Identified') is not None:
            self.identified = m.get('Identified')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LoadAll') is not None:
            self.load_all = m.get('LoadAll')

        return self

