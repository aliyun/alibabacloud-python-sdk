# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IncreaseInstanceRequest(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        callback_address: str = None,
        instance_name: str = None,
        path: str = None,
    ):
        # The name of the Object Storage Service (OSS) bucket.
        # 
        # >  The bucket must be in the same region as the Image Search instance.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name
        # The callback address.
        self.callback_address = callback_address
        # The name of the instance.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The absolute path to the increment.meta file in the bucket. The path must start with a forward slash (/) and cannot end with a forward slash (/).
        # 
        # This parameter is required.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.callback_address is not None:
            result['CallbackAddress'] = self.callback_address

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('CallbackAddress') is not None:
            self.callback_address = m.get('CallbackAddress')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

