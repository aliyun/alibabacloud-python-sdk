# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDocumentsRequest(DaraModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        max_results: int = None,
        namespace: str = None,
        namespace_password: str = None,
        next_token: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The name of the document collection.
        # 
        # > The document collection is created by calling the [CreateDocumentCollection](https://help.aliyun.com/document_detail/2618448.html) operation. You can call the [ListDocumentCollections](https://help.aliyun.com/document_detail/2618452.html) operation to view the created document collections.
        # 
        # This parameter is required.
        self.collection = collection
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to view the details of all AnalyticDB for PostgreSQL instances in the target region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The maximum number of documents to return per page. Valid values: 1 to 100.
        self.max_results = max_results
        # The namespace. Default value: public.
        # 
        # > You can create a namespace by calling the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation and view the namespace list by calling the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation.
        self.namespace = namespace
        # The password of the namespace.
        # 
        # > This value is specified when you call the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        # The paging token used to start the next paged query.
        self.next_token = next_token
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id

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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

