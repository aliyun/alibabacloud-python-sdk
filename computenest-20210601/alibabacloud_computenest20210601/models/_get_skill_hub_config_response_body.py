# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSkillHubConfigResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        oss_bucket_name: str = None,
        oss_region_id: str = None,
        request_id: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.oss_bucket_name = oss_bucket_name
        self.oss_region_id = oss_region_id
        # Id of the request
        self.request_id = request_id
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

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_region_id is not None:
            result['OssRegionId'] = self.oss_region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssRegionId') is not None:
            self.oss_region_id = m.get('OssRegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

