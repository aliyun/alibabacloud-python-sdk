# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserPublicKeyRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        instance_id: str = None,
        public_key: str = None,
        public_key_name: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # The description of the public key. The description can be up to 500 characters in length.
        self.comment = comment
        # The ID of the bastion host on which you want to create a public key for the user.
        # 
        # > You can call the [listinstances](https://help.aliyun.com/document_detail/204522.html) operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The public key. Encode the value by using the Base64 algorithm.
        # 
        # This parameter is required.
        self.public_key = public_key
        # The name of the public key.
        # 
        # This parameter is required.
        self.public_key_name = public_key_name
        # Specifies the region ID of the bastion host on which you want to create a public key for the user.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The ID of the user for whom you want to create a public key.
        # 
        # >  You can call the [ListUsers](https://help.aliyun.com/document_detail/204522.html) operation to query the user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.public_key is not None:
            result['PublicKey'] = self.public_key

        if self.public_key_name is not None:
            result['PublicKeyName'] = self.public_key_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')

        if m.get('PublicKeyName') is not None:
            self.public_key_name = m.get('PublicKeyName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

