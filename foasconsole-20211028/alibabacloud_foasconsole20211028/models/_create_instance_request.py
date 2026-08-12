# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_foasconsole20211028 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        architecture_type: str = None,
        auto_renew: bool = None,
        charge_type: str = None,
        duration: int = None,
        extra: str = None,
        ha: bool = None,
        ha_resource_spec: main_models.CreateInstanceRequestHaResourceSpec = None,
        ha_vswitch_ids: List[str] = None,
        instance_name: str = None,
        monitor_type: str = None,
        pricing_cycle: str = None,
        promotion_code: str = None,
        region: str = None,
        resource_group_id: str = None,
        resource_spec: main_models.CreateInstanceRequestResourceSpec = None,
        storage: main_models.CreateInstanceRequestStorage = None,
        tag: List[main_models.CreateInstanceRequestTag] = None,
        use_promotion_code: bool = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        # The processor architecture.
        self.architecture_type = architecture_type
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Disabled. This is the default value.
        # 
        # > This parameter does not take effect for pay-as-you-go instances.
        self.auto_renew = auto_renew
        # The billing method. Valid values:
        # - POST: pay-as-you-go.
        # - PRE: subscription.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The subscription duration.
        # 
        # > This parameter is required when ChargeType is set to PRE.
        self.duration = duration
        # The extended field.
        self.extra = extra
        # Specifies whether to use zone-disaster recovery resources.
        self.ha = ha
        # The zone-disaster recovery resource specifications.
        self.ha_resource_spec = ha_resource_spec
        # The list of vSwitch IDs in the secondary zone for zone-disaster recovery.
        self.ha_vswitch_ids = ha_vswitch_ids
        # The workspace name. The name must start with a lowercase letter and can contain lowercase letters, digits, and hyphens (-). The name cannot end with a hyphen.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The type of monitoring and alerting service. You can select ARMS or CloudMonitor.
        self.monitor_type = monitor_type
        # The unit of the subscription duration. Valid values:
        # 
        # - **year**: year.
        # - **month**: month.
        # 
        # > This parameter is required when ChargeType is set to PRE.
        self.pricing_cycle = pricing_cycle
        # The coupon code.
        self.promotion_code = promotion_code
        # The region ID.
        # 
        # This parameter is required.
        self.region = region
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resource specifications.
        # 
        # > This parameter is required when ChargeType is set to PRE.
        self.resource_spec = resource_spec
        # The storage parameters.
        # 
        # This parameter is required.
        self.storage = storage
        # The list of tags. A maximum of 20 tags can be specified.
        self.tag = tag
        # Specifies whether to use a coupon. Valid values:
        # - true: Use a coupon.
        # - false: Do not use a coupon.
        self.use_promotion_code = use_promotion_code
        # The list of vSwitch IDs.
        # 
        # This parameter is required.
        self.v_switch_ids = v_switch_ids
        # The virtual private cloud (VPC) ID.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        if self.ha_resource_spec:
            self.ha_resource_spec.validate()
        if self.resource_spec:
            self.resource_spec.validate()
        if self.storage:
            self.storage.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture_type is not None:
            result['ArchitectureType'] = self.architecture_type

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.ha is not None:
            result['Ha'] = self.ha

        if self.ha_resource_spec is not None:
            result['HaResourceSpec'] = self.ha_resource_spec.to_map()

        if self.ha_vswitch_ids is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()

        if self.storage is not None:
            result['Storage'] = self.storage.to_map()

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.use_promotion_code is not None:
            result['UsePromotionCode'] = self.use_promotion_code

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchitectureType') is not None:
            self.architecture_type = m.get('ArchitectureType')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('Ha') is not None:
            self.ha = m.get('Ha')

        if m.get('HaResourceSpec') is not None:
            temp_model = main_models.CreateInstanceRequestHaResourceSpec()
            self.ha_resource_spec = temp_model.from_map(m.get('HaResourceSpec'))

        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids = m.get('HaVSwitchIds')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceSpec') is not None:
            temp_model = main_models.CreateInstanceRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m.get('ResourceSpec'))

        if m.get('Storage') is not None:
            temp_model = main_models.CreateInstanceRequestStorage()
            self.storage = temp_model.from_map(m.get('Storage'))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateInstanceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UsePromotionCode') is not None:
            self.use_promotion_code = m.get('UsePromotionCode')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateInstanceRequestStorage(DaraModel):
    def __init__(
        self,
        fully_managed: bool = None,
        oss: main_models.CreateInstanceRequestStorageOss = None,
    ):
        # Specifies whether to use fully managed storage. You can select only one of fully managed storage or binding an OSS bucket. Valid values:
        # - true: Use fully managed storage.
        # - false: Do not use fully managed storage.
        self.fully_managed = fully_managed
        # The Object Storage Service (OSS) storage.
        self.oss = oss

    def validate(self):
        if self.oss:
            self.oss.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fully_managed is not None:
            result['FullyManaged'] = self.fully_managed

        if self.oss is not None:
            result['Oss'] = self.oss.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullyManaged') is not None:
            self.fully_managed = m.get('FullyManaged')

        if m.get('Oss') is not None:
            temp_model = main_models.CreateInstanceRequestStorageOss()
            self.oss = temp_model.from_map(m.get('Oss'))

        return self

class CreateInstanceRequestStorageOss(DaraModel):
    def __init__(
        self,
        bucket: str = None,
    ):
        # The name of the OSS bucket to bind.
        self.bucket = bucket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        return self

class CreateInstanceRequestResourceSpec(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        # The number of CPUs.
        # > - This parameter is required for subscription workspaces. For pay-as-you-go workspaces, you do not need to specify this parameter.- The number of CPUs for the target project must be less than the remaining CPUs in the workspace (total purchased CPUs minus CPUs already allocated to other projects). Otherwise, an error is returned.
        self.cpu = cpu
        # The memory size. Unit: GB.
        # 
        # > The memory size must be 4 times the number of CPUs.
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')

        return self

class CreateInstanceRequestHaResourceSpec(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        # The number of CPUs for zone-disaster recovery.
        self.cpu = cpu
        # The memory size for zone-disaster recovery.
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')

        return self

