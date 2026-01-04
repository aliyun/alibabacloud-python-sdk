# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSDGRequest(DaraModel):
    def __init__(
        self,
        billing_cycle: str = None,
        description: str = None,
        disk_type: str = None,
        from_sdgid: str = None,
        instance_id: str = None,
        performance_level: int = None,
        size: str = None,
    ):
        self.billing_cycle = billing_cycle
        # The description of the SDG.
        # 
        # >  We recommend that you specify this parameter in details for subsequent queries.
        self.description = description
        self.disk_type = disk_type
        # The ID of the SDG from which you want to create an SDG.
        # 
        # > 
        # 
        # *   The first time you create an SDG, the **FromSDGId** parameter is empty.
        # 
        # *   If the value of the **FromSDGId** parameter is invalid or does not correspond to an original disk, an error is reported.
        # 
        # *   If the value of the **FromSDGId** parameter is not empty, you have created an SDG, and the operation is performed on the existing SDG.
        self.from_sdgid = from_sdgid
        # The ID of the AIC instance. You can call the [DescribeARMServerInstances](~~DescribeARMServerInstances~~) operation to query the ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.performance_level = performance_level
        # The maximum capacity of the SDG. Unit: GB.
        # 
        # > 
        # 
        # *   To save costs, we recommend that you specify this parameter based on your business requirements.
        # 
        # *   The first time that you create an SDG, the **Size** parameter is required.
        # 
        # *   When the amount of data increases, you can pass a new **Size** parameter for resizing. If the value of the new **Size** parameter is greater than the value of the old **Size** parameter, the disk size of the SDG is increased to the size that is specified by the new **Size** parameter. If the value of the new **Size** parameter is empty or smaller than that of the old **Size** parameter, no operation is performed.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.description is not None:
            result['Description'] = self.description

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.from_sdgid is not None:
            result['FromSDGId'] = self.from_sdgid

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('FromSDGId') is not None:
            self.from_sdgid = m.get('FromSDGId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

