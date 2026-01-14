# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestoreOssImageRequest(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        lang: str = None,
        object_key: str = None,
        service_region_id: str = None,
        target_object_key: str = None,
    ):
        # This parameter is required.
        self.bucket = bucket
        self.lang = lang
        # This parameter is required.
        self.object_key = object_key
        # This parameter is required.
        self.service_region_id = service_region_id
        self.target_object_key = target_object_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        if self.target_object_key is not None:
            result['TargetObjectKey'] = self.target_object_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        if m.get('TargetObjectKey') is not None:
            self.target_object_key = m.get('TargetObjectKey')

        return self

