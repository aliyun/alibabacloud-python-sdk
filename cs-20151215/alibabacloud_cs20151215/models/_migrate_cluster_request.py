# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MigrateClusterRequest(DaraModel):
    def __init__(
        self,
        oss_bucket_endpoint: str = None,
        oss_bucket_name: str = None,
    ):
        # The endpoint of the OSS bucket.
        self.oss_bucket_endpoint = oss_bucket_endpoint
        # The name of the Object Storage Service (OSS) bucket.
        self.oss_bucket_name = oss_bucket_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_bucket_endpoint is not None:
            result['oss_bucket_endpoint'] = self.oss_bucket_endpoint

        if self.oss_bucket_name is not None:
            result['oss_bucket_name'] = self.oss_bucket_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oss_bucket_endpoint') is not None:
            self.oss_bucket_endpoint = m.get('oss_bucket_endpoint')

        if m.get('oss_bucket_name') is not None:
            self.oss_bucket_name = m.get('oss_bucket_name')

        return self

