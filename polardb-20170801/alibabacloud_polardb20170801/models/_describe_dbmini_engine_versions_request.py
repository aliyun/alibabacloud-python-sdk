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
        # The CPU architecture. Valid values:
        # 
        # - **X86**
        # 
        # - **ARM**
        self.architecture = architecture
        # The product series. Valid values:
        # 
        # - **Normal**: Cluster Edition (default)
        # 
        # - **SENormal**: Standard Edition
        # 
        # For more information about product series, see [Product series](https://help.aliyun.com/document_detail/183258.html).
        self.creation_category = creation_category
        # The minor version of the database engine.
        # 
        # - If `DBVersion` is set to **8.0**, valid values are:
        # 
        #   - **8.0.2**
        # 
        #   - **8.0.1**
        # 
        # - If `DBVersion` is set to **5.7**, the valid value is **5.7.28**.
        # 
        # - If `DBVersion` is set to **5.6**, the valid value is **5.6.16**.
        self.dbminor_version = dbminor_version
        # The database type. The only valid value is **MySQL**.
        # 
        # - **MySQL**.
        # 
        # This parameter is required.
        self.dbtype = dbtype
        # The major version of the database engine. Valid values:
        # 
        # - **8.0**
        # 
        # - **5.7**
        # 
        # - **5.6**
        # 
        # This parameter is required.
        self.dbversion = dbversion
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The zone.
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

