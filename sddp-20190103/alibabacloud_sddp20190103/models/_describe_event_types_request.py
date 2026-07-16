# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventTypesRequest(DaraModel):
    def __init__(
        self,
        feature_type: int = None,
        lang: str = None,
        parent_type_id: int = None,
        resource_id: int = None,
        status: int = None,
    ):
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The language of the request and response. Valid values:
        # 
        # - **zh**: Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The ID of the parent anomalous activity type to which the child anomalous activity type belongs. Valid values:
        # 
        # - **01**: anomalous permission access.
        # 
        # - **02**: anomalous data flow.
        # 
        # - **03**: anomalous data operation.
        self.parent_type_id = parent_type_id
        # The resource type of the product. Valid values:
        # 
        # - **1**: MaxCompute.
        # 
        # - **2**: Object Storage Service (OSS).
        # 
        # - **3**: AnalyticDB for MySQL.
        # 
        # - **4**: Tablestore.
        # 
        # - **5**. ApsaraDB RDS.
        self.resource_id = resource_id
        # The status. Valid values:
        # 
        # - **1**: active.
        # 
        # - **2**: inactive.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.parent_type_id is not None:
            result['ParentTypeId'] = self.parent_type_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ParentTypeId') is not None:
            self.parent_type_id = m.get('ParentTypeId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

