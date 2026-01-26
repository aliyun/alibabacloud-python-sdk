# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListEnvironmentDashboardsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListEnvironmentDashboardsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The result of the operation.
        self.data = data
        # The returned message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListEnvironmentDashboardsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListEnvironmentDashboardsResponseBodyData(DaraModel):
    def __init__(
        self,
        dashboards: List[main_models.ListEnvironmentDashboardsResponseBodyDataDashboards] = None,
        total: int = None,
    ):
        # The dashboards.
        self.dashboards = dashboards
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.dashboards:
            for v1 in self.dashboards:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dashboards'] = []
        if self.dashboards is not None:
            for k1 in self.dashboards:
                result['Dashboards'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dashboards = []
        if m.get('Dashboards') is not None:
            for k1 in m.get('Dashboards'):
                temp_model = main_models.ListEnvironmentDashboardsResponseBodyDataDashboards()
                self.dashboards.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListEnvironmentDashboardsResponseBodyDataDashboards(DaraModel):
    def __init__(
        self,
        folder_uid: str = None,
        region: str = None,
        tags: List[str] = None,
        title: str = None,
        uid: str = None,
        url: str = None,
    ):
        # The UID of the folder.
        self.folder_uid = folder_uid
        # The region ID.
        self.region = region
        # The keyword.
        self.tags = tags
        # The title of the Grafana dashboard.
        self.title = title
        # The unique identifier of the dashboard.
        self.uid = uid
        # The complete URL of the dashboard.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_uid is not None:
            result['FolderUid'] = self.folder_uid

        if self.region is not None:
            result['Region'] = self.region

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderUid') is not None:
            self.folder_uid = m.get('FolderUid')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

