# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTrailResponseBody(DaraModel):
    def __init__(
        self,
        event_rw: str = None,
        home_region: str = None,
        max_compute_project_arn: str = None,
        max_compute_write_role_arn: str = None,
        name: str = None,
        oss_bucket_name: str = None,
        oss_key_prefix: str = None,
        oss_write_role_arn: str = None,
        request_id: str = None,
        sls_project_arn: str = None,
        sls_write_role_arn: str = None,
        trail_region: str = None,
    ):
        # The read/write type of the events to be delivered.
        self.event_rw = event_rw
        # The home region of the trail.
        self.home_region = home_region
        # ARN of the Big Data Compute Service project for tracking delivery.
        self.max_compute_project_arn = max_compute_project_arn
        # The ARN of the role that Operation Audit assumes when delivering operation events to the Big Data Compute Service project.
        self.max_compute_write_role_arn = max_compute_write_role_arn
        # The name of the trail.
        self.name = name
        # The name of the OSS bucket.
        self.oss_bucket_name = oss_bucket_name
        # The prefix of the log files to be stored in the destination OSS bucket.
        self.oss_key_prefix = oss_key_prefix
        # The ARN of the RAM role that is assumed by ActionTrail to deliver events to the OSS bucket.
        self.oss_write_role_arn = oss_write_role_arn
        # The ID of the request.
        self.request_id = request_id
        # The ARN of the Log Service project to which events are to be delivered.
        self.sls_project_arn = sls_project_arn
        # The ARN of the RAM role that is assumed by ActionTrail is to deliver events to the Log Service project.
        self.sls_write_role_arn = sls_write_role_arn
        # The one or more regions from which the trail delivers events.
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

        if self.home_region is not None:
            result['HomeRegion'] = self.home_region

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('HomeRegion') is not None:
            self.home_region = m.get('HomeRegion')

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlsProjectArn') is not None:
            self.sls_project_arn = m.get('SlsProjectArn')

        if m.get('SlsWriteRoleArn') is not None:
            self.sls_write_role_arn = m.get('SlsWriteRoleArn')

        if m.get('TrailRegion') is not None:
            self.trail_region = m.get('TrailRegion')

        return self

