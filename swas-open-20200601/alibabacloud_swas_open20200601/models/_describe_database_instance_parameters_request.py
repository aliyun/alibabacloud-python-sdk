# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDatabaseInstanceParametersRequest(DaraModel):
    def __init__(
        self,
        database_instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the lightweight database instance.
        # 
        # This parameter is required.
        self.database_instance_id = database_instance_id
        # The ID of the region where the lightweight database instance is located. You can call [ListRegions](https://help.aliyun.com/document_detail/189315.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

