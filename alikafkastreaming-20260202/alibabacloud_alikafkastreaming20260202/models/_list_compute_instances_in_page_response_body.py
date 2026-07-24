# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafkastreaming20260202 import models as main_models
from darabonba.model import DaraModel

class ListComputeInstancesInPageResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        current_page: int = None,
        data: List[main_models.ListComputeInstancesInPageResponseBodyData] = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current_page = current_page
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListComputeInstancesInPageResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListComputeInstancesInPageResponseBodyData(DaraModel):
    def __init__(
        self,
        auto_renew_flag: bool = None,
        charge_type: str = None,
        commodity_code: str = None,
        create_time: str = None,
        cu: int = None,
        cu_limit_sum: float = None,
        cu_reserved_sum: float = None,
        cu_used_sum: float = None,
        expire_time: str = None,
        instance_id: str = None,
        instance_name: str = None,
        owner: str = None,
        region_id: str = None,
        service_status: str = None,
        total_jobs: int = None,
        total_running_jobs: int = None,
        v_switch_ids: List[str] = None,
        version: str = None,
        vpc_id: str = None,
    ):
        self.auto_renew_flag = auto_renew_flag
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        self.cu = cu
        self.cu_limit_sum = cu_limit_sum
        self.cu_reserved_sum = cu_reserved_sum
        self.cu_used_sum = cu_used_sum
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.owner = owner
        self.region_id = region_id
        self.service_status = service_status
        self.total_jobs = total_jobs
        self.total_running_jobs = total_running_jobs
        self.v_switch_ids = v_switch_ids
        self.version = version
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew_flag is not None:
            result['AutoRenewFlag'] = self.auto_renew_flag

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cu is not None:
            result['Cu'] = self.cu

        if self.cu_limit_sum is not None:
            result['CuLimitSum'] = self.cu_limit_sum

        if self.cu_reserved_sum is not None:
            result['CuReservedSum'] = self.cu_reserved_sum

        if self.cu_used_sum is not None:
            result['CuUsedSum'] = self.cu_used_sum

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        if self.total_jobs is not None:
            result['TotalJobs'] = self.total_jobs

        if self.total_running_jobs is not None:
            result['TotalRunningJobs'] = self.total_running_jobs

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.version is not None:
            result['Version'] = self.version

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewFlag') is not None:
            self.auto_renew_flag = m.get('AutoRenewFlag')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('CuLimitSum') is not None:
            self.cu_limit_sum = m.get('CuLimitSum')

        if m.get('CuReservedSum') is not None:
            self.cu_reserved_sum = m.get('CuReservedSum')

        if m.get('CuUsedSum') is not None:
            self.cu_used_sum = m.get('CuUsedSum')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        if m.get('TotalJobs') is not None:
            self.total_jobs = m.get('TotalJobs')

        if m.get('TotalRunningJobs') is not None:
            self.total_running_jobs = m.get('TotalRunningJobs')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

