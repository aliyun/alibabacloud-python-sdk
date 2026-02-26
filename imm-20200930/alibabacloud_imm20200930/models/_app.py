# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class App(DaraModel):
    def __init__(
        self,
        app_description: str = None,
        app_id: str = None,
        app_key: str = None,
        app_name: str = None,
        app_region: int = None,
        app_type: int = None,
        english_name: str = None,
        owner_id: str = None,
        package_name: str = None,
    ):
        # AppDescription
        self.app_description = app_description
        # AppId
        self.app_id = app_id
        # AppKey
        self.app_key = app_key
        # AppName
        self.app_name = app_name
        # AppRegion
        self.app_region = app_region
        # AppType
        self.app_type = app_type
        # EnglishName
        self.english_name = english_name
        # OwnerId
        self.owner_id = owner_id
        # PackageName
        self.package_name = package_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_description is not None:
            result['AppDescription'] = self.app_description

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_region is not None:
            result['AppRegion'] = self.app_region

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.english_name is not None:
            result['EnglishName'] = self.english_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.package_name is not None:
            result['PackageName'] = self.package_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppRegion') is not None:
            self.app_region = m.get('AppRegion')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('EnglishName') is not None:
            self.english_name = m.get('EnglishName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')

        return self

