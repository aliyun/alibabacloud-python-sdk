# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class UpsertChunksRequest(DaraModel):
    def __init__(
        self,
        allow_insert_with_filter: bool = None,
        collection: str = None,
        dbinstance_id: str = None,
        file_name: str = None,
        namespace: str = None,
        namespace_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        should_replace_file: bool = None,
        text_chunks: List[main_models.UpsertChunksRequestTextChunks] = None,
    ):
        # Specifies whether to allow data insertion when a filter is specified. This parameter takes effect only when the Filter parameter in TextChunks is specified.
        # 
        # If AllowInsertWithFilter is set to true, an insert operation is performed when the filter does not match any data.
        # 
        # If AllowInsertWithFilter is set to false, no operation is performed when the filter does not match any data.
        # 
        # Default value: true.
        self.allow_insert_with_filter = allow_insert_with_filter
        # The name of the document collection.
        # 
        # > The document collection is created by calling the [CreateDocumentCollection](https://help.aliyun.com/document_detail/2618448.html) operation. You can call the [ListDocumentCollections](https://help.aliyun.com/document_detail/2618452.html) operation to view the created document collections.
        # 
        # This parameter is required.
        self.collection = collection
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including the instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The file name.
        # 
        # > If this parameter is not empty, the system determines whether to overwrite the data associated with this file name based on the value of the ShouldReplaceFile parameter. If this parameter is empty, the chunk data is directly appended and uploaded to the document collection.
        self.file_name = file_name
        # The namespace. Default value: public.
        # 
        # > You can call the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation to create a namespace and call the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to view the namespace list.
        self.namespace = namespace
        # The password for the namespace.
        # > This value is specified in the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to overwrite the data associated with the specified file name. This parameter takes effect only when the FileName parameter is specified.
        # 
        # If ShouldReplaceFile is set to true, all data associated with the file name is deleted before new data is inserted.
        # 
        # If ShouldReplaceFile is set to false, the data associated with the file name is not deleted. Instead, chunks are inserted or updated based on the specific TextChunks parameter.
        # 
        # Default value: true.
        self.should_replace_file = should_replace_file
        # The list of chunked documents.
        self.text_chunks = text_chunks

    def validate(self):
        if self.text_chunks:
            for v1 in self.text_chunks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_insert_with_filter is not None:
            result['AllowInsertWithFilter'] = self.allow_insert_with_filter

        if self.collection is not None:
            result['Collection'] = self.collection

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.should_replace_file is not None:
            result['ShouldReplaceFile'] = self.should_replace_file

        result['TextChunks'] = []
        if self.text_chunks is not None:
            for k1 in self.text_chunks:
                result['TextChunks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowInsertWithFilter') is not None:
            self.allow_insert_with_filter = m.get('AllowInsertWithFilter')

        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ShouldReplaceFile') is not None:
            self.should_replace_file = m.get('ShouldReplaceFile')

        self.text_chunks = []
        if m.get('TextChunks') is not None:
            for k1 in m.get('TextChunks'):
                temp_model = main_models.UpsertChunksRequestTextChunks()
                self.text_chunks.append(temp_model.from_map(k1))

        return self

class UpsertChunksRequestTextChunks(DaraModel):
    def __init__(
        self,
        content: str = None,
        filter: str = None,
        id: str = None,
        metadata: Dict[str, Any] = None,
    ):
        # The document content.
        # 
        # This parameter is required.
        self.content = content
        # The filter condition for the data to be updated, in the format of an SQL WHERE clause.
        self.filter = filter
        # The unique ID of the vector data.
        self.id = id
        # The metadata.
        self.metadata = metadata

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.id is not None:
            result['Id'] = self.id

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        return self

