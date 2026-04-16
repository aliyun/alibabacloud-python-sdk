# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class DescribeResourceConstraintsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: main_models.DescribeResourceConstraintsResponseBodyData = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # AccessDeniedDetail
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeResourceConstraintsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeResourceConstraintsResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_cu: List[int] = None,
        be_cu: List[int] = None,
        be_cu_on_ecs: List[int] = None,
        be_number: main_models.DescribeResourceConstraintsResponseBodyDataBeNumber = None,
        be_storage_constraints: List[main_models.DescribeResourceConstraintsResponseBodyDataBeStorageConstraints] = None,
        big_data_instance_type_constraints: List[main_models.DescribeResourceConstraintsResponseBodyDataBigDataInstanceTypeConstraints] = None,
        fe_cu: List[int] = None,
        fe_cu_on_ecs: List[int] = None,
        fe_number: main_models.DescribeResourceConstraintsResponseBodyDataFeNumber = None,
        fe_spec_type: List[main_models.DescribeResourceConstraintsResponseBodyDataFeSpecType] = None,
        fe_storage: main_models.DescribeResourceConstraintsResponseBodyDataFeStorage = None,
        ha_fe_resource_spec: main_models.DescribeResourceConstraintsResponseBodyDataHaFeResourceSpec = None,
        local_ssdinstance_type_constraints: List[main_models.DescribeResourceConstraintsResponseBodyDataLocalSSDInstanceTypeConstraints] = None,
        normal_fe_resource_spec: main_models.DescribeResourceConstraintsResponseBodyDataNormalFeResourceSpec = None,
        spec_type: List[main_models.DescribeResourceConstraintsResponseBodyDataSpecType] = None,
        split_disk_threshold_map: Dict[str, dict] = None,
        version_constraint: main_models.DescribeResourceConstraintsResponseBodyDataVersionConstraint = None,
        zone_supported_eed_types: Dict[str, List[str]] = None,
        zone_supported_spec_types: Dict[str, List[str]] = None,
        compaction_service_cu_constraint: main_models.DescribeResourceConstraintsResponseBodyDataCompactionServiceCuConstraint = None,
        zone_support_compaction_service: Dict[str, List[main_models.DataZoneSupportCompactionServiceValue]] = None,
    ):
        self.agent_cu = agent_cu
        self.be_cu = be_cu
        self.be_cu_on_ecs = be_cu_on_ecs
        self.be_number = be_number
        self.be_storage_constraints = be_storage_constraints
        self.big_data_instance_type_constraints = big_data_instance_type_constraints
        self.fe_cu = fe_cu
        self.fe_cu_on_ecs = fe_cu_on_ecs
        self.fe_number = fe_number
        self.fe_spec_type = fe_spec_type
        self.fe_storage = fe_storage
        self.ha_fe_resource_spec = ha_fe_resource_spec
        self.local_ssdinstance_type_constraints = local_ssdinstance_type_constraints
        self.normal_fe_resource_spec = normal_fe_resource_spec
        self.spec_type = spec_type
        self.split_disk_threshold_map = split_disk_threshold_map
        self.version_constraint = version_constraint
        self.zone_supported_eed_types = zone_supported_eed_types
        self.zone_supported_spec_types = zone_supported_spec_types
        self.compaction_service_cu_constraint = compaction_service_cu_constraint
        self.zone_support_compaction_service = zone_support_compaction_service

    def validate(self):
        if self.be_number:
            self.be_number.validate()
        if self.be_storage_constraints:
            for v1 in self.be_storage_constraints:
                 if v1:
                    v1.validate()
        if self.big_data_instance_type_constraints:
            for v1 in self.big_data_instance_type_constraints:
                 if v1:
                    v1.validate()
        if self.fe_number:
            self.fe_number.validate()
        if self.fe_spec_type:
            for v1 in self.fe_spec_type:
                 if v1:
                    v1.validate()
        if self.fe_storage:
            self.fe_storage.validate()
        if self.ha_fe_resource_spec:
            self.ha_fe_resource_spec.validate()
        if self.local_ssdinstance_type_constraints:
            for v1 in self.local_ssdinstance_type_constraints:
                 if v1:
                    v1.validate()
        if self.normal_fe_resource_spec:
            self.normal_fe_resource_spec.validate()
        if self.spec_type:
            for v1 in self.spec_type:
                 if v1:
                    v1.validate()
        if self.version_constraint:
            self.version_constraint.validate()
        if self.compaction_service_cu_constraint:
            self.compaction_service_cu_constraint.validate()
        if self.zone_support_compaction_service:
            for v1 in self.zone_support_compaction_service.values():
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_cu is not None:
            result['AgentCu'] = self.agent_cu

        if self.be_cu is not None:
            result['BeCu'] = self.be_cu

        if self.be_cu_on_ecs is not None:
            result['BeCuOnEcs'] = self.be_cu_on_ecs

        if self.be_number is not None:
            result['BeNumber'] = self.be_number.to_map()

        result['BeStorageConstraints'] = []
        if self.be_storage_constraints is not None:
            for k1 in self.be_storage_constraints:
                result['BeStorageConstraints'].append(k1.to_map() if k1 else None)

        result['BigDataInstanceTypeConstraints'] = []
        if self.big_data_instance_type_constraints is not None:
            for k1 in self.big_data_instance_type_constraints:
                result['BigDataInstanceTypeConstraints'].append(k1.to_map() if k1 else None)

        if self.fe_cu is not None:
            result['FeCu'] = self.fe_cu

        if self.fe_cu_on_ecs is not None:
            result['FeCuOnEcs'] = self.fe_cu_on_ecs

        if self.fe_number is not None:
            result['FeNumber'] = self.fe_number.to_map()

        result['FeSpecType'] = []
        if self.fe_spec_type is not None:
            for k1 in self.fe_spec_type:
                result['FeSpecType'].append(k1.to_map() if k1 else None)

        if self.fe_storage is not None:
            result['FeStorage'] = self.fe_storage.to_map()

        if self.ha_fe_resource_spec is not None:
            result['HaFeResourceSpec'] = self.ha_fe_resource_spec.to_map()

        result['LocalSSDInstanceTypeConstraints'] = []
        if self.local_ssdinstance_type_constraints is not None:
            for k1 in self.local_ssdinstance_type_constraints:
                result['LocalSSDInstanceTypeConstraints'].append(k1.to_map() if k1 else None)

        if self.normal_fe_resource_spec is not None:
            result['NormalFeResourceSpec'] = self.normal_fe_resource_spec.to_map()

        result['SpecType'] = []
        if self.spec_type is not None:
            for k1 in self.spec_type:
                result['SpecType'].append(k1.to_map() if k1 else None)

        if self.split_disk_threshold_map is not None:
            result['SplitDiskThresholdMap'] = self.split_disk_threshold_map

        if self.version_constraint is not None:
            result['VersionConstraint'] = self.version_constraint.to_map()

        if self.zone_supported_eed_types is not None:
            result['ZoneSupportedEedTypes'] = self.zone_supported_eed_types

        if self.zone_supported_spec_types is not None:
            result['ZoneSupportedSpecTypes'] = self.zone_supported_spec_types

        if self.compaction_service_cu_constraint is not None:
            result['compactionServiceCuConstraint'] = self.compaction_service_cu_constraint.to_map()

        result['zoneSupportCompactionService'] = {}
        if self.zone_support_compaction_service is not None:
            for k1, v1 in self.zone_support_compaction_service.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['zoneSupportCompactionService'][k1] = l1

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentCu') is not None:
            self.agent_cu = m.get('AgentCu')

        if m.get('BeCu') is not None:
            self.be_cu = m.get('BeCu')

        if m.get('BeCuOnEcs') is not None:
            self.be_cu_on_ecs = m.get('BeCuOnEcs')

        if m.get('BeNumber') is not None:
            temp_model = main_models.DescribeResourceConstraintsResponseBodyDataBeNumber()
            self.be_number = temp_model.from_map(m.get('BeNumber'))

        self.be_storage_constraints = []
        if m.get('BeStorageConstraints') is not None:
            for k1 in m.get('BeStorageConstraints'):
                temp_model = main_models.DescribeResourceConstraintsResponseBodyDataBeStorageConstraints()
                self.be_storage_constraints.append(temp_model.from_map(k1))

        self.big_data_instance_type_constraints = []
        if m.get('BigDataInstanceTypeConstraints') is not None:
            for k1 in m.get('BigDataInstanceTypeConstraints'):
                temp_model = main_models.DescribeResourceConstraintsResponseBodyDataBigDataInstanceTypeConstraints()
                self.big_data_instance_type_constraints.append(temp_model.from_map(k1))

        if m.get('FeCu') is not None:
            self.fe_cu = m.get('FeCu')

        if m.get('FeCuOnEcs') is not None:
            self.fe_cu_on_ecs = m.get('FeCuOnEcs')

        if m.get('FeNumber') is not None:
            temp_model = main_models.DescribeResourceConstraintsResponseBodyDataFeNumber()
            self.fe_number = temp_model.from_map(m.get('FeNumber'))

        self.fe_spec_type = []
        if m.get('FeSpecType') is not None:
            for k1 in m.get('FeSpecType'):
                temp_model = main_models.DescribeResourceConstraintsResponseBodyDataFeSpecType()
                self.fe_spec_type.append(temp_model.from_map(k1))

        if m.get('FeStorage') is not None:
            temp_model = main_models.DescribeResourceConstraintsResponseBodyDataFeStorage()
            self.fe_storage = temp_model.from_map(m.get('FeStorage'))

        if m.get('HaFeResourceSpec') is not None:
            temp_model = main_models.DescribeResourceConstraintsResponseBodyDataHaFeResourceSpec()
            self.ha_fe_resource_spec = temp_model.from_map(m.get('HaFeResourceSpec'))

        self.local_ssdinstance_type_constraints = []
        if m.get('LocalSSDInstanceTypeConstraints') is not None:
            for k1 in m.get('LocalSSDInstanceTypeConstraints'):
                temp_model = main_models.DescribeResourceConstraintsResponseBodyDataLocalSSDInstanceTypeConstraints()
                self.local_ssdinstance_type_constraints.append(temp_model.from_map(k1))

        if m.get('NormalFeResourceSpec') is not None:
            temp_model = main_models.DescribeResourceConstraintsResponseBodyDataNormalFeResourceSpec()
            self.normal_fe_resource_spec = temp_model.from_map(m.get('NormalFeResourceSpec'))

        self.spec_type = []
        if m.get('SpecType') is not None:
            for k1 in m.get('SpecType'):
                temp_model = main_models.DescribeResourceConstraintsResponseBodyDataSpecType()
                self.spec_type.append(temp_model.from_map(k1))

        if m.get('SplitDiskThresholdMap') is not None:
            self.split_disk_threshold_map = m.get('SplitDiskThresholdMap')

        if m.get('VersionConstraint') is not None:
            temp_model = main_models.DescribeResourceConstraintsResponseBodyDataVersionConstraint()
            self.version_constraint = temp_model.from_map(m.get('VersionConstraint'))

        if m.get('ZoneSupportedEedTypes') is not None:
            self.zone_supported_eed_types = m.get('ZoneSupportedEedTypes')

        if m.get('ZoneSupportedSpecTypes') is not None:
            self.zone_supported_spec_types = m.get('ZoneSupportedSpecTypes')

        if m.get('compactionServiceCuConstraint') is not None:
            temp_model = main_models.DescribeResourceConstraintsResponseBodyDataCompactionServiceCuConstraint()
            self.compaction_service_cu_constraint = temp_model.from_map(m.get('compactionServiceCuConstraint'))

        self.zone_support_compaction_service = {}
        if m.get('zoneSupportCompactionService') is not None:
            for k1, v1 in m.get('zoneSupportCompactionService').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.DataZoneSupportCompactionServiceValue()
                    l1.append(temp_model.from_map(k2))
                self.zone_support_compaction_service[k1] = l1

        return self

class DescribeResourceConstraintsResponseBodyDataCompactionServiceCuConstraint(DaraModel):
    def __init__(
        self,
        def_: int = None,
        max: int = None,
        min: int = None,
        step: int = None,
    ):
        self.def_ = def_
        self.max = max
        self.min = min
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.def_ is not None:
            result['def'] = self.def_

        if self.max is not None:
            result['max'] = self.max

        if self.min is not None:
            result['min'] = self.min

        if self.step is not None:
            result['step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('def') is not None:
            self.def_ = m.get('def')

        if m.get('max') is not None:
            self.max = m.get('max')

        if m.get('min') is not None:
            self.min = m.get('min')

        if m.get('step') is not None:
            self.step = m.get('step')

        return self

class DescribeResourceConstraintsResponseBodyDataVersionConstraint(DaraModel):
    def __init__(
        self,
        beta_versions: List[str] = None,
        default_version: str = None,
        versions: List[str] = None,
    ):
        self.beta_versions = beta_versions
        self.default_version = default_version
        self.versions = versions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.beta_versions is not None:
            result['BetaVersions'] = self.beta_versions

        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version

        if self.versions is not None:
            result['Versions'] = self.versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BetaVersions') is not None:
            self.beta_versions = m.get('BetaVersions')

        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')

        if m.get('Versions') is not None:
            self.versions = m.get('Versions')

        return self

class DescribeResourceConstraintsResponseBodyDataSpecType(DaraModel):
    def __init__(
        self,
        display: str = None,
        name: str = None,
    ):
        self.display = display
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['Display'] = self.display

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeResourceConstraintsResponseBodyDataNormalFeResourceSpec(DaraModel):
    def __init__(
        self,
        cu: int = None,
        node_number: int = None,
        storage_size: int = None,
    ):
        self.cu = cu
        self.node_number = node_number
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['Cu'] = self.cu

        if self.node_number is not None:
            result['NodeNumber'] = self.node_number

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('NodeNumber') is not None:
            self.node_number = m.get('NodeNumber')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        return self

class DescribeResourceConstraintsResponseBodyDataLocalSSDInstanceTypeConstraints(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        disk_number: str = None,
        display: str = None,
        ecs_instance_type: str = None,
        instance_type: str = None,
        is_default: str = None,
        memory: int = None,
        storage_size: str = None,
    ):
        self.cpu = cpu
        self.disk_number = disk_number
        self.display = display
        self.ecs_instance_type = ecs_instance_type
        self.instance_type = instance_type
        self.is_default = is_default
        self.memory = memory
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.disk_number is not None:
            result['DiskNumber'] = self.disk_number

        if self.display is not None:
            result['Display'] = self.display

        if self.ecs_instance_type is not None:
            result['EcsInstanceType'] = self.ecs_instance_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DiskNumber') is not None:
            self.disk_number = m.get('DiskNumber')

        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('EcsInstanceType') is not None:
            self.ecs_instance_type = m.get('EcsInstanceType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        return self

class DescribeResourceConstraintsResponseBodyDataHaFeResourceSpec(DaraModel):
    def __init__(
        self,
        cu: int = None,
        node_number: int = None,
        storage_size: int = None,
    ):
        self.cu = cu
        self.node_number = node_number
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['Cu'] = self.cu

        if self.node_number is not None:
            result['NodeNumber'] = self.node_number

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('NodeNumber') is not None:
            self.node_number = m.get('NodeNumber')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        return self

class DescribeResourceConstraintsResponseBodyDataFeStorage(DaraModel):
    def __init__(
        self,
        default: int = None,
        max: int = None,
        min: int = None,
        step: int = None,
    ):
        self.default = default
        self.max = max
        self.min = min
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default is not None:
            result['Default'] = self.default

        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Default') is not None:
            self.default = m.get('Default')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

class DescribeResourceConstraintsResponseBodyDataFeSpecType(DaraModel):
    def __init__(
        self,
        display: str = None,
        name: str = None,
    ):
        self.display = display
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['Display'] = self.display

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeResourceConstraintsResponseBodyDataFeNumber(DaraModel):
    def __init__(
        self,
        default: int = None,
        max: int = None,
        min: int = None,
        step: int = None,
    ):
        self.default = default
        self.max = max
        self.min = min
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default is not None:
            result['Default'] = self.default

        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Default') is not None:
            self.default = m.get('Default')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

class DescribeResourceConstraintsResponseBodyDataBigDataInstanceTypeConstraints(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        disk_number: str = None,
        display: str = None,
        ecs_instance_type: str = None,
        instance_type: str = None,
        is_default: str = None,
        memory: int = None,
        storage_size: str = None,
    ):
        self.cpu = cpu
        self.disk_number = disk_number
        self.display = display
        self.ecs_instance_type = ecs_instance_type
        self.instance_type = instance_type
        self.is_default = is_default
        self.memory = memory
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.disk_number is not None:
            result['DiskNumber'] = self.disk_number

        if self.display is not None:
            result['Display'] = self.display

        if self.ecs_instance_type is not None:
            result['EcsInstanceType'] = self.ecs_instance_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DiskNumber') is not None:
            self.disk_number = m.get('DiskNumber')

        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('EcsInstanceType') is not None:
            self.ecs_instance_type = m.get('EcsInstanceType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        return self

class DescribeResourceConstraintsResponseBodyDataBeStorageConstraints(DaraModel):
    def __init__(
        self,
        desc: str = None,
        disk_number_constraint: main_models.DescribeResourceConstraintsResponseBodyDataBeStorageConstraintsDiskNumberConstraint = None,
        is_default: bool = None,
        level: str = None,
        value_constraint: main_models.DescribeResourceConstraintsResponseBodyDataBeStorageConstraintsValueConstraint = None,
    ):
        self.desc = desc
        self.disk_number_constraint = disk_number_constraint
        self.is_default = is_default
        self.level = level
        self.value_constraint = value_constraint

    def validate(self):
        if self.disk_number_constraint:
            self.disk_number_constraint.validate()
        if self.value_constraint:
            self.value_constraint.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.disk_number_constraint is not None:
            result['DiskNumberConstraint'] = self.disk_number_constraint.to_map()

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.level is not None:
            result['Level'] = self.level

        if self.value_constraint is not None:
            result['ValueConstraint'] = self.value_constraint.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('DiskNumberConstraint') is not None:
            temp_model = main_models.DescribeResourceConstraintsResponseBodyDataBeStorageConstraintsDiskNumberConstraint()
            self.disk_number_constraint = temp_model.from_map(m.get('DiskNumberConstraint'))

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('ValueConstraint') is not None:
            temp_model = main_models.DescribeResourceConstraintsResponseBodyDataBeStorageConstraintsValueConstraint()
            self.value_constraint = temp_model.from_map(m.get('ValueConstraint'))

        return self

class DescribeResourceConstraintsResponseBodyDataBeStorageConstraintsValueConstraint(DaraModel):
    def __init__(
        self,
        default: int = None,
        max: int = None,
        min: int = None,
        step: int = None,
    ):
        self.default = default
        self.max = max
        self.min = min
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default is not None:
            result['Default'] = self.default

        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Default') is not None:
            self.default = m.get('Default')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

class DescribeResourceConstraintsResponseBodyDataBeStorageConstraintsDiskNumberConstraint(DaraModel):
    def __init__(
        self,
        default: int = None,
        max: int = None,
        min: int = None,
        step: int = None,
    ):
        self.default = default
        self.max = max
        self.min = min
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default is not None:
            result['Default'] = self.default

        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Default') is not None:
            self.default = m.get('Default')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

class DescribeResourceConstraintsResponseBodyDataBeNumber(DaraModel):
    def __init__(
        self,
        default: int = None,
        max: int = None,
        min: int = None,
        step: int = None,
    ):
        self.default = default
        self.max = max
        self.min = min
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default is not None:
            result['Default'] = self.default

        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Default') is not None:
            self.default = m.get('Default')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

