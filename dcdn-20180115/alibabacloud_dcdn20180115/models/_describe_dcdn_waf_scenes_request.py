# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnWafScenesRequest(DaraModel):
    def __init__(
        self,
        defense_scenes: str = None,
    ):
        # The types of the protection policies that you want to query. Separate multiple types with commas (,). Valid values:
        # 
        # *   waf_group: basic web protection
        # *   custom_acl: custom protection
        # *   whitelist: IP address whitelist
        # *   ip_blacklist: IP address blacklist
        # *   region_block: region blacklist
        # *   bot: bot management
        # 
        # > If you do not set this parameter, all types of protection policies are queried.
        self.defense_scenes = defense_scenes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_scenes is not None:
            result['DefenseScenes'] = self.defense_scenes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScenes') is not None:
            self.defense_scenes = m.get('DefenseScenes')

        return self

