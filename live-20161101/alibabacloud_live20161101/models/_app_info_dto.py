# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class AppInfoDTO(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: int = None,
        creation_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        item_id: str = None,
        modification_time: str = None,
        platforms: List[main_models.AppInfoDTOPlatforms] = None,
        user_id: int = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.creation_time = creation_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.item_id = item_id
        self.modification_time = modification_time
        self.platforms = platforms
        self.user_id = user_id

    def validate(self):
        if self.platforms:
            for v1 in self.platforms:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        result['Platforms'] = []
        if self.platforms is not None:
            for k1 in self.platforms:
                result['Platforms'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        self.platforms = []
        if m.get('Platforms') is not None:
            for k1 in m.get('Platforms'):
                temp_model = main_models.AppInfoDTOPlatforms()
                self.platforms.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self



class AppInfoDTOPlatforms(DaraModel):
    def __init__(
        self,
        item_id: str = None,
        license_item_ids: List[str] = None,
        pkg_name: str = None,
        pkg_signature: str = None,
        platform_type: int = None,
        type: int = None,
    ):
        self.item_id = item_id
        self.license_item_ids = license_item_ids
        self.pkg_name = pkg_name
        self.pkg_signature = pkg_signature
        self.platform_type = platform_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.license_item_ids is not None:
            result['LicenseItemIds'] = self.license_item_ids

        if self.pkg_name is not None:
            result['PkgName'] = self.pkg_name

        if self.pkg_signature is not None:
            result['PkgSignature'] = self.pkg_signature

        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('LicenseItemIds') is not None:
            self.license_item_ids = m.get('LicenseItemIds')

        if m.get('PkgName') is not None:
            self.pkg_name = m.get('PkgName')

        if m.get('PkgSignature') is not None:
            self.pkg_signature = m.get('PkgSignature')

        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

