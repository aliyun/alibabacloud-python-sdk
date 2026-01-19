# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeAppsResponseBody(DaraModel):
    def __init__(
        self,
        apps: main_models.DescribeAppsResponseBodyApps = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned app information. It is an array consisting of AppItem data.
        self.apps = apps
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.apps:
            self.apps.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apps is not None:
            result['Apps'] = self.apps.to_map()

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
        if m.get('Apps') is not None:
            temp_model = main_models.DescribeAppsResponseBodyApps()
            self.apps = temp_model.from_map(m.get('Apps'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAppsResponseBodyApps(DaraModel):
    def __init__(
        self,
        app_item: List[main_models.DescribeAppsResponseBodyAppsAppItem] = None,
    ):
        self.app_item = app_item

    def validate(self):
        if self.app_item:
            for v1 in self.app_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppItem'] = []
        if self.app_item is not None:
            for k1 in self.app_item:
                result['AppItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_item = []
        if m.get('AppItem') is not None:
            for k1 in m.get('AppItem'):
                temp_model = main_models.DescribeAppsResponseBodyAppsAppItem()
                self.app_item.append(temp_model.from_map(k1))

        return self

class DescribeAppsResponseBodyAppsAppItem(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        description: str = None,
    ):
        # The ID of the app.
        self.app_id = app_id
        # The name of the app.
        self.app_name = app_name
        # The description of the app.
        self.description = description

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

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

