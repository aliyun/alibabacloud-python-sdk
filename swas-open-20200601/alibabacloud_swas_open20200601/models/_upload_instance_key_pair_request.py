# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadInstanceKeyPairRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        key_pair_name: str = None,
        public_key: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The ID of the simple application server.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # The public key.
        self.public_key = public_key
        # The region ID of the simple application server. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the most recent region list.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.public_key is not None:
            result['PublicKey'] = self.public_key

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

