# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBMiniEngineVersionsRequest(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        creation_category: str = None,
        dbminor_version: str = None,
        dbtype: str = None,
        dbversion: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.architecture = architecture
        self.creation_category = creation_category
        self.dbminor_version = dbminor_version
        # This parameter is required.
        self.dbtype = dbtype
        # This parameter is required.
        self.dbversion = dbversion
        # This parameter is required.
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.creation_category is not None:
            result['CreationCategory'] = self.creation_category

        if self.dbminor_version is not None:
            result['DBMinorVersion'] = self.dbminor_version

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('CreationCategory') is not None:
            self.creation_category = m.get('CreationCategory')

        if m.get('DBMinorVersion') is not None:
            self.dbminor_version = m.get('DBMinorVersion')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

