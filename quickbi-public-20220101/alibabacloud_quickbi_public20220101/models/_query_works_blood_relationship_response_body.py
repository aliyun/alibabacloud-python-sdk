# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryWorksBloodRelationshipResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.QueryWorksBloodRelationshipResponseBodyResult] = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # List of work blood information.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.QueryWorksBloodRelationshipResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryWorksBloodRelationshipResponseBodyResult(DaraModel):
    def __init__(
        self,
        component_id: str = None,
        component_name: str = None,
        component_type: int = None,
        component_type_cn_name: str = None,
        component_type_name: str = None,
        dataset_id: str = None,
        query_params: List[main_models.QueryWorksBloodRelationshipResponseBodyResultQueryParams] = None,
    ):
        # The ID of the component that you want to modify.
        self.component_id = component_id
        # The name of the component.
        self.component_name = component_name
        # The type of the image component.
        self.component_type = component_type
        # Chinese name of the component type
        self.component_type_cn_name = component_type_cn_name
        # The name of the component type.
        self.component_type_name = component_type_name
        # The ID of the training dataset that you want to remove from the specified custom linguistic model.
        self.dataset_id = dataset_id
        # A list of query parameter reference columns.
        self.query_params = query_params

    def validate(self):
        if self.query_params:
            for v1 in self.query_params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.component_type_cn_name is not None:
            result['ComponentTypeCnName'] = self.component_type_cn_name

        if self.component_type_name is not None:
            result['ComponentTypeName'] = self.component_type_name

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        result['QueryParams'] = []
        if self.query_params is not None:
            for k1 in self.query_params:
                result['QueryParams'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('ComponentTypeCnName') is not None:
            self.component_type_cn_name = m.get('ComponentTypeCnName')

        if m.get('ComponentTypeName') is not None:
            self.component_type_name = m.get('ComponentTypeName')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        self.query_params = []
        if m.get('QueryParams') is not None:
            for k1 in m.get('QueryParams'):
                temp_model = main_models.QueryWorksBloodRelationshipResponseBodyResultQueryParams()
                self.query_params.append(temp_model.from_map(k1))

        return self

class QueryWorksBloodRelationshipResponseBodyResultQueryParams(DaraModel):
    def __init__(
        self,
        area_id: str = None,
        area_name: str = None,
        caption: str = None,
        data_type: str = None,
        expression: str = None,
        is_measure: bool = None,
        path_id: str = None,
        uid: str = None,
    ):
        # The ID of the owning location.
        self.area_id = area_id
        # The name of the owning location.
        self.area_name = area_name
        # The display name of the field.
        self.caption = caption
        # The type of the field. Valid values:
        # 
        # *   string: string type
        # *   date: a date type that contains only the year, month, and day parts
        # *   datetime: a common date type
        # *   time: a date type that contains only hours, minutes, and seconds.
        # *   number: numeric
        # *   boolean: Boolean type
        # *   geographical: geographical location
        # *   url: string type
        # *   imageUrl: the type of the image link.
        # *   multivalue: a multi-value column
        self.data_type = data_type
        # Calculate field expression.
        self.expression = expression
        # Indices whether the metric. Valid values:
        # 
        # true false
        self.is_measure = is_measure
        # The globally unique PathId.
        self.path_id = path_id
        # The unique ID of the field.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area_id is not None:
            result['AreaId'] = self.area_id

        if self.area_name is not None:
            result['AreaName'] = self.area_name

        if self.caption is not None:
            result['Caption'] = self.caption

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.is_measure is not None:
            result['IsMeasure'] = self.is_measure

        if self.path_id is not None:
            result['PathId'] = self.path_id

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')

        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')

        if m.get('Caption') is not None:
            self.caption = m.get('Caption')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('IsMeasure') is not None:
            self.is_measure = m.get('IsMeasure')

        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

