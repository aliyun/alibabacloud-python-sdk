# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOSSBucketAttachmentRequest(DaraModel):
    def __init__(
        self,
        ossbucket: str = None,
    ):
        # The name of the OSS bucket.
        # 
        # This parameter is required.
        self.ossbucket = ossbucket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')

        return self

