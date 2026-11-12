# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCreateIndexJobRequest(DaraModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        job_id: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        workspace_id: str = None,
    ):
        # The name of the collection.
        # 
        # > You can call the [ListCollections](https://help.aliyun.com/document_detail/2401503.html) operation to query the list.
        # 
        # This parameter is required.
        self.collection = collection
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in the specified region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # The ID of the index creation task, which is obtained from the CreateIndex operation.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The namespace.
        # 
        # > You can call the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to query the list.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The password for the namespace.
        # 
        # > This value is specified in the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query available region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the workspace that consists of multiple database instances. This parameter and the DBInstanceId parameter cannot be both left empty. If both are specified, this parameter takes precedence.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection is not None:
            result['Collection'] = self.collection

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

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
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

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

