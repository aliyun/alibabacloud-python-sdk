# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class ListApplicationUpdateDynamicsResponseBody(DaraModel):
    def __init__(
        self,
        dynamics: List[main_models.ListApplicationUpdateDynamicsResponseBodyDynamics] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of update records for the application signature library, sorted in descending order of update time.
        self.dynamics = dynamics
        # The current page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of update records that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.dynamics:
            for v1 in self.dynamics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dynamics'] = []
        if self.dynamics is not None:
            for k1 in self.dynamics:
                result['Dynamics'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dynamics = []
        if m.get('Dynamics') is not None:
            for k1 in m.get('Dynamics'):
                temp_model = main_models.ListApplicationUpdateDynamicsResponseBodyDynamics()
                self.dynamics.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApplicationUpdateDynamicsResponseBodyDynamics(DaraModel):
    def __init__(
        self,
        applications: List[main_models.ListApplicationUpdateDynamicsResponseBodyDynamicsApplications] = None,
        dynamic_info: str = None,
        update_time: int = None,
    ):
        # The list of applications added or updated in this update.
        self.applications = applications
        # The update description. The description is returned in Chinese or English based on the Lang parameter.
        self.dynamic_info = dynamic_info
        # The time when the signature library was updated. The value is a UNIX timestamp in seconds.
        self.update_time = update_time

    def validate(self):
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['Applications'].append(k1.to_map() if k1 else None)

        if self.dynamic_info is not None:
            result['DynamicInfo'] = self.dynamic_info

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.ListApplicationUpdateDynamicsResponseBodyDynamicsApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('DynamicInfo') is not None:
            self.dynamic_info = m.get('DynamicInfo')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListApplicationUpdateDynamicsResponseBodyDynamicsApplications(DaraModel):
    def __init__(
        self,
        application_id: int = None,
        application_name: str = None,
    ):
        # The ID of the application in the built-in application signature library.
        self.application_id = application_id
        # The name of the application. The name is returned in Chinese or English based on the Lang parameter.
        self.application_name = application_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        return self

