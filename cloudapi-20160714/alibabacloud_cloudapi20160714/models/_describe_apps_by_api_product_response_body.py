# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeAppsByApiProductResponseBody(DaraModel):
    def __init__(
        self,
        authorized_apps: main_models.DescribeAppsByApiProductResponseBodyAuthorizedApps = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about authorized applications.
        self.authorized_apps = authorized_apps
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.authorized_apps:
            self.authorized_apps.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorized_apps is not None:
            result['AuthorizedApps'] = self.authorized_apps.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedApps') is not None:
            temp_model = main_models.DescribeAppsByApiProductResponseBodyAuthorizedApps()
            self.authorized_apps = temp_model.from_map(m.get('AuthorizedApps'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAppsByApiProductResponseBodyAuthorizedApps(DaraModel):
    def __init__(
        self,
        authorized_app: List[main_models.DescribeAppsByApiProductResponseBodyAuthorizedAppsAuthorizedApp] = None,
    ):
        self.authorized_app = authorized_app

    def validate(self):
        if self.authorized_app:
            for v1 in self.authorized_app:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthorizedApp'] = []
        if self.authorized_app is not None:
            for k1 in self.authorized_app:
                result['AuthorizedApp'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorized_app = []
        if m.get('AuthorizedApp') is not None:
            for k1 in m.get('AuthorizedApp'):
                temp_model = main_models.DescribeAppsByApiProductResponseBodyAuthorizedAppsAuthorizedApp()
                self.authorized_app.append(temp_model.from_map(k1))

        return self

class DescribeAppsByApiProductResponseBodyAuthorizedAppsAuthorizedApp(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        auth_valid_time: str = None,
        authorized_time: str = None,
        description: str = None,
        extend: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The expiration time of the authorization. The time is in GMT. An empty value indicates that the authorization does not expire.
        self.auth_valid_time = auth_valid_time
        # The time when the authorization was created. The time is in GMT.
        self.authorized_time = authorized_time
        # The authorization description.
        self.description = description
        # The extended information.
        self.extend = extend

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

        if self.auth_valid_time is not None:
            result['AuthValidTime'] = self.auth_valid_time

        if self.authorized_time is not None:
            result['AuthorizedTime'] = self.authorized_time

        if self.description is not None:
            result['Description'] = self.description

        if self.extend is not None:
            result['Extend'] = self.extend

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AuthValidTime') is not None:
            self.auth_valid_time = m.get('AuthValidTime')

        if m.get('AuthorizedTime') is not None:
            self.authorized_time = m.get('AuthorizedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        return self

