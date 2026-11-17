# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetKnowledgeObjectResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetKnowledgeObjectResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business error code. You can use this code to determine the error type when a request fails.
        self.code = code
        # The business data returned when the request is successful.
        self.data = data
        # The error message returned when the request fails.
        self.message = message
        # The unique identifier of the request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetKnowledgeObjectResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetKnowledgeObjectResponseBodyData(DaraModel):
    def __init__(
        self,
        content: main_models.GetKnowledgeObjectResponseBodyDataContent = None,
        create_time: int = None,
        description: str = None,
        download_files: List[main_models.GetKnowledgeObjectResponseBodyDataDownloadFiles] = None,
        download_url: str = None,
        editable: bool = None,
        expires_in: int = None,
        file_name: str = None,
        knowledge_base_id: str = None,
        knowledge_object_id: str = None,
        modify_time: int = None,
        name: str = None,
        size_bytes: int = None,
        source_references: List[main_models.GetKnowledgeObjectResponseBodyDataSourceReferences] = None,
        type: str = None,
        version_no: int = None,
    ):
        # The current valid typed knowledge content. The structure returned is a document or semantic model based on the object type.
        self.content = content
        # The time when the object was first created. This field is not returned for existing objects whose creation time cannot be reliably determined.
        self.create_time = create_time
        # The brief description of the object. This field is editable. Pass an empty string to clear the description.
        self.description = description
        # The complete shards returned for multi-file specification snapshots. Each item contains a FileName and a DownloadUrl. For single-file snapshots, use the DownloadUrl field.
        self.download_files = download_files
        # The temporary download URL of the uploaded original file for documents. For semantic models, this is the temporary download URL of the complete specification YAML for the current version.
        self.download_url = download_url
        # Indicates whether the current caller has full content editing permissions. The value is true for OWNER and ADMIN and false for VIEWER. Authorization is checked again for write operations.
        self.editable = editable
        # The validity period of the download URL, in seconds. The value is fixed at 300.
        self.expires_in = expires_in
        # The original file name of the uploaded document. This field is read-only. Renaming the object does not change this value. This field is not returned for external documents and semantic models.
        self.file_name = file_name
        # The ID of the knowledge base.
        self.knowledge_base_id = knowledge_base_id
        # The ID of the knowledge object. For semantic models, use the model ID from the semantic layer. For documents, use the stable ID from the local document table. Callers must treat the ID as opaque and must not use a retrieval ID in its place.
        self.knowledge_object_id = knowledge_object_id
        # The time when the object was last modified, in milliseconds. This value is used for conditional updates of the document body. This field does not indicate that the semantic model supports optimistic locking.
        self.modify_time = modify_time
        # The user-facing name of the object. This field is editable. Renaming the object does not change the knowledge object ID.
        self.name = name
        # The size of the uploaded original file in bytes. This field is read-only and does not reflect the length of the edited text.
        self.size_bytes = size_bytes
        # The array of source references. An empty array is currently returned.
        self.source_references = source_references
        # The object type. Current valid values are SEMANTIC_MODEL and DOCUMENT. This field may be extended in the future.
        self.type = type
        # The version of the semantic model read in this request. This version is used to specify the target version for subsequent saves and is not an optimistic lock.
        self.version_no = version_no

    def validate(self):
        if self.content:
            self.content.validate()
        if self.download_files:
            for v1 in self.download_files:
                 if v1:
                    v1.validate()
        if self.source_references:
            for v1 in self.source_references:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        result['DownloadFiles'] = []
        if self.download_files is not None:
            for k1 in self.download_files:
                result['DownloadFiles'].append(k1.to_map() if k1 else None)

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.editable is not None:
            result['Editable'] = self.editable

        if self.expires_in is not None:
            result['ExpiresIn'] = self.expires_in

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.knowledge_object_id is not None:
            result['KnowledgeObjectId'] = self.knowledge_object_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.size_bytes is not None:
            result['SizeBytes'] = self.size_bytes

        result['SourceReferences'] = []
        if self.source_references is not None:
            for k1 in self.source_references:
                result['SourceReferences'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.version_no is not None:
            result['VersionNo'] = self.version_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.GetKnowledgeObjectResponseBodyDataContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.download_files = []
        if m.get('DownloadFiles') is not None:
            for k1 in m.get('DownloadFiles'):
                temp_model = main_models.GetKnowledgeObjectResponseBodyDataDownloadFiles()
                self.download_files.append(temp_model.from_map(k1))

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('Editable') is not None:
            self.editable = m.get('Editable')

        if m.get('ExpiresIn') is not None:
            self.expires_in = m.get('ExpiresIn')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('KnowledgeObjectId') is not None:
            self.knowledge_object_id = m.get('KnowledgeObjectId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SizeBytes') is not None:
            self.size_bytes = m.get('SizeBytes')

        self.source_references = []
        if m.get('SourceReferences') is not None:
            for k1 in m.get('SourceReferences'):
                temp_model = main_models.GetKnowledgeObjectResponseBodyDataSourceReferences()
                self.source_references.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VersionNo') is not None:
            self.version_no = m.get('VersionNo')

        return self

class GetKnowledgeObjectResponseBodyDataSourceReferences(DaraModel):
    def __init__(
        self,
        source_id: str = None,
        type: str = None,
    ):
        # The source ID registered in the knowledge base. This field is present only when the type is KNOWLEDGE_SOURCE.
        self.source_id = source_id
        # The type of the source reference. The structure reserves KNOWLEDGE_SOURCE. Currently, the SourceReferences array is empty.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetKnowledgeObjectResponseBodyDataDownloadFiles(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        file_name: str = None,
    ):
        # The temporary HTTPS download URL of the shard. The validity period is specified by the ExpiresIn field.
        self.download_url = download_url
        # The file name of the specification YAML shard. Multiple shards form the complete model and do not represent the object identity.
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.file_name is not None:
            result['FileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        return self

class GetKnowledgeObjectResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        document: main_models.GetKnowledgeObjectResponseBodyDataContentDocument = None,
        semantic_model: main_models.GetKnowledgeObjectResponseBodyDataContentSemanticModel = None,
    ):
        # The document content. This field is present only when the type is DOCUMENT.
        self.document = document
        # The semantic model content. This field is present only when the type is SEMANTIC_MODEL.
        self.semantic_model = semantic_model

    def validate(self):
        if self.document:
            self.document.validate()
        if self.semantic_model:
            self.semantic_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document is not None:
            result['Document'] = self.document.to_map()

        if self.semantic_model is not None:
            result['SemanticModel'] = self.semantic_model.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Document') is not None:
            temp_model = main_models.GetKnowledgeObjectResponseBodyDataContentDocument()
            self.document = temp_model.from_map(m.get('Document'))

        if m.get('SemanticModel') is not None:
            temp_model = main_models.GetKnowledgeObjectResponseBodyDataContentSemanticModel()
            self.semantic_model = temp_model.from_map(m.get('SemanticModel'))

        return self

class GetKnowledgeObjectResponseBodyDataContentSemanticModel(DaraModel):
    def __init__(
        self,
        datasets: List[main_models.GetKnowledgeObjectResponseBodyDataContentSemanticModelDatasets] = None,
        metrics: List[main_models.GetKnowledgeObjectResponseBodyDataContentSemanticModelMetrics] = None,
        relationships: List[main_models.GetKnowledgeObjectResponseBodyDataContentSemanticModelRelationships] = None,
    ):
        # The logical datasets included in the model. An empty array is returned if no public datasets are available.
        self.datasets = datasets
        # The executable metrics in the model. An empty array is returned if no metrics are available. Metrics with only candidate formulas are not included.
        self.metrics = metrics
        # The defined relationships expressed by field pairs in the model. An empty array is returned if no relationships are defined. Relationships are not inferred from graph paths.
        self.relationships = relationships

    def validate(self):
        if self.datasets:
            for v1 in self.datasets:
                 if v1:
                    v1.validate()
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()
        if self.relationships:
            for v1 in self.relationships:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Datasets'] = []
        if self.datasets is not None:
            for k1 in self.datasets:
                result['Datasets'].append(k1.to_map() if k1 else None)

        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        result['Relationships'] = []
        if self.relationships is not None:
            for k1 in self.relationships:
                result['Relationships'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.datasets = []
        if m.get('Datasets') is not None:
            for k1 in m.get('Datasets'):
                temp_model = main_models.GetKnowledgeObjectResponseBodyDataContentSemanticModelDatasets()
                self.datasets.append(temp_model.from_map(k1))

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.GetKnowledgeObjectResponseBodyDataContentSemanticModelMetrics()
                self.metrics.append(temp_model.from_map(k1))

        self.relationships = []
        if m.get('Relationships') is not None:
            for k1 in m.get('Relationships'):
                temp_model = main_models.GetKnowledgeObjectResponseBodyDataContentSemanticModelRelationships()
                self.relationships.append(temp_model.from_map(k1))

        return self

class GetKnowledgeObjectResponseBodyDataContentSemanticModelRelationships(DaraModel):
    def __init__(
        self,
        from_dataset: str = None,
        join_keys: List[main_models.GetKnowledgeObjectResponseBodyDataContentSemanticModelRelationshipsJoinKeys] = None,
        name: str = None,
        to_dataset: str = None,
    ):
        # The name of the source dataset.
        self.from_dataset = from_dataset
        # The equi-join key pairs for the fields at both ends. At least one pair is required. Composite joins are listed as individual pairs.
        self.join_keys = join_keys
        # The name of the relationship within the model.
        self.name = name
        # The name of the target dataset.
        self.to_dataset = to_dataset

    def validate(self):
        if self.join_keys:
            for v1 in self.join_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_dataset is not None:
            result['FromDataset'] = self.from_dataset

        result['JoinKeys'] = []
        if self.join_keys is not None:
            for k1 in self.join_keys:
                result['JoinKeys'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.to_dataset is not None:
            result['ToDataset'] = self.to_dataset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromDataset') is not None:
            self.from_dataset = m.get('FromDataset')

        self.join_keys = []
        if m.get('JoinKeys') is not None:
            for k1 in m.get('JoinKeys'):
                temp_model = main_models.GetKnowledgeObjectResponseBodyDataContentSemanticModelRelationshipsJoinKeys()
                self.join_keys.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ToDataset') is not None:
            self.to_dataset = m.get('ToDataset')

        return self

class GetKnowledgeObjectResponseBodyDataContentSemanticModelRelationshipsJoinKeys(DaraModel):
    def __init__(
        self,
        from_field: str = None,
        to_field: str = None,
    ):
        # The field name in FromDataset.Fields.
        self.from_field = from_field
        # The field name in ToDataset.Fields.
        self.to_field = to_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_field is not None:
            result['FromField'] = self.from_field

        if self.to_field is not None:
            result['ToField'] = self.to_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromField') is not None:
            self.from_field = m.get('FromField')

        if m.get('ToField') is not None:
            self.to_field = m.get('ToField')

        return self

class GetKnowledgeObjectResponseBodyDataContentSemanticModelMetrics(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        description: str = None,
        expression: main_models.GetKnowledgeObjectResponseBodyDataContentSemanticModelMetricsExpression = None,
        name: str = None,
        unit: str = None,
    ):
        # The name of the dataset to which the metric belongs. This name must match a dataset in the Datasets array of the model.
        self.dataset_name = dataset_name
        # The definition of the metric. This field is optional.
        self.description = description
        # The executable expression. This field must contain at least one dialect version and is not auto-generated by the model.
        self.expression = expression
        # The name of the metric.
        self.name = name
        # The explicitly declared unit of the metric. This field is optional and is not returned if no reliable source is available.
        self.unit = unit

    def validate(self):
        if self.expression:
            self.expression.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.description is not None:
            result['Description'] = self.description

        if self.expression is not None:
            result['Expression'] = self.expression.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Expression') is not None:
            temp_model = main_models.GetKnowledgeObjectResponseBodyDataContentSemanticModelMetricsExpression()
            self.expression = temp_model.from_map(m.get('Expression'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

class GetKnowledgeObjectResponseBodyDataContentSemanticModelMetricsExpression(DaraModel):
    def __init__(
        self,
        dialects: List[main_models.GetKnowledgeObjectResponseBodyDataContentSemanticModelMetricsExpressionDialects] = None,
    ):
        # The expressions of the metric in different SQL dialects. At least one item is required. Duplicate dialects are not allowed.
        self.dialects = dialects

    def validate(self):
        if self.dialects:
            for v1 in self.dialects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dialects'] = []
        if self.dialects is not None:
            for k1 in self.dialects:
                result['Dialects'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialects = []
        if m.get('Dialects') is not None:
            for k1 in m.get('Dialects'):
                temp_model = main_models.GetKnowledgeObjectResponseBodyDataContentSemanticModelMetricsExpressionDialects()
                self.dialects.append(temp_model.from_map(k1))

        return self

class GetKnowledgeObjectResponseBodyDataContentSemanticModelMetricsExpressionDialects(DaraModel):
    def __init__(
        self,
        dialect: str = None,
        sql: str = None,
    ):
        # The SQL dialect, such as MaxCompute or ANSI_SQL.
        self.dialect = dialect
        # The non-empty calculation expression in the specified dialect. This is not a complete query statement.
        self.sql = sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dialect is not None:
            result['Dialect'] = self.dialect

        if self.sql is not None:
            result['Sql'] = self.sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dialect') is not None:
            self.dialect = m.get('Dialect')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        return self

class GetKnowledgeObjectResponseBodyDataContentSemanticModelDatasets(DaraModel):
    def __init__(
        self,
        description: str = None,
        entity_id: str = None,
        fields: List[main_models.GetKnowledgeObjectResponseBodyDataContentSemanticModelDatasetsFields] = None,
        name: str = None,
        primary_key: List[str] = None,
    ):
        # The business description of the dataset. This field is optional.
        self.description = description
        # The DataWorks Data Map table entity ID. This field is returned when a reliable association exists. If the ID is omitted for an existing dataset of the same name, the existing ID is retained. Submitted values are processed according to the semantic layer rules for saving data.
        self.entity_id = entity_id
        # The defined and publicly accessible fields of the dataset. An empty array is returned if no field definitions are provided.
        self.fields = fields
        # The name of the dataset within the model. This name is used to locate relationships within the model.
        self.name = name
        # The explicitly declared primary key field names. This field is optional. Each field must exist in the Fields array of the dataset.
        self.primary_key = primary_key

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.GetKnowledgeObjectResponseBodyDataContentSemanticModelDatasetsFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        return self

class GetKnowledgeObjectResponseBodyDataContentSemanticModelDatasetsFields(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        description: str = None,
        name: str = None,
    ):
        # The data type of the field. This field is required for publicly accessible model fields and is not inferred by the server.
        self.data_type = data_type
        # The business description of the field. This field is optional.
        self.description = description
        # The name of the field.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetKnowledgeObjectResponseBodyDataContentDocument(DaraModel):
    def __init__(
        self,
        content_format: str = None,
        text: str = None,
    ):
        # The content format. This field is required when Text is provided. Initially, the supported values are MARKDOWN and TEXT.
        self.content_format = content_format
        # The current document body that can be provided to the caller. This field is optional. It is omitted if parsing is incomplete, access is not authorized, or the full document cannot be provided securely. A single retrieved snippet does not stand in for the entire document.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_format is not None:
            result['ContentFormat'] = self.content_format

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentFormat') is not None:
            self.content_format = m.get('ContentFormat')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

