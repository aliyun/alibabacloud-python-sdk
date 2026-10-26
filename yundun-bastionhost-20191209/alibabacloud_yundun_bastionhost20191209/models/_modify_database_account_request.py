# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDatabaseAccountRequest(DaraModel):
    def __init__(
        self,
        database_account_id: str = None,
        database_account_name: str = None,
        database_schema: str = None,
        instance_id: str = None,
        password: str = None,
        project_id: int = None,
        region_id: str = None,
    ):
        # The ID of the database account to be modified.
        # > You can call the [ListDatabaseAccounts](https://help.aliyun.com/document_detail/2758839.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.database_account_id = database_account_id
        # The new name of the database account. The name can be up to 128 characters in length.
        self.database_account_name = database_account_name
        # The new database schema name. This parameter is required when the database specified by DatabaseId is a PostgreSQL or Oracle database.
        self.database_schema = database_schema
        # The instance ID of the Bastionhost instance where the database account to be modified resides.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The new password of the database account.
        self.password = password
        # The project ID.
        self.project_id = project_id
        # The region ID of the Bastionhost instance where the database account to be modified resides.
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_account_id is not None:
            result['DatabaseAccountId'] = self.database_account_id

        if self.database_account_name is not None:
            result['DatabaseAccountName'] = self.database_account_name

        if self.database_schema is not None:
            result['DatabaseSchema'] = self.database_schema

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.password is not None:
            result['Password'] = self.password

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')

        if m.get('DatabaseAccountName') is not None:
            self.database_account_name = m.get('DatabaseAccountName')

        if m.get('DatabaseSchema') is not None:
            self.database_schema = m.get('DatabaseSchema')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

