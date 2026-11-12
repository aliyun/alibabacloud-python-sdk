# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DetachKeyPairRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_ids: List[str] = None,
        key_pair_name: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **token** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The IDs of the simple application servers from which you want to unbind SSH key pairs. You can specify a maximum of 50 IDs of simple application servers.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The name of the key pair. The name must be globally unique. The name must be 2 to 64 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). The name must start with a letter but cannot start with http\\:// or https\\://.
        # 
        # This parameter is required.
        self.key_pair_name = key_pair_name
        # The region ID of the simple application servers.
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

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

