# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListPublishedAppInstanceGroupResponseBody(DaraModel):
    def __init__(
        self,
        app_instance_group_models: List[main_models.ListPublishedAppInstanceGroupResponseBodyAppInstanceGroupModels] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of published delivery groups on the current page, sorted by creation time from newest to oldest. An empty list is returned if no results match or if the requested page exceeds the result range.
        self.app_instance_group_models = app_instance_group_models
        # The page number specified in this request.
        self.page_number = page_number
        # The number of delivery groups per page specified in the request. Unit: delivery groups. This value does not represent the actual number of delivery groups returned on the current page. The actual number on the current page may be less than this value.
        self.page_size = page_size
        # The request ID. You can use this ID to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of delivery groups that match all filter conditions. Unit: delivery groups. This value is not the number of delivery groups returned on the current page. Each delivery group is counted only once. The value is `0` if no results match.
        self.total_count = total_count

    def validate(self):
        if self.app_instance_group_models:
            for v1 in self.app_instance_group_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppInstanceGroupModels'] = []
        if self.app_instance_group_models is not None:
            for k1 in self.app_instance_group_models:
                result['AppInstanceGroupModels'].append(k1.to_map() if k1 else None)

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
        self.app_instance_group_models = []
        if m.get('AppInstanceGroupModels') is not None:
            for k1 in m.get('AppInstanceGroupModels'):
                temp_model = main_models.ListPublishedAppInstanceGroupResponseBodyAppInstanceGroupModels()
                self.app_instance_group_models.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPublishedAppInstanceGroupResponseBodyAppInstanceGroupModels(DaraModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        app_instance_type: str = None,
        apps: List[main_models.ListPublishedAppInstanceGroupResponseBodyAppInstanceGroupModelsApps] = None,
        expired_time: str = None,
        gmt_create: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # The application image ID.
        self.app_center_image_id = app_center_image_id
        # The delivery group ID.
        self.app_instance_group_id = app_instance_group_id
        # The delivery group name.
        self.app_instance_group_name = app_instance_group_name
        # The delivery group specification type.
        self.app_instance_type = app_instance_type
        # The list of deployed applications in the delivery group image. The `AppId` and `AppName` parameters in the request only determine whether a delivery group is included in the results. They do not trim this list to only the matched applications.
        self.apps = apps
        # The expiration time of the delivery group. For delivery groups sold as resources, this is the resource expiration time. For other delivery groups, this is the delivery group expiration time. The value is in ISO 8601 format with milliseconds and a time zone offset. The returned time zone offset is +00:00. Format: yyyy-MM-ddTHH:mm:ss.SSS+HH:mm.
        self.expired_time = expired_time
        # The creation time of the delivery group. The value is in ISO 8601 format with milliseconds and a time zone offset. The returned time zone offset is +00:00. Format: yyyy-MM-ddTHH:mm:ss.SSS+HH:mm.
        self.gmt_create = gmt_create
        # The region ID of the delivery group.
        self.region_id = region_id
        # The delivery group status. This operation returns delivery groups only in the following status:
        # 
        # - `PUBLISHED`: Published and listed. The delivery group can appear in the query results of this operation. This status does not indicate that a specified user has been granted access permissions.
        self.status = status

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
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name

        if self.app_instance_type is not None:
            result['AppInstanceType'] = self.app_instance_type

        result['Apps'] = []
        if self.apps is not None:
            for k1 in self.apps:
                result['Apps'].append(k1.to_map() if k1 else None)

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        if m.get('AppInstanceType') is not None:
            self.app_instance_type = m.get('AppInstanceType')

        self.apps = []
        if m.get('Apps') is not None:
            for k1 in m.get('Apps'):
                temp_model = main_models.ListPublishedAppInstanceGroupResponseBodyAppInstanceGroupModelsApps()
                self.apps.append(temp_model.from_map(k1))

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListPublishedAppInstanceGroupResponseBodyAppInstanceGroupModelsApps(DaraModel):
    def __init__(
        self,
        app_icon: str = None,
        app_id: str = None,
        app_name: str = None,
        app_version: str = None,
        app_version_name: str = None,
    ):
        # The application icon.
        self.app_icon = app_icon
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The application version.
        self.app_version = app_version
        # The application version name.
        self.app_version_name = app_version_name

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

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIcon') is not None:
            self.app_icon = m.get('AppIcon')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')

        return self

