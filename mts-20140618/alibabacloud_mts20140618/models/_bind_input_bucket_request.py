# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindInputBucketRequest(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        owner_account: str = None,
        owner_id: int = None,
        referer: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The name of the input media bucket to be bound. The name can be up to 64 bytes in size. To obtain the media bucket name, you can log on to the **ApsaraVideo Media Processing (MPS) console** and choose **Workflows** > **Media Buckets** in the left-side navigation pane.
        # 
        # > The bucket name can contain lowercase letters, digits, and hyphens (-), and cannot start or end with a hyphen (-).
        # 
        # This parameter is required.
        self.bucket = bucket
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The settings of Object Storage Service (OSS) hotlink protection. For more information, see [Hotlink protection](https://help.aliyun.com/document_detail/31869.html).
        self.referer = referer
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.referer is not None:
            result['Referer'] = self.referer

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Referer') is not None:
            self.referer = m.get('Referer')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

