# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListInstancesResponseBodyInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of instance information.
        self.instances = instances
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
                temp_model = main_models.ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        cross_region_replication: str = None,
        cross_region_replication_role: str = None,
        default_endpoint: main_models.ListInstancesResponseBodyInstancesDefaultEndpoint = None,
        description: str = None,
        instance_failover_status: str = None,
        instance_id: str = None,
        managed_service_code: str = None,
        replication_configuration: main_models.ListInstancesResponseBodyInstancesReplicationConfiguration = None,
        service_managed: bool = None,
        status: str = None,
    ):
        # The instance creation time, in UNIX timestamp format. Unit: milliseconds.
        self.create_time = create_time
        # Indicates whether cross-region replication is enabled. Valid values: enabled or disabled.
        self.cross_region_replication = cross_region_replication
        # The cross-region replication role. Valid values: primary (primary instance) or backup (backup instance).
        self.cross_region_replication_role = cross_region_replication_role
        # The default endpoint of the instance.
        self.default_endpoint = default_endpoint
        # The instance description.
        self.description = description
        # The instance failover activation status. Valid values: active (activated) or inactive (not activated).
        self.instance_failover_status = instance_failover_status
        # The instance ID.
        self.instance_id = instance_id
        # The service code of the Alibaba Cloud service that manages the instance.
        self.managed_service_code = managed_service_code
        # The replication configuration. This parameter is returned only when CrossRegionReplication is set to enabled.
        self.replication_configuration = replication_configuration
        # Indicates whether the instance is managed by an Alibaba Cloud service.
        self.service_managed = service_managed
        # The instance status. Valid values:
        # - creating: Being created.
        # - running: Running.
        self.status = status

    def validate(self):
        if self.default_endpoint:
            self.default_endpoint.validate()
        if self.replication_configuration:
            self.replication_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cross_region_replication is not None:
            result['CrossRegionReplication'] = self.cross_region_replication

        if self.cross_region_replication_role is not None:
            result['CrossRegionReplicationRole'] = self.cross_region_replication_role

        if self.default_endpoint is not None:
            result['DefaultEndpoint'] = self.default_endpoint.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_failover_status is not None:
            result['InstanceFailoverStatus'] = self.instance_failover_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.managed_service_code is not None:
            result['ManagedServiceCode'] = self.managed_service_code

        if self.replication_configuration is not None:
            result['ReplicationConfiguration'] = self.replication_configuration.to_map()

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CrossRegionReplication') is not None:
            self.cross_region_replication = m.get('CrossRegionReplication')

        if m.get('CrossRegionReplicationRole') is not None:
            self.cross_region_replication_role = m.get('CrossRegionReplicationRole')

        if m.get('DefaultEndpoint') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstancesDefaultEndpoint()
            self.default_endpoint = temp_model.from_map(m.get('DefaultEndpoint'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceFailoverStatus') is not None:
            self.instance_failover_status = m.get('InstanceFailoverStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ManagedServiceCode') is not None:
            self.managed_service_code = m.get('ManagedServiceCode')

        if m.get('ReplicationConfiguration') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstancesReplicationConfiguration()
            self.replication_configuration = temp_model.from_map(m.get('ReplicationConfiguration'))

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListInstancesResponseBodyInstancesReplicationConfiguration(DaraModel):
    def __init__(
        self,
        backup_instance_id: str = None,
        backup_instance_region_id: str = None,
        primary_instance_id: str = None,
        primary_instance_region_id: str = None,
        replication_create_time: int = None,
    ):
        # The instance ID of the backup instance.
        self.backup_instance_id = backup_instance_id
        # The region ID of the backup instance.
        self.backup_instance_region_id = backup_instance_region_id
        # The instance ID of the primary instance.
        self.primary_instance_id = primary_instance_id
        # The region ID of the primary instance.
        self.primary_instance_region_id = primary_instance_region_id
        # The time when the disaster recovery data replication was created, in UNIX timestamp format. Unit: milliseconds.
        self.replication_create_time = replication_create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_instance_id is not None:
            result['BackupInstanceId'] = self.backup_instance_id

        if self.backup_instance_region_id is not None:
            result['BackupInstanceRegionId'] = self.backup_instance_region_id

        if self.primary_instance_id is not None:
            result['PrimaryInstanceId'] = self.primary_instance_id

        if self.primary_instance_region_id is not None:
            result['PrimaryInstanceRegionId'] = self.primary_instance_region_id

        if self.replication_create_time is not None:
            result['ReplicationCreateTime'] = self.replication_create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupInstanceId') is not None:
            self.backup_instance_id = m.get('BackupInstanceId')

        if m.get('BackupInstanceRegionId') is not None:
            self.backup_instance_region_id = m.get('BackupInstanceRegionId')

        if m.get('PrimaryInstanceId') is not None:
            self.primary_instance_id = m.get('PrimaryInstanceId')

        if m.get('PrimaryInstanceRegionId') is not None:
            self.primary_instance_region_id = m.get('PrimaryInstanceRegionId')

        if m.get('ReplicationCreateTime') is not None:
            self.replication_create_time = m.get('ReplicationCreateTime')

        return self

class ListInstancesResponseBodyInstancesDefaultEndpoint(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        status: str = None,
    ):
        # The endpoint address of the instance.
        self.endpoint = endpoint
        # The endpoint status. Valid values:
        # - resolved: Resolved.
        # - unresolved: Not resolved.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

