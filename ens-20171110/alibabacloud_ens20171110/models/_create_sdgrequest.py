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
        # The billing logic for SDG child disks. This parameter specifies the billing method for the RBD child disks produced by this SDG. This parameter does not apply to standard cloud disks.
        # Optional parameter values:
        # 
        # - Hour.
        # 
        # -  Day. This is the default value.
        # 
        # 
        # > - Parameter description: The longer the cycle, the lower the cost. If the disk is released before the billing cycle ends, a service fee is charged.
        self.billing_cycle = billing_cycle
        # The description of the SDG.
        # > Provide a detailed description for easier future queries.
        self.description = description
        # The type of the source disk.
        # Optional parameter values:
        # -  standard: standard cloud disk. This is the default value.
        # -  rbd: RBD disk.
        # 
        # > - Limits: RBD disk SDGs and standard disk SDGs cannot inherit from each other.
        self.disk_type = disk_type
        # The ID of an existing SDG.
        # > - If you are creating an SDG for the first time, leave **FromSDGId** empty.
        # >- If **FromSDGId** is invalid or the corresponding raw cloud disk cannot be found, an error is returned.
        # >- If **FromSDGId** is not empty, this indicates that you are operating on an existing SDG rather than creating one for the first time.
        self.from_sdgid = from_sdgid
        # The AIC instance ID. You can call the [DescribeARMServerInstances](~~DescribeARMServerInstances~~) operation to obtain the InstanceId value.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The SDG sharing ratio parameter. This parameter supports cloud disks with different maximum sharing ratios.
        self.performance_level = performance_level
        # The maximum capacity of the SDG. Unit: GB.
        # >- To reduce costs, evaluate the required capacity as needed.
        # >- If you are creating an SDG for the first time, **Size** is required.
        # >- If the data volume increases later, pass a new **Size** value to expand the capacity. If **Size** is not empty and is greater than the original **Size** value of the SDG, the raw cloud disk of the SDG is expanded to the specified **Size**. If **Size** is empty or the specified **Size** is less than the original **Size** value of the SDG, no action is taken.
        # 
        # The minimum tested usable value is 150 GB.
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

