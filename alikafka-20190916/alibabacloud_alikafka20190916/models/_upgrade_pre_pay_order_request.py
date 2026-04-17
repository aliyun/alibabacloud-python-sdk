# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class UpgradePrePayOrderRequest(DaraModel):
    def __init__(
        self,
        confluent_config: main_models.UpgradePrePayOrderRequestConfluentConfig = None,
        disk_size: int = None,
        eip_max: int = None,
        eip_model: bool = None,
        instance_id: str = None,
        io_max: int = None,
        io_max_spec: str = None,
        paid_type: int = None,
        partition_num: int = None,
        region_id: str = None,
        spec_type: str = None,
        topic_quota: int = None,
    ):
        self.confluent_config = confluent_config
        # The size of the disk.
        # 
        # *   The disk size that you specify must be greater than or equal to the current disk size of the instance.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.disk_size = disk_size
        # The Internet traffic for the instance.
        # 
        # *   The Internet traffic volume that you specify must be greater than or equal to the current Internet traffic volume of the instance.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        # > - If the **EipModel** parameter is set to **true**, set the **EipMax** parameter to a value that is greater than 0.
        # > - If the **EipModel** parameter is set to **false**, set the **EipMax** parameter to **0**.
        self.eip_max = eip_max
        # Specifies whether to enable Internet access for the instance. Valid values:
        # 
        # *   true: enables Internet access.
        # *   false: disables Internet access.
        self.eip_model = eip_model
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum traffic for the instance. We recommend that you do not configure this parameter.
        # 
        # *   The maximum traffic volume that you specify must be greater than or equal to the current maximum traffic volume of the instance.
        # *   You must configure at least one of the IoMax and IoMaxSpec parameters. If you configure both parameters, the value of the IoMaxSpec parameter takes effect. We recommend that you configure only the IoMaxSpec parameter.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.io_max = io_max
        # The traffic specification of the instance. We recommend that you configure this parameter.
        # 
        # *   The traffic specification that you specify must be greater than or equal to the current traffic specification of the instance.
        # *   You must configure at least one of the IoMax and IoMaxSpec parameters. If you configure both parameters, the value of the IoMaxSpec parameter takes effect. We recommend that you configure only the IoMaxSpec parameter.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.io_max_spec = io_max_spec
        self.paid_type = paid_type
        # The number of partitions. We recommend that you configure this parameter.
        # 
        # *   You must specify at least one of the PartitionNum and TopicQuota parameters. We recommend that you configure only the PartitionNum parameter.
        # *   If you specify both parameters, the topic-based sales model is used to check whether the PartitionNum value and the TopicQuota value are the same. If they are not the same, a failure response is returned. If they are the same, the order is placed based on the PartitionNum value.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The edition of the instance. Valid values:
        # 
        # *   **normal**: Standard Edition (High Write)
        # *   **professional**: Professional Edition (High Write)
        # *   **professionalForHighRead**: Professional Edition (High Read)
        # 
        # You cannot downgrade an instance from the Professional Edition to the Standard Edition. For more information about these instance editions, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.spec_type = spec_type
        # The number of topics. We recommend that you do not configure this parameter.
        # 
        # *   You must specify at least one of the PartitionNum and TopicQuota parameters. We recommend that you configure only the PartitionNum parameter.
        # *   If you specify both parameters, the topic-based sales model is used to check whether the PartitionNum value and the TopicQuota value are the same. If they are not the same, a failure response is returned. If they are the same, the order is placed based on the PartitionNum value.
        # *   The default value of the TopicQuota parameter varies based on the value of the IoMaxSpec parameter. If the number of topics that you consume exceeds the default value, you are charged additional fees.
        # *   For more information about the valid values, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.topic_quota = topic_quota

    def validate(self):
        if self.confluent_config:
            self.confluent_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confluent_config is not None:
            result['ConfluentConfig'] = self.confluent_config.to_map()

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.eip_max is not None:
            result['EipMax'] = self.eip_max

        if self.eip_model is not None:
            result['EipModel'] = self.eip_model

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfluentConfig') is not None:
            temp_model = main_models.UpgradePrePayOrderRequestConfluentConfig()
            self.confluent_config = temp_model.from_map(m.get('ConfluentConfig'))

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')

        if m.get('EipModel') is not None:
            self.eip_model = m.get('EipModel')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

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

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')

        return self

class UpgradePrePayOrderRequestConfluentConfig(DaraModel):
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
        ksql_list: List[main_models.UpgradePrePayOrderRequestConfluentConfigKsqlList] = None,
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
                temp_model = main_models.UpgradePrePayOrderRequestConfluentConfigKsqlList()
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

class UpgradePrePayOrderRequestConfluentConfigKsqlList(DaraModel):
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

