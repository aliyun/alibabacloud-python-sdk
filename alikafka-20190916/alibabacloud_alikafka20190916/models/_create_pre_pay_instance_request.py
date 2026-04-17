# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class CreatePrePayInstanceRequest(DaraModel):
    def __init__(
        self,
        confluent_config: main_models.CreatePrePayInstanceRequestConfluentConfig = None,
        deploy_type: int = None,
        disk_size: int = None,
        disk_type: str = None,
        duration: int = None,
        eip_max: int = None,
        io_max_spec: str = None,
        paid_type: int = None,
        partition_num: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        spec_type: str = None,
        tag: List[main_models.CreatePrePayInstanceRequestTag] = None,
    ):
        self.confluent_config = confluent_config
        self.deploy_type = deploy_type
        self.disk_size = disk_size
        self.disk_type = disk_type
        self.duration = duration
        self.eip_max = eip_max
        self.io_max_spec = io_max_spec
        self.paid_type = paid_type
        self.partition_num = partition_num
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.spec_type = spec_type
        self.tag = tag

    def validate(self):
        if self.confluent_config:
            self.confluent_config.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confluent_config is not None:
            result['ConfluentConfig'] = self.confluent_config.to_map()

        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.eip_max is not None:
            result['EipMax'] = self.eip_max

        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec

        if self.paid_type is not None:
            result['PaidType'] = self.paid_type

        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfluentConfig') is not None:
            temp_model = main_models.CreatePrePayInstanceRequestConfluentConfig()
            self.confluent_config = temp_model.from_map(m.get('ConfluentConfig'))

        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')

        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')

        if m.get('PaidType') is not None:
            self.paid_type = m.get('PaidType')

        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreatePrePayInstanceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreatePrePayInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
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

class CreatePrePayInstanceRequestConfluentConfig(DaraModel):
    def __init__(
        self,
        connect_cu: int = None,
        connect_replica: int = None,
        control_center_cu: int = None,
        control_center_replica: int = None,
        control_center_storage: int = None,
        kafka_cu: int = None,
        kafka_replica: int = None,
        kafka_rest_proxy_cu: int = None,
        kafka_rest_proxy_replica: int = None,
        kafka_storage: int = None,
        ksql_cu: int = None,
        ksql_list: List[main_models.CreatePrePayInstanceRequestConfluentConfigKsqlList] = None,
        ksql_replica: int = None,
        ksql_storage: int = None,
        schema_registry_cu: int = None,
        schema_registry_replica: int = None,
        zoo_keeper_cu: int = None,
        zoo_keeper_replica: int = None,
        zoo_keeper_storage: int = None,
    ):
        self.connect_cu = connect_cu
        self.connect_replica = connect_replica
        self.control_center_cu = control_center_cu
        self.control_center_replica = control_center_replica
        self.control_center_storage = control_center_storage
        self.kafka_cu = kafka_cu
        self.kafka_replica = kafka_replica
        self.kafka_rest_proxy_cu = kafka_rest_proxy_cu
        self.kafka_rest_proxy_replica = kafka_rest_proxy_replica
        self.kafka_storage = kafka_storage
        self.ksql_cu = ksql_cu
        self.ksql_list = ksql_list
        self.ksql_replica = ksql_replica
        self.ksql_storage = ksql_storage
        self.schema_registry_cu = schema_registry_cu
        self.schema_registry_replica = schema_registry_replica
        self.zoo_keeper_cu = zoo_keeper_cu
        self.zoo_keeper_replica = zoo_keeper_replica
        self.zoo_keeper_storage = zoo_keeper_storage

    def validate(self):
        if self.ksql_list:
            for v1 in self.ksql_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_cu is not None:
            result['ConnectCU'] = self.connect_cu

        if self.connect_replica is not None:
            result['ConnectReplica'] = self.connect_replica

        if self.control_center_cu is not None:
            result['ControlCenterCU'] = self.control_center_cu

        if self.control_center_replica is not None:
            result['ControlCenterReplica'] = self.control_center_replica

        if self.control_center_storage is not None:
            result['ControlCenterStorage'] = self.control_center_storage

        if self.kafka_cu is not None:
            result['KafkaCU'] = self.kafka_cu

        if self.kafka_replica is not None:
            result['KafkaReplica'] = self.kafka_replica

        if self.kafka_rest_proxy_cu is not None:
            result['KafkaRestProxyCU'] = self.kafka_rest_proxy_cu

        if self.kafka_rest_proxy_replica is not None:
            result['KafkaRestProxyReplica'] = self.kafka_rest_proxy_replica

        if self.kafka_storage is not None:
            result['KafkaStorage'] = self.kafka_storage

        if self.ksql_cu is not None:
            result['KsqlCU'] = self.ksql_cu

        result['KsqlList'] = []
        if self.ksql_list is not None:
            for k1 in self.ksql_list:
                result['KsqlList'].append(k1.to_map() if k1 else None)

        if self.ksql_replica is not None:
            result['KsqlReplica'] = self.ksql_replica

        if self.ksql_storage is not None:
            result['KsqlStorage'] = self.ksql_storage

        if self.schema_registry_cu is not None:
            result['SchemaRegistryCU'] = self.schema_registry_cu

        if self.schema_registry_replica is not None:
            result['SchemaRegistryReplica'] = self.schema_registry_replica

        if self.zoo_keeper_cu is not None:
            result['ZooKeeperCU'] = self.zoo_keeper_cu

        if self.zoo_keeper_replica is not None:
            result['ZooKeeperReplica'] = self.zoo_keeper_replica

        if self.zoo_keeper_storage is not None:
            result['ZooKeeperStorage'] = self.zoo_keeper_storage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectCU') is not None:
            self.connect_cu = m.get('ConnectCU')

        if m.get('ConnectReplica') is not None:
            self.connect_replica = m.get('ConnectReplica')

        if m.get('ControlCenterCU') is not None:
            self.control_center_cu = m.get('ControlCenterCU')

        if m.get('ControlCenterReplica') is not None:
            self.control_center_replica = m.get('ControlCenterReplica')

        if m.get('ControlCenterStorage') is not None:
            self.control_center_storage = m.get('ControlCenterStorage')

        if m.get('KafkaCU') is not None:
            self.kafka_cu = m.get('KafkaCU')

        if m.get('KafkaReplica') is not None:
            self.kafka_replica = m.get('KafkaReplica')

        if m.get('KafkaRestProxyCU') is not None:
            self.kafka_rest_proxy_cu = m.get('KafkaRestProxyCU')

        if m.get('KafkaRestProxyReplica') is not None:
            self.kafka_rest_proxy_replica = m.get('KafkaRestProxyReplica')

        if m.get('KafkaStorage') is not None:
            self.kafka_storage = m.get('KafkaStorage')

        if m.get('KsqlCU') is not None:
            self.ksql_cu = m.get('KsqlCU')

        self.ksql_list = []
        if m.get('KsqlList') is not None:
            for k1 in m.get('KsqlList'):
                temp_model = main_models.CreatePrePayInstanceRequestConfluentConfigKsqlList()
                self.ksql_list.append(temp_model.from_map(k1))

        if m.get('KsqlReplica') is not None:
            self.ksql_replica = m.get('KsqlReplica')

        if m.get('KsqlStorage') is not None:
            self.ksql_storage = m.get('KsqlStorage')

        if m.get('SchemaRegistryCU') is not None:
            self.schema_registry_cu = m.get('SchemaRegistryCU')

        if m.get('SchemaRegistryReplica') is not None:
            self.schema_registry_replica = m.get('SchemaRegistryReplica')

        if m.get('ZooKeeperCU') is not None:
            self.zoo_keeper_cu = m.get('ZooKeeperCU')

        if m.get('ZooKeeperReplica') is not None:
            self.zoo_keeper_replica = m.get('ZooKeeperReplica')

        if m.get('ZooKeeperStorage') is not None:
            self.zoo_keeper_storage = m.get('ZooKeeperStorage')

        return self

class CreatePrePayInstanceRequestConfluentConfigKsqlList(DaraModel):
    def __init__(
        self,
        internal_id: str = None,
        cu: int = None,
        replica: int = None,
        storage: int = None,
        type: str = None,
    ):
        self.internal_id = internal_id
        self.cu = cu
        self.replica = replica
        self.storage = storage
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internal_id is not None:
            result['InternalId'] = self.internal_id

        if self.cu is not None:
            result['cu'] = self.cu

        if self.replica is not None:
            result['replica'] = self.replica

        if self.storage is not None:
            result['storage'] = self.storage

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternalId') is not None:
            self.internal_id = m.get('InternalId')

        if m.get('cu') is not None:
            self.cu = m.get('cu')

        if m.get('replica') is not None:
            self.replica = m.get('replica')

        if m.get('storage') is not None:
            self.storage = m.get('storage')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

