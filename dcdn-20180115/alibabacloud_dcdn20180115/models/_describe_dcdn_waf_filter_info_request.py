# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnWafFilterInfoRequest(DaraModel):
    def __init__(
        self,
        defense_scenes: str = None,
        language: str = None,
    ):
        # The type of the protection policy. Separate multiple types with commas (,). Valid values:
        # 
        # *   waf_group: basic web protection
        # *   custom_acl: custom protection
        # *   whitelist: IP address whitelist
        # 
        # >If you do not specify this parameter, all types are returned.
        self.defense_scenes = defense_scenes
        # The language of the returned information. Valid values:
        # 
        # *   en: English
        # *   cn: Simplified Chinese
        # 
        # This parameter is required.
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_scenes is not None:
            result['DefenseScenes'] = self.defense_scenes

        if self.language is not None:
            result['Language'] = self.language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScenes') is not None:
            self.defense_scenes = m.get('DefenseScenes')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        return self

