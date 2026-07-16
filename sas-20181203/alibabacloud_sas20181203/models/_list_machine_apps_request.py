# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMachineAppsRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_region_id: str = None,
        auth_version: str = None,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        resource_directory_uid: int = None,
    ):
        # The SAE application ID.
        self.app_id = app_id
        # The SAE application name.
        self.app_name = app_name
        # The region ID.
        self.app_region_id = app_region_id
        # The authorization version of the asset. Valid values:
        # - **6**: Anti-virus Edition
        # - **5**: Premium Edition
        # - **3**: Enterprise Edition
        # - **7**: Ultimate Edition
        # - **10**: value-added service Edition.
        self.auth_version = auth_version
        # The page number of the current page in a paging query.
        self.current_page = current_page
        # The language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries per page in a paging query.
        self.page_size = page_size
        # The UID of the resource directory.
        self.resource_directory_uid = resource_directory_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_region_id is not None:
            result['AppRegionId'] = self.app_region_id

        if self.auth_version is not None:
            result['AuthVersion'] = self.auth_version

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_directory_uid is not None:
            result['ResourceDirectoryUid'] = self.resource_directory_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppRegionId') is not None:
            self.app_region_id = m.get('AppRegionId')

        if m.get('AuthVersion') is not None:
            self.auth_version = m.get('AuthVersion')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceDirectoryUid') is not None:
            self.resource_directory_uid = m.get('ResourceDirectoryUid')

        return self

