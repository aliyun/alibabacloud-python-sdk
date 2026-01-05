# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveDBClusterFromGDNRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        force: bool = None,
        gdnid: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        target_dbcluster_id: str = None,
    ):
        # The ID of the cluster in the GDN.
        # 
        # >  You can call the [DescribeGlobalDatabaseNetwork](https://help.aliyun.com/document_detail/264580.html) operation to view the ID of the cluster in the GDN.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.force = force
        # The ID of the GDN.
        # 
        # This parameter is required.
        self.gdnid = gdnid
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        self.target_dbcluster_id = target_dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.force is not None:
            result['Force'] = self.force

        if self.gdnid is not None:
            result['GDNId'] = self.gdnid

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.target_dbcluster_id is not None:
            result['TargetDBClusterId'] = self.target_dbcluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('GDNId') is not None:
            self.gdnid = m.get('GDNId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('TargetDBClusterId') is not None:
            self.target_dbcluster_id = m.get('TargetDBClusterId')

        return self

