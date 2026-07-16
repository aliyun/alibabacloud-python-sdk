# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class Logstore(DaraModel):
    def __init__(
        self,
        append_meta: bool = None,
        auto_split: bool = None,
        create_time: int = None,
        enable_modify: bool = None,
        enable_tracking: bool = None,
        encrypt_conf: main_models.EncryptConf = None,
        hot_ttl: int = None,
        infrequent_access_ttl: int = None,
        last_modify_time: int = None,
        logstore_name: str = None,
        max_split_shard: int = None,
        mode: str = None,
        processor_id: str = None,
        product_type: str = None,
        resource_group_id: str = None,
        shard_count: int = None,
        sharding_policy: main_models.ShardingPolicy = None,
        telemetry_type: str = None,
        ttl: int = None,
    ):
        # Specifies whether to include the client\\"s public IP address in the log data. The default is false.
        # 
        # - true: Records the public IP address.
        # 
        # - false: Does not record the public IP address.
        self.append_meta = append_meta
        # Specifies whether to enable auto split.
        # 
        # - true: Enables auto split.
        # 
        # - false: Disables auto split.
        self.auto_split = auto_split
        # The creation time of the Logstore, specified as a UNIX timestamp (the number of seconds since January 1, 1970, 00:00:00 UTC).
        self.create_time = create_time
        self.enable_modify = enable_modify
        # Specifies whether to enable WebTracking. The default value is false.
        # 
        # - true: Enables WebTracking.
        # 
        # - false: Disables WebTracking.
        self.enable_tracking = enable_tracking
        # The data encryption configuration.
        self.encrypt_conf = encrypt_conf
        # The number of days to retain data in the hot storage tier. The minimum value is 30.
        self.hot_ttl = hot_ttl
        # The number of days to retain data in the infrequent access storage tier.
        self.infrequent_access_ttl = infrequent_access_ttl
        # The time the Logstore was last modified, specified as a UNIX timestamp (the number of seconds since January 1, 1970, 00:00:00 UTC).
        self.last_modify_time = last_modify_time
        # The name of the Logstore.
        # 
        # This parameter is required.
        self.logstore_name = logstore_name
        # The maximum number of shards that an auto split can create. Valid values: 1 to 64.
        self.max_split_shard = max_split_shard
        # Log Service provides two types of Logstores: Standard and Query.
        # 
        # - **Standard**: Supports the full suite of Log Service data analysis features. This mode is ideal for real-time monitoring, interactive analysis, and building complete observability solutions.
        # 
        # - **Query**: Optimized for high-performance queries with indexing traffic costs that are approximately half those of the Standard mode. This mode does not support SQL analysis and is best for use cases involving large data volumes and long retention periods, where complex log analysis is not a requirement.
        self.mode = mode
        # The IngestProcessor ID.
        self.processor_id = processor_id
        # The product type of the logs.
        self.product_type = product_type
        self.resource_group_id = resource_group_id
        # The number of shards in the Logstore.
        # 
        # This parameter is required.
        self.shard_count = shard_count
        self.sharding_policy = sharding_policy
        # The type of log data. Valid values:
        # 
        # - Metrics: The Logstore is optimized for time-series storage.
        # 
        # - None: The Logstore uses standard storage for logs.
        self.telemetry_type = telemetry_type
        # The data retention period in days. Valid values: 1 to 3,650. A value of 3,650 indicates permanent storage.
        # 
        # This parameter is required.
        self.ttl = ttl

    def validate(self):
        if self.encrypt_conf:
            self.encrypt_conf.validate()
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

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.enable_modify is not None:
            result['enableModify'] = self.enable_modify

        if self.enable_tracking is not None:
            result['enable_tracking'] = self.enable_tracking

        if self.encrypt_conf is not None:
            result['encrypt_conf'] = self.encrypt_conf.to_map()

        if self.hot_ttl is not None:
            result['hot_ttl'] = self.hot_ttl

        if self.infrequent_access_ttl is not None:
            result['infrequentAccessTTL'] = self.infrequent_access_ttl

        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time

        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name

        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard

        if self.mode is not None:
            result['mode'] = self.mode

        if self.processor_id is not None:
            result['processorId'] = self.processor_id

        if self.product_type is not None:
            result['productType'] = self.product_type

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.shard_count is not None:
            result['shardCount'] = self.shard_count

        if self.sharding_policy is not None:
            result['shardingPolicy'] = self.sharding_policy.to_map()

        if self.telemetry_type is not None:
            result['telemetryType'] = self.telemetry_type

        if self.ttl is not None:
            result['ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appendMeta') is not None:
            self.append_meta = m.get('appendMeta')

        if m.get('autoSplit') is not None:
            self.auto_split = m.get('autoSplit')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('enableModify') is not None:
            self.enable_modify = m.get('enableModify')

        if m.get('enable_tracking') is not None:
            self.enable_tracking = m.get('enable_tracking')

        if m.get('encrypt_conf') is not None:
            temp_model = main_models.EncryptConf()
            self.encrypt_conf = temp_model.from_map(m.get('encrypt_conf'))

        if m.get('hot_ttl') is not None:
            self.hot_ttl = m.get('hot_ttl')

        if m.get('infrequentAccessTTL') is not None:
            self.infrequent_access_ttl = m.get('infrequentAccessTTL')

        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')

        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')

        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('processorId') is not None:
            self.processor_id = m.get('processorId')

        if m.get('productType') is not None:
            self.product_type = m.get('productType')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')

        if m.get('shardingPolicy') is not None:
            temp_model = main_models.ShardingPolicy()
            self.sharding_policy = temp_model.from_map(m.get('shardingPolicy'))

        if m.get('telemetryType') is not None:
            self.telemetry_type = m.get('telemetryType')

        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')

        return self

