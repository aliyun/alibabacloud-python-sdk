# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTrailsRequest(DaraModel):
    def __init__(
        self,
        include_organization_trail: bool = None,
        include_shadow_trails: bool = None,
        name_list: str = None,
    ):
        # Specifies whether to query the information about multi-account trails. Valid values:
        # 
        # - true
        # 
        # - false (default)
        self.include_organization_trail = include_organization_trail
        # Specifies whether to return the information about shadow trails. Valid values:
        # 
        # - false: Do not return the information about shadow trails. It is the default value.
        # 
        # - true: Return the information about shadow trails.
        self.include_shadow_trails = include_shadow_trails
        # The names of the trails whose information you want to query. Separate multiple trail names with commas (,).
        self.name_list = name_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_organization_trail is not None:
            result['IncludeOrganizationTrail'] = self.include_organization_trail

        if self.include_shadow_trails is not None:
            result['IncludeShadowTrails'] = self.include_shadow_trails

        if self.name_list is not None:
            result['NameList'] = self.name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeOrganizationTrail') is not None:
            self.include_organization_trail = m.get('IncludeOrganizationTrail')

        if m.get('IncludeShadowTrails') is not None:
            self.include_shadow_trails = m.get('IncludeShadowTrails')

        if m.get('NameList') is not None:
            self.name_list = m.get('NameList')

        return self

