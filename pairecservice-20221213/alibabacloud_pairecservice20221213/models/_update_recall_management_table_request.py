# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class UpdateRecallManagementTableRequest(DaraModel):
    def __init__(
        self,
        enable_data_size_fluctuation_threshold: bool = None,
        enable_row_count_fluctuation_threshold: bool = None,
        fields: main_models.UpdateRecallManagementTableRequestFields = None,
        index_version_id: str = None,
        instance_id: str = None,
        max_data_size_fluctuation_threshold: int = None,
        max_row_count_fluctuation_threshold: int = None,
        min_data_size_fluctuation_threshold: int = None,
        min_row_count_fluctuation_threshold: int = None,
    ):
        # Specifies whether to enable the data size fluctuation threshold.
        self.enable_data_size_fluctuation_threshold = enable_data_size_fluctuation_threshold
        # Specifies whether to enable the row count fluctuation threshold.
        self.enable_row_count_fluctuation_threshold = enable_row_count_fluctuation_threshold
        # A list of fields.
        self.fields = fields
        # The version ID of the table.
        self.index_version_id = index_version_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum value for the data size fluctuation threshold.
        self.max_data_size_fluctuation_threshold = max_data_size_fluctuation_threshold
        # The maximum value for the row count fluctuation threshold.
        self.max_row_count_fluctuation_threshold = max_row_count_fluctuation_threshold
        # The minimum value for the data size fluctuation threshold.
        self.min_data_size_fluctuation_threshold = min_data_size_fluctuation_threshold
        # The minimum value for the row count fluctuation threshold.
        self.min_row_count_fluctuation_threshold = min_row_count_fluctuation_threshold

    def validate(self):
        if self.fields:
            self.fields.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_data_size_fluctuation_threshold is not None:
            result['EnableDataSizeFluctuationThreshold'] = self.enable_data_size_fluctuation_threshold

        if self.enable_row_count_fluctuation_threshold is not None:
            result['EnableRowCountFluctuationThreshold'] = self.enable_row_count_fluctuation_threshold

        if self.fields is not None:
            result['Fields'] = self.fields.to_map()

        if self.index_version_id is not None:
            result['IndexVersionId'] = self.index_version_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_data_size_fluctuation_threshold is not None:
            result['MaxDataSizeFluctuationThreshold'] = self.max_data_size_fluctuation_threshold

        if self.max_row_count_fluctuation_threshold is not None:
            result['MaxRowCountFluctuationThreshold'] = self.max_row_count_fluctuation_threshold

        if self.min_data_size_fluctuation_threshold is not None:
            result['MinDataSizeFluctuationThreshold'] = self.min_data_size_fluctuation_threshold

        if self.min_row_count_fluctuation_threshold is not None:
            result['MinRowCountFluctuationThreshold'] = self.min_row_count_fluctuation_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableDataSizeFluctuationThreshold') is not None:
            self.enable_data_size_fluctuation_threshold = m.get('EnableDataSizeFluctuationThreshold')

        if m.get('EnableRowCountFluctuationThreshold') is not None:
            self.enable_row_count_fluctuation_threshold = m.get('EnableRowCountFluctuationThreshold')

        if m.get('Fields') is not None:
            temp_model = main_models.UpdateRecallManagementTableRequestFields()
            self.fields = temp_model.from_map(m.get('Fields'))

        if m.get('IndexVersionId') is not None:
            self.index_version_id = m.get('IndexVersionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxDataSizeFluctuationThreshold') is not None:
            self.max_data_size_fluctuation_threshold = m.get('MaxDataSizeFluctuationThreshold')

        if m.get('MaxRowCountFluctuationThreshold') is not None:
            self.max_row_count_fluctuation_threshold = m.get('MaxRowCountFluctuationThreshold')

        if m.get('MinDataSizeFluctuationThreshold') is not None:
            self.min_data_size_fluctuation_threshold = m.get('MinDataSizeFluctuationThreshold')

        if m.get('MinRowCountFluctuationThreshold') is not None:
            self.min_row_count_fluctuation_threshold = m.get('MinRowCountFluctuationThreshold')

        return self

class UpdateRecallManagementTableRequestFields(DaraModel):
    def __init__(
        self,
        attributes: List[str] = None,
        name: str = None,
        type: str = None,
        vector_dimension: int = None,
        vector_metric_type: str = None,
    ):
        # Specifies the role of the field. Valid values:
        # 
        # - `Primary`: The primary key field.
        # 
        # - `Item`: The item field.
        # 
        # - `Score`: The recall score field.
        # 
        # - `Vector`: The vector field.
        # 
        # - `Index`: The index field.
        self.attributes = attributes
        # The field name.
        self.name = name
        # The data type of the field.
        self.type = type
        # The vector dimension.
        self.vector_dimension = vector_dimension
        # The vector metric type.
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

