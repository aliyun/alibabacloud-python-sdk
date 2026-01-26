# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRumAppShrinkRequest(DaraModel):
    def __init__(
        self,
        app_group: str = None,
        app_name: str = None,
        description: str = None,
        language: str = None,
        nick_name: str = None,
        package_name: str = None,
        real_region_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        site_type: str = None,
        source: str = None,
        tag_shrink: str = None,
    ):
        # The name of the application group.
        self.app_group = app_group
        # The application name.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The description of the application.
        self.description = description
        # The language used by the client.
        self.language = language
        # The nickname of the application.
        self.nick_name = nick_name
        # The name of the Android application package. This parameter is required if you create an Android application.
        self.package_name = package_name
        # The region where the application resides. You can leave this parameter empty or set it to China East 2 Finance.
        self.real_region_id = real_region_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The application type. Valid values: web, miniapp, ios, and android.
        # 
        # This parameter is required.
        self.site_type = site_type
        # The source. This is a reserved parameter.
        self.source = source
        # The list of tags. You can specify a maximum of 20 tags.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_group is not None:
            result['AppGroup'] = self.app_group

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.description is not None:
            result['Description'] = self.description

        if self.language is not None:
            result['Language'] = self.language

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.package_name is not None:
            result['PackageName'] = self.package_name

        if self.real_region_id is not None:
            result['RealRegionId'] = self.real_region_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.site_type is not None:
            result['SiteType'] = self.site_type

        if self.source is not None:
            result['Source'] = self.source

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGroup') is not None:
            self.app_group = m.get('AppGroup')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')

        if m.get('RealRegionId') is not None:
            self.real_region_id = m.get('RealRegionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SiteType') is not None:
            self.site_type = m.get('SiteType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

