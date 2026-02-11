# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class GetStorageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetStorageResponseBodyData = None,
        request_id: str = None,
    ):
        # The information about the storage.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetStorageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetStorageResponseBodyData(DaraModel):
    def __init__(
        self,
        can_operate: bool = None,
        display_region: bool = None,
        region: str = None,
        ttl: int = None,
    ):
        # Indicates whether the storage region can be changed for once. Default value: false Valid values:
        # 
        # *   true
        # *   false
        self.can_operate = can_operate
        # Indicates whether the storage region can be changed. Default value: false Valid values:
        # 
        # *   true
        # *   false
        self.display_region = display_region
        # The region where the data is stored.
        # 
        # If the data management center is **cn-hangzhou**, the default value of **Region** is cn-shanghai, which specifies the China (Shanghai) region. If the data management center is **ap-southeast-1**, the default value of **Region** is ap-southeast-1, which specifies the Singapore region.
        self.region = region
        # The storage period of logs. Unit: day. Default value: 180. Valid values: 30 to 3000.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_operate is not None:
            result['CanOperate'] = self.can_operate

        if self.display_region is not None:
            result['DisplayRegion'] = self.display_region

        if self.region is not None:
            result['Region'] = self.region

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanOperate') is not None:
            self.can_operate = m.get('CanOperate')

        if m.get('DisplayRegion') is not None:
            self.display_region = m.get('DisplayRegion')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

