# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InputCodeLocation(DaraModel):
    def __init__(
        self,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        zip_file: str = None,
    ):
        self.oss_bucket_name = oss_bucket_name
        self.oss_object_name = oss_object_name
        self.zip_file = zip_file

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_bucket_name is not None:
            result['ossBucketName'] = self.oss_bucket_name

        if self.oss_object_name is not None:
            result['ossObjectName'] = self.oss_object_name

        if self.zip_file is not None:
            result['zipFile'] = self.zip_file

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ossBucketName') is not None:
            self.oss_bucket_name = m.get('ossBucketName')

        if m.get('ossObjectName') is not None:
            self.oss_object_name = m.get('ossObjectName')

        if m.get('zipFile') is not None:
            self.zip_file = m.get('zipFile')

        return self

