# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class DLStorageDescriptor(DaraModel):
    def __init__(
        self,
        bucket_cols: List[str] = None,
        columns: List[main_models.DLColumn] = None,
        input_format: str = None,
        is_compressed: bool = None,
        location: str = None,
        num_buckets: int = None,
        original_columns: List[main_models.DLColumn] = None,
        output_format: str = None,
        parameters: Dict[str, Any] = None,
        serde_info: main_models.DLSerdeInfo = None,
        skewed_info: main_models.DLSkewedInfo = None,
        sort_cols: List[main_models.DLOrder] = None,
    ):
        self.bucket_cols = bucket_cols
        self.columns = columns
        self.input_format = input_format
        self.is_compressed = is_compressed
        self.location = location
        self.num_buckets = num_buckets
        self.original_columns = original_columns
        self.output_format = output_format
        self.parameters = parameters
        self.serde_info = serde_info
        self.skewed_info = skewed_info
        self.sort_cols = sort_cols

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()
        if self.original_columns:
            for v1 in self.original_columns:
                 if v1:
                    v1.validate()
        if self.serde_info:
            self.serde_info.validate()
        if self.skewed_info:
            self.skewed_info.validate()
        if self.sort_cols:
            for v1 in self.sort_cols:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_cols is not None:
            result['BucketCols'] = self.bucket_cols

        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        if self.input_format is not None:
            result['InputFormat'] = self.input_format

        if self.is_compressed is not None:
            result['IsCompressed'] = self.is_compressed

        if self.location is not None:
            result['Location'] = self.location

        if self.num_buckets is not None:
            result['NumBuckets'] = self.num_buckets

        result['OriginalColumns'] = []
        if self.original_columns is not None:
            for k1 in self.original_columns:
                result['OriginalColumns'].append(k1.to_map() if k1 else None)

        if self.output_format is not None:
            result['OutputFormat'] = self.output_format

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.serde_info is not None:
            result['SerdeInfo'] = self.serde_info.to_map()

        if self.skewed_info is not None:
            result['SkewedInfo'] = self.skewed_info.to_map()

        result['SortCols'] = []
        if self.sort_cols is not None:
            for k1 in self.sort_cols:
                result['SortCols'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketCols') is not None:
            self.bucket_cols = m.get('BucketCols')

        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.DLColumn()
                self.columns.append(temp_model.from_map(k1))

        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')

        if m.get('IsCompressed') is not None:
            self.is_compressed = m.get('IsCompressed')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('NumBuckets') is not None:
            self.num_buckets = m.get('NumBuckets')

        self.original_columns = []
        if m.get('OriginalColumns') is not None:
            for k1 in m.get('OriginalColumns'):
                temp_model = main_models.DLColumn()
                self.original_columns.append(temp_model.from_map(k1))

        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('SerdeInfo') is not None:
            temp_model = main_models.DLSerdeInfo()
            self.serde_info = temp_model.from_map(m.get('SerdeInfo'))

        if m.get('SkewedInfo') is not None:
            temp_model = main_models.DLSkewedInfo()
            self.skewed_info = temp_model.from_map(m.get('SkewedInfo'))

        self.sort_cols = []
        if m.get('SortCols') is not None:
            for k1 in m.get('SortCols'):
                temp_model = main_models.DLOrder()
                self.sort_cols.append(temp_model.from_map(k1))

        return self

