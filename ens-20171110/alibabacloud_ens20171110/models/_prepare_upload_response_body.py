# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PrepareUploadResponseBody(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        endpoint: str = None,
        request_id: str = None,
    ):
        # The name of the bucket. This parameter is available only when the OSS SDK is used.
        self.bucket_name = bucket_name
        # The endpoint. This parameter is available only when the OSS SDK is used.
        self.endpoint = endpoint
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

