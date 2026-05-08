# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeAvailableResourceResponseBody(DaraModel):
    def __init__(
        self,
        available_zone_list: List[main_models.DescribeAvailableResourceResponseBodyAvailableZoneList] = None,
        region_id: str = None,
        request_id: str = None,
    ):
        # The supported zones.
        self.available_zone_list = available_zone_list
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.available_zone_list:
            for v1 in self.available_zone_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableZoneList'] = []
        if self.available_zone_list is not None:
            for k1 in self.available_zone_list:
                result['AvailableZoneList'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_zone_list = []
        if m.get('AvailableZoneList') is not None:
            for k1 in m.get('AvailableZoneList'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZoneList()
                self.available_zone_list.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAvailableResourceResponseBodyAvailableZoneList(DaraModel):
    def __init__(
        self,
        supported_compute_resource: List[str] = None,
        supported_mode: List[main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedMode] = None,
        supported_storage_resource: List[str] = None,
        zone_id: str = None,
        zone_name: str = None,
    ):
        # A reserved parameter.
        self.supported_compute_resource = supported_compute_resource
        # The supported modes.
        self.supported_mode = supported_mode
        # A reserved parameter.
        self.supported_storage_resource = supported_storage_resource
        # The zone ID.
        self.zone_id = zone_id
        # The name of the zone.
        self.zone_name = zone_name

    def validate(self):
        if self.supported_mode:
            for v1 in self.supported_mode:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_compute_resource is not None:
            result['SupportedComputeResource'] = self.supported_compute_resource

        result['SupportedMode'] = []
        if self.supported_mode is not None:
            for k1 in self.supported_mode:
                result['SupportedMode'].append(k1.to_map() if k1 else None)

        if self.supported_storage_resource is not None:
            result['SupportedStorageResource'] = self.supported_storage_resource

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedComputeResource') is not None:
            self.supported_compute_resource = m.get('SupportedComputeResource')

        self.supported_mode = []
        if m.get('SupportedMode') is not None:
            for k1 in m.get('SupportedMode'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedMode()
                self.supported_mode.append(temp_model.from_map(k1))

        if m.get('SupportedStorageResource') is not None:
            self.supported_storage_resource = m.get('SupportedStorageResource')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedMode(DaraModel):
    def __init__(
        self,
        mode: str = None,
        supported_serial_list: List[main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialList] = None,
    ):
        # The supported mode. Valid values:
        # 
        # *   **flexible**: elastic mode.
        # *   **reserver**: reserved mode.
        self.mode = mode
        # The supported editions.
        self.supported_serial_list = supported_serial_list

    def validate(self):
        if self.supported_serial_list:
            for v1 in self.supported_serial_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['Mode'] = self.mode

        result['SupportedSerialList'] = []
        if self.supported_serial_list is not None:
            for k1 in self.supported_serial_list:
                result['SupportedSerialList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        self.supported_serial_list = []
        if m.get('SupportedSerialList') is not None:
            for k1 in m.get('SupportedSerialList'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialList()
                self.supported_serial_list.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialList(DaraModel):
    def __init__(
        self,
        serial: str = None,
        supported_flexible_resource: List[main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResource] = None,
        supported_instance_class_list: List[main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassList] = None,
    ):
        # The supported edition. Valid values:
        # 
        # *   **basic**: Basic Edition.
        # *   **cluster**: Cluster Edition.
        # *   **mixed_storage**: elastic mode for Cluster Edition.
        self.serial = serial
        # The supported resources in elastic mode.
        self.supported_flexible_resource = supported_flexible_resource
        # The supported resources in reserved mode.
        self.supported_instance_class_list = supported_instance_class_list

    def validate(self):
        if self.supported_flexible_resource:
            for v1 in self.supported_flexible_resource:
                 if v1:
                    v1.validate()
        if self.supported_instance_class_list:
            for v1 in self.supported_instance_class_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.serial is not None:
            result['Serial'] = self.serial

        result['SupportedFlexibleResource'] = []
        if self.supported_flexible_resource is not None:
            for k1 in self.supported_flexible_resource:
                result['SupportedFlexibleResource'].append(k1.to_map() if k1 else None)

        result['SupportedInstanceClassList'] = []
        if self.supported_instance_class_list is not None:
            for k1 in self.supported_instance_class_list:
                result['SupportedInstanceClassList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Serial') is not None:
            self.serial = m.get('Serial')

        self.supported_flexible_resource = []
        if m.get('SupportedFlexibleResource') is not None:
            for k1 in m.get('SupportedFlexibleResource'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResource()
                self.supported_flexible_resource.append(temp_model.from_map(k1))

        self.supported_instance_class_list = []
        if m.get('SupportedInstanceClassList') is not None:
            for k1 in m.get('SupportedInstanceClassList'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassList()
                self.supported_instance_class_list.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassList(DaraModel):
    def __init__(
        self,
        instance_class: str = None,
        supported_executor_list: List[main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorList] = None,
        supported_node_count_list: List[main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountList] = None,
        tips: str = None,
    ):
        # The supported instance type.
        self.instance_class = instance_class
        # A reserved parameter.
        self.supported_executor_list = supported_executor_list
        # The supported compute nodes.
        self.supported_node_count_list = supported_node_count_list
        # The description of the instance type.
        self.tips = tips

    def validate(self):
        if self.supported_executor_list:
            for v1 in self.supported_executor_list:
                 if v1:
                    v1.validate()
        if self.supported_node_count_list:
            for v1 in self.supported_node_count_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        result['SupportedExecutorList'] = []
        if self.supported_executor_list is not None:
            for k1 in self.supported_executor_list:
                result['SupportedExecutorList'].append(k1.to_map() if k1 else None)

        result['SupportedNodeCountList'] = []
        if self.supported_node_count_list is not None:
            for k1 in self.supported_node_count_list:
                result['SupportedNodeCountList'].append(k1.to_map() if k1 else None)

        if self.tips is not None:
            result['Tips'] = self.tips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        self.supported_executor_list = []
        if m.get('SupportedExecutorList') is not None:
            for k1 in m.get('SupportedExecutorList'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorList()
                self.supported_executor_list.append(temp_model.from_map(k1))

        self.supported_node_count_list = []
        if m.get('SupportedNodeCountList') is not None:
            for k1 in m.get('SupportedNodeCountList'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountList()
                self.supported_node_count_list.append(temp_model.from_map(k1))

        if m.get('Tips') is not None:
            self.tips = m.get('Tips')

        return self

class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountList(DaraModel):
    def __init__(
        self,
        node_count: main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountListNodeCount = None,
        storage_size: List[str] = None,
    ):
        # The number of the supported compute nodes.
        self.node_count = node_count
        # The support storage capacity. Unit: GB.
        self.storage_size = storage_size

    def validate(self):
        if self.node_count:
            self.node_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_count is not None:
            result['NodeCount'] = self.node_count.to_map()

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeCount') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountListNodeCount()
            self.node_count = temp_model.from_map(m.get('NodeCount'))

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        return self

class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedNodeCountListNodeCount(DaraModel):
    def __init__(
        self,
        max_count: str = None,
        min_count: str = None,
        step: str = None,
    ):
        # The maximum number of compute nodes.
        self.max_count = max_count
        # The minimum number of compute nodes.
        self.min_count = min_count
        # The step size.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_count is not None:
            result['MaxCount'] = self.max_count

        if self.min_count is not None:
            result['MinCount'] = self.min_count

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')

        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorList(DaraModel):
    def __init__(
        self,
        node_count: main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorListNodeCount = None,
    ):
        # The information about the supported compute nodes.
        self.node_count = node_count

    def validate(self):
        if self.node_count:
            self.node_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_count is not None:
            result['NodeCount'] = self.node_count.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeCount') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorListNodeCount()
            self.node_count = temp_model.from_map(m.get('NodeCount'))

        return self

class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedInstanceClassListSupportedExecutorListNodeCount(DaraModel):
    def __init__(
        self,
        max_count: str = None,
        min_count: str = None,
        step: str = None,
    ):
        # A reserved parameter.
        self.max_count = max_count
        # A reserved parameter.
        self.min_count = min_count
        # A reserved parameter.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_count is not None:
            result['MaxCount'] = self.max_count

        if self.min_count is not None:
            result['MinCount'] = self.min_count

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')

        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResource(DaraModel):
    def __init__(
        self,
        storage_type: str = None,
        supported_compute_resource: List[str] = None,
        supported_elastic_ioresource: main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResourceSupportedElasticIOResource = None,
        supported_storage_resource: List[str] = None,
    ):
        # The disk storage type. Valid values:
        # 
        # *   **hdd**
        # *   **ssd**
        self.storage_type = storage_type
        # The supported computing resources.
        self.supported_compute_resource = supported_compute_resource
        # The supported elastic I/O resources.
        self.supported_elastic_ioresource = supported_elastic_ioresource
        # The supported storage resources.
        self.supported_storage_resource = supported_storage_resource

    def validate(self):
        if self.supported_elastic_ioresource:
            self.supported_elastic_ioresource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.supported_compute_resource is not None:
            result['SupportedComputeResource'] = self.supported_compute_resource

        if self.supported_elastic_ioresource is not None:
            result['SupportedElasticIOResource'] = self.supported_elastic_ioresource.to_map()

        if self.supported_storage_resource is not None:
            result['SupportedStorageResource'] = self.supported_storage_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('SupportedComputeResource') is not None:
            self.supported_compute_resource = m.get('SupportedComputeResource')

        if m.get('SupportedElasticIOResource') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResourceSupportedElasticIOResource()
            self.supported_elastic_ioresource = temp_model.from_map(m.get('SupportedElasticIOResource'))

        if m.get('SupportedStorageResource') is not None:
            self.supported_storage_resource = m.get('SupportedStorageResource')

        return self

class DescribeAvailableResourceResponseBodyAvailableZoneListSupportedModeSupportedSerialListSupportedFlexibleResourceSupportedElasticIOResource(DaraModel):
    def __init__(
        self,
        max_count: str = None,
        min_count: str = None,
        step: str = None,
    ):
        # The maximum amount of elastic I/O resources.
        self.max_count = max_count
        # The minimum amount of elastic I/O resources.
        self.min_count = min_count
        # The step size.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_count is not None:
            result['MaxCount'] = self.max_count

        if self.min_count is not None:
            result['MinCount'] = self.min_count

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')

        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

