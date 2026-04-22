# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIntranetUserCanAnalysisVpcsRequest(DaraModel):
    def __init__(
        self,
        network_type: str = None,
        page_number: int = None,
        page_size: int = None,
        query_tree_level: int = None,
        region_id: str = None,
        vpc_owner: int = None,
        vpc_type: str = None,
    ):
        self.network_type = network_type
        self.page_number = page_number
        self.page_size = page_size
        self.query_tree_level = query_tree_level
        self.region_id = region_id
        self.vpc_owner = vpc_owner
        self.vpc_type = vpc_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_tree_level is not None:
            result['QueryTreeLevel'] = self.query_tree_level

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpc_owner is not None:
            result['VpcOwner'] = self.vpc_owner

        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryTreeLevel') is not None:
            self.query_tree_level = m.get('QueryTreeLevel')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpcOwner') is not None:
            self.vpc_owner = m.get('VpcOwner')

        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')

        return self

