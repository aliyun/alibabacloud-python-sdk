# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeOfflineMachinesResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        machine_list: List[main_models.DescribeOfflineMachinesResponseBodyMachineList] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # An array that consists of the information about servers.
        self.machine_list = machine_list
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.machine_list:
            for v1 in self.machine_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['MachineList'] = []
        if self.machine_list is not None:
            for k1 in self.machine_list:
                result['MachineList'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.machine_list = []
        if m.get('MachineList') is not None:
            for k1 in m.get('MachineList'):
                temp_model = main_models.DescribeOfflineMachinesResponseBodyMachineList()
                self.machine_list.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeOfflineMachinesResponseBodyMachineList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        machine_region: str = None,
        os: str = None,
        region_id: str = None,
        uuid: str = None,
        vendor: int = None,
        vendor_name: str = None,
    ):
        # The ID of the server.
        self.instance_id = instance_id
        # The name of the server.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The region in which the server resides.
        self.machine_region = machine_region
        # The operating system of the server. Valid values:
        # 
        # *   **linux**
        # *   **windows**
        # *   **windows-2003**
        self.os = os
        # The ID of the region in which the server resides.
        self.region_id = region_id
        # The UUID of the server.
        self.uuid = uuid
        # The source of the server. Valid values:
        # 
        # *   **0**: an asset provided by Alibaba Cloud.
        # *   **1**: a third-party cloud server
        # *   **2**: a server in a data center
        # *   **3**, **4**, **5**, and **7**: other cloud asset
        # *   **8**: a lightweight asset
        self.vendor = vendor
        # The name of the service provider (SP) for the server.
        # 
        # Valid values:
        # 
        # *   **ALIYUN**: Alibaba Cloud
        # *   **OUT**: a third-party service provider
        # *   **IDC**: a data center
        # *   **TENCENT**: Tencent Cloud
        # *   **HUAWEICLOUD**: Huawei Cloud
        # *   **Microsoft**: Microsoft
        # *   **AWS**: Amazon Web Services (AWS)
        # *   **TRIPARTITE**: a lightweight server
        self.vendor_name = vendor_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.machine_region is not None:
            result['MachineRegion'] = self.machine_region

        if self.os is not None:
            result['Os'] = self.os

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('MachineRegion') is not None:
            self.machine_region = m.get('MachineRegion')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')

        return self

