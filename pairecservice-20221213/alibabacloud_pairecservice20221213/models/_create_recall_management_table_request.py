# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class CreateRecallManagementTableRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        data_source: str = None,
        description: str = None,
        enable_data_size_fluctuation_threshold: bool = None,
        enable_row_count_fluctuation_threshold: bool = None,
        fields: List[main_models.CreateRecallManagementTableRequestFields] = None,
        instance_id: str = None,
        max_data_size_fluctuation_threshold: int = None,
        max_row_count_fluctuation_threshold: int = None,
        maxcompute_project_name: str = None,
        maxcompute_schema: str = None,
        maxcompute_table_name: str = None,
        min_data_size_fluctuation_threshold: int = None,
        min_row_count_fluctuation_threshold: int = None,
        name: str = None,
        recall_type: str = None,
        type: str = None,
    ):
        self.config = config
        self.data_source = data_source
        self.description = description
        self.enable_data_size_fluctuation_threshold = enable_data_size_fluctuation_threshold
        self.enable_row_count_fluctuation_threshold = enable_row_count_fluctuation_threshold
        self.fields = fields
        # This parameter is required.
        self.instance_id = instance_id
        self.max_data_size_fluctuation_threshold = max_data_size_fluctuation_threshold
        self.max_row_count_fluctuation_threshold = max_row_count_fluctuation_threshold
        self.maxcompute_project_name = maxcompute_project_name
        self.maxcompute_schema = maxcompute_schema
        self.maxcompute_table_name = maxcompute_table_name
        self.min_data_size_fluctuation_threshold = min_data_size_fluctuation_threshold
        self.min_row_count_fluctuation_threshold = min_row_count_fluctuation_threshold
        self.name = name
        self.recall_type = recall_type
        self.type = type

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
        if self.config is not None:
            result['Config'] = self.config

        if self.data_source is not None:
            result['DataSource'] = self.data_source

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_data_size_fluctuation_threshold is not None:
            result['EnableDataSizeFluctuationThreshold'] = self.enable_data_size_fluctuation_threshold

        if self.enable_row_count_fluctuation_threshold is not None:
            result['EnableRowCountFluctuationThreshold'] = self.enable_row_count_fluctuation_threshold

        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_data_size_fluctuation_threshold is not None:
            result['MaxDataSizeFluctuationThreshold'] = self.max_data_size_fluctuation_threshold

        if self.max_row_count_fluctuation_threshold is not None:
            result['MaxRowCountFluctuationThreshold'] = self.max_row_count_fluctuation_threshold

        if self.maxcompute_project_name is not None:
            result['MaxcomputeProjectName'] = self.maxcompute_project_name

        if self.maxcompute_schema is not None:
            result['MaxcomputeSchema'] = self.maxcompute_schema

        if self.maxcompute_table_name is not None:
            result['MaxcomputeTableName'] = self.maxcompute_table_name

        if self.min_data_size_fluctuation_threshold is not None:
            result['MinDataSizeFluctuationThreshold'] = self.min_data_size_fluctuation_threshold

        if self.min_row_count_fluctuation_threshold is not None:
            result['MinRowCountFluctuationThreshold'] = self.min_row_count_fluctuation_threshold

        if self.name is not None:
            result['Name'] = self.name

        if self.recall_type is not None:
            result['RecallType'] = self.recall_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableDataSizeFluctuationThreshold') is not None:
            self.enable_data_size_fluctuation_threshold = m.get('EnableDataSizeFluctuationThreshold')

        if m.get('EnableRowCountFluctuationThreshold') is not None:
            self.enable_row_count_fluctuation_threshold = m.get('EnableRowCountFluctuationThreshold')

        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.CreateRecallManagementTableRequestFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxDataSizeFluctuationThreshold') is not None:
            self.max_data_size_fluctuation_threshold = m.get('MaxDataSizeFluctuationThreshold')

        if m.get('MaxRowCountFluctuationThreshold') is not None:
            self.max_row_count_fluctuation_threshold = m.get('MaxRowCountFluctuationThreshold')

        if m.get('MaxcomputeProjectName') is not None:
            self.maxcompute_project_name = m.get('MaxcomputeProjectName')

        if m.get('MaxcomputeSchema') is not None:
            self.maxcompute_schema = m.get('MaxcomputeSchema')

        if m.get('MaxcomputeTableName') is not None:
            self.maxcompute_table_name = m.get('MaxcomputeTableName')

        if m.get('MinDataSizeFluctuationThreshold') is not None:
            self.min_data_size_fluctuation_threshold = m.get('MinDataSizeFluctuationThreshold')

        if m.get('MinRowCountFluctuationThreshold') is not None:
            self.min_row_count_fluctuation_threshold = m.get('MinRowCountFluctuationThreshold')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RecallType') is not None:
            self.recall_type = m.get('RecallType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateRecallManagementTableRequestFields(DaraModel):
    def __init__(
        self,
        attributes: List[str] = None,
        name: str = None,
        type: str = None,
        vector_dimension: int = None,
        vector_metric_type: str = None,
    ):
        self.attributes = attributes
        self.name = name
        self.type = type
        self.vector_dimension = vector_dimension
        self.vector_metric_type = vector_metric_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.vector_dimension is not None:
            result['VectorDimension'] = self.vector_dimension

        if self.vector_metric_type is not None:
            result['VectorMetricType'] = self.vector_metric_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VectorDimension') is not None:
            self.vector_dimension = m.get('VectorDimension')

        if m.get('VectorMetricType') is not None:
            self.vector_metric_type = m.get('VectorMetricType')

        return self

