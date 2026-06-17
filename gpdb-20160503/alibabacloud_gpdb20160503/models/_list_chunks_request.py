# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListChunksRequest(DaraModel):
    def __init__(
        self,
        collection: str = None,
        dbinstance_id: str = None,
        file_name: str = None,
        filter: str = None,
        include_vector: bool = None,
        namespace: str = None,
        namespace_password: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The name of the document collection.
        # 
        # > A document collection is created by calling the [CreateDocumentCollection](https://help.aliyun.com/document_detail/2618448.html) operation. You can call the [ListDocumentCollections](https://help.aliyun.com/document_detail/2618452.html) operation to query the created document collections.
        # 
        # This parameter is required.
        self.collection = collection
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including the instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the file.
        # 
        # > The name of an uploaded file. You can call the [ListDocuments](https://help.aliyun.com/document_detail/2618453.html) operation to query the file list.
        self.file_name = file_name
        # The filter conditions for the data to be queried. The format is the same as the WHERE clause in SQL. It is an expression that returns a Boolean value. The conditions can be simple comparison operators, such as equal to (=), not equal to (<> or !=), greater than (>), less than (<), greater than or equal to (>=), and less than or equal to (<=). They can also be more complex expressions that are combined with logical operators (AND, OR, and NOT), and conditions that use keywords such as IN, BETWEEN, and LIKE.
        # 
        # > - For more information about the syntax, see [PostgreSQL WHERE](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-where/).
        self.filter = filter
        # Specifies whether to return vectors. Default value: false.
        # 
        # > - **false**: Vectors are not returned.
        # >
        # > - **true**: Vectors are returned.
        self.include_vector = include_vector
        # The name of the namespace. Default value: public.
        # 
        # > You can call the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation to create a namespace or call the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to query a list of namespaces.
        self.namespace = namespace
        # The password of the namespace.
        # 
        # > This parameter is specified when you call the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # - **20**
        # 
        # - **50**
        # 
        # - **100**
        # 
        # Default value: **20**.
        self.page_size = page_size
        # The region ID.
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

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.include_vector is not None:
            result['IncludeVector'] = self.include_vector

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('IncludeVector') is not None:
            self.include_vector = m.get('IncludeVector')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

