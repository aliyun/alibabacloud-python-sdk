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
        # The ID of the instance whose fees are deducted by using the RI. If this parameter is left empty, the usage details of all instances are queried.
        self.deducted_instance_id = deducted_instance_id
        # The time when the RI expires. Specify the time in the YYYY-MM-DD HH:mm:ss format.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The instance type of the RI.
        self.instance_spec = instance_spec
        # The number of the page to return. Default value: 1.
        self.page_num = page_num
        # The number of entries to return on each page. Default value: 20. Maximum value: 300.
        self.page_size = page_size
        # The code of the service to which the RI is applied. Default value: ecsRi. Valid values:
        # 
        # *   ecsRi: ECS RI.
        # *   scu_bag: storage capacity unit (SCU).
        # 
        # This parameter is required.
        self.ricommodity_code = ricommodity_code
        # The ID of the RI. If this parameter is left empty, the usage details of all RIs are queried.
        self.riinstance_id = riinstance_id
        # The time when the RI was created. Specify the time in the YYYY-MM-DD HH:mm:ss format.
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

