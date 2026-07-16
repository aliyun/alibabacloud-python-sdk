# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yundun_dbaudit20180320 import models as main_models
from darabonba.model import DaraModel

class DescribeSyncInfoResponseBody(DaraModel):
    def __init__(
        self,
        instance_info: main_models.DescribeSyncInfoResponseBodyInstanceInfo = None,
        request_id: str = None,
    ):
        self.instance_info = instance_info
        self.request_id = request_id

    def validate(self):
        if self.instance_info:
            self.instance_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_info is not None:
            result['InstanceInfo'] = self.instance_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceInfo') is not None:
            temp_model = main_models.DescribeSyncInfoResponseBodyInstanceInfo()
            self.instance_info = temp_model.from_map(m.get('InstanceInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSyncInfoResponseBodyInstanceInfo(DaraModel):
    def __init__(
        self,
        access_type: int = None,
        aliuid: int = None,
        custom_name: str = None,
        ecs_eip: str = None,
        ecs_instance_id: str = None,
        ecs_internet_ip: str = None,
        ecs_intranet_ip: str = None,
        ecs_network_type: str = None,
        ecs_status: str = None,
        ecs_uuid: str = None,
        expire_time: int = None,
        image_version_name: str = None,
        instance_id: str = None,
        plan_code: str = None,
        plan_name: str = None,
        plan_upgrade_status: int = None,
        plan_upgradeable: str = None,
        product_code: str = None,
        product_name: str = None,
        public_access_control: int = None,
        region_name: str = None,
        region_no: str = None,
        renewable: bool = None,
        start_time: int = None,
        status: int = None,
        upgrade_status: int = None,
        vendor_code: str = None,
        vswitch_id: str = None,
        zone_no: str = None,
    ):
        self.access_type = access_type
        self.aliuid = aliuid
        self.custom_name = custom_name
        self.ecs_eip = ecs_eip
        self.ecs_instance_id = ecs_instance_id
        self.ecs_internet_ip = ecs_internet_ip
        self.ecs_intranet_ip = ecs_intranet_ip
        self.ecs_network_type = ecs_network_type
        self.ecs_status = ecs_status
        self.ecs_uuid = ecs_uuid
        self.expire_time = expire_time
        self.image_version_name = image_version_name
        self.instance_id = instance_id
        self.plan_code = plan_code
        self.plan_name = plan_name
        self.plan_upgrade_status = plan_upgrade_status
        self.plan_upgradeable = plan_upgradeable
        self.product_code = product_code
        self.product_name = product_name
        self.public_access_control = public_access_control
        self.region_name = region_name
        self.region_no = region_no
        self.renewable = renewable
        self.start_time = start_time
        self.status = status
        self.upgrade_status = upgrade_status
        self.vendor_code = vendor_code
        self.vswitch_id = vswitch_id
        self.zone_no = zone_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid

        if self.custom_name is not None:
            result['CustomName'] = self.custom_name

        if self.ecs_eip is not None:
            result['EcsEip'] = self.ecs_eip

        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

        if self.ecs_internet_ip is not None:
            result['EcsInternetIp'] = self.ecs_internet_ip

        if self.ecs_intranet_ip is not None:
            result['EcsIntranetIp'] = self.ecs_intranet_ip

        if self.ecs_network_type is not None:
            result['EcsNetworkType'] = self.ecs_network_type

        if self.ecs_status is not None:
            result['EcsStatus'] = self.ecs_status

        if self.ecs_uuid is not None:
            result['EcsUuid'] = self.ecs_uuid

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.image_version_name is not None:
            result['ImageVersionName'] = self.image_version_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.plan_code is not None:
            result['PlanCode'] = self.plan_code

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.plan_upgrade_status is not None:
            result['PlanUpgradeStatus'] = self.plan_upgrade_status

        if self.plan_upgradeable is not None:
            result['PlanUpgradeable'] = self.plan_upgradeable

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.public_access_control is not None:
            result['PublicAccessControl'] = self.public_access_control

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.renewable is not None:
            result['Renewable'] = self.renewable

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status

        if self.vendor_code is not None:
            result['VendorCode'] = self.vendor_code

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        if self.zone_no is not None:
            result['ZoneNo'] = self.zone_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')

        if m.get('CustomName') is not None:
            self.custom_name = m.get('CustomName')

        if m.get('EcsEip') is not None:
            self.ecs_eip = m.get('EcsEip')

        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

        if m.get('EcsInternetIp') is not None:
            self.ecs_internet_ip = m.get('EcsInternetIp')

        if m.get('EcsIntranetIp') is not None:
            self.ecs_intranet_ip = m.get('EcsIntranetIp')

        if m.get('EcsNetworkType') is not None:
            self.ecs_network_type = m.get('EcsNetworkType')

        if m.get('EcsStatus') is not None:
            self.ecs_status = m.get('EcsStatus')

        if m.get('EcsUuid') is not None:
            self.ecs_uuid = m.get('EcsUuid')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ImageVersionName') is not None:
            self.image_version_name = m.get('ImageVersionName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PlanCode') is not None:
            self.plan_code = m.get('PlanCode')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('PlanUpgradeStatus') is not None:
            self.plan_upgrade_status = m.get('PlanUpgradeStatus')

        if m.get('PlanUpgradeable') is not None:
            self.plan_upgradeable = m.get('PlanUpgradeable')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('PublicAccessControl') is not None:
            self.public_access_control = m.get('PublicAccessControl')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('Renewable') is not None:
            self.renewable = m.get('Renewable')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')

        if m.get('VendorCode') is not None:
            self.vendor_code = m.get('VendorCode')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('ZoneNo') is not None:
            self.zone_no = m.get('ZoneNo')

        return self

