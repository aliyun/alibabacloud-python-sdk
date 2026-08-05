# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLakebaseS3AccountRequest(DaraModel):
    def __init__(
        self,
        pfs_instance_id: str = None,
        region_id: str = None,
        user_acc_ak: str = None,
        user_acc_policy: str = None,
        user_acc_sk: str = None,
    ):
        # The PolarFS instance ID.
        # 
        # This parameter is required.
        self.pfs_instance_id = pfs_instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The Access Key of the S3 account.
        # 
        # > The account name can contain only uppercase letters, lowercase letters, and digits, and cannot exceed 32 characters in length.
        # 
        # This parameter is required.
        self.user_acc_ak = user_acc_ak
        # A policy document in JSON format that defines the permissions of the S3 account. If this parameter is not specified, the default policy is used.
        self.user_acc_policy = user_acc_policy
        # The Secret Key of the S3 account (@sensitive, encryption in transit).
        # 
        # > The key must contain uppercase letters, lowercase letters, and digits, and must be greater than 18 and no more than 32 characters in length.
        # 
        # This parameter is required.
        self.user_acc_sk = user_acc_sk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pfs_instance_id is not None:
            result['PfsInstanceId'] = self.pfs_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_acc_ak is not None:
            result['UserAccAk'] = self.user_acc_ak

        if self.user_acc_policy is not None:
            result['UserAccPolicy'] = self.user_acc_policy

        if self.user_acc_sk is not None:
            result['UserAccSk'] = self.user_acc_sk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PfsInstanceId') is not None:
            self.pfs_instance_id = m.get('PfsInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserAccAk') is not None:
            self.user_acc_ak = m.get('UserAccAk')

        if m.get('UserAccPolicy') is not None:
            self.user_acc_policy = m.get('UserAccPolicy')

        if m.get('UserAccSk') is not None:
            self.user_acc_sk = m.get('UserAccSk')

        return self

