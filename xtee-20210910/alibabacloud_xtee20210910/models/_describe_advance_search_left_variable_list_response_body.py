# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeAdvanceSearchLeftVariableListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: List[main_models.DescribeAdvanceSearchLeftVariableListResponseBodyResultObject] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeAdvanceSearchLeftVariableListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        return self

class DescribeAdvanceSearchLeftVariableListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        display_type: str = None,
        field_rank: int = None,
        field_type: str = None,
        id: int = None,
        name: str = None,
        parent_name: str = None,
        source_type: str = None,
        title: str = None,
        type: str = None,
    ):
        # Variable code
        self.code = code
        # Description.
        self.description = description
        # Display type and grouping label
        self.display_type = display_type
        # Variable return value type
        self.field_rank = field_rank
        # Field table sorting
        self.field_type = field_type
        # Primary key ID
        self.id = id
        # Variable name
        self.name = name
        # Parent node
        self.parent_name = parent_name
        # Data source
        self.source_type = source_type
        # Title.
        self.title = title
        # Variable type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.description is not None:
            result['description'] = self.description

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.parent_name is not None:
            result['parentName'] = self.parent_name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parentName') is not None:
            self.parent_name = m.get('parentName')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

