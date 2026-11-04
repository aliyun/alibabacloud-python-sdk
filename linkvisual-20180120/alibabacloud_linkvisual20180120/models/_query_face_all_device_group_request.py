# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryFaceAllDeviceGroupRequest(DaraModel):
    def __init__(
        self,
        iot_instance_id: str = None,
        isolation_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # The instance ID.
        self.iot_instance_id = iot_instance_id
        # The isolation ID.
        # 
        # This parameter is required.
        self.isolation_id = isolation_id
        # The page number.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

