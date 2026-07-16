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
        # The details of the storage settings.
        self.data = data
        # The ID of the request.
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
        # Indicates whether you can change the storage region. You can change the storage region only once. The default value is false. Valid values:
        # 
        # - true: You can change the storage region.
        # 
        # - false: You cannot change the storage region.
        self.can_operate = can_operate
        # Indicates whether you have permission to change the storage region. The default value is false. Valid values:
        # 
        # - true: You have permission.
        # 
        # - false: You do not have permission.
        self.display_region = display_region
        # The storage region.
        # 
        # If the Data Management hub is in the **cn-hangzhou** region, the default value of **Region** is \\`cn-shanghai\\`. If the Data Management hub is in the **ap-southeast-1** region, the default value of **Region** is \\`ap-southeast-1\\`.
        self.region = region
        # The storage duration in days. The default value is 180. The value must be an integer from 30 to 3000.
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

