# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLaboratoryResponseBody(DaraModel):
    def __init__(
        self,
        bucket_count: int = None,
        bucket_type: str = None,
        buckets: str = None,
        crowd_id: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        environment: str = None,
        filter: str = None,
        name: str = None,
        request_id: str = None,
        scene_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.bucket_count = bucket_count
        self.bucket_type = bucket_type
        self.buckets = buckets
        self.crowd_id = crowd_id
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        self.description = description
        self.environment = environment
        self.filter = filter
        self.name = name
        # Id of the request
        self.request_id = request_id
        self.scene_id = scene_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count

        if self.bucket_type is not None:
            result['BucketType'] = self.bucket_type

        if self.buckets is not None:
            result['Buckets'] = self.buckets

        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id

        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id

        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users

        if self.description is not None:
            result['Description'] = self.description

        if self.environment is not None:
            result['Environment'] = self.environment

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')

        if m.get('BucketType') is not None:
            self.bucket_type = m.get('BucketType')

        if m.get('Buckets') is not None:
            self.buckets = m.get('Buckets')

        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')

        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')

        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

