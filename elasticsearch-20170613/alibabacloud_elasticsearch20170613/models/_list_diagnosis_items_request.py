# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDiagnosisItemsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        level: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The supported request language. Default value: the browser request language. Valid values:
        # 
        # - en: English
        # - zh: Simplified Chinese
        # - zt: Traditional Chinese
        # - es: Spanish
        # - fr: French
        self.lang = lang
        # The diagnostic item level. Valid values:
        # 
        # - BASIC: basic inspection item (free).
        # - ADVANCED: advanced inspection item (consumes billable tokens).
        # 
        # If this parameter is not specified, diagnostic items of all levels are returned.
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.lang is not None:
            result['lang'] = self.lang

        if self.level is not None:
            result['level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('level') is not None:
            self.level = m.get('level')

        return self

