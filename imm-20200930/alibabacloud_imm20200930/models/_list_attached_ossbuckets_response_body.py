# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ListAttachedOSSBucketsResponseBody(DaraModel):
    def __init__(
        self,
        attached_ossbuckets: List[main_models.ListAttachedOSSBucketsResponseBodyAttachedOSSBuckets] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # List of bound OSS Buckets.
        self.attached_ossbuckets = attached_ossbuckets
        # Pagination token. When the total number of tasks in the list exceeds the set MaxResults, this token is used for pagination. This parameter has a value only when not all matching task lists are returned.
        # 
        # Use this value as NextToken in the next call to return the subsequent task list.
        self.next_token = next_token
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.attached_ossbuckets:
            for v1 in self.attached_ossbuckets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttachedOSSBuckets'] = []
        if self.attached_ossbuckets is not None:
            for k1 in self.attached_ossbuckets:
                result['AttachedOSSBuckets'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attached_ossbuckets = []
        if m.get('AttachedOSSBuckets') is not None:
            for k1 in m.get('AttachedOSSBuckets'):
                temp_model = main_models.ListAttachedOSSBucketsResponseBodyAttachedOSSBuckets()
                self.attached_ossbuckets.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAttachedOSSBucketsResponseBodyAttachedOSSBuckets(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        ossbucket: str = None,
        owner_id: str = None,
        project_name: str = None,
        update_time: str = None,
    ):
        # Timestamp of the project creation time, formatted as RFC3339Nano.
        self.create_time = create_time
        # Description
        self.description = description
        # OSS Bucket name.
        self.ossbucket = ossbucket
        # User ID.
        self.owner_id = owner_id
        # Project name.
        self.project_name = project_name
        # Timestamp of the project modification time, formatted as RFC3339Nano.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

