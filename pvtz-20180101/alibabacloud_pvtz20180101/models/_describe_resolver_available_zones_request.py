# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeResolverAvailableZonesRequest(DaraModel):
    def __init__(
        self,
        az_id: str = None,
        lang: str = None,
        resolver_region_id: str = None,
    ):
        # The zone ID.
        self.az_id = az_id
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The region ID.
        # 
        # This parameter is required.
        self.resolver_region_id = resolver_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.az_id is not None:
            result['AzId'] = self.az_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.resolver_region_id is not None:
            result['ResolverRegionId'] = self.resolver_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AzId') is not None:
            self.az_id = m.get('AzId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ResolverRegionId') is not None:
            self.resolver_region_id = m.get('ResolverRegionId')

        return self

