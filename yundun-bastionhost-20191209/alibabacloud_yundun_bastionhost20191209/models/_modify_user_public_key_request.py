# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyUserPublicKeyRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        instance_id: str = None,
        public_key: str = None,
        public_key_id: str = None,
        public_key_name: str = None,
        region_id: str = None,
    ):
        # The new description of the user group. The description can be up to 500 characters in length.
        self.comment = comment
        # The ID of the bastion host on which you want to modify the public key of a user.
        # 
        # >  You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The new public key.
        # 
        # >  Specify a Base64-encoded string.
        self.public_key = public_key
        # The ID of the public key that you want to modify.
        # 
        # >  You can call the [ListUserPublicKeys](https://help.aliyun.com/document_detail/477555.html) operation to query the public key ID.
        # 
        # This parameter is required.
        self.public_key_id = public_key_id
        # The name of the public key that you want to modify. This name can be up to 128 characters in length.
        self.public_key_name = public_key_name
        # The region ID of the bastion host that is used to modify the public key of the user.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

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

        if self.public_key_id is not None:
            result['PublicKeyId'] = self.public_key_id

        if self.public_key_name is not None:
            result['PublicKeyName'] = self.public_key_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')

        if m.get('PublicKeyId') is not None:
            self.public_key_id = m.get('PublicKeyId')

        if m.get('PublicKeyName') is not None:
            self.public_key_name = m.get('PublicKeyName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

