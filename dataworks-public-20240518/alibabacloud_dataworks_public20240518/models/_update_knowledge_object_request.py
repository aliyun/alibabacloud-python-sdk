# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateKnowledgeObjectRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        content: main_models.UpdateKnowledgeObjectRequestContent = None,
        description: str = None,
        expected_modify_time: int = None,
        knowledge_base_id: str = None,
        knowledge_object_id: str = None,
        name: str = None,
        upload_id: str = None,
        version_no: int = None,
    ):
        # The client token. This parameter is supported only for DOCUMENT. Model updates do not guarantee exactly-once remote save notifications.
        self.client_token = client_token
        # The typed content update. Object properties are submitted as needed. Arrays are replaced in their entirety when submitted. Unspecified properties are retained.
        self.content = content
        # The new description. An empty string clears the description. If this parameter is not specified, the original value is retained.
        self.description = description
        # The expected modification time. This parameter is supported only for DOCUMENT. It is required when modifying the body text and optional when modifying metadata.
        self.expected_modify_time = expected_modify_time
        # The ID of the knowledge base to which the object belongs.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The stable knowledge object ID returned by the Get or List operation.
        # 
        # This parameter is required.
        self.knowledge_object_id = knowledge_object_id
        # The new name. This parameter cannot be empty. If this parameter is not specified, the original value is retained.
        self.name = name
        # The upload ID. This parameter is supported only for SEMANTIC_MODEL. It replaces the public model content with a complete YAML file and is mutually exclusive with Content.
        self.upload_id = upload_id
        # The version number. This parameter is required when updating Content or UploadId for SEMANTIC_MODEL. Use the VersionNo returned by the Get operation. This is not an optimistic lock.
        self.version_no = version_no

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.expected_modify_time is not None:
            result['ExpectedModifyTime'] = self.expected_modify_time

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.knowledge_object_id is not None:
            result['KnowledgeObjectId'] = self.knowledge_object_id

        if self.name is not None:
            result['Name'] = self.name

        if self.upload_id is not None:
            result['UploadId'] = self.upload_id

        if self.version_no is not None:
            result['VersionNo'] = self.version_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Content') is not None:
            temp_model = main_models.UpdateKnowledgeObjectRequestContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpectedModifyTime') is not None:
            self.expected_modify_time = m.get('ExpectedModifyTime')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('KnowledgeObjectId') is not None:
            self.knowledge_object_id = m.get('KnowledgeObjectId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')

        if m.get('VersionNo') is not None:
            self.version_no = m.get('VersionNo')

        return self

class UpdateKnowledgeObjectRequestContent(DaraModel):
    def __init__(
        self,
        document: main_models.UpdateKnowledgeObjectRequestContentDocument = None,
        semantic_model: main_models.UpdateKnowledgeObjectRequestContentSemanticModel = None,
    ):
        # The document content. This property exists only when Type is set to DOCUMENT.
        self.document = document
        # The semantic model content. This property exists only when Type is set to SEMANTIC_MODEL.
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
            temp_model = main_models.UpdateKnowledgeObjectRequestContentDocument()
            self.document = temp_model.from_map(m.get('Document'))

        if m.get('SemanticModel') is not None:
            temp_model = main_models.UpdateKnowledgeObjectRequestContentSemanticModel()
            self.semantic_model = temp_model.from_map(m.get('SemanticModel'))

        return self

class UpdateKnowledgeObjectRequestContentSemanticModel(DaraModel):
    def __init__(
        self,
        datasets: List[main_models.UpdateKnowledgeObjectRequestContentSemanticModelDatasets] = None,
        metrics: List[main_models.UpdateKnowledgeObjectRequestContentSemanticModelMetrics] = None,
        relationships: List[main_models.UpdateKnowledgeObjectRequestContentSemanticModelRelationships] = None,
    ):
        # The logical datasets contained in the model. This is an empty array if no public datasets are available.
        self.datasets = datasets
        # The executable metrics in the model. This is an empty array if no metrics are available. Metrics with only candidate formulas are not included.
        self.metrics = metrics
        # The defined relationships in the model expressed by field pairs. This is an empty array if no relationships are available. Relationships are not inferred from graph paths.
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
                temp_model = main_models.UpdateKnowledgeObjectRequestContentSemanticModelDatasets()
                self.datasets.append(temp_model.from_map(k1))

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.UpdateKnowledgeObjectRequestContentSemanticModelMetrics()
                self.metrics.append(temp_model.from_map(k1))

        self.relationships = []
        if m.get('Relationships') is not None:
            for k1 in m.get('Relationships'):
                temp_model = main_models.UpdateKnowledgeObjectRequestContentSemanticModelRelationships()
                self.relationships.append(temp_model.from_map(k1))

        return self

class UpdateKnowledgeObjectRequestContentSemanticModelRelationships(DaraModel):
    def __init__(
        self,
        from_dataset: str = None,
        join_keys: List[main_models.UpdateKnowledgeObjectRequestContentSemanticModelRelationshipsJoinKeys] = None,
        name: str = None,
        to_dataset: str = None,
    ):
        # The name of the source SemanticDataset.
        self.from_dataset = from_dataset
        # The equi-join key pairs for the fields at both ends. At least one item is required. Composite joins are listed item by item.
        self.join_keys = join_keys
        # The name of the relationship within the model.
        self.name = name
        # The name of the target SemanticDataset.
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
                temp_model = main_models.UpdateKnowledgeObjectRequestContentSemanticModelRelationshipsJoinKeys()
                self.join_keys.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ToDataset') is not None:
            self.to_dataset = m.get('ToDataset')

        return self

class UpdateKnowledgeObjectRequestContentSemanticModelRelationshipsJoinKeys(DaraModel):
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

class UpdateKnowledgeObjectRequestContentSemanticModelMetrics(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        description: str = None,
        expression: main_models.UpdateKnowledgeObjectRequestContentSemanticModelMetricsExpression = None,
        name: str = None,
        unit: str = None,
    ):
        # The name of the associated SemanticDataset. This must be locatable within the Datasets of this model.
        self.dataset_name = dataset_name
        # The description of the metric calculation logic. This parameter is optional.
        self.description = description
        # The executable expression. This must include at least one dialect version and is not auto-generated by the model.
        self.expression = expression
        # The name of the metric.
        self.name = name
        # The explicitly declared unit of the metric. This parameter is optional and is not returned if no reliable source is available.
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
            temp_model = main_models.UpdateKnowledgeObjectRequestContentSemanticModelMetricsExpression()
            self.expression = temp_model.from_map(m.get('Expression'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

class UpdateKnowledgeObjectRequestContentSemanticModelMetricsExpression(DaraModel):
    def __init__(
        self,
        dialects: List[main_models.UpdateKnowledgeObjectRequestContentSemanticModelMetricsExpressionDialects] = None,
    ):
        # The expressions for the same metric in different SQL dialects. At least one item is required. Dialects cannot be duplicated.
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
                temp_model = main_models.UpdateKnowledgeObjectRequestContentSemanticModelMetricsExpressionDialects()
                self.dialects.append(temp_model.from_map(k1))

        return self

class UpdateKnowledgeObjectRequestContentSemanticModelMetricsExpressionDialects(DaraModel):
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

class UpdateKnowledgeObjectRequestContentSemanticModelDatasets(DaraModel):
    def __init__(
        self,
        description: str = None,
        entity_id: str = None,
        fields: List[main_models.UpdateKnowledgeObjectRequestContentSemanticModelDatasetsFields] = None,
        name: str = None,
        primary_key: List[str] = None,
    ):
        # The business description of the dataset. This parameter is optional.
        self.description = description
        # The DataWorks Data Map table entity ID. This field is returned when a reliable association exists. If the ID is omitted for an existing dataset of the same name, the existing ID is retained. Submitted values are processed according to the semantic layer rules for saving data.
        self.entity_id = entity_id
        # The defined and publicly available fields of the dataset. This is an empty array if no field definitions are provided.
        self.fields = fields
        # The name of the dataset within the model, used for relationship positioning within the model.
        self.name = name
        # The explicitly declared primary key field name. This parameter is optional. Each item must exist in the Fields of this dataset.
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
                temp_model = main_models.UpdateKnowledgeObjectRequestContentSemanticModelDatasetsFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        return self

class UpdateKnowledgeObjectRequestContentSemanticModelDatasetsFields(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        description: str = None,
        name: str = None,
    ):
        # The data type of the field. This parameter is required for publicly available model fields and is not inferred by the server.
        self.data_type = data_type
        # The business description of the field. This parameter is optional.
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

class UpdateKnowledgeObjectRequestContentDocument(DaraModel):
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

