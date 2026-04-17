# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class CreatePrePayOrderRequest(DaraModel):
    def __init__(
        self,
        confluent_config: main_models.CreatePrePayOrderRequestConfluentConfig = None,
        deploy_type: int = None,
        disk_size: int = None,
        disk_type: str = None,
        duration: int = None,
        eip_max: int = None,
        io_max: int = None,
        io_max_spec: str = None,
        paid_type: int = None,
        partition_num: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        spec_type: str = None,
        tag: List[main_models.CreatePrePayOrderRequestTag] = None,
        topic_quota: int = None,
    ):
        # The configurations of Confluent.
        # 
        # >  When you create an ApsaraMQ for Confluent instance, you must configure this parameter.
        self.confluent_config = confluent_config
        # The type of the network in which the instance is deployed. Valid values:
        # 
        # *   **4**: Internet and virtual private cloud (VPC)
        # *   **5**: VPC
        # 
        # >  If you create an ApsaraMQ for Confluent instance, set the value to 5. After the instance is created, you can specify whether to enable each component.
        self.deploy_type = deploy_type
        # The disk size. Unit: GB
        # 
        # For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.disk_size = disk_size
        # The disk type. Valid values:
        # 
        # *   **0**: ultra disk
        # *   **1**: standard SSD
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.disk_type = disk_type
        # The subscription duration. Unit: months. Default value: 1. Valid values:
        # 
        # *   **1 to 12**
        self.duration = duration
        # The maximum Internet traffic in the instance.
        # 
        # *   If you set **DeployType** to **4**, you must configure this parameter.
        # *   For information about the valid values, see [Pay-as-you-go](https://help.aliyun.com/document_detail/72142.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.eip_max = eip_max
        # The maximum traffic in the instance. We recommend that you do not configure this parameter.
        # 
        # *   You must set one of **IoMax** and **IoMaxSpec**. If both parameters are configured, the value of **IoMaxSpec** is used. We recommend that you configure only **IoMaxSpec**.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.io_max = io_max
        # The traffic specification of the instance. We recommend that you configure this parameter.
        # 
        # *   You must configure one of **IoMax** and **IoMaxSpec**. If both parameters are configured, the value of **IoMaxSpec** is used. We recommend that you configure only **IoMaxSpec**.
        # *   For more information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.io_max_spec = io_max_spec
        # The billing method of the instance. Valid values:
        # 
        # *   **0**: the subscription billing method
        # *   **4**: the subscription billing method for ApsaraMQ for Confluent instances
        self.paid_type = paid_type
        # The number of partitions. We recommend that you configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only PartitionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        # 
        # If this parameter is left empty, the default resource group is used. You can view the resource group ID on the Resource Group page in the Resource Management console.
        self.resource_group_id = resource_group_id
        # The instance edition. Valid values:
        # 
        # *   **normal**: Standard Edition (High Write)
        # *   **professional**: Professional Edition (High Write)
        # *   **professionalForHighRead**: Professional Edition (High Read)
        # 
        # For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.spec_type = spec_type
        # The tags.
        self.tag = tag
        # The number of topics. We recommend that you do not configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only PartitionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   The default value of TopicQuota varies based on the value of IoMaxSpec. If the number of topics that you use exceeds the default value, you are charged additional fees.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create an ApsaraMQ for Confluent instance, you do not need to configure this parameter.
        self.topic_quota = topic_quota

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

        if self.io_max is not None:
            result['IoMax'] = self.io_max

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

        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfluentConfig') is not None:
            temp_model = main_models.CreatePrePayOrderRequestConfluentConfig()
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

        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')

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
                temp_model = main_models.CreatePrePayOrderRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')

        return self

class CreatePrePayOrderRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   If this parameter is left empty, the keys of all tags are matched.
        # *   The tag key can be up to 128 characters in length and cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        # 
        # This parameter is required.
        self.key = key
        # The value of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   This parameter can be left empty.
        # *   The tag value can be 1 to 128 characters in length and cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
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

class CreatePrePayOrderRequestConfluentConfig(DaraModel):
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
        ksql_list: List[main_models.CreatePrePayOrderRequestConfluentConfigKsqlList] = None,
        ksql_replica: int = None,
        ksql_storage: int = None,
        schema_registry_cu: int = None,
        schema_registry_replica: int = None,
        zoo_keeper_cu: int = None,
        zoo_keeper_replica: int = None,
        zoo_keeper_storage: int = None,
    ):
        # The number of CPU cores of Connect.
        self.connect_cu = connect_cu
        # The number of replicas of Connect.
        self.connect_replica = connect_replica
        # The number of CPU cores of Control Center.
        self.control_center_cu = control_center_cu
        # The number of replicas of Control Center.
        self.control_center_replica = control_center_replica
        # The disk capacity of Control Center. Unit: GB
        self.control_center_storage = control_center_storage
        # The number of CPU cores of the Kafka broker.
        self.kafka_cu = kafka_cu
        # The number of replicas of the Kafka broker.
        self.kafka_replica = kafka_replica
        # The number of CPU cores of Kafka Rest Proxy.
        self.kafka_rest_proxy_cu = kafka_rest_proxy_cu
        # The number of replicas of Kafka Rest Proxy.
        self.kafka_rest_proxy_replica = kafka_rest_proxy_replica
        # The disk capacity of the Kafka broker. Unit: GB
        self.kafka_storage = kafka_storage
        # The number of CPU cores of ksqIDB.
        self.ksql_cu = ksql_cu
        self.ksql_list = ksql_list
        # The number of replicas of ksqlDB.
        self.ksql_replica = ksql_replica
        # The disk capacity of ksqlDB. Unit: GB
        self.ksql_storage = ksql_storage
        # The number of CPU cores of Schema Registry.
        self.schema_registry_cu = schema_registry_cu
        # The number of replicas of Schema Registry.
        self.schema_registry_replica = schema_registry_replica
        # The number of CPU cores of ZooKeeper.
        self.zoo_keeper_cu = zoo_keeper_cu
        # The number of replicas of ZooKeeper.
        self.zoo_keeper_replica = zoo_keeper_replica
        # The disk capacity of ZooKeeper. Unit: GB
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
                temp_model = main_models.CreatePrePayOrderRequestConfluentConfigKsqlList()
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

class CreatePrePayOrderRequestConfluentConfigKsqlList(DaraModel):
    def __init__(
        self,
        cu: int = None,
        internal_id: str = None,
        replica: int = None,
        storage: int = None,
        type: str = None,
    ):
        self.cu = cu
        self.internal_id = internal_id
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
        if self.cu is not None:
            result['Cu'] = self.cu

        if self.internal_id is not None:
            result['InternalId'] = self.internal_id

        if self.replica is not None:
            result['Replica'] = self.replica

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('InternalId') is not None:
            self.internal_id = m.get('InternalId')

        if m.get('Replica') is not None:
            self.replica = m.get('Replica')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

