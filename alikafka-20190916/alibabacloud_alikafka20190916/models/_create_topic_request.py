# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class CreateTopicRequest(DaraModel):
    def __init__(
        self,
        compact_topic: bool = None,
        config: str = None,
        instance_id: str = None,
        local_topic: bool = None,
        min_insync_replicas: int = None,
        partition_num: str = None,
        region_id: str = None,
        remark: str = None,
        replication_factor: int = None,
        tag: List[main_models.CreateTopicRequestTag] = None,
        topic: str = None,
    ):
        # The log cleanup policy that is used for the topic. This parameter is available only when LocalTopic is set to true. Valid values:
        # 
        # *   false: The topic uses the default log cleanup policy.
        # *   true: The topic uses the log compaction policy.
        self.compact_topic = compact_topic
        # The additional configuration.
        # 
        # *   The value must be in JSON format.
        # *   Set Key to **replications**. This value specifies the number of replicas of the topic. The value must be an integer that ranges from 1 to 3.
        # *   You can configure this parameter only if you set **LocalTopic** to **true** or specify **Open Source Edition (Local Disk)** as the instance edition.****
        # 
        # >  If you specify replications in this parameter, **ReplicationFactor** does not take effect.
        self.config = config
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of storage that the topic uses. Valid values:
        # 
        # *   false: The topic uses cloud storage.
        # *   true: The topic uses local storage.
        self.local_topic = local_topic
        # The minimum number of in-sync replicas (ISRs).
        # 
        # *   This parameter is available only when **LocalTopic** is set to **true**, or the instance is of the **Open Source Edition (Local Disk)**.****
        # *   The value of this parameter must be smaller than the value of ReplicationFactor.
        # *   Valid values: 1 to 3.
        self.min_insync_replicas = min_insync_replicas
        # The number of partitions in the topic.
        # 
        # *   Valid values: 1 to 360.
        # *   In the ApsaraMQ for Kafka console, you can view the number of partitions that the system recommends based on the specifications of the instance. We recommend that you specify the number that is recommended by the system as the value of this parameter to reduce the risk of data skew.
        # 
        # Default values:
        # 
        # *   ApsaraMQ for Kafka V2 instance: 12
        # *   ApsaraMQ for Kafka V3 instance: 3
        self.partition_num = partition_num
        # The region ID of the instance in which you want to create a topic.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The description of the topic.
        # 
        # *   The description can contain only letters, digits, hyphens (-), and underscores (_).
        # *   The description must be 3 to 64 characters in length.
        # 
        # This parameter is required.
        self.remark = remark
        # The number of replicas for the topic.
        # 
        # *   This parameter is available only when **LocalTopic** is set to **true**, or the instance is of the **Open Source Edition (Local Disk)**.****
        # *   Valid values: 1 to 3.
        # 
        # > If you set this parameter to **1**, data loss may occur. Exercise caution when you configure this parameter.
        self.replication_factor = replication_factor
        # The tags that you want to add to the topic.
        self.tag = tag
        # The topic name.
        # 
        # *   The name can contain only letters, digits, hyphens (-), and underscores (_).
        # *   The name must be 3 to 64 characters in length. If the name that you specify contains more than 64 characters, the system automatically truncates the name.
        # *   After a topic is created, you cannot change the name of the topic.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compact_topic is not None:
            result['CompactTopic'] = self.compact_topic

        if self.config is not None:
            result['Config'] = self.config

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.local_topic is not None:
            result['LocalTopic'] = self.local_topic

        if self.min_insync_replicas is not None:
            result['MinInsyncReplicas'] = self.min_insync_replicas

        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.replication_factor is not None:
            result['ReplicationFactor'] = self.replication_factor

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompactTopic') is not None:
            self.compact_topic = m.get('CompactTopic')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LocalTopic') is not None:
            self.local_topic = m.get('LocalTopic')

        if m.get('MinInsyncReplicas') is not None:
            self.min_insync_replicas = m.get('MinInsyncReplicas')

        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ReplicationFactor') is not None:
            self.replication_factor = m.get('ReplicationFactor')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateTopicRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class CreateTopicRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # *   If you do not specify this parameter, the keys of all tags are matched.
        # *   The tag key must be 1 to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `aliyun` or `acs:`.
        # 
        # This parameter is required.
        self.key = key
        # The tag value.
        # 
        # *   You can leave this parameter empty.
        # *   The tag value must be 1 to 128 characters in length and cannot contain http:// or https://. The tag value cannot start with aliyun or acs:.
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

