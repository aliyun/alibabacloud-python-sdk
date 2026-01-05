# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListLineagesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListLineagesResponseBodyPagingInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.paging_info = paging_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListLineagesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListLineagesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        lineages: List[main_models.ListLineagesResponseBodyPagingInfoLineages] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.lineages = lineages
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.lineages:
            for v1 in self.lineages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Lineages'] = []
        if self.lineages is not None:
            for k1 in self.lineages:
                result['Lineages'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lineages = []
        if m.get('Lineages') is not None:
            for k1 in m.get('Lineages'):
                temp_model = main_models.ListLineagesResponseBodyPagingInfoLineages()
                self.lineages.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLineagesResponseBodyPagingInfoLineages(DaraModel):
    def __init__(
        self,
        dst_entity: main_models.LineageEntity = None,
        relationships: List[main_models.LineageRelationship] = None,
        src_entity: main_models.LineageEntity = None,
    ):
        self.dst_entity = dst_entity
        self.relationships = relationships
        self.src_entity = src_entity

    def validate(self):
        if self.dst_entity:
            self.dst_entity.validate()
        if self.relationships:
            for v1 in self.relationships:
                 if v1:
                    v1.validate()
        if self.src_entity:
            self.src_entity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_entity is not None:
            result['DstEntity'] = self.dst_entity.to_map()

        result['Relationships'] = []
        if self.relationships is not None:
            for k1 in self.relationships:
                result['Relationships'].append(k1.to_map() if k1 else None)

        if self.src_entity is not None:
            result['SrcEntity'] = self.src_entity.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstEntity') is not None:
            temp_model = main_models.LineageEntity()
            self.dst_entity = temp_model.from_map(m.get('DstEntity'))

        self.relationships = []
        if m.get('Relationships') is not None:
            for k1 in m.get('Relationships'):
                temp_model = main_models.LineageRelationship()
                self.relationships.append(temp_model.from_map(k1))

        if m.get('SrcEntity') is not None:
            temp_model = main_models.LineageEntity()
            self.src_entity = temp_model.from_map(m.get('SrcEntity'))

        return self

