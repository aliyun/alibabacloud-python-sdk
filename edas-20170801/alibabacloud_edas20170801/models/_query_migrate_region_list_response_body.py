# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class QueryMigrateRegionListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        region_entity_list: main_models.QueryMigrateRegionListResponseBodyRegionEntityList = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The message that is returned.
        self.message = message
        self.region_entity_list = region_entity_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.region_entity_list:
            self.region_entity_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.region_entity_list is not None:
            result['RegionEntityList'] = self.region_entity_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RegionEntityList') is not None:
            temp_model = main_models.QueryMigrateRegionListResponseBodyRegionEntityList()
            self.region_entity_list = temp_model.from_map(m.get('RegionEntityList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryMigrateRegionListResponseBodyRegionEntityList(DaraModel):
    def __init__(
        self,
        region_entity: List[main_models.QueryMigrateRegionListResponseBodyRegionEntityListRegionEntity] = None,
    ):
        self.region_entity = region_entity

    def validate(self):
        if self.region_entity:
            for v1 in self.region_entity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionEntity'] = []
        if self.region_entity is not None:
            for k1 in self.region_entity:
                result['RegionEntity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_entity = []
        if m.get('RegionEntity') is not None:
            for k1 in m.get('RegionEntity'):
                temp_model = main_models.QueryMigrateRegionListResponseBodyRegionEntityListRegionEntity()
                self.region_entity.append(temp_model.from_map(k1))

        return self

class QueryMigrateRegionListResponseBodyRegionEntityListRegionEntity(DaraModel):
    def __init__(
        self,
        region_name: str = None,
        region_no: str = None,
    ):
        self.region_name = region_name
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

