# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNamespaceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        manager_account: str = None,
        manager_account_password: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        workspace_id: str = None,
    ):
        # The instance ID.
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/196830.html) operation to view the details of all instances in the specified region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The name of the administrator account that has the rds_superuser permission.
        # 
        # > You can create an account in the console by navigating to Account Management, or call the [CreateAccount](https://help.aliyun.com/document_detail/2361789.html) operation.
        # 
        # This parameter is required.
        self.manager_account = manager_account
        # The password of the administrator account.
        # 
        # This parameter is required.
        self.manager_account_password = manager_account_password
        # The name of the namespace to create, which is used for tenant isolation (the backend performs automatic creation of a user account with the same name).
        # 
        # > The name must comply with PostgreSQL object naming rules.
        self.namespace = namespace
        # The password for the namespace.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the workspace that consists of multiple database instances. This parameter and the DBInstanceId parameter cannot be left empty at the same time. If both parameters are specified, this parameter takes precedence.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account

        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')

        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

