# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VodPackagingGroup(DaraModel):
    def __init__(
        self,
        approximate_asset_count: int = None,
        configuration_count: int = None,
        create_time: str = None,
        description: str = None,
        domain_name: str = None,
        group_name: str = None,
    ):
        self.approximate_asset_count = approximate_asset_count
        self.configuration_count = configuration_count
        self.create_time = create_time
        self.description = description
        self.domain_name = domain_name
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approximate_asset_count is not None:
            result['ApproximateAssetCount'] = self.approximate_asset_count

        if self.configuration_count is not None:
            result['ConfigurationCount'] = self.configuration_count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproximateAssetCount') is not None:
            self.approximate_asset_count = m.get('ApproximateAssetCount')

        if m.get('ConfigurationCount') is not None:
            self.configuration_count = m.get('ConfigurationCount')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

