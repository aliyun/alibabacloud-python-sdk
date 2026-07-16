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
        # Specifies whether to record public IP addresses. Default value: false.
        # 
        # - true: records public IP addresses.
        # 
        # - false: does not record public IP addresses.
        self.append_meta = append_meta
        # Specifies whether to automatically split a shard.
        # 
        # - true: automatically splits a shard.
        # 
        # - false: does not automatically split a shard.
        self.auto_split = auto_split
        # Specifies whether to enable web tracking. Default value: false.
        # 
        # - true: enables web tracking.
        # 
        # - false: does not enable web tracking.
        self.enable_tracking = enable_tracking
        # The encryption configuration.
        self.encrypt_conf = encrypt_conf
        # The retention period of data in the hot tier of the Logstore. Minimum value: 7. Unit: days. Valid values: 7 to 3000. After the retention period of the hot tier ends, the data is moved to the Infrequent Access (IA) storage class. For more information, see [Automatic Storage Tiering](https://help.aliyun.com/document_detail/308645.html).
        self.hot_ttl = hot_ttl
        # The retention period for data in the IA storage class. Data in this storage class has no minimum retention period. Data must be stored for at least 30 days before it is moved to Archive storage.
        self.infrequent_access_ttl = infrequent_access_ttl
        # The name of the Logstore.
        # 
        # This parameter is required.
        self.logstore_name = logstore_name
        # The maximum number of shards to which a shard can be split. The value must be an integer from 1 to 256.
        # 
        # > This parameter is required if autoSplit is set to true.
        self.max_split_shard = max_split_shard
        # SLS provides two types of Logstores: Standard and Query.
        # 
        # - **standard**: supports one-stop data analytics. This type of Logstore is suitable for scenarios such as real-time monitoring, interactive analysis, and building a complete observability system.
        # 
        # - **query**: supports high-performance queries. The index traffic cost of a Query Logstore is about half that of a Standard Logstore. However, a Query Logstore does not support SQL analysis. This type of Logstore is suitable for scenarios that involve large data volumes, long retention periods of weeks or months, and no log analysis.
        self.mode = mode
        # The number of shards.
        # 
        # > You cannot update the number of shards with this operation. To change the number of shards, call the SplitShard or MergeShards operation.
        self.shard_count = shard_count
        # The hash-based write configuration.
        self.sharding_policy = sharding_policy
        # The type of observable data. Valid values:
        # 
        # - None: logs. This is the default value.
        # 
        # - Metrics: metrics.
        self.telemetry_type = telemetry_type
        # The data retention period. Unit: days. Valid values: 1 to 3650. If you set this parameter to 3650, the data is permanently retained.
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

