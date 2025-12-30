# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAddonTemplateRequest(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        addon_version: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        # The addon name.
        # 
        # This parameter is required.
        self.addon_name = addon_name
        # The addon version.
        # 
        # This parameter is required.
        self.addon_version = addon_version
        # The page number of the page returned. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_name is not None:
            result['AddonName'] = self.addon_name

        if self.addon_version is not None:
            result['AddonVersion'] = self.addon_version

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonName') is not None:
            self.addon_name = m.get('AddonName')

        if m.get('AddonVersion') is not None:
            self.addon_version = m.get('AddonVersion')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

