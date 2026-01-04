# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class ListApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        applications: main_models.ListApplicationsResponseBodyApplications = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about applications.
        self.applications = applications
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.applications:
            self.applications.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()

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
        if m.get('Applications') is not None:
            temp_model = main_models.ListApplicationsResponseBodyApplications()
            self.applications = temp_model.from_map(m.get('Applications'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApplicationsResponseBodyApplications(DaraModel):
    def __init__(
        self,
        application: List[main_models.ListApplicationsResponseBodyApplicationsApplication] = None,
    ):
        self.application = application

    def validate(self):
        if self.application:
            for v1 in self.application:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Application'] = []
        if self.application is not None:
            for k1 in self.application:
                result['Application'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application = []
        if m.get('Application') is not None:
            for k1 in m.get('Application'):
                temp_model = main_models.ListApplicationsResponseBodyApplicationsApplication()
                self.application.append(temp_model.from_map(k1))

        return self

class ListApplicationsResponseBodyApplicationsApplication(DaraModel):
    def __init__(
        self,
        app_list: main_models.ListApplicationsResponseBodyApplicationsApplicationAppList = None,
        cluster_name: str = None,
    ):
        # Details about the application.
        self.app_list = app_list
        # The name of the cluster.
        self.cluster_name = cluster_name

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

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppList') is not None:
            temp_model = main_models.ListApplicationsResponseBodyApplicationsApplicationAppList()
            self.app_list = temp_model.from_map(m.get('AppList'))

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        return self

class ListApplicationsResponseBodyApplicationsApplicationAppList(DaraModel):
    def __init__(
        self,
        app: List[main_models.ListApplicationsResponseBodyApplicationsApplicationAppListApp] = None,
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
                temp_model = main_models.ListApplicationsResponseBodyApplicationsApplicationAppListApp()
                self.app.append(temp_model.from_map(k1))

        return self

class ListApplicationsResponseBodyApplicationsApplicationAppListApp(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_info: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The information about the application, such as the resource specification, parameter configuration, and resources.
        self.app_info = app_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_info is not None:
            result['AppInfo'] = self.app_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppInfo') is not None:
            self.app_info = m.get('AppInfo')

        return self

