# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class CreateMetricStoreRequest(DaraModel):
    def __init__(
        self,
        append_meta: bool = None,
        auto_split: bool = None,
        hot_ttl: int = None,
        infrequent_access_ttl: int = None,
        max_split_shard: int = None,
        metric_type: str = None,
        mode: str = None,
        name: str = None,
        shard_count: int = None,
        sharding_policy: main_models.ShardingPolicy = None,
        ttl: int = None,
    ):
        # Specifies whether to record the public IP address of the client. The default value is false.
        # 
        # - true: Records the public IP address.
        # 
        # - false: Does not record the public IP address.
        self.append_meta = append_meta
        # Specifies whether to enable automatic shard splitting.
        self.auto_split = auto_split
        # The period for which data is stored in the hot tier. Unit: days. The value must be at least 7 and cannot be greater than the value of ttl. If you set this parameter to -1, all data is stored in the hot tier for the duration specified by ttl.
        # 
        # When the hot storage period ends, the data is moved to the IA storage class. For more information, see [Tiered Storage of Hot and Cold Data](https://help.aliyun.com/document_detail/308645.html).
        self.hot_ttl = hot_ttl
        # The retention period of data in the IA storage class. Unit: days. The minimum value is 30. After this period, data is moved to Archive Storage.
        self.infrequent_access_ttl = infrequent_access_ttl
        # The maximum number of shards into which a shard can be split. This parameter is valid only if autoSplit is set to true.
        self.max_split_shard = max_split_shard
        # The type of the Metricstore. Only prometheus is supported. The default value is prometheus.
        self.metric_type = metric_type
        # The type of the Metricstore. Only standard is supported. The default value is standard.
        self.mode = mode
        # The name of the Metricstore to create.
        # 
        # This parameter is required.
        self.name = name
        # The number of [shards](https://help.aliyun.com/document_detail/28976.html) for the Metricstore.
        # 
        # This parameter is required.
        self.shard_count = shard_count
        # The write hashing configuration.
        self.sharding_policy = sharding_policy
        # The data retention period of the Metricstore. Unit: days.
        # 
        # This parameter is required.
        self.ttl = ttl

    def validate(self):
        if self.sharding_policy:
            self.sharding_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.append_meta is not None:
            result['appendMeta'] = self.append_meta

        if self.auto_split is not None:
            result['autoSplit'] = self.auto_split

        if self.hot_ttl is not None:
            result['hot_ttl'] = self.hot_ttl

        if self.infrequent_access_ttl is not None:
            result['infrequentAccessTTL'] = self.infrequent_access_ttl

        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard

        if self.metric_type is not None:
            result['metricType'] = self.metric_type

        if self.mode is not None:
            result['mode'] = self.mode

        if self.name is not None:
            result['name'] = self.name

        if self.shard_count is not None:
            result['shardCount'] = self.shard_count

        if self.sharding_policy is not None:
            result['shardingPolicy'] = self.sharding_policy.to_map()

        if self.ttl is not None:
            result['ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appendMeta') is not None:
            self.append_meta = m.get('appendMeta')

        if m.get('autoSplit') is not None:
            self.auto_split = m.get('autoSplit')

        if m.get('hot_ttl') is not None:
            self.hot_ttl = m.get('hot_ttl')

        if m.get('infrequentAccessTTL') is not None:
            self.infrequent_access_ttl = m.get('infrequentAccessTTL')

        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')

        if m.get('metricType') is not None:
            self.metric_type = m.get('metricType')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')

        if m.get('shardingPolicy') is not None:
            temp_model = main_models.ShardingPolicy()
            self.sharding_policy = temp_model.from_map(m.get('shardingPolicy'))

        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')

        return self

