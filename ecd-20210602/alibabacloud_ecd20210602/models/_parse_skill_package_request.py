# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ParseSkillPackageRequest(DaraModel):
    def __init__(
        self,
        oss_object_etag: str = None,
        oss_object_key: str = None,
    ):
        # The OSS ETag returned after the file is uploaded to OSS.
        # 
        # This parameter is required.
        self.oss_object_etag = oss_object_etag
        # The OSS path of the skill package.
        # 
        # This parameter is required.
        self.oss_object_key = oss_object_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_object_etag is not None:
            result['OssObjectETag'] = self.oss_object_etag

        if self.oss_object_key is not None:
            result['OssObjectKey'] = self.oss_object_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssObjectETag') is not None:
            self.oss_object_etag = m.get('OssObjectETag')

        if m.get('OssObjectKey') is not None:
            self.oss_object_key = m.get('OssObjectKey')

        return self

