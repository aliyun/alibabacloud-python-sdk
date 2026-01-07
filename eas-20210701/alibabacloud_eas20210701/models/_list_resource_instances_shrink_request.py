# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourceInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        filter: str = None,
        instance_ip: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        label_shrink: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort: str = None,
        zone: str = None,
    ):
        # The billing method of the instance. Valid values:
        # 
        # *   PrePaid: subscription.
        # *   PostPaid: pay-as-you-go.
        self.charge_type = charge_type
        # The keyword used to query instances. Instances can be queried by instance ID or instance IP address.
        self.filter = filter
        # The IP address of the instance.
        self.instance_ip = instance_ip
        # The instance ID. For more information about how to query the instance ID, see [ListResourceInstances](https://help.aliyun.com/document_detail/412129.html).
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The instance state.
        # 
        # Valid values:
        # 
        # *   Ready-SchedulingDisabled
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The instance is available but unschedulable
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Ready
        # 
        #     <!-- -->
        # 
        #     : The instance
        # 
        #     <!-- -->
        # 
        #     is running
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   NotReady
        # 
        #     <!-- -->
        # 
        #     : The instance is unready.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Stopped
        # 
        #     <!-- -->
        # 
        #     : The instance has stopped.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   NotReady-SchedulingDisabled
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The instance is unavailable and unschedulable
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Attaching
        # 
        #     <!-- -->
        # 
        #     : The instance
        # 
        #     <!-- -->
        # 
        #     is starting
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Deleting
        # 
        #     <!-- -->
        # 
        #     : The instance is being deleted.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CreateFailed: The instance failed to be created.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.instance_status = instance_status
        # The tag.
        self.label_shrink = label_shrink
        # The sorting order.
        # 
        # Valid values:
        # 
        # *   asc: The instances are sorted in ascending order.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   desc
        # 
        #     <!-- -->
        # 
        #     : The instances are sorted in descending order.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 100.
        self.page_size = page_size
        # The field that you use to sort the query results.
        # 
        # Valid values:
        # 
        # *   CreateTime
        # 
        #     <!-- -->
        # 
        #     : The instances are sorted based on the time when the instances were created.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   MemoryUsed
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The instances are sorted based on the memory usage of the instances
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   GpuUsed
        # 
        #     <!-- -->
        # 
        #     : The instances are sorted based on the
        # 
        #     <!-- -->
        # 
        #     GPU usage of the instances.
        # 
        #     <!-- -->
        # 
        # *   ExpireTime: The instances are sorted based on the time when the instances expired.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CpuUsed
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The instances are sorted based on the CPU utilization of the instances.
        # 
        #     <!-- -->
        self.sort = sort
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.instance_ip is not None:
            result['InstanceIP'] = self.instance_ip

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.label_shrink is not None:
            result['Label'] = self.label_shrink

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('InstanceIP') is not None:
            self.instance_ip = m.get('InstanceIP')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('Label') is not None:
            self.label_shrink = m.get('Label')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

