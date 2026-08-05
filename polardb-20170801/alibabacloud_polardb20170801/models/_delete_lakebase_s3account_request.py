# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLakebaseS3AccountRequest(DaraModel):
    def __init__(
        self,
        pfs_instance_id: str = None,
        region_id: str = None,
        user_acc_ak: str = None,
    ):
        # The PolarFS instance ID.
        # 
        # This parameter is required.
        self.pfs_instance_id = pfs_instance_id
        # The region ID.
        # >You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query available region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The access key of the S3 account to delete.
        # 
        # > The default account cannot be deleted.
        # 
        # This parameter is required.
        self.user_acc_ak = user_acc_ak

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PfsInstanceId') is not None:
            self.pfs_instance_id = m.get('PfsInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserAccAk') is not None:
            self.user_acc_ak = m.get('UserAccAk')

        return self

