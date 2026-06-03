# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_dbaudit20180320 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.DescribeInstancesResponseBodyInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instances = instances
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        description: str = None,
        ecs_status: str = None,
        expire_time: int = None,
        image_version_name: str = None,
        instance_id: str = None,
        instance_status: str = None,
        internet_endpoint: str = None,
        internet_ip: str = None,
        intranet_endpoint: str = None,
        intranet_ip: str = None,
        legacy: bool = None,
        license_code: str = None,
        network_type: str = None,
        operatable: bool = None,
        plan_upgrade_status: int = None,
        plan_upgradeable: bool = None,
        region_id: str = None,
        renewable: bool = None,
        series_code: str = None,
        start_time: int = None,
        upgrade_status: int = None,
        upgradeable: bool = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.description = description
        self.ecs_status = ecs_status
        self.expire_time = expire_time
        self.image_version_name = image_version_name
        self.instance_id = instance_id
        self.instance_status = instance_status
        self.internet_endpoint = internet_endpoint
        self.internet_ip = internet_ip
        self.intranet_endpoint = intranet_endpoint
        self.intranet_ip = intranet_ip
        self.legacy = legacy
        self.license_code = license_code
        self.network_type = network_type
        self.operatable = operatable
        self.plan_upgrade_status = plan_upgrade_status
        self.plan_upgradeable = plan_upgradeable
        self.region_id = region_id
        self.renewable = renewable
        self.series_code = series_code
        self.start_time = start_time
        self.upgrade_status = upgrade_status
        self.upgradeable = upgradeable
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.ecs_status is not None:
            result['EcsStatus'] = self.ecs_status

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.image_version_name is not None:
            result['ImageVersionName'] = self.image_version_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.legacy is not None:
            result['Legacy'] = self.legacy

        if self.license_code is not None:
            result['LicenseCode'] = self.license_code

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.operatable is not None:
            result['Operatable'] = self.operatable

        if self.plan_upgrade_status is not None:
            result['PlanUpgradeStatus'] = self.plan_upgrade_status

        if self.plan_upgradeable is not None:
            result['PlanUpgradeable'] = self.plan_upgradeable

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.renewable is not None:
            result['Renewable'] = self.renewable

        if self.series_code is not None:
            result['SeriesCode'] = self.series_code

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status

        if self.upgradeable is not None:
            result['Upgradeable'] = self.upgradeable

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EcsStatus') is not None:
            self.ecs_status = m.get('EcsStatus')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ImageVersionName') is not None:
            self.image_version_name = m.get('ImageVersionName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Legacy') is not None:
            self.legacy = m.get('Legacy')

        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Operatable') is not None:
            self.operatable = m.get('Operatable')

        if m.get('PlanUpgradeStatus') is not None:
            self.plan_upgrade_status = m.get('PlanUpgradeStatus')

        if m.get('PlanUpgradeable') is not None:
            self.plan_upgradeable = m.get('PlanUpgradeable')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Renewable') is not None:
            self.renewable = m.get('Renewable')

        if m.get('SeriesCode') is not None:
            self.series_code = m.get('SeriesCode')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')

        if m.get('Upgradeable') is not None:
            self.upgradeable = m.get('Upgradeable')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

