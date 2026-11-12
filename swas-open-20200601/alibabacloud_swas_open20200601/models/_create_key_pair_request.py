# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKeyPairRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        key_pair_name: str = None,
        region_id: str = None,
    ):
        # Ensures the idempotence of the request. You can generate the value on your client to ensure that the value is unique across different requests. The ClientToken parameter supports only ASCII characters and can be up to 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The name of the key pair. The name must be 2 to 64 characters in length, and can contain English letters and Chinese characters. It must start with a letter or a Chinese character and cannot start with http:// or https://. It can contain digits, colons (:), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.key_pair_name = key_pair_name
        # The region ID of the specified simple application server instance. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the list of supported Alibaba Cloud regions.
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

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

