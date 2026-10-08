# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListUserDefineRegionResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        user_define_region_list: main_models.ListUserDefineRegionResponseBodyUserDefineRegionList = None,
    ):
        # The status of the API call or a POP error code.
        self.code = code
        # Additional information.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        self.user_define_region_list = user_define_region_list

    def validate(self):
        if self.user_define_region_list:
            self.user_define_region_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_define_region_list is not None:
            result['UserDefineRegionList'] = self.user_define_region_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserDefineRegionList') is not None:
            temp_model = main_models.ListUserDefineRegionResponseBodyUserDefineRegionList()
            self.user_define_region_list = temp_model.from_map(m.get('UserDefineRegionList'))

        return self

class ListUserDefineRegionResponseBodyUserDefineRegionList(DaraModel):
    def __init__(
        self,
        user_define_region_entity: List[main_models.ListUserDefineRegionResponseBodyUserDefineRegionListUserDefineRegionEntity] = None,
    ):
        self.user_define_region_entity = user_define_region_entity

    def validate(self):
        if self.user_define_region_entity:
            for v1 in self.user_define_region_entity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UserDefineRegionEntity'] = []
        if self.user_define_region_entity is not None:
            for k1 in self.user_define_region_entity:
                result['UserDefineRegionEntity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_define_region_entity = []
        if m.get('UserDefineRegionEntity') is not None:
            for k1 in m.get('UserDefineRegionEntity'):
                temp_model = main_models.ListUserDefineRegionResponseBodyUserDefineRegionListUserDefineRegionEntity()
                self.user_define_region_entity.append(temp_model.from_map(k1))

        return self

class ListUserDefineRegionResponseBodyUserDefineRegionListUserDefineRegionEntity(DaraModel):
    def __init__(
        self,
        belong_region: str = None,
        debug_enable: bool = None,
        description: str = None,
        id: int = None,
        mse_instance_id: str = None,
        region_id: str = None,
        region_name: str = None,
        registry_type: str = None,
        user_id: str = None,
    ):
        self.belong_region = belong_region
        self.debug_enable = debug_enable
        self.description = description
        self.id = id
        self.mse_instance_id = mse_instance_id
        self.region_id = region_id
        self.region_name = region_name
        self.registry_type = registry_type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.belong_region is not None:
            result['BelongRegion'] = self.belong_region

        if self.debug_enable is not None:
            result['DebugEnable'] = self.debug_enable

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.mse_instance_id is not None:
            result['MseInstanceId'] = self.mse_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.registry_type is not None:
            result['RegistryType'] = self.registry_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BelongRegion') is not None:
            self.belong_region = m.get('BelongRegion')

        if m.get('DebugEnable') is not None:
            self.debug_enable = m.get('DebugEnable')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MseInstanceId') is not None:
            self.mse_instance_id = m.get('MseInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('RegistryType') is not None:
            self.registry_type = m.get('RegistryType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

