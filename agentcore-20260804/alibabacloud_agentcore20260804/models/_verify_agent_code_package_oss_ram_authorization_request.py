# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyAgentCodePackageOssRamAuthorizationRequest(DaraModel):
    def __init__(
        self,
        oss_bucket_name: str = None,
    ):
        # The name of the source OSS bucket.
        # 
        # This parameter is required.
        self.oss_bucket_name = oss_bucket_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_bucket_name is not None:
            result['ossBucketName'] = self.oss_bucket_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ossBucketName') is not None:
            self.oss_bucket_name = m.get('ossBucketName')

        return self

