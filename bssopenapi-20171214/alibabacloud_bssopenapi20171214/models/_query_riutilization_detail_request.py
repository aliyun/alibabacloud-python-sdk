# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRIUtilizationDetailRequest(DaraModel):
    def __init__(
        self,
        deducted_instance_id: str = None,
        end_time: str = None,
        instance_spec: str = None,
        page_num: int = None,
        page_size: int = None,
        ricommodity_code: str = None,
        riinstance_id: str = None,
        start_time: str = None,
    ):
        # The ID of the deducted instance. If this parameter is left empty, the details of all instances are returned.
        self.deducted_instance_id = deducted_instance_id
        # The end time. Format: YYYY-MM-DD HH:mm:ss.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The instance type corresponding to the reserved instance.
        self.instance_spec = instance_spec
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 20. Maximum value: 300.
        self.page_size = page_size
        # Valid values:
        # - ecsRi: ECS reserved instances. This is the default value.
        # - scu_bag: Storage capacity unit (SCU) plans.
        # 
        # This parameter is required.
        self.ricommodity_code = ricommodity_code
        # The instance ID of the reserved instance for the filtered query. If this parameter is left empty, the details of all used reserved instances are returned.
        self.riinstance_id = riinstance_id
        # The start time. Format: YYYY-MM-DD HH:mm:ss.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deducted_instance_id is not None:
            result['DeductedInstanceId'] = self.deducted_instance_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.ricommodity_code is not None:
            result['RICommodityCode'] = self.ricommodity_code

        if self.riinstance_id is not None:
            result['RIInstanceId'] = self.riinstance_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeductedInstanceId') is not None:
            self.deducted_instance_id = m.get('DeductedInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RICommodityCode') is not None:
            self.ricommodity_code = m.get('RICommodityCode')

        if m.get('RIInstanceId') is not None:
            self.riinstance_id = m.get('RIInstanceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

