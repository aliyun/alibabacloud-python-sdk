# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateExternalDataServiceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
        service_description: str = None,
        service_name: str = None,
        service_spec: str = None,
    ):
        # Instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Region ID, you can view available region IDs through the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) interface.
        self.region_id = region_id
        # Service description.
        self.service_description = service_description
        # Service name.
        # 
        # This parameter is required.
        self.service_name = service_name
        # Service specification (in CU), value:
        # 
        # - 8
        # 
        # This parameter is required.
        self.service_spec = service_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_spec is not None:
            result['ServiceSpec'] = self.service_spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceSpec') is not None:
            self.service_spec = m.get('ServiceSpec')

        return self

