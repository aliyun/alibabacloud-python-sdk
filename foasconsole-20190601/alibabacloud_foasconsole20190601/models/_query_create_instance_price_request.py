# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_foasconsole20190601 import models as main_models
from darabonba.model import DaraModel

class QueryCreateInstancePriceRequest(DaraModel):
    def __init__(
        self,
        create_instance_request: main_models.QueryCreateInstancePriceRequestCreateInstanceRequest = None,
    ):
        # This parameter is required.
        self.create_instance_request = create_instance_request

    def validate(self):
        if self.create_instance_request:
            self.create_instance_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_instance_request is not None:
            result['CreateInstanceRequest'] = self.create_instance_request.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateInstanceRequest') is not None:
            temp_model = main_models.QueryCreateInstancePriceRequestCreateInstanceRequest()
            self.create_instance_request = temp_model.from_map(m.get('CreateInstanceRequest'))

        return self

class QueryCreateInstancePriceRequestCreateInstanceRequest(DaraModel):
    def __init__(
        self,
        architecture_type: str = None,
        auto_renew: bool = None,
        charge_type: str = None,
        duration: int = None,
        extra: str = None,
        ha: bool = None,
        ha_resource_spec: main_models.QueryCreateInstancePriceRequestCreateInstanceRequestHaResourceSpec = None,
        instance_name: str = None,
        pricing_cycle: str = None,
        promotion_code: str = None,
        region: str = None,
        resource_spec: main_models.QueryCreateInstancePriceRequestCreateInstanceRequestResourceSpec = None,
        storage: main_models.QueryCreateInstancePriceRequestCreateInstanceRequestStorage = None,
        use_promotion_code: bool = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.architecture_type = architecture_type
        self.auto_renew = auto_renew
        # This parameter is required.
        self.charge_type = charge_type
        self.duration = duration
        self.extra = extra
        self.ha = ha
        self.ha_resource_spec = ha_resource_spec
        self.instance_name = instance_name
        self.pricing_cycle = pricing_cycle
        self.promotion_code = promotion_code
        # This parameter is required.
        self.region = region
        self.resource_spec = resource_spec
        self.storage = storage
        self.use_promotion_code = use_promotion_code
        self.v_switch_ids = v_switch_ids
        # VPC ID。
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.ha_resource_spec:
            self.ha_resource_spec.validate()
        if self.resource_spec:
            self.resource_spec.validate()
        if self.storage:
            self.storage.validate()

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

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()

        if self.storage is not None:
            result['Storage'] = self.storage.to_map()

        if self.use_promotion_code is not None:
            result['UsePromotionCode'] = self.use_promotion_code

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

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
            temp_model = main_models.QueryCreateInstancePriceRequestCreateInstanceRequestHaResourceSpec()
            self.ha_resource_spec = temp_model.from_map(m.get('HaResourceSpec'))

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceSpec') is not None:
            temp_model = main_models.QueryCreateInstancePriceRequestCreateInstanceRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m.get('ResourceSpec'))

        if m.get('Storage') is not None:
            temp_model = main_models.QueryCreateInstancePriceRequestCreateInstanceRequestStorage()
            self.storage = temp_model.from_map(m.get('Storage'))

        if m.get('UsePromotionCode') is not None:
            self.use_promotion_code = m.get('UsePromotionCode')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class QueryCreateInstancePriceRequestCreateInstanceRequestStorage(DaraModel):
    def __init__(
        self,
        oss: main_models.QueryCreateInstancePriceRequestCreateInstanceRequestStorageOss = None,
    ):
        self.oss = oss

    def validate(self):
        if self.oss:
            self.oss.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss is not None:
            result['Oss'] = self.oss.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Oss') is not None:
            temp_model = main_models.QueryCreateInstancePriceRequestCreateInstanceRequestStorageOss()
            self.oss = temp_model.from_map(m.get('Oss'))

        return self

class QueryCreateInstancePriceRequestCreateInstanceRequestStorageOss(DaraModel):
    def __init__(
        self,
        bucket: str = None,
    ):
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

class QueryCreateInstancePriceRequestCreateInstanceRequestResourceSpec(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
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

class QueryCreateInstancePriceRequestCreateInstanceRequestHaResourceSpec(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        self.cpu = cpu
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

