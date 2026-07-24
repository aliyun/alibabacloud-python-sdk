# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafkastreaming20260202 import models as main_models
from darabonba.model import DaraModel

class GetComputeInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetComputeInstanceResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetComputeInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetComputeInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        create_time: str = None,
        cu_limit_sum: float = None,
        cu_reserved_sum: float = None,
        cu_used_sum: float = None,
        expire_time: str = None,
        instance_id: str = None,
        instance_name: str = None,
        order_id: str = None,
        region_id: str = None,
        service_status: str = None,
        service_version: str = None,
        total_jobs: int = None,
        total_running_jobs: int = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.charge_type = charge_type
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        self.cu_limit_sum = cu_limit_sum
        self.cu_reserved_sum = cu_reserved_sum
        self.cu_used_sum = cu_used_sum
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.order_id = order_id
        self.region_id = region_id
        self.service_status = service_status
        self.service_version = service_version
        self.total_jobs = total_jobs
        self.total_running_jobs = total_running_jobs
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

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

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.total_jobs is not None:
            result['TotalJobs'] = self.total_jobs

        if self.total_running_jobs is not None:
            result['TotalRunningJobs'] = self.total_running_jobs

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

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

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('TotalJobs') is not None:
            self.total_jobs = m.get('TotalJobs')

        if m.get('TotalRunningJobs') is not None:
            self.total_running_jobs = m.get('TotalRunningJobs')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

