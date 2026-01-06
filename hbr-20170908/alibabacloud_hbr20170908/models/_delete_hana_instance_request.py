# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteHanaInstanceRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        resource_group_id: str = None,
        sid: str = None,
        vault_id: str = None,
    ):
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The security identifier (SID) of the SAP HANA database. You must specify a valid SID. The SID must be three characters in length and start with a letter. For more information, see [How to find sid user and instance number of HANA db?](https://answers.sap.com/questions/555192/how-to-find-sid-user-and-instance-number-of-hana-d.html?)
        # 
        # This parameter is required.
        self.sid = sid
        # The ID of the backup vault.
        # 
        # This parameter is required.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sid is not None:
            result['Sid'] = self.sid

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

