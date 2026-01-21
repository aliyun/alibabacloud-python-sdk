# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMonitoringAgentHostsRequest(DaraModel):
    def __init__(
        self,
        aliyun_host: bool = None,
        host_name: str = None,
        instance_ids: str = None,
        instance_region_id: str = None,
        key_word: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        serial_numbers: str = None,
        status: str = None,
        sysom_status: str = None,
    ):
        # Specifies whether to query Elastic Compute Service (ECS) instances that are provided by Alibaba Cloud or to query hosts that are not provided by Alibaba Cloud. Valid values:
        # 
        # *   true (default value): queries all the ECS instances that are provided by Alibaba Cloud.
        # *   false: queries all the hosts that are not provided by Alibaba Cloud.
        self.aliyun_host = aliyun_host
        # The name of the host.
        self.host_name = host_name
        # The ID of the instance.
        self.instance_ids = instance_ids
        # The region ID of the instance.
        self.instance_region_id = instance_region_id
        # The keyword that is used in fuzzy match.
        self.key_word = key_word
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # *   10
        # *   20
        # *   50
        # *   100
        # 
        # > Although Alibaba Cloud does not limit the maximum value of this parameter, we recommend that you do not set it to an excessively large value. If you set it to an excessively large value, a timeout error may occur.
        self.page_size = page_size
        self.region_id = region_id
        # The serial number of the host.
        # 
        # After the CloudMonitor agent is installed on a host, a globally unique serial number is generated. A host that is not provided by Alibaba Cloud has a serial number instead of an instance ID.
        # 
        # > This parameter can be used to accurately search for a monitored host.
        self.serial_numbers = serial_numbers
        # The status of the hosts that you want to query. Valid values:
        # 
        # *   Running: queries the hosts that are running.
        # *   Stopped: queries the hosts that are stopped, are not installed, or fail to be installed.
        self.status = status
        # The status of SysOM. Valid values:
        # 
        # *   installing: SysOM is being installed.
        # *   running: SysOM is running.
        # *   stopped: SysOM is stopped.
        # *   uninstalling: SysOM is being uninstalled.
        self.sysom_status = sysom_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_host is not None:
            result['AliyunHost'] = self.aliyun_host

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.instance_region_id is not None:
            result['InstanceRegionId'] = self.instance_region_id

        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.serial_numbers is not None:
            result['SerialNumbers'] = self.serial_numbers

        if self.status is not None:
            result['Status'] = self.status

        if self.sysom_status is not None:
            result['SysomStatus'] = self.sysom_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunHost') is not None:
            self.aliyun_host = m.get('AliyunHost')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InstanceRegionId') is not None:
            self.instance_region_id = m.get('InstanceRegionId')

        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SerialNumbers') is not None:
            self.serial_numbers = m.get('SerialNumbers')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SysomStatus') is not None:
            self.sysom_status = m.get('SysomStatus')

        return self

