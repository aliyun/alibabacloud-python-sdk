# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDedicatedClusterResponseBody(DaraModel):
    def __init__(
        self,
        cpu_utilization: int = None,
        dedicated_cluster_id: str = None,
        dedicated_cluster_name: str = None,
        disk_utilization: int = None,
        dts_instance_id: str = None,
        du: int = None,
        du_utilization: int = None,
        err_code: str = None,
        err_message: str = None,
        gmt_created: int = None,
        gmt_finished: int = None,
        http_status_code: str = None,
        mem_utilization: int = None,
        node_count: int = None,
        oversold_du: int = None,
        region_id: str = None,
        request_id: str = None,
        state: str = None,
        success: str = None,
        total_cpu_core: int = None,
        total_disk_gbsize: int = None,
        total_mem_gbsize: int = None,
        used_cpu_core: int = None,
        used_disk_gbsize: int = None,
        used_du: int = None,
        used_mem_gbsize: int = None,
    ):
        # The CPU utilization. Unit: percentage.
        self.cpu_utilization = cpu_utilization
        # The ID of the cluster.
        self.dedicated_cluster_id = dedicated_cluster_id
        # The name of the cluster.
        self.dedicated_cluster_name = dedicated_cluster_name
        # The disk usage.
        self.disk_utilization = disk_utilization
        # The ID of the instance.
        self.dts_instance_id = dts_instance_id
        # The number of DTS units (DUs).
        self.du = du
        # The DU usage. Unit: percentage.
        self.du_utilization = du_utilization
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The time when the cluster was created.
        self.gmt_created = gmt_created
        # The time when the cluster stopped.
        self.gmt_finished = gmt_finished
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The memory usage.
        self.mem_utilization = mem_utilization
        # The number of nodes in the cluster.
        self.node_count = node_count
        # The number of DUs that exceeds the upper limit.
        self.oversold_du = oversold_du
        # The ID of the region in which the instance resides.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The status of the cluster. Valid values:
        # 
        # *   **init**: The cluster is being initialized.
        # *   **schedule**: The cluster is pending scheduling.
        # *   **running**: The cluster is running.
        # *   **upgrade**: The cluster is being upgraded.
        # *   **downgrade**: The cluster is being downgraded.
        # *   **locked**: The cluster is locked.
        # *   **releasing**: The cluster is being released.
        # *   **released**: The cluster is released.
        self.state = state
        # Indicates whether the request was successful.
        self.success = success
        # The total number of CPU cores.
        self.total_cpu_core = total_cpu_core
        # The total disk size. Unit: GB.
        self.total_disk_gbsize = total_disk_gbsize
        # The total amount of memory. Unit: GB.
        self.total_mem_gbsize = total_mem_gbsize
        # The number of used CPU cores.
        self.used_cpu_core = used_cpu_core
        # The used disk size. Unit: GB.
        self.used_disk_gbsize = used_disk_gbsize
        # The number of used DUs.
        self.used_du = used_du
        # The amount of used memory. Unit: GB.
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

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_finished is not None:
            result['GmtFinished'] = self.gmt_finished

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.mem_utilization is not None:
            result['MemUtilization'] = self.mem_utilization

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.oversold_du is not None:
            result['OversoldDu'] = self.oversold_du

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state is not None:
            result['State'] = self.state

        if self.success is not None:
            result['Success'] = self.success

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

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtFinished') is not None:
            self.gmt_finished = m.get('GmtFinished')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MemUtilization') is not None:
            self.mem_utilization = m.get('MemUtilization')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('OversoldDu') is not None:
            self.oversold_du = m.get('OversoldDu')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Success') is not None:
            self.success = m.get('Success')

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

