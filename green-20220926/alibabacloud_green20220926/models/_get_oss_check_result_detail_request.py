# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOssCheckResultDetailRequest(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        media_type: int = None,
        object: str = None,
        parent_task_id: str = None,
        query_request_id: str = None,
        region_id: str = None,
        service_code: str = None,
    ):
        # Bucket name.
        self.bucket = bucket
        # Media type.
        self.media_type = media_type
        # Object name.
        self.object = object
        # Parent task ID.
        self.parent_task_id = parent_task_id
        # Query request ID.
        self.query_request_id = query_request_id
        # Region ID.
        self.region_id = region_id
        # Service code.
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.object is not None:
            result['Object'] = self.object

        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id

        if self.query_request_id is not None:
            result['QueryRequestId'] = self.query_request_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')

        if m.get('QueryRequestId') is not None:
            self.query_request_id = m.get('QueryRequestId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        return self

