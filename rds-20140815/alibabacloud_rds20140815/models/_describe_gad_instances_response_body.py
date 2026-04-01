# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeGadInstancesResponseBody(DaraModel):
    def __init__(
        self,
        gad_instances: List[main_models.DescribeGadInstancesResponseBodyGadInstances] = None,
        request_id: str = None,
    ):
        # The details about the global active database cluster.
        self.gad_instances = gad_instances
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.gad_instances:
            for v1 in self.gad_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GadInstances'] = []
        if self.gad_instances is not None:
            for k1 in self.gad_instances:
                result['GadInstances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gad_instances = []
        if m.get('GadInstances') is not None:
            for k1 in m.get('GadInstances'):
                temp_model = main_models.DescribeGadInstancesResponseBodyGadInstances()
                self.gad_instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeGadInstancesResponseBodyGadInstances(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        gad_instance_members: List[main_models.DescribeGadInstancesResponseBodyGadInstancesGadInstanceMembers] = None,
        gad_instance_name: str = None,
        modification_time: str = None,
        service: str = None,
        status: str = None,
    ):
        # The time when the global active database cluster was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The name of the cluster.
        self.description = description
        # The information about each node in the cluster.
        self.gad_instance_members = gad_instance_members
        # The ID of the global active database cluster.
        self.gad_instance_name = gad_instance_name
        # The time when the most recent modification was made to the global active database cluster. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.modification_time = modification_time
        # The database engine that is run by the global active database cluster.
        # 
        # >  The value of this parameter is fixed as **mysql**.
        self.service = service
        # The status of the cluster. Valid values:
        # 
        # *   **activation**: The cluster is running.
        # *   **creating**: The cluster is being created.
        # *   **replica_adding**: Nodes are being added to the cluster.
        self.status = status

    def validate(self):
        if self.gad_instance_members:
            for v1 in self.gad_instance_members:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        result['GadInstanceMembers'] = []
        if self.gad_instance_members is not None:
            for k1 in self.gad_instance_members:
                result['GadInstanceMembers'].append(k1.to_map() if k1 else None)

        if self.gad_instance_name is not None:
            result['GadInstanceName'] = self.gad_instance_name

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.service is not None:
            result['Service'] = self.service

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.gad_instance_members = []
        if m.get('GadInstanceMembers') is not None:
            for k1 in m.get('GadInstanceMembers'):
                temp_model = main_models.DescribeGadInstancesResponseBodyGadInstancesGadInstanceMembers()
                self.gad_instance_members.append(temp_model.from_map(k1))

        if m.get('GadInstanceName') is not None:
            self.gad_instance_name = m.get('GadInstanceName')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeGadInstancesResponseBodyGadInstancesGadInstanceMembers(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dts_instance: str = None,
        engine: str = None,
        engine_version: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        role: str = None,
        status: str = None,
    ):
        # The ID of the node.
        self.dbinstance_id = dbinstance_id
        # A JSON array that consists of the details about the Data Transmission Service (DTS) synchronization task.
        # 
        # >  Each unit node (secondary node) synchronizes data from the central node (primary node) by using DTS. This parameter contains the synchronization link ID and request ID of DTS.
        self.dts_instance = dts_instance
        # The database engine that is run by the node.
        # 
        # >  The value of this parameter is fixed as **mysql**.
        self.engine = engine
        # The database engine version that is run by the node.
        self.engine_version = engine_version
        # The ID of the region where the node resides.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The type of the node. Valid values:
        # 
        # *   **CENTRAL**: The node is a central node. Each global active database cluster has only one central node. All unit nodes synchronize data from the central node.
        # *   **UNIT**: The node is a unit node. Each global active database cluster can have up to 10 unit nodes. All unit nodes synchronize data from the central node.
        self.role = role
        # The node status. Valid values:
        # 
        # *   **activation**: The node is running.
        # *   **creating**: The node is being created.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceID'] = self.dbinstance_id

        if self.dts_instance is not None:
            result['DtsInstance'] = self.dts_instance

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.role is not None:
            result['Role'] = self.role

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceID') is not None:
            self.dbinstance_id = m.get('DBInstanceID')

        if m.get('DtsInstance') is not None:
            self.dts_instance = m.get('DtsInstance')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

