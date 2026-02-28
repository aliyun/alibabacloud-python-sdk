# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeAppsResponseBody(DaraModel):
    def __init__(
        self,
        app_list: main_models.DescribeAppsResponseBodyAppList = None,
        request_id: str = None,
        total_num: int = None,
        total_page: int = None,
    ):
        self.app_list = app_list
        self.request_id = request_id
        self.total_num = total_num
        self.total_page = total_page

    def validate(self):
        if self.app_list:
            self.app_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_list is not None:
            result['AppList'] = self.app_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppList') is not None:
            temp_model = main_models.DescribeAppsResponseBodyAppList()
            self.app_list = temp_model.from_map(m.get('AppList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeAppsResponseBodyAppList(DaraModel):
    def __init__(
        self,
        app: List[main_models.DescribeAppsResponseBodyAppListApp] = None,
    ):
        self.app = app

    def validate(self):
        if self.app:
            for v1 in self.app:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['App'] = []
        if self.app is not None:
            for k1 in self.app:
                result['App'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app = []
        if m.get('App') is not None:
            for k1 in m.get('App'):
                temp_model = main_models.DescribeAppsResponseBodyAppListApp()
                self.app.append(temp_model.from_map(k1))

        return self

class DescribeAppsResponseBodyAppListApp(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        bill_type: str = None,
        create_time: str = None,
        service_areas: main_models.DescribeAppsResponseBodyAppListAppServiceAreas = None,
        status: int = None,
        version: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_type = app_type
        self.bill_type = bill_type
        self.create_time = create_time
        self.service_areas = service_areas
        self.status = status
        self.version = version

    def validate(self):
        if self.service_areas:
            self.service_areas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.bill_type is not None:
            result['BillType'] = self.bill_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.service_areas is not None:
            result['ServiceAreas'] = self.service_areas.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ServiceAreas') is not None:
            temp_model = main_models.DescribeAppsResponseBodyAppListAppServiceAreas()
            self.service_areas = temp_model.from_map(m.get('ServiceAreas'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeAppsResponseBodyAppListAppServiceAreas(DaraModel):
    def __init__(
        self,
        service_area: List[str] = None,
    ):
        self.service_area = service_area

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_area is not None:
            result['ServiceArea'] = self.service_area

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')

        return self

