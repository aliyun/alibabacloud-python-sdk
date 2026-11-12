# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLakebaseS3AccountPolicyRequest(DaraModel):
    def __init__(
        self,
        pfs_instance_id: str = None,
        region_id: str = None,
        user_acc_ak: str = None,
        user_acc_policy: str = None,
    ):
        # The PolarFS instance ID. You can call the DescribePolarFs operation to query available instances and their IDs.
        # 
        # This parameter is required.
        self.pfs_instance_id = pfs_instance_id
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to view the regions of all clusters under the target account.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The access key of the S3 account whose policy you want to modify.
        # 
        # > You cannot modify the default account.
        # 
        # > You can call the ListLakebaseS3Accounts operation to obtain the account access key. Select an account with AccountType set to user.
        # 
        # This parameter is required.
        self.user_acc_ak = user_acc_ak
        # The user account policy in JSON object format. The Version and Statement fields are required. Statement.Action must specify explicit actions such as s3:GetObject and s3:PutObject. The s3:* wildcard is not supported. Statement.Resource must specify explicit ARNs such as arn:aws:s3:::bucket-name/*. A standalone asterisk (*) is not supported.
        # 
        # This parameter is required.
        self.user_acc_policy = user_acc_policy

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

        return self

