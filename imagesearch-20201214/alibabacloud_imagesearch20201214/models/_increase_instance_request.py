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
        # The name of the bucket.
        # > Only a bucket in the same region as the instance is supported.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name
        # The callback URL of the task.
        self.callback_address = callback_address
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # If you have purchased an Image Search instance, log on to the [Image Search console](https://imagesearch.console.aliyun.com/) to view the instance name.
        # If you have not purchased an Image Search instance, refer to [Activate the service](https://help.aliyun.com/document_detail/179178.html) and [Create an instance](https://help.aliyun.com/document_detail/66569.html).
        # >The instance name is not the instance ID. Make sure that you distinguish between the two.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The absolute path of the increment.meta file in OSS. The path must start with a forward slash (/) and must not end with a forward slash (/).
        # > Prepare the increment.meta file in advance. For more information, see [Batch operations](https://help.aliyun.com/document_detail/66580.html).
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

