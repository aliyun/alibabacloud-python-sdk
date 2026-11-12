# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyImageShareStatusRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        image_id: str = None,
        operation: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The image ID.
        # 
        # This parameter is required.
        self.image_id = image_id
        # Valid values:
        # 
        # - Share
        # 
        # - UnShare
        # 
        # This parameter is required.
        self.operation = operation
        # The region ID of the custom image. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

