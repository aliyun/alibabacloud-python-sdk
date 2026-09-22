# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListPublishedAppsResponseBody(DaraModel):
    def __init__(
        self,
        apps: List[main_models.ListPublishedAppsResponseBodyApps] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of application records on the current page. Each record corresponds to a deployed application in a published delivery group. The list is sorted by the creation time of the delivery group in descending order. An empty list is returned if no results match or the requested page exceeds the result range.
        self.apps = apps
        # The page number specified in this request.
        self.page_number = page_number
        # The number of records per page specified in this request. This value does not represent the actual number of records returned on the current page. The actual number may be less than this value.
        self.page_size = page_size
        # The request ID. You can use this ID to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of records that match all filter conditions. Records are counted on a per-delivery-group-plus-application basis. If the same application appears in multiple published delivery groups, each combination is counted separately. This value does not represent the number of records returned on the current page. The value is `0` if no results match.
        self.total_count = total_count

    def validate(self):
        if self.apps:
            for v1 in self.apps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Apps'] = []
        if self.apps is not None:
            for k1 in self.apps:
                result['Apps'].append(k1.to_map() if k1 else None)

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
        self.apps = []
        if m.get('Apps') is not None:
            for k1 in m.get('Apps'):
                temp_model = main_models.ListPublishedAppsResponseBodyApps()
                self.apps.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPublishedAppsResponseBodyApps(DaraModel):
    def __init__(
        self,
        app_icon: str = None,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        app_name: str = None,
        app_version: str = None,
        app_version_name: str = None,
        authorized_user_count: int = None,
    ):
        # The URL of the application icon.
        self.app_icon = app_icon
        # The application ID. Pass this value together with `AppInstanceGroupId` when you invoke the [AuthorizeUsersForApp](~~AuthorizeUsersForApp~~) operation to authorize users for this application.
        self.app_id = app_id
        # The ID of the published delivery group to which this application belongs.
        self.app_instance_group_id = app_instance_group_id
        # The name of the published delivery group to which this application belongs.
        self.app_instance_group_name = app_instance_group_name
        # The application name.
        self.app_name = app_name
        # The application version number.
        self.app_version = app_version
        # The application version name, which is the name assigned to this version when the application was published.
        self.app_version_name = app_version_name
        # The number of users authorized by application for this application within its delivery group. Only users authorized through [AuthorizeUsersForApp](~~AuthorizeUsersForApp~~) by application are counted. The value is `0` if no users have been authorized by application.
        self.authorized_user_count = authorized_user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_icon is not None:
            result['AppIcon'] = self.app_icon

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name

        if self.authorized_user_count is not None:
            result['AuthorizedUserCount'] = self.authorized_user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIcon') is not None:
            self.app_icon = m.get('AppIcon')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')

        if m.get('AuthorizedUserCount') is not None:
            self.authorized_user_count = m.get('AuthorizedUserCount')

        return self

