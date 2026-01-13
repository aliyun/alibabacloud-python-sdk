# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListInstanceResourcesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resources: List[main_models.ListInstanceResourcesResponseBodyResources] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.resources = resources
        self.total_count = total_count

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.ListInstanceResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstanceResourcesResponseBodyResources(DaraModel):
    def __init__(
        self,
        category: str = None,
        config: str = None,
        gmt_create_at: str = None,
        gmt_modified_at: str = None,
        group: str = None,
        resource_id: str = None,
        type: str = None,
        uri: str = None,
    ):
        self.category = category
        self.config = config
        self.gmt_create_at = gmt_create_at
        self.gmt_modified_at = gmt_modified_at
        self.group = group
        self.resource_id = resource_id
        self.type = type
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.config is not None:
            result['Config'] = self.config

        if self.gmt_create_at is not None:
            result['GmtCreateAt'] = self.gmt_create_at

        if self.gmt_modified_at is not None:
            result['GmtModifiedAt'] = self.gmt_modified_at

        if self.group is not None:
            result['Group'] = self.group

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.type is not None:
            result['Type'] = self.type

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('GmtCreateAt') is not None:
            self.gmt_create_at = m.get('GmtCreateAt')

        if m.get('GmtModifiedAt') is not None:
            self.gmt_modified_at = m.get('GmtModifiedAt')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

