# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListAliyunRegionResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        region_entity_list: main_models.ListAliyunRegionResponseBodyRegionEntityList = None,
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
            temp_model = main_models.ListAliyunRegionResponseBodyRegionEntityList()
            self.region_entity_list = temp_model.from_map(m.get('RegionEntityList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAliyunRegionResponseBodyRegionEntityList(DaraModel):
    def __init__(
        self,
        region_entity: List[main_models.ListAliyunRegionResponseBodyRegionEntityListRegionEntity] = None,
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
                temp_model = main_models.ListAliyunRegionResponseBodyRegionEntityListRegionEntity()
                self.region_entity.append(temp_model.from_map(k1))

        return self

class ListAliyunRegionResponseBodyRegionEntityListRegionEntity(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

