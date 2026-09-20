# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevokeRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        acl_actions: str = None,
        cluster_id: str = None,
        namespace: str = None,
        table_name: str = None,
    ):
        # The database account.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The list of permissions. Separate multiple permissions with commas (,). Valid values:
        # - READ: read permission.
        # - WRITE: write permission.
        # - ADMIN: administrative permission.
        # - TRASH: purge permission.
        # 
        # This parameter is required.
        self.acl_actions = acl_actions
        # The target instance ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The namespace. An asterisk (*) indicates global, which means all namespaces.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The table name. An asterisk (*) indicates global, which means all tables.
        # 
        # This parameter is required.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.acl_actions is not None:
            result['AclActions'] = self.acl_actions

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AclActions') is not None:
            self.acl_actions = m.get('AclActions')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

