# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDatabaseAccountRequest(DaraModel):
    def __init__(
        self,
        database_account_id: str = None,
        instance_id: str = None,
        project_id: int = None,
        region_id: str = None,
    ):
        # The ID of the database account to delete.
        # > You can call the [ListDatabaseAccounts](https://help.aliyun.com/document_detail/2758839.html) operation to query this parameter.
        # 
        # This parameter is required.
        self.database_account_id = database_account_id
        # The ID of the bastion host instance to which the database account to be deleted belongs.
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The project ID.
        self.project_id = project_id
        # The region ID of the bastion host to which the database account to be deleted belongs.
        # > For the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAccountId') is not None:
            self.database_account_id = m.get('DatabaseAccountId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

