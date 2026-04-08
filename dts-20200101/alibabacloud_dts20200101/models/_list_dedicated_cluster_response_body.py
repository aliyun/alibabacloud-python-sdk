# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class ListDedicatedClusterResponseBody(DaraModel):
    def __init__(
        self,
        dedicated_cluster_status_list: main_models.ListDedicatedClusterResponseBodyDedicatedClusterStatusList = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        success: str = None,
        total_record_count: int = None,
    ):
        self.dedicated_cluster_status_list = dedicated_cluster_status_list
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The page number of the returned page. The value must be an integer that is greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of clusters that meet the query condition.
        self.total_record_count = total_record_count

    def validate(self):
        if self.dedicated_cluster_status_list:
            self.dedicated_cluster_status_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_cluster_status_list is not None:
            result['DedicatedClusterStatusList'] = self.dedicated_cluster_status_list.to_map()

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedClusterStatusList') is not None:
            temp_model = main_models.ListDedicatedClusterResponseBodyDedicatedClusterStatusList()
            self.dedicated_cluster_status_list = temp_model.from_map(m.get('DedicatedClusterStatusList'))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class ListDedicatedClusterResponseBodyDedicatedClusterStatusList(DaraModel):
    def __init__(
        self,
        dedicated_cluster_status: List[main_models.ListDedicatedClusterResponseBodyDedicatedClusterStatusListDedicatedClusterStatus] = None,
    ):
        self.dedicated_cluster_status = dedicated_cluster_status

    def validate(self):
        if self.dedicated_cluster_status:
            for v1 in self.dedicated_cluster_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DedicatedClusterStatus'] = []
        if self.dedicated_cluster_status is not None:
            for k1 in self.dedicated_cluster_status:
                result['DedicatedClusterStatus'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dedicated_cluster_status = []
        if m.get('DedicatedClusterStatus') is not None:
            for k1 in m.get('DedicatedClusterStatus'):
                temp_model = main_models.ListDedicatedClusterResponseBodyDedicatedClusterStatusListDedicatedClusterStatus()
                self.dedicated_cluster_status.append(temp_model.from_map(k1))

        return self

class ListDedicatedClusterResponseBodyDedicatedClusterStatusListDedicatedClusterStatus(DaraModel):
    def __init__(
        self,
        cpu_utilization: int = None,
        dedicated_cluster_id: str = None,
        dedicated_cluster_name: str = None,
        disk_utilization: int = None,
        dts_instance_id: str = None,
        du: int = None,
        du_utilization: int = None,
        gmt_created: int = None,
        mem_utilization: int = None,
        node_count: int = None,
        oversold_du: int = None,
        region_id: str = None,
        state: str = None,
        total_cpu_core: int = None,
        total_disk_gbsize: int = None,
        total_mem_gbsize: int = None,
        used_cpu_core: int = None,
        used_disk_gbsize: int = None,
        used_du: int = None,
        used_mem_gbsize: int = None,
    ):
        self.cpu_utilization = cpu_utilization
        self.dedicated_cluster_id = dedicated_cluster_id
        self.dedicated_cluster_name = dedicated_cluster_name
        self.disk_utilization = disk_utilization
        self.dts_instance_id = dts_instance_id
        self.du = du
        self.du_utilization = du_utilization
        self.gmt_created = gmt_created
        self.mem_utilization = mem_utilization
        self.node_count = node_count
        self.oversold_du = oversold_du
        self.region_id = region_id
        self.state = state
        self.total_cpu_core = total_cpu_core
        self.total_disk_gbsize = total_disk_gbsize
        self.total_mem_gbsize = total_mem_gbsize
        self.used_cpu_core = used_cpu_core
        self.used_disk_gbsize = used_disk_gbsize
        self.used_du = used_du
        self.used_mem_gbsize = used_mem_gbsize

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_utilization is not None:
            result['CpuUtilization'] = self.cpu_utilization

        if self.dedicated_cluster_id is not None:
            result['DedicatedClusterId'] = self.dedicated_cluster_id

        if self.dedicated_cluster_name is not None:
            result['DedicatedClusterName'] = self.dedicated_cluster_name

        if self.disk_utilization is not None:
            result['DiskUtilization'] = self.disk_utilization

        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id

        if self.du is not None:
            result['Du'] = self.du

        if self.du_utilization is not None:
            result['DuUtilization'] = self.du_utilization

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.mem_utilization is not None:
            result['MemUtilization'] = self.mem_utilization

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.oversold_du is not None:
            result['OversoldDu'] = self.oversold_du

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.state is not None:
            result['State'] = self.state

        if self.total_cpu_core is not None:
            result['TotalCpuCore'] = self.total_cpu_core

        if self.total_disk_gbsize is not None:
            result['TotalDiskGBSize'] = self.total_disk_gbsize

        if self.total_mem_gbsize is not None:
            result['TotalMemGBSize'] = self.total_mem_gbsize

        if self.used_cpu_core is not None:
            result['UsedCpuCore'] = self.used_cpu_core

        if self.used_disk_gbsize is not None:
            result['UsedDiskGBSize'] = self.used_disk_gbsize

        if self.used_du is not None:
            result['UsedDu'] = self.used_du

        if self.used_mem_gbsize is not None:
            result['UsedMemGBSize'] = self.used_mem_gbsize

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuUtilization') is not None:
            self.cpu_utilization = m.get('CpuUtilization')

        if m.get('DedicatedClusterId') is not None:
            self.dedicated_cluster_id = m.get('DedicatedClusterId')

        if m.get('DedicatedClusterName') is not None:
            self.dedicated_cluster_name = m.get('DedicatedClusterName')

        if m.get('DiskUtilization') is not None:
            self.disk_utilization = m.get('DiskUtilization')

        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')

        if m.get('Du') is not None:
            self.du = m.get('Du')

        if m.get('DuUtilization') is not None:
            self.du_utilization = m.get('DuUtilization')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('MemUtilization') is not None:
            self.mem_utilization = m.get('MemUtilization')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('OversoldDu') is not None:
            self.oversold_du = m.get('OversoldDu')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TotalCpuCore') is not None:
            self.total_cpu_core = m.get('TotalCpuCore')

        if m.get('TotalDiskGBSize') is not None:
            self.total_disk_gbsize = m.get('TotalDiskGBSize')

        if m.get('TotalMemGBSize') is not None:
            self.total_mem_gbsize = m.get('TotalMemGBSize')

        if m.get('UsedCpuCore') is not None:
            self.used_cpu_core = m.get('UsedCpuCore')

        if m.get('UsedDiskGBSize') is not None:
            self.used_disk_gbsize = m.get('UsedDiskGBSize')

        if m.get('UsedDu') is not None:
            self.used_du = m.get('UsedDu')

        if m.get('UsedMemGBSize') is not None:
            self.used_mem_gbsize = m.get('UsedMemGBSize')

        return self

