# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLiveAIProduceRulesRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        domain: str = None,
        owner_id: int = None,
        region_id: str = None,
        rules_id: str = None,
        suffix_name: str = None,
    ):
        # The name of the application to which the live stream belongs.
        # 
        # This parameter is required.
        self.app = app
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain = domain
        self.owner_id = owner_id
        self.region_id = region_id
        # The ID of the subtitle rule.
        self.rules_id = rules_id
        # The suffix of the subtitle rule.
        # 
        # >  Set the value to the name of the subtitle template.
        self.suffix_name = suffix_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rules_id is not None:
            result['RulesId'] = self.rules_id

        if self.suffix_name is not None:
            result['SuffixName'] = self.suffix_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RulesId') is not None:
            self.rules_id = m.get('RulesId')

        if m.get('SuffixName') is not None:
            self.suffix_name = m.get('SuffixName')

        return self

