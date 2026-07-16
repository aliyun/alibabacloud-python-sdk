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
        # The cleanup policy for the topic. This parameter is available only if the storage engine of the topic is local storage. Valid values:
        # 
        # - false: The delete cleanup policy.
        # 
        # - true: The compact cleanup policy.
        self.compact_topic = compact_topic
        # The advanced configurations of the topic.
        # 
        # - Configure this parameter in the JSON format.
        # 
        # - This parameter is available only if **LocalTopic** is set to **true**.
        # 
        # - The following configurations are supported for reserved instances:
        # 
        #   - **retention.ms**: The message retention period. The value must be an integer from 3,600,000 to 31,536,000,000. Unit: milliseconds.
        # 
        #   - **max.message.bytes**: The maximum size of a message that can be sent. The value must be an integer from 1,048,576 to 10,485,760. Unit: bytes.
        # 
        #   - message.timestamp.type: The timestamp type of a message. Valid values: CreateTime or LogAppendTime. CreateTime indicates that the message timestamp is the time when the producer creates the message. If you do not specify a timestamp, the client time is used. LogAppendTime indicates that the message timestamp is the time when the server stores the message. The default value is CreateTime. We recommend that you set this parameter to **LogAppendTime**.
        # 
        # - The following configurations are supported for Serverless instances:
        # 
        #   - **retention.hours**: The message retention period. The value is of the string type. The value must be an integer from 24 to 8,760.
        # 
        #   - **max.message.bytes**: The maximum size of a message that can be sent. The value is of the string type. The value must be an integer from 1,048,576 to 10,485,760.
        # 
        #   - message.timestamp.type: The timestamp type of a message. Valid values: CreateTime or LogAppendTime. CreateTime indicates that the message timestamp is the time when the producer creates the message. If you do not specify a timestamp, the client time is used. LogAppendTime indicates that the message timestamp is the time when the server stores the message. The default value is CreateTime. We recommend that you set this parameter to **LogAppendTime**.
        self.config = config
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The storage engine of the topic. Valid values:
        # 
        # - false: cloud storage.
        # 
        # - true: local storage.
        self.local_topic = local_topic
        # The minimum number of in-sync replicas (ISRs).
        # 
        # - This parameter is available only if **LocalTopic** is set to **true**.
        # 
        # - The value of this parameter must be smaller than the number of replicas for the topic.
        # 
        # - The value must be an integer from 1 to 3.
        self.min_insync_replicas = min_insync_replicas
        # The number of partitions in the topic.
        # 
        # - The value must be an integer from 1 to 360.
        # 
        # - The console suggests a number of partitions based on the instance type. Follow the suggestion to reduce the risk of data skew.
        # 
        # Default value:
        # 
        # - Reserved instance: 12
        # 
        # - Serverless instance: 3
        self.partition_num = partition_num
        # The ID of the region where the instance that contains the topic is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The remarks on the topic.
        # 
        # - The remarks can contain only letters, digits, underscores (_), and hyphens (-).
        # 
        # - The remarks must be 3 to 64 characters in length.
        # 
        # This parameter is required.
        self.remark = remark
        # The number of replicas for the topic.
        # 
        # - This parameter is available only if **LocalTopic** is set to **true**.
        # 
        # - The value must be an integer from 1 to 3.
        # 
        # > If you set the number of replicas to **1**, you may lose data. Set this parameter with caution.
        self.replication_factor = replication_factor
        # The list of tags.
        self.tag = tag
        # The name of the topic.
        # 
        # - Reserved instance: The name can contain uppercase letters, lowercase letters, digits, underscores (_), hyphens (-), and periods (.). The name must be 3 to 64 characters in length.
        # 
        # - Serverless instance: The name can contain uppercase letters, lowercase letters, digits, underscores (_), hyphens (-), and periods (.). The name must be 1 to 249 characters in length.
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
        # - N specifies the number of the tag. The value of N must be an integer from 1 to 20.
        # 
        # - If this parameter is left empty, all tag keys are matched.
        # 
        # - The tag key can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        # 
        # This parameter is required.
        self.key = key
        # The tag value of the resource.
        # 
        # - N specifies the number of the tag. The value of N must be an integer from 1 to 20.
        # 
        # - The tag value can be empty.
        # 
        # - The tag value can be up to 128 characters in length. It cannot start with aliyun or acs:, and cannot contain http\\:// or https\\://.
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

