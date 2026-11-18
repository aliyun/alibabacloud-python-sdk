# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class ListApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        applications: List[main_models.ListApplicationsResponseBodyApplications] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of applications. In the Chinese environment, the applications are sorted in descending order of group name and ascending order of application level.
        self.applications = applications
        # The current page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of applications that meet the filter conditions.
        self.total_count = total_count

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
        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.ListApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

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
        application_id: int = None,
        application_name: str = None,
        category_id: int = None,
        category_name: str = None,
        default_action: str = None,
        description: str = None,
        group_name: str = None,
        level: int = None,
        protocol: List[str] = None,
        requirements: List[str] = None,
        risk: str = None,
        technology: str = None,
        updated_time: int = None,
        vendor: str = None,
    ):
        # The application ID in the built-in application signature library.
        self.application_id = application_id
        # The application name. The name is returned in Chinese or English based on the Lang parameter.
        self.application_name = application_name
        # The application category ID.
        self.category_id = category_id
        # The application category name. The name is returned in Chinese or English based on the Lang parameter.
        self.category_name = category_name
        # The default action for the application in the built-in application library. The value is fixed as Alert (Monitor).
        self.default_action = default_action
        # The application description. The description is returned in Chinese or English based on the Lang parameter.
        self.description = description
        # The application group name.
        self.group_name = group_name
        # The level value of the application. The value is obtained from the built-in application signature library and used for list sorting.
        self.level = level
        # The list of protocols used by the application.
        self.protocol = protocol
        # The list of detection prerequisites for the application.
        self.requirements = requirements
        # The risk level. Valid values:
        # - **Information**: Informational.
        # - **Low**: Low.
        # - **Medium**: Medium.
        # - **High**: High.
        # - **Critical**: Critical.
        self.risk = risk
        # The technology type name. The name is returned in Chinese or English based on the Lang parameter.
        self.technology = technology
        # The last update time of the application information. The value is a UNIX timestamp in seconds.
        self.updated_time = updated_time
        # The application vendor name. The name is returned in Chinese or English based on the Lang parameter.
        self.vendor = vendor

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

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.default_action is not None:
            result['DefaultAction'] = self.default_action

        if self.description is not None:
            result['Description'] = self.description

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.level is not None:
            result['Level'] = self.level

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.requirements is not None:
            result['Requirements'] = self.requirements

        if self.risk is not None:
            result['Risk'] = self.risk

        if self.technology is not None:
            result['Technology'] = self.technology

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('DefaultAction') is not None:
            self.default_action = m.get('DefaultAction')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Requirements') is not None:
            self.requirements = m.get('Requirements')

        if m.get('Risk') is not None:
            self.risk = m.get('Risk')

        if m.get('Technology') is not None:
            self.technology = m.get('Technology')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

