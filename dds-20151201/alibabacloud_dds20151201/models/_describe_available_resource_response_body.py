# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeAvailableResourceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        supported_dbtypes: main_models.DescribeAvailableResourceResponseBodySupportedDBTypes = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The supported database types.
        self.supported_dbtypes = supported_dbtypes

    def validate(self):
        if self.supported_dbtypes:
            self.supported_dbtypes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.supported_dbtypes is not None:
            result['SupportedDBTypes'] = self.supported_dbtypes.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SupportedDBTypes') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodySupportedDBTypes()
            self.supported_dbtypes = temp_model.from_map(m.get('SupportedDBTypes'))

        return self

class DescribeAvailableResourceResponseBodySupportedDBTypes(DaraModel):
    def __init__(
        self,
        supported_dbtype: List[main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBType] = None,
    ):
        self.supported_dbtype = supported_dbtype

    def validate(self):
        if self.supported_dbtype:
            for v1 in self.supported_dbtype:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedDBType'] = []
        if self.supported_dbtype is not None:
            for k1 in self.supported_dbtype:
                result['SupportedDBType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_dbtype = []
        if m.get('SupportedDBType') is not None:
            for k1 in m.get('SupportedDBType'):
                temp_model = main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBType()
                self.supported_dbtype.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBType(DaraModel):
    def __init__(
        self,
        available_zones: main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZones = None,
        db_type: str = None,
    ):
        # The available zones.
        self.available_zones = available_zones
        # The architecture of the instance. Valid values:
        # 
        # *   **normal**: replica set instance
        # *   **sharding**: sharded cluster instance
        self.db_type = db_type

    def validate(self):
        if self.available_zones:
            self.available_zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones.to_map()

        if self.db_type is not None:
            result['DbType'] = self.db_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableZones') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZones()
            self.available_zones = temp_model.from_map(m.get('AvailableZones'))

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        return self

class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZones(DaraModel):
    def __init__(
        self,
        available_zone: List[main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZone] = None,
    ):
        self.available_zone = available_zone

    def validate(self):
        if self.available_zone:
            for v1 in self.available_zone:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableZone'] = []
        if self.available_zone is not None:
            for k1 in self.available_zone:
                result['AvailableZone'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_zone = []
        if m.get('AvailableZone') is not None:
            for k1 in m.get('AvailableZone'):
                temp_model = main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZone()
                self.available_zone.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZone(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        supported_engine_versions: main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersions = None,
        zone_id: str = None,
    ):
        # The ID of the region.
        self.region_id = region_id
        # The supported storage engine versions.
        self.supported_engine_versions = supported_engine_versions
        # The ID of the zone.
        self.zone_id = zone_id

    def validate(self):
        if self.supported_engine_versions:
            self.supported_engine_versions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.supported_engine_versions is not None:
            result['SupportedEngineVersions'] = self.supported_engine_versions.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SupportedEngineVersions') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersions()
            self.supported_engine_versions = temp_model.from_map(m.get('SupportedEngineVersions'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersions(DaraModel):
    def __init__(
        self,
        supported_engine_version: List[main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersion] = None,
    ):
        self.supported_engine_version = supported_engine_version

    def validate(self):
        if self.supported_engine_version:
            for v1 in self.supported_engine_version:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedEngineVersion'] = []
        if self.supported_engine_version is not None:
            for k1 in self.supported_engine_version:
                result['SupportedEngineVersion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_engine_version = []
        if m.get('SupportedEngineVersion') is not None:
            for k1 in m.get('SupportedEngineVersion'):
                temp_model = main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersion()
                self.supported_engine_version.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersion(DaraModel):
    def __init__(
        self,
        supported_engines: main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEngines = None,
        version: str = None,
    ):
        # The supported storage engines.
        self.supported_engines = supported_engines
        # The database engine version of the instance.
        self.version = version

    def validate(self):
        if self.supported_engines:
            self.supported_engines.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_engines is not None:
            result['SupportedEngines'] = self.supported_engines.to_map()

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedEngines') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEngines()
            self.supported_engines = temp_model.from_map(m.get('SupportedEngines'))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEngines(DaraModel):
    def __init__(
        self,
        supported_engine: List[main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngine] = None,
    ):
        self.supported_engine = supported_engine

    def validate(self):
        if self.supported_engine:
            for v1 in self.supported_engine:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedEngine'] = []
        if self.supported_engine is not None:
            for k1 in self.supported_engine:
                result['SupportedEngine'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_engine = []
        if m.get('SupportedEngine') is not None:
            for k1 in m.get('SupportedEngine'):
                temp_model = main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngine()
                self.supported_engine.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngine(DaraModel):
    def __init__(
        self,
        engine: str = None,
        supported_node_types: main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypes = None,
    ):
        # The storage engine of the instance.
        self.engine = engine
        # The supported instance types.
        self.supported_node_types = supported_node_types

    def validate(self):
        if self.supported_node_types:
            self.supported_node_types.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.supported_node_types is not None:
            result['SupportedNodeTypes'] = self.supported_node_types.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('SupportedNodeTypes') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypes()
            self.supported_node_types = temp_model.from_map(m.get('SupportedNodeTypes'))

        return self

class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypes(DaraModel):
    def __init__(
        self,
        supported_node_type: List[main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeType] = None,
    ):
        self.supported_node_type = supported_node_type

    def validate(self):
        if self.supported_node_type:
            for v1 in self.supported_node_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedNodeType'] = []
        if self.supported_node_type is not None:
            for k1 in self.supported_node_type:
                result['SupportedNodeType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_node_type = []
        if m.get('SupportedNodeType') is not None:
            for k1 in m.get('SupportedNodeType'):
                temp_model = main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeType()
                self.supported_node_type.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeType(DaraModel):
    def __init__(
        self,
        available_resources: main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResources = None,
        network_types: str = None,
        node_type: str = None,
    ):
        # The details of the available resources.
        self.available_resources = available_resources
        # The network type of the instance.
        self.network_types = network_types
        # The number of nodes in the instance.
        self.node_type = node_type

    def validate(self):
        if self.available_resources:
            self.available_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_resources is not None:
            result['AvailableResources'] = self.available_resources.to_map()

        if self.network_types is not None:
            result['NetworkTypes'] = self.network_types

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableResources') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResources()
            self.available_resources = temp_model.from_map(m.get('AvailableResources'))

        if m.get('NetworkTypes') is not None:
            self.network_types = m.get('NetworkTypes')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        return self

class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResources(DaraModel):
    def __init__(
        self,
        available_resource: List[main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResource] = None,
    ):
        self.available_resource = available_resource

    def validate(self):
        if self.available_resource:
            for v1 in self.available_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableResource'] = []
        if self.available_resource is not None:
            for k1 in self.available_resource:
                result['AvailableResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_resource = []
        if m.get('AvailableResource') is not None:
            for k1 in m.get('AvailableResource'):
                temp_model = main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResource()
                self.available_resource.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResource(DaraModel):
    def __init__(
        self,
        dbinstance_storage_range: main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResourceDBInstanceStorageRange = None,
        instance_class: str = None,
        instance_class_remark: str = None,
    ):
        # The storage capacity range of the instance.
        self.dbinstance_storage_range = dbinstance_storage_range
        # The instance family.
        self.instance_class = instance_class
        # The type of the instance.
        self.instance_class_remark = instance_class_remark

    def validate(self):
        if self.dbinstance_storage_range:
            self.dbinstance_storage_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_storage_range is not None:
            result['DBInstanceStorageRange'] = self.dbinstance_storage_range.to_map()

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_class_remark is not None:
            result['InstanceClassRemark'] = self.instance_class_remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceStorageRange') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResourceDBInstanceStorageRange()
            self.dbinstance_storage_range = temp_model.from_map(m.get('DBInstanceStorageRange'))

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceClassRemark') is not None:
            self.instance_class_remark = m.get('InstanceClassRemark')

        return self

class DescribeAvailableResourceResponseBodySupportedDBTypesSupportedDBTypeAvailableZonesAvailableZoneSupportedEngineVersionsSupportedEngineVersionSupportedEnginesSupportedEngineSupportedNodeTypesSupportedNodeTypeAvailableResourcesAvailableResourceDBInstanceStorageRange(DaraModel):
    def __init__(
        self,
        max: int = None,
        min: int = None,
        step: int = None,
    ):
        # The maximum storage capacity. Unit: GB.
        self.max = max
        # The minimum storage capacity. Unit: GB.
        self.min = min
        # The step size for adjusting the storage capacity. Unit: GB.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

