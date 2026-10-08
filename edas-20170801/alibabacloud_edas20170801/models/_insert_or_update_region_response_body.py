# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class InsertOrUpdateRegionResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        user_define_region_entity: main_models.InsertOrUpdateRegionResponseBodyUserDefineRegionEntity = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The information about the custom namespace.
        self.user_define_region_entity = user_define_region_entity

    def validate(self):
        if self.user_define_region_entity:
            self.user_define_region_entity.validate()

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

        if self.user_define_region_entity is not None:
            result['UserDefineRegionEntity'] = self.user_define_region_entity.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserDefineRegionEntity') is not None:
            temp_model = main_models.InsertOrUpdateRegionResponseBodyUserDefineRegionEntity()
            self.user_define_region_entity = temp_model.from_map(m.get('UserDefineRegionEntity'))

        return self

class InsertOrUpdateRegionResponseBodyUserDefineRegionEntity(DaraModel):
    def __init__(
        self,
        belong_region: str = None,
        debug_enable: bool = None,
        description: str = None,
        id: int = None,
        region_id: str = None,
        region_name: str = None,
        user_id: str = None,
    ):
        # The ID of the region to which the namespace belongs.
        self.belong_region = belong_region
        # Indicates whether remote debugging is enabled. Valid values:
        # 
        # - true: Remote debugging is enabled.
        # 
        # - false: Remote debugging is disabled.
        self.debug_enable = debug_enable
        # The description of the namespace.
        self.description = description
        # Indicates whether the namespace is created or modified. If this parameter is left empty or 0 is returned, the namespace is created. Otherwise, the namespace is modified.
        self.id = id
        # The ID of the namespace.
        # 
        # - The ID of a custom namespace is in the `region ID:namespace identifier` format. Example: cn-beijing:tdy218.
        # 
        # - The ID of the default namespace is in the `region ID` format. Example: cn-beijing.
        self.region_id = region_id
        # The name of the namespace.
        self.region_name = region_name
        # The ID of the Alibaba Cloud account to which the custom namespace belongs.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

