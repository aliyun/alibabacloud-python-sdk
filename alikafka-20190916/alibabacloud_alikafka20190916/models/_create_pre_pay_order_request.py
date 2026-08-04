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
        # The Confluent component configurations.
        # 
        # 
        # > This parameter is required when you create a Confluent instance.
        self.confluent_config = confluent_config
        # The deployment type. Valid values:
        # 
        # - **4**: Internet- and VPC-connected instance
        # 
        # - **5**: VPC-connected instance
        # 
        # 
        # > If you create a Confluent instance, the deployment type is not supported. You can only set this parameter to 5. After the purchase, you can configure whether to enable public access for each component.
        self.deploy_type = deploy_type
        # The disk capacity. Unit: GB.
        # 
        # For the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > If you create a Confluent instance, you do not need to specify this parameter.
        self.disk_size = disk_size
        # The disk type. Valid values:
        # 
        # - **0**: ultra cloud disk
        # 
        # - **1**: SSD
        # 
        # > If you create a Confluent instance, you do not need to specify this parameter.
        self.disk_type = disk_type
        # The subscription duration. Unit: months. Default value: 1. Valid values:
        # 
        # - **Confluent instances: 1 or 12**
        # - **Kafka instances: 1**
        self.duration = duration
        # The public network traffic.
        # 
        # - This parameter is required if **DeployType** is set to **4**.
        # 
        # - For the value range, see [Pay-as-you-go billing method](https://help.aliyun.com/document_detail/72142.html).
        # 
        # 
        # > If you create a Confluent instance, you do not need to specify this parameter.
        self.eip_max = eip_max
        # The peak traffic (not recommended).
        # 
        # - You must specify at least one of **IoMax** and **IoMaxSpec**. If you specify both, **IoMaxSpec** takes precedence. We recommend that you specify only **IoMaxSpec**.
        # 
        # - For the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > If you create a Confluent instance, you do not need to specify this parameter.
        self.io_max = io_max
        # The traffic specification (recommended).
        # 
        # - You must specify at least one of **IoMax** and **IoMaxSpec**. If you specify both, **IoMaxSpec** takes precedence. We recommend that you specify only **IoMaxSpec**.
        # 
        # - For the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # > If you create a Confluent instance, you do not need to specify this parameter.
        self.io_max_spec = io_max_spec
        # The billing type. Valid values:
        # 
        # - **0**: subscription
        # 
        # - **4**: Confluent subscription
        self.paid_type = paid_type
        # The number of partitions (recommended).
        # 
        # * You must specify either the number of partitions or the topic specification. We recommend that you specify only the number of partitions.
        # 
        # * If you specify both the number of partitions and the topic specification, the system verifies whether the number of partitions and the topic specification are equivalent based on the legacy topic sales model. If they are not equivalent, the request fails. If they are equivalent, the purchase is made based on the number of partitions.
        # 
        # * For the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > If you create a Confluent instance, you do not need to specify this parameter.
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        # 
        # If you do not specify this parameter, the instance is placed in the default resource group. You can view the resource group ID in the Resource Group console.
        self.resource_group_id = resource_group_id
        # The specification type.
        # 
        # Valid values for ApsaraMQ for Kafka instances:
        # 
        # - **normal**: Normal Edition (shared high-write)
        # 
        # - **professional**: Professional Edition (shared high-write)
        # 
        # - **professionalForHighRead**: Professional Edition (shared high-read)
        # 
        # Valid values for Confluent instances:
        # 
        # - **professional**: Professional Edition
        # 
        # - **enterprise**: Enterprise Edition
        # 
        # For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        self.spec_type = spec_type
        # The tags.
        self.tag = tag
        # The number of topics (not recommended).
        # 
        # - You must specify either the number of partitions or the topic specification. We recommend that you specify only the number of partitions.
        # 
        # - If you specify both the number of partitions and the topic specification, the system verifies whether the number of partitions and the topic specification are equivalent based on the legacy topic sales model. If they are not equivalent, the request fails. If they are equivalent, the purchase is made based on the number of partitions.
        # 
        # - The default value varies based on the traffic specification. Additional fees are charged if the value exceeds the default value.
        # 
        # - For the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # > If you create a Confluent instance, you do not need to specify this parameter.
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
        # The tag key of the resource.
        # 
        # - N ranges from 1 to 20.
        # 
        # - If this parameter is left empty, all tag keys are matched.
        # 
        # - The tag key can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        # 
        # This parameter is required.
        self.key = key
        # The tag value of the resource.
        # 
        # - N ranges from 1 to 20.
        # 
        # - This parameter can be left empty.
        # 
        # - The tag value can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
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
        confluent_version: str = None,
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
        kraft_controller_cu: int = None,
        kraft_controller_replica: int = None,
        kraft_controller_storage: int = None,
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
        self.confluent_version = confluent_version
        # The number of CPU cores for the Connect component.
        self.connect_cu = connect_cu
        # The number of Connect component replicas.
        self.connect_replica = connect_replica
        # The number of CPU cores for the ControlCenter component.
        self.control_center_cu = control_center_cu
        # The number of ControlCenter component replicas.
        self.control_center_replica = control_center_replica
        # The disk capacity of the ControlCenter component. Unit: GB.
        self.control_center_storage = control_center_storage
        # The number of CPU cores for Kafka Broker.
        self.kafka_cu = kafka_cu
        # The number of Kafka Broker replicas.
        self.kafka_replica = kafka_replica
        # The number of CPU cores for the KafkaRestProxy component.
        self.kafka_rest_proxy_cu = kafka_rest_proxy_cu
        # The number of KafkaRestProxy component replicas.
        self.kafka_rest_proxy_replica = kafka_rest_proxy_replica
        # The disk capacity of Kafka Broker. Unit: GB.
        self.kafka_storage = kafka_storage
        self.kraft_controller_cu = kraft_controller_cu
        self.kraft_controller_replica = kraft_controller_replica
        self.kraft_controller_storage = kraft_controller_storage
        # The number of CPU cores for the KsqlDB component.
        self.ksql_cu = ksql_cu
        self.ksql_list = ksql_list
        # The number of KsqlDB component replicas.
        self.ksql_replica = ksql_replica
        # The disk capacity of the KsqlDB component. Unit: GB.
        self.ksql_storage = ksql_storage
        # The number of CPU cores for the SchemaRegistry component.
        self.schema_registry_cu = schema_registry_cu
        # The number of SchemaRegistry component replicas.
        self.schema_registry_replica = schema_registry_replica
        # The number of CPU cores for the ZooKeeper component.
        self.zoo_keeper_cu = zoo_keeper_cu
        # The number of ZooKeeper component replicas.
        self.zoo_keeper_replica = zoo_keeper_replica
        # The disk capacity of the ZooKeeper component. Unit: GB.
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
        if self.confluent_version is not None:
            result['ConfluentVersion'] = self.confluent_version

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

        if self.kraft_controller_cu is not None:
            result['KraftControllerCU'] = self.kraft_controller_cu

        if self.kraft_controller_replica is not None:
            result['KraftControllerReplica'] = self.kraft_controller_replica

        if self.kraft_controller_storage is not None:
            result['KraftControllerStorage'] = self.kraft_controller_storage

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
        if m.get('ConfluentVersion') is not None:
            self.confluent_version = m.get('ConfluentVersion')

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

        if m.get('KraftControllerCU') is not None:
            self.kraft_controller_cu = m.get('KraftControllerCU')

        if m.get('KraftControllerReplica') is not None:
            self.kraft_controller_replica = m.get('KraftControllerReplica')

        if m.get('KraftControllerStorage') is not None:
            self.kraft_controller_storage = m.get('KraftControllerStorage')

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

