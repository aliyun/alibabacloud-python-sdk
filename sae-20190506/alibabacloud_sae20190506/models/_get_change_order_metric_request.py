# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetChangeOrderMetricRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_source: str = None,
        co_type: str = None,
        cpu_strategy: str = None,
        create_time: str = None,
        limit: int = None,
        order_by: str = None,
        region_id: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The type of the Serverless App Engine (SAE) application.
        # 
        # - **micro_service**
        # - **web**
        # - **job**
        self.app_source = app_source
        # The change order type.
        self.co_type = co_type
        # The CPU allocation strategy. Valid values:
        # 
        # - **request**: Allocates CPU resources only when requests are received.
        # - **always**: Always allocates a fixed amount of CPU resources.
        self.cpu_strategy = cpu_strategy
        # The start time of change order creation.
        # 
        # This parameter is required.
        self.create_time = create_time
        # The number of entries to return. Valid values: 0 to 100.
        # 
        # This parameter is required.
        self.limit = limit
        # The field used to sort the query results.
        # 
        # This parameter is required.
        self.order_by = order_by
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_source is not None:
            result['AppSource'] = self.app_source

        if self.co_type is not None:
            result['CoType'] = self.co_type

        if self.cpu_strategy is not None:
            result['CpuStrategy'] = self.cpu_strategy

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppSource') is not None:
            self.app_source = m.get('AppSource')

        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')

        if m.get('CpuStrategy') is not None:
            self.cpu_strategy = m.get('CpuStrategy')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

