# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveOrUpdateOssConfigRequest(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        end_point: str = None,
        workspace_id: str = None,
    ):
        self.bucket_name = bucket_name
        self.end_point = end_point
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.end_point is not None:
            result['EndPoint'] = self.end_point

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

