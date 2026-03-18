# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class QueryPriceV1Request(DaraModel):
    def __init__(
        self,
        agent_node_group: main_models.QueryPriceV1RequestAgentNodeGroup = None,
        backend_node_groups: List[main_models.QueryPriceV1RequestBackendNodeGroups] = None,
        duration: int = None,
        frontend_node_groups: List[main_models.QueryPriceV1RequestFrontendNodeGroups] = None,
        observer_node_groups: List[main_models.QueryPriceV1RequestObserverNodeGroups] = None,
        package_type: str = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        promotion_option_no: str = None,
        region_id: str = None,
        run_mode: str = None,
    ):
        self.agent_node_group = agent_node_group
        self.backend_node_groups = backend_node_groups
        self.duration = duration
        self.frontend_node_groups = frontend_node_groups
        self.observer_node_groups = observer_node_groups
        self.package_type = package_type
        self.pay_type = pay_type
        self.pricing_cycle = pricing_cycle
        self.promotion_option_no = promotion_option_no
        self.region_id = region_id
        self.run_mode = run_mode

    def validate(self):
        if self.agent_node_group:
            self.agent_node_group.validate()
        if self.backend_node_groups:
            for v1 in self.backend_node_groups:
                 if v1:
                    v1.validate()
        if self.frontend_node_groups:
            for v1 in self.frontend_node_groups:
                 if v1:
                    v1.validate()
        if self.observer_node_groups:
            for v1 in self.observer_node_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_node_group is not None:
            result['AgentNodeGroup'] = self.agent_node_group.to_map()

        result['BackendNodeGroups'] = []
        if self.backend_node_groups is not None:
            for k1 in self.backend_node_groups:
                result['BackendNodeGroups'].append(k1.to_map() if k1 else None)

        if self.duration is not None:
            result['Duration'] = self.duration

        result['FrontendNodeGroups'] = []
        if self.frontend_node_groups is not None:
            for k1 in self.frontend_node_groups:
                result['FrontendNodeGroups'].append(k1.to_map() if k1 else None)

        result['ObserverNodeGroups'] = []
        if self.observer_node_groups is not None:
            for k1 in self.observer_node_groups:
                result['ObserverNodeGroups'].append(k1.to_map() if k1 else None)

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentNodeGroup') is not None:
            temp_model = main_models.QueryPriceV1RequestAgentNodeGroup()
            self.agent_node_group = temp_model.from_map(m.get('AgentNodeGroup'))

        self.backend_node_groups = []
        if m.get('BackendNodeGroups') is not None:
            for k1 in m.get('BackendNodeGroups'):
                temp_model = main_models.QueryPriceV1RequestBackendNodeGroups()
                self.backend_node_groups.append(temp_model.from_map(k1))

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        self.frontend_node_groups = []
        if m.get('FrontendNodeGroups') is not None:
            for k1 in m.get('FrontendNodeGroups'):
                temp_model = main_models.QueryPriceV1RequestFrontendNodeGroups()
                self.frontend_node_groups.append(temp_model.from_map(k1))

        self.observer_node_groups = []
        if m.get('ObserverNodeGroups') is not None:
            for k1 in m.get('ObserverNodeGroups'):
                temp_model = main_models.QueryPriceV1RequestObserverNodeGroups()
                self.observer_node_groups.append(temp_model.from_map(k1))

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        return self

class QueryPriceV1RequestObserverNodeGroups(DaraModel):
    def __init__(
        self,
        cu: str = None,
        disk_number: int = None,
        local_storage_instance_type: str = None,
        resident_node_number: int = None,
        spec_type: str = None,
        storage_performance_level: str = None,
        storage_size: int = None,
    ):
        self.cu = cu
        self.disk_number = disk_number
        self.local_storage_instance_type = local_storage_instance_type
        self.resident_node_number = resident_node_number
        self.spec_type = spec_type
        self.storage_performance_level = storage_performance_level
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['cu'] = self.cu

        if self.disk_number is not None:
            result['diskNumber'] = self.disk_number

        if self.local_storage_instance_type is not None:
            result['localStorageInstanceType'] = self.local_storage_instance_type

        if self.resident_node_number is not None:
            result['residentNodeNumber'] = self.resident_node_number

        if self.spec_type is not None:
            result['specType'] = self.spec_type

        if self.storage_performance_level is not None:
            result['storagePerformanceLevel'] = self.storage_performance_level

        if self.storage_size is not None:
            result['storageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')

        if m.get('diskNumber') is not None:
            self.disk_number = m.get('diskNumber')

        if m.get('localStorageInstanceType') is not None:
            self.local_storage_instance_type = m.get('localStorageInstanceType')

        if m.get('residentNodeNumber') is not None:
            self.resident_node_number = m.get('residentNodeNumber')

        if m.get('specType') is not None:
            self.spec_type = m.get('specType')

        if m.get('storagePerformanceLevel') is not None:
            self.storage_performance_level = m.get('storagePerformanceLevel')

        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')

        return self

class QueryPriceV1RequestFrontendNodeGroups(DaraModel):
    def __init__(
        self,
        cu: str = None,
        disk_number: int = None,
        local_storage_instance_type: str = None,
        resident_node_number: int = None,
        spec_type: str = None,
        storage_performance_level: str = None,
        storage_size: int = None,
    ):
        self.cu = cu
        self.disk_number = disk_number
        self.local_storage_instance_type = local_storage_instance_type
        self.resident_node_number = resident_node_number
        self.spec_type = spec_type
        self.storage_performance_level = storage_performance_level
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['cu'] = self.cu

        if self.disk_number is not None:
            result['diskNumber'] = self.disk_number

        if self.local_storage_instance_type is not None:
            result['localStorageInstanceType'] = self.local_storage_instance_type

        if self.resident_node_number is not None:
            result['residentNodeNumber'] = self.resident_node_number

        if self.spec_type is not None:
            result['specType'] = self.spec_type

        if self.storage_performance_level is not None:
            result['storagePerformanceLevel'] = self.storage_performance_level

        if self.storage_size is not None:
            result['storageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')

        if m.get('diskNumber') is not None:
            self.disk_number = m.get('diskNumber')

        if m.get('localStorageInstanceType') is not None:
            self.local_storage_instance_type = m.get('localStorageInstanceType')

        if m.get('residentNodeNumber') is not None:
            self.resident_node_number = m.get('residentNodeNumber')

        if m.get('specType') is not None:
            self.spec_type = m.get('specType')

        if m.get('storagePerformanceLevel') is not None:
            self.storage_performance_level = m.get('storagePerformanceLevel')

        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')

        return self

class QueryPriceV1RequestBackendNodeGroups(DaraModel):
    def __init__(
        self,
        cu: str = None,
        disk_number: int = None,
        local_storage_instance_type: str = None,
        resident_node_number: int = None,
        spec_type: str = None,
        storage_performance_level: str = None,
        storage_size: int = None,
    ):
        self.cu = cu
        self.disk_number = disk_number
        self.local_storage_instance_type = local_storage_instance_type
        self.resident_node_number = resident_node_number
        self.spec_type = spec_type
        self.storage_performance_level = storage_performance_level
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['cu'] = self.cu

        if self.disk_number is not None:
            result['diskNumber'] = self.disk_number

        if self.local_storage_instance_type is not None:
            result['localStorageInstanceType'] = self.local_storage_instance_type

        if self.resident_node_number is not None:
            result['residentNodeNumber'] = self.resident_node_number

        if self.spec_type is not None:
            result['specType'] = self.spec_type

        if self.storage_performance_level is not None:
            result['storagePerformanceLevel'] = self.storage_performance_level

        if self.storage_size is not None:
            result['storageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')

        if m.get('diskNumber') is not None:
            self.disk_number = m.get('diskNumber')

        if m.get('localStorageInstanceType') is not None:
            self.local_storage_instance_type = m.get('localStorageInstanceType')

        if m.get('residentNodeNumber') is not None:
            self.resident_node_number = m.get('residentNodeNumber')

        if m.get('specType') is not None:
            self.spec_type = m.get('specType')

        if m.get('storagePerformanceLevel') is not None:
            self.storage_performance_level = m.get('storagePerformanceLevel')

        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')

        return self

class QueryPriceV1RequestAgentNodeGroup(DaraModel):
    def __init__(
        self,
        cu: int = None,
    ):
        self.cu = cu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['cu'] = self.cu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')

        return self

