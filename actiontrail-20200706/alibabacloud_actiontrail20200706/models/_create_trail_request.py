# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTrailRequest(DaraModel):
    def __init__(
        self,
        event_rw: str = None,
        is_organization_trail: bool = None,
        max_compute_project_arn: str = None,
        max_compute_write_role_arn: str = None,
        name: str = None,
        oss_bucket_name: str = None,
        oss_key_prefix: str = None,
        oss_write_role_arn: str = None,
        sls_project_arn: str = None,
        sls_write_role_arn: str = None,
        trail_region: str = None,
    ):
        # Specifies the read/write type of events that the trail delivers. Valid values:
        # 
        # - Write: Write events.
        # 
        # - Read: Read events.
        # 
        # - All (default): All read and write events.
        self.event_rw = event_rw
        # Specifies whether the trail is a multi-account trail. Valid values:
        # 
        # - true
        # 
        # - false (default)
        # 
        # To create a trail for an organization, set this parameter to `true`. The trail will collect events from all member accounts in the organization.
        self.is_organization_trail = is_organization_trail
        # The ARN of the MaxCompute project to which ActionTrail delivers events.
        # 
        # > You must specify a destination for the trail by providing at least one of the following parameters: `OssBucketName`, `SlsProjectArn`, or `MaxComputeProjectArn`.
        # 
        # > The project name in the ARN must start with `actiontrail_`.
        self.max_compute_project_arn = max_compute_project_arn
        # The ARN of the RAM role that ActionTrail assumes to deliver events to the MaxCompute project.
        # 
        # - If this parameter is not specified, ActionTrail creates a service-linked role to deliver events. For more information, see [ActionTrail service-linked role](https://help.aliyun.com/document_detail/169244.html).
        # 
        # - If you specify a role, it must be a RAM role that you created. This role must have a trust policy that allows the ActionTrail service (\\`actiontrail.aliyuncs.com\\`) to assume it. The role\\"s permission policy must grant permissions to write to the specified MaxCompute project. For more information about cross-account delivery, see [Deliver events from multiple Alibaba Cloud accounts to the same account](https://help.aliyun.com/document_detail/207462.html).
        self.max_compute_write_role_arn = max_compute_write_role_arn
        # The name of the trail.
        # 
        # > - Length: 6 to 36 characters.
        # >
        # > - Characters: Lowercase letters, digits, hyphens (-), and underscores (_).
        # >
        # > - Must start with a lowercase letter.
        # >
        # > - Must be uniquewithin an Alibaba Cloud account.
        # 
        # This parameter is required.
        self.name = name
        # The name of the OSS bucket to which ActionTrail delivers events.
        # 
        # - Length: 3 to 63 characters.
        # 
        # - Characters: Lowercase letters, digits, and hyphens (-).
        # 
        # - Must start with a lowercase letter or a digit.
        # 
        # > You must specify a destination for the trail by providing at least one of the following parameters: `OssBucketName`, `SlsProjectArn`, or `MaxComputeProjectArn`.
        self.oss_bucket_name = oss_bucket_name
        # The prefix for the names of log files that ActionTrail delivers to your OSS bucket.
        # 
        # - Length: 6 to 32 characters.
        # 
        # - Characters: Letters, digits, hyphens (-), forward slashes (/), and underscores (_).
        # 
        # - Must start with a letter.
        self.oss_key_prefix = oss_key_prefix
        # The Alibaba Cloud Resource Name (ARN) of the RAM role that ActionTrail assumes to deliver events to the OSS bucket.
        # 
        # - If you do not specify this parameter, ActionTrail creates a service-linked role to deliver events. For more information, see [ActionTrail service-linked role](https://help.aliyun.com/document_detail/169244.html).
        # 
        # - If you specify a role, it must be a RAM role that you created. This role must have a trust policy that allows the ActionTrail service (actiontrail.aliyuncs.com) to assume it. The role\\"s RAM policy must grant permissions to write to the specified OSS bucket. For more information about cross-account delivery, see [Deliver events from multiple Alibaba Cloud accounts to the same account](https://help.aliyun.com/document_detail/207462.html).
        self.oss_write_role_arn = oss_write_role_arn
        # The ARN of the SLS project to which ActionTrail delivers events.
        # 
        # > You must specify a destination for the trail by providing at least one of the following parameters: `OssBucketName`, `SlsProjectArn`, or `MaxComputeProjectArn`.
        self.sls_project_arn = sls_project_arn
        # The ARN of the RAM role that ActionTrail assumes to deliver events to the SLS project.
        # 
        # - If this parameter is not specified, ActionTrail creates a service-linked role to deliver events. For more information, see [ActionTrail service-linked role](https://help.aliyun.com/document_detail/169244.html).
        # 
        # - If you specify a role, it must be a RAM role that you created. This role must have a trust policy that allows the ActionTrail service (actiontrail.aliyuncs.com) to assume it. The role\\"s permission policy must grant permissions to write to the specified SLS project. For more information about cross-account delivery, see [Deliver events from multiple Alibaba Cloud accounts to the same account](https://help.aliyun.com/document_detail/207462.html).
        self.sls_write_role_arn = sls_write_role_arn
        # The region in which the trail is created. By default, a trail is created in all regions and this parameter is set to `All`. To create a trail in a specific region, provide the region ID. For more information about regions, call the [DescribeRegions](https://help.aliyun.com/document_detail/213597.html) operation.
        self.trail_region = trail_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_rw is not None:
            result['EventRW'] = self.event_rw

        if self.is_organization_trail is not None:
            result['IsOrganizationTrail'] = self.is_organization_trail

        if self.max_compute_project_arn is not None:
            result['MaxComputeProjectArn'] = self.max_compute_project_arn

        if self.max_compute_write_role_arn is not None:
            result['MaxComputeWriteRoleArn'] = self.max_compute_write_role_arn

        if self.name is not None:
            result['Name'] = self.name

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_key_prefix is not None:
            result['OssKeyPrefix'] = self.oss_key_prefix

        if self.oss_write_role_arn is not None:
            result['OssWriteRoleArn'] = self.oss_write_role_arn

        if self.sls_project_arn is not None:
            result['SlsProjectArn'] = self.sls_project_arn

        if self.sls_write_role_arn is not None:
            result['SlsWriteRoleArn'] = self.sls_write_role_arn

        if self.trail_region is not None:
            result['TrailRegion'] = self.trail_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventRW') is not None:
            self.event_rw = m.get('EventRW')

        if m.get('IsOrganizationTrail') is not None:
            self.is_organization_trail = m.get('IsOrganizationTrail')

        if m.get('MaxComputeProjectArn') is not None:
            self.max_compute_project_arn = m.get('MaxComputeProjectArn')

        if m.get('MaxComputeWriteRoleArn') is not None:
            self.max_compute_write_role_arn = m.get('MaxComputeWriteRoleArn')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssKeyPrefix') is not None:
            self.oss_key_prefix = m.get('OssKeyPrefix')

        if m.get('OssWriteRoleArn') is not None:
            self.oss_write_role_arn = m.get('OssWriteRoleArn')

        if m.get('SlsProjectArn') is not None:
            self.sls_project_arn = m.get('SlsProjectArn')

        if m.get('SlsWriteRoleArn') is not None:
            self.sls_write_role_arn = m.get('SlsWriteRoleArn')

        if m.get('TrailRegion') is not None:
            self.trail_region = m.get('TrailRegion')

        return self

