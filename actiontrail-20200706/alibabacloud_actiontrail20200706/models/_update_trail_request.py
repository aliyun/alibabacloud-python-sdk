# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTrailRequest(DaraModel):
    def __init__(
        self,
        event_rw: str = None,
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
        # The read/write type of the events to be delivered. Valid values:
        # 
        # - Write: write events. It is the default value.
        # 
        # - Read: read events.
        # 
        # - All: read and write events.
        self.event_rw = event_rw
        # The ARN of the MaxCompute project to which you want to deliver events.
        # 
        # > The name of the MaxCompute project must be prefixed with actiontrail_.
        self.max_compute_project_arn = max_compute_project_arn
        # The ARN of the role that is assumed by ActionTrail to deliver events to the destination Simple Log Service project.
        # 
        # - If you do not specify this parameter, ActionTrail creates a service-linked role to create the required resources. For more information, see [Manage the service-linked role](https://help.aliyun.com/document_detail/169244.html).
        # 
        # - If you specify this parameter and deliver events to the current account, you must grant the RAM role the permissions on the service-linked role for ActionTrail. If you want to deliver events to other accounts, you must attach a system policy to the RAM role. For more information about how to deliver events across Alibaba Cloud accounts, see [Deliver events across Alibaba Cloud accounts](https://help.aliyun.com/document_detail/207462.html).
        self.max_compute_write_role_arn = max_compute_write_role_arn
        # The name of the trail whose configurations you want to update.
        # 
        # The name must be 6 to 36 characters in length and can contain lowercase letters, digits, hyphens (-), and underscores (_). It must start with a lowercase letter.
        # 
        # > The name must be unique within an Alibaba Cloud account.
        # 
        # This parameter is required.
        self.name = name
        # The name of the Object Storage Service (OSS) bucket to which you want to deliver events.
        # 
        # The name must be 3 to 63 characters in length. The name must start with a lowercase letter or a digit and can contain lowercase letters, digits, and hyphens (-).
        # 
        # > Make sure that the bucket exists before you update the configuration of the trail.
        self.oss_bucket_name = oss_bucket_name
        # The prefix of the files that are stored in the OSS bucket.
        # 
        # The prefix must be 6 to 32 characters in length. The prefix must start with a letter and can contain letters, digits, hyphens (-), forward slashes (/), and underscores (_).
        self.oss_key_prefix = oss_key_prefix
        # The Alibaba Cloud Resource Name (ARN) of the RAM role that is assumed by ActionTrail to deliver events to the OSS bucket.
        # 
        # - If you do not specify this parameter, ActionTrail creates a service-linked role to create the required resources. For more information, see [Manage the service-linked role](https://help.aliyun.com/document_detail/169244.html).
        # 
        # - If you specify this parameter, you must grant the permissions of the service-linked role that is assumed by ActionTrail to the RAM role before you can deliver events to your Alibaba Cloud account. If you need to deliver events to other Alibaba Cloud accounts, you must attach the permission policy that is used to grant permissions related to event delivery to the RAM role. For more information about how to deliver events across Alibaba Cloud accounts, see [Deliver events across Alibaba Cloud accounts](https://help.aliyun.com/document_detail/207462.html).
        self.oss_write_role_arn = oss_write_role_arn
        # The ARN of the Log Service project to which you want to deliver events.
        self.sls_project_arn = sls_project_arn
        # The ARN of the RAM role that is assumed by ActionTrail to deliver events to the Log Service project.
        # 
        # - If you do not specify this parameter, ActionTrail creates a service-linked role to create the corresponding resource. For more information, see [Manage the service-linked role](https://help.aliyun.com/document_detail/169244.html).
        # 
        # - If you specify this parameter, you must grant the permissions of the service-linked role that is assumed by ActionTrail to the RAM role before you can deliver events to your Alibaba Cloud account. If you need to deliver events to other Alibaba Cloud accounts, you must attach the permission policy that is used to grant permissions related to event delivery to the RAM role. For more information about how to deliver events across Alibaba Cloud accounts, see [Deliver events across Alibaba Cloud accounts](https://help.aliyun.com/document_detail/207462.html).
        self.sls_write_role_arn = sls_write_role_arn
        # The region of the trail.
        # 
        # - The default value is All, which indicates that the trail delivers events from all regions.
        # 
        # You can also specify specific regions. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/213597.html) operation to query all the supported regions.
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

