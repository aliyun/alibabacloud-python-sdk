# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeDataSourceResponseBody(DaraModel):
    def __init__(
        self,
        meta_datas: List[main_models.DescribeDataSourceResponseBodyMetaDatas] = None,
        request_id: str = None,
    ):
        # The metadata of the data sources.
        self.meta_datas = meta_datas
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.meta_datas:
            for v1 in self.meta_datas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MetaDatas'] = []
        if self.meta_datas is not None:
            for k1 in self.meta_datas:
                result['MetaDatas'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.meta_datas = []
        if m.get('MetaDatas') is not None:
            for k1 in m.get('MetaDatas'):
                temp_model = main_models.DescribeDataSourceResponseBodyMetaDatas()
                self.meta_datas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDataSourceResponseBodyMetaDatas(DaraModel):
    def __init__(
        self,
        data_source_id: int = None,
        data_source_name: str = None,
        description: str = None,
        meta_data_fields: List[main_models.DescribeDataSourceResponseBodyMetaDatasMetaDataFields] = None,
    ):
        # The ID of the data source.
        self.data_source_id = data_source_id
        # The name of the data source.
        self.data_source_name = data_source_name
        # The description of the data source.
        self.description = description
        # The metadata files.
        self.meta_data_fields = meta_data_fields

    def validate(self):
        if self.meta_data_fields:
            for v1 in self.meta_data_fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.description is not None:
            result['Description'] = self.description

        result['MetaDataFields'] = []
        if self.meta_data_fields is not None:
            for k1 in self.meta_data_fields:
                result['MetaDataFields'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.meta_data_fields = []
        if m.get('MetaDataFields') is not None:
            for k1 in m.get('MetaDataFields'):
                temp_model = main_models.DescribeDataSourceResponseBodyMetaDatasMetaDataFields()
                self.meta_data_fields.append(temp_model.from_map(k1))

        return self

class DescribeDataSourceResponseBodyMetaDatasMetaDataFields(DaraModel):
    def __init__(
        self,
        filed: str = None,
        filed_name: str = None,
        operator_list: List[main_models.DescribeDataSourceResponseBodyMetaDatasMetaDataFieldsOperatorList] = None,
        sample: str = None,
        value_type: str = None,
    ):
        # The key of the field.
        self.filed = filed
        # The name of the field.
        self.filed_name = filed_name
        # The operators.
        self.operator_list = operator_list
        # The sample field.
        self.sample = sample
        # The value type of the field.
        self.value_type = value_type

    def validate(self):
        if self.operator_list:
            for v1 in self.operator_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filed is not None:
            result['Filed'] = self.filed

        if self.filed_name is not None:
            result['FiledName'] = self.filed_name

        result['OperatorList'] = []
        if self.operator_list is not None:
            for k1 in self.operator_list:
                result['OperatorList'].append(k1.to_map() if k1 else None)

        if self.sample is not None:
            result['Sample'] = self.sample

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filed') is not None:
            self.filed = m.get('Filed')

        if m.get('FiledName') is not None:
            self.filed_name = m.get('FiledName')

        self.operator_list = []
        if m.get('OperatorList') is not None:
            for k1 in m.get('OperatorList'):
                temp_model = main_models.DescribeDataSourceResponseBodyMetaDatasMetaDataFieldsOperatorList()
                self.operator_list.append(temp_model.from_map(k1))

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

class DescribeDataSourceResponseBodyMetaDatasMetaDataFieldsOperatorList(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
    ):
        # The description of the operator.
        self.description = description
        # The name of the operator.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

