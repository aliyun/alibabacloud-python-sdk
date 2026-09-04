# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class UpdateLogStoreRequest(DaraModel):
    def __init__(
        self,
        append_meta: bool = None,
        auto_split: bool = None,
        enable_tracking: bool = None,
        encrypt_conf: main_models.EncryptConf = None,
        hot_ttl: int = None,
        infrequent_access_ttl: int = None,
        logstore_name: str = None,
        max_split_shard: int = None,
        mode: str = None,
        shard_count: int = None,
        sharding_policy: main_models.ShardingPolicy = None,
        telemetry_type: str = None,
        ttl: int = None,
    ):
        # Specifies whether to record the public IP address and log arrival time. Default value: false.
        # 
        # - true: enables the feature. After this feature is enabled, Simple Log Service automatically adds the public IP address of the log source device and the time when the log arrives at the server to the Tag field of the log.
        # - false: disables the feature.
        self.append_meta = append_meta
        # Specifies whether to enable automatic sharding. After this feature is enabled, a shard is automatically split when the write traffic continuously exceeds the limit, which improves write capacity. You must set maxSplitShard (the maximum number of shards after splitting) when you enable automatic sharding.
        self.auto_split = auto_split
        # Specifies whether to enable the WebTracking feature. Default value: false. You can use the WebTracking feature to collect and analyze user behavior data in browsers or mini programs, such as page views, purchase records, and time on site.
        # 
        # - true: enables WebTracking.
        # - false: disables WebTracking.
        self.enable_tracking = enable_tracking
        # The encryption configuration. Encryption is disabled by default.
        # 
        # Example 1 (enable default encryption):
        # ```
        # {
        #     "enable": true,
        #     "encrypt_conf": "default"
        # }
        # ```
        # Example 2 (enable BYOK encryption):
        # ```
        # {
        #     "enable": true,
        #     "encrypt_conf": "default",
        #     "user_cmk_info": {
        #         "cmk_key_id": "xxxxx",
        #         "arn": "acs:ram::112340000000:role/rolename",
        #         "region": "ap-southeast-1"
        #     }
        # }
        # ```
        self.encrypt_conf = encrypt_conf
        # The retention period of data in the hot tier of the Logstore. Unit: days. Minimum value: 7. The value cannot exceed the value of ttl. By default, all data within the retention period is stored in the hot tier.
        # 
        # After the data storage time exceeds the configured hot data retention period, the data is moved to the infrequent access (IA) tier. When you enable the IA tier, the hot data retention period must be at least 7 days. For more information, see [Intelligent tiering](https://help.aliyun.com/document_detail/308645.html).
        # 
        # Examples:
        # - Scenario 1 (hot tier only, 30 days): `{"ttl": 30}` or `{"ttl": 30, "hot_ttl": 30}`
        # - Scenario 2 (hot tier 7 days, IA tier 23 days): `{"ttl": 30, "hot_ttl": 7}`
        self.hot_ttl = hot_ttl
        # Infrequent access (IA) tier. No minimum storage time is required. Data must be stored for at least 30 days before being moved to the archive tier.
        # 
        # When the log retention period exceeds the sum of the hot tier retention period and the IA tier retention period, the remaining storage time is converted to archive tier storage.
        # 
        # Examples:
        # - Scenario 1 (hot tier 7 days, IA tier 23 days): `{"ttl": 30, "hot_ttl": 7}`
        # - Scenario 2 (hot tier 7 days, IA tier 30 days, archive tier 60 days): `{"ttl": 97, "hot_ttl": 7, "infrequentAccessTTL": 30}`
        # - Scenario 3 (hot tier 60 days, IA tier 0 days, archive tier 60 days): `{"ttl": 120, "hot_ttl": 60, "infrequentAccessTTL": 0}`
        self.infrequent_access_ttl = infrequent_access_ttl
        # The name of the Logstore.
        # 
        # This parameter is required.
        self.logstore_name = logstore_name
        # The maximum number of shards for automatic sharding. Minimum value: 1. Maximum value: 256.
        # 
        # > This parameter is required when autoSplit is set to true.
        self.max_split_shard = max_split_shard
        # Simple Log Service provides two types of Logstores: Standard and Query.
        # 
        # - **standard**: supports one-stop data analytics capabilities of Simple Log Service. This type is suitable for scenarios such as real-time monitoring, interactive analysis, and building complete observability systems.
        # - **query**: supports high-performance queries. The index traffic fee is approximately half that of the Standard type. However, SQL analysis is not supported. This type is suitable for scenarios with large data volumes, long storage periods (weeks or months), and no log analysis requirements.
        self.mode = mode
        # The number of shards.
        # 
        # > This operation does not support updating the number of shards. You can modify the number of shards only by calling the SplitShard or MergeShards operation.
        self.shard_count = shard_count
        # The hash-based write configuration. When data is written, logs are routed to shards based on the configured hash policy. Before configuring this parameter, ensure that the hash ranges of shards are evenly distributed. This configuration may affect write capacity. Proceed with caution.
        self.sharding_policy = sharding_policy
        # The type of observable data. The default value is log data. Valid values:
        # 
        # - None: log data. This is the default value.
        # - Metrics: time series data.
        self.telemetry_type = telemetry_type
        # The data retention period. Unit: days. Valid values: 1 to 3650. A value of 3650 indicates permanent retention.
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

        if self.enable_tracking is not None:
            result['enable_tracking'] = self.enable_tracking

        if self.encrypt_conf is not None:
            result['encrypt_conf'] = self.encrypt_conf.to_map()

        if self.hot_ttl is not None:
            result['hot_ttl'] = self.hot_ttl

        if self.infrequent_access_ttl is not None:
            result['infrequentAccessTTL'] = self.infrequent_access_ttl

        if self.logstore_name is not None:
            result['logstoreName'] = self.logstore_name

        if self.max_split_shard is not None:
            result['maxSplitShard'] = self.max_split_shard

        if self.mode is not None:
            result['mode'] = self.mode

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

        if m.get('enable_tracking') is not None:
            self.enable_tracking = m.get('enable_tracking')

        if m.get('encrypt_conf') is not None:
            temp_model = main_models.EncryptConf()
            self.encrypt_conf = temp_model.from_map(m.get('encrypt_conf'))

        if m.get('hot_ttl') is not None:
            self.hot_ttl = m.get('hot_ttl')

        if m.get('infrequentAccessTTL') is not None:
            self.infrequent_access_ttl = m.get('infrequentAccessTTL')

        if m.get('logstoreName') is not None:
            self.logstore_name = m.get('logstoreName')

        if m.get('maxSplitShard') is not None:
            self.max_split_shard = m.get('maxSplitShard')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

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

