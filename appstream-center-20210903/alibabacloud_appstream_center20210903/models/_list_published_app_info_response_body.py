# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210903 import models as main_models
from darabonba.model import DaraModel

class ListPublishedAppInfoResponseBody(DaraModel):
    def __init__(
        self,
        app_models: List[main_models.ListPublishedAppInfoResponseBodyAppModels] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The list of published applications.
        self.app_models = app_models
        # The starting token for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.app_models:
            for v1 in self.app_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppModels'] = []
        if self.app_models is not None:
            for k1 in self.app_models:
                result['AppModels'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_models = []
        if m.get('AppModels') is not None:
            for k1 in m.get('AppModels'):
                temp_model = main_models.ListPublishedAppInfoResponseBodyAppModels()
                self.app_models.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPublishedAppInfoResponseBodyAppModels(DaraModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_id: str = None,
        app_name: str = None,
        app_theme_color: str = None,
        app_version: str = None,
        app_version_name: str = None,
        auth_time: str = None,
        category_id: int = None,
        category_type: int = None,
        icon_url: str = None,
        is_auth: bool = None,
        used_in_session: bool = None,
    ):
        # The application image ID. You can obtain the ID from the Image Management page in the WUYING Cloud App console.
        self.app_center_image_id = app_center_image_id
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The theme color of the application.
        self.app_theme_color = app_theme_color
        # The application version number.
        self.app_version = app_version
        # The application version name.
        self.app_version_name = app_version_name
        # The authorization time of the application.
        # The return value is a serialized datetime string from the server in the format of `EEE MMM dd HH:mm:ss zzz yyyy`, which represents the day of the week, month, day, hour:minute:second, time zone abbreviation, and year in sequence. For example, `Wed Jan 14 20:47:02 CST 2026`, where `CST` is the time zone abbreviation of the server\\"s time zone (China Standard Time, UTC+08:00).
        self.auth_time = auth_time
        # The specific category information of the application, which is the secondary category.
        # Valid values:
        # 
        # - 1: All applications
        # - 2: Design software
        # - 3: Programming and development
        # - 4: Office essentials
        # - 5: Input methods
        # - 6: Image and video
        # - 7: System tools
        # - 8: Browsers
        self.category_id = category_id
        # The primary category of the application. Valid values:
        # 
        # - 0: Cloud application
        # - 1: Cloud game
        self.category_type = category_type
        # The URL of the application icon.
        self.icon_url = icon_url
        # Indicates whether the user has permissions.
        # The value is True.
        self.is_auth = is_auth
        # Indicates whether the application is in use.
        self.used_in_session = used_in_session

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_theme_color is not None:
            result['AppThemeColor'] = self.app_theme_color

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name

        if self.auth_time is not None:
            result['AuthTime'] = self.auth_time

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.is_auth is not None:
            result['IsAuth'] = self.is_auth

        if self.used_in_session is not None:
            result['UsedInSession'] = self.used_in_session

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppThemeColor') is not None:
            self.app_theme_color = m.get('AppThemeColor')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')

        if m.get('AuthTime') is not None:
            self.auth_time = m.get('AuthTime')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('IsAuth') is not None:
            self.is_auth = m.get('IsAuth')

        if m.get('UsedInSession') is not None:
            self.used_in_session = m.get('UsedInSession')

        return self

