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
        # The cleanup policy configured when the storage engine of the topic is set to local storage. Valid values:
        # 
        # - false: delete cleanup policy.
        # - true: compact cleanup policy.
        self.compact_topic = compact_topic
        # The supplementary configuration.
        # 
        # - Must be in JSON format.
        # 
        # 
        # - This parameter takes effect only when **LocalTopic** is set to **true**.
        # 
        # - Supported configurations for reserved instances:
        #   -   **retention.ms** (message retention period): ranges from 3600000 to 31536000000 milliseconds.
        #   - **max.message.bytes** (maximum message size): ranges from 1048576 to 10485760 bytes. 
        #   - **message.timestamp.type**: specifies the type of message timestamp. CreateTime indicates the timestamp specified by the producer when sending a message. If not specified, it is the message creation time on the client. LogAppendTime indicates the time when the message is written to disk on the server. Valid values: CreateTime or LogAppendTime. Default value: CreateTime. We recommend LogAppendTime.
        # 
        #  - Supported configurations for Serverless instances:
        #    -  **retention.hours** (message retention period): value type is String. Valid values: 24 to 8760.
        #    -  **max.message.bytes** (maximum message size): value type is String. Valid values: 1048576 to 10485760.
        #    -  **message.timestamp.type** (type of message timestamp): CreateTime indicates the timestamp specified by the producer when sending a message. If not specified, it is the message creation time on the client. LogAppendTime indicates the time when the message is written to disk on the server. Valid values: CreateTime or LogAppendTime. Default value: CreateTime. We recommend LogAppendTime.
        self.config = config
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The storage engine of the topic. Valid values:
        # 
        # - false: cloud storage.
        # - true: local storage.
        self.local_topic = local_topic
        # The minimum number of in-sync replicas (ISR).
        # 
        # - This parameter takes effect only when **LocalTopic** is set to **true**.
        # 
        # - The value must be less than the number of topic replicas.
        # 
        # - The number of in-sync replicas ranges from 1 to 3.
        self.min_insync_replicas = min_insync_replicas
        # The number of partitions for the topic.
        # 
        # - The number of partitions ranges from 1 to 360.
        # 
        # - The console provides different configuration suggestions based on the instance edition. Configure the number of partitions based on the console suggestions to reduce the risk of data skew.
        # 
        # Default value:
        # 
        # - Reserved instances: 12
        # 
        # - Serverless instances: 3
        self.partition_num = partition_num
        # The region ID of the instance to which the topic belongs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The description of the topic.
        # 
        # - Can contain only letters, digits, underscores (_), and hyphens (-).
        # 
        # - Must be 3 to 64 characters in length.
        # 
        # This parameter is required.
        self.remark = remark
        # The number of replicas for the topic.
        # 
        # - This parameter takes effect only when **LocalTopic** is set to **true**.
        # 
        # - The number of replicas ranges from 1 to 3.
        # 
        # > If the number of replicas is set to **1**, data loss may occur. Set this parameter with caution.
        self.replication_factor = replication_factor
        # The tag list.
        self.tag = tag
        # The name of the topic.
        # 
        # - Reserved instances:
        # Supports uppercase and lowercase letters, digits, underscores (_), hyphens (-), and periods (.). The name must be 3 to 64 characters in length.
        # - Serverless instances:
        # Supports uppercase and lowercase letters, digits, underscores (_), hyphens (-), and periods (.). The name must be 1 to 249 characters in length.
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
        # The tag key of the resource.
        # 
        # - N ranges from 1 to 20.
        # 
        # - If this parameter is left empty, all tag keys are matched.
        # 
        # - The tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`, or contain `http://` or `https://`.
        # 
        # This parameter is required.
        self.key = key
        # The tag value of the resource.
        # 
        # - N ranges from 1 to 20.
        # 
        # - This parameter can be left empty.
        # 
        # - The tag value can be up to 128 characters in length and cannot start with aliyun or acs:, or contain http:// or https://.
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

