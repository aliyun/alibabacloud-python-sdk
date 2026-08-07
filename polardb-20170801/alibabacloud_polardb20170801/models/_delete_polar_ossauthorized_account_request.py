# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePolarOSSAuthorizedAccountRequest(DaraModel):
    def __init__(
        self,
        authorized_user_ids: str = None,
        dbcluster_id: str = None,
        pfs_instance_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.authorized_user_ids = authorized_user_ids
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.pfs_instance_id = pfs_instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorized_user_ids is not None:
            result['AuthorizedUserIds'] = self.authorized_user_ids

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.pfs_instance_id is not None:
            result['PfsInstanceId'] = self.pfs_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedUserIds') is not None:
            self.authorized_user_ids = m.get('AuthorizedUserIds')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('PfsInstanceId') is not None:
            self.pfs_instance_id = m.get('PfsInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

