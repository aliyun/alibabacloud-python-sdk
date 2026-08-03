# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class DescribeTrailsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        trail_list: List[main_models.DescribeTrailsResponseBodyTrailList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The trails.
        self.trail_list = trail_list

    def validate(self):
        if self.trail_list:
            for v1 in self.trail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TrailList'] = []
        if self.trail_list is not None:
            for k1 in self.trail_list:
                result['TrailList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.trail_list = []
        if m.get('TrailList') is not None:
            for k1 in m.get('TrailList'):
                temp_model = main_models.DescribeTrailsResponseBodyTrailList()
                self.trail_list.append(temp_model.from_map(k1))

        return self

class DescribeTrailsResponseBodyTrailList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        event_rw: str = None,
        home_region: str = None,
        is_organization_trail: bool = None,
        max_compute_project_arn: str = None,
        max_compute_write_role_arn: str = None,
        name: str = None,
        organization_id: str = None,
        oss_bucket_location: str = None,
        oss_bucket_name: str = None,
        oss_key_prefix: str = None,
        oss_write_role_arn: str = None,
        region: str = None,
        sls_project_arn: str = None,
        sls_write_role_arn: str = None,
        start_logging_time: str = None,
        status: str = None,
        stop_logging_time: str = None,
        trail_arn: str = None,
        trail_region: str = None,
        update_time: str = None,
    ):
        # The time when the trail was created.
        self.create_time = create_time
        # The read/write type of the events that are delivered. Valid values:
        # 
        # - Write: write events. This is the default value.
        # 
        # - Read: read events.
        # 
        # - All: read and write events.
        self.event_rw = event_rw
        # The home region of the trail.
        self.home_region = home_region
        # Indicates whether the trail is a multi-account trail. Valid values:
        # 
        # - false (default)
        # 
        # - true
        self.is_organization_trail = is_organization_trail
        # The ARN of the MaxCompute project.
        self.max_compute_project_arn = max_compute_project_arn
        # The ARN of the role that is assumed by ActionTrail to deliver events to the MaxCompute project.
        self.max_compute_write_role_arn = max_compute_write_role_arn
        # The name of the trail.
        self.name = name
        # The ID of the resource directory.
        # 
        # > This parameter is returned only when the trail is a multi-account trail.
        self.organization_id = organization_id
        # The region where the OSS bucket resides.
        self.oss_bucket_location = oss_bucket_location
        # The name of the OSS bucket to which events are delivered.
        self.oss_bucket_name = oss_bucket_name
        # The prefix of the files that are stored in the Object Storage Service (OSS) bucket.
        self.oss_key_prefix = oss_key_prefix
        # The Alibaba Cloud Resource Name (ARN) of the RAM role that is assumed by ActionTrail to deliver events to the OSS bucket.
        self.oss_write_role_arn = oss_write_role_arn
        # The region where the trail resides.
        self.region = region
        # The ARN of the Log Service project to which events are delivered.
        self.sls_project_arn = sls_project_arn
        # The ARN of the RAM role that is assumed by ActionTrail to deliver events to the Log Service project.
        self.sls_write_role_arn = sls_write_role_arn
        # The time when the trail was last enabled.
        self.start_logging_time = start_logging_time
        # The status of the trail. Valid values:
        # 
        # - Disable: disabled.
        # 
        # - Enable: enabled.
        # 
        # - Fresh: The trail is created but is not enabled.
        self.status = status
        # The time when the trail was last disabled.
        self.stop_logging_time = stop_logging_time
        # The ARN of the trail.
        self.trail_arn = trail_arn
        # The region of the trail.
        self.trail_region = trail_region
        # The time when the configurations of the trail were last updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.event_rw is not None:
            result['EventRW'] = self.event_rw

        if self.home_region is not None:
            result['HomeRegion'] = self.home_region

        if self.is_organization_trail is not None:
            result['IsOrganizationTrail'] = self.is_organization_trail

        if self.max_compute_project_arn is not None:
            result['MaxComputeProjectArn'] = self.max_compute_project_arn

        if self.max_compute_write_role_arn is not None:
            result['MaxComputeWriteRoleArn'] = self.max_compute_write_role_arn

        if self.name is not None:
            result['Name'] = self.name

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        if self.oss_bucket_location is not None:
            result['OssBucketLocation'] = self.oss_bucket_location

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_key_prefix is not None:
            result['OssKeyPrefix'] = self.oss_key_prefix

        if self.oss_write_role_arn is not None:
            result['OssWriteRoleArn'] = self.oss_write_role_arn

        if self.region is not None:
            result['Region'] = self.region

        if self.sls_project_arn is not None:
            result['SlsProjectArn'] = self.sls_project_arn

        if self.sls_write_role_arn is not None:
            result['SlsWriteRoleArn'] = self.sls_write_role_arn

        if self.start_logging_time is not None:
            result['StartLoggingTime'] = self.start_logging_time

        if self.status is not None:
            result['Status'] = self.status

        if self.stop_logging_time is not None:
            result['StopLoggingTime'] = self.stop_logging_time

        if self.trail_arn is not None:
            result['TrailArn'] = self.trail_arn

        if self.trail_region is not None:
            result['TrailRegion'] = self.trail_region

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EventRW') is not None:
            self.event_rw = m.get('EventRW')

        if m.get('HomeRegion') is not None:
            self.home_region = m.get('HomeRegion')

        if m.get('IsOrganizationTrail') is not None:
            self.is_organization_trail = m.get('IsOrganizationTrail')

        if m.get('MaxComputeProjectArn') is not None:
            self.max_compute_project_arn = m.get('MaxComputeProjectArn')

        if m.get('MaxComputeWriteRoleArn') is not None:
            self.max_compute_write_role_arn = m.get('MaxComputeWriteRoleArn')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        if m.get('OssBucketLocation') is not None:
            self.oss_bucket_location = m.get('OssBucketLocation')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssKeyPrefix') is not None:
            self.oss_key_prefix = m.get('OssKeyPrefix')

        if m.get('OssWriteRoleArn') is not None:
            self.oss_write_role_arn = m.get('OssWriteRoleArn')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SlsProjectArn') is not None:
            self.sls_project_arn = m.get('SlsProjectArn')

        if m.get('SlsWriteRoleArn') is not None:
            self.sls_write_role_arn = m.get('SlsWriteRoleArn')

        if m.get('StartLoggingTime') is not None:
            self.start_logging_time = m.get('StartLoggingTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StopLoggingTime') is not None:
            self.stop_logging_time = m.get('StopLoggingTime')

        if m.get('TrailArn') is not None:
            self.trail_arn = m.get('TrailArn')

        if m.get('TrailRegion') is not None:
            self.trail_region = m.get('TrailRegion')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

