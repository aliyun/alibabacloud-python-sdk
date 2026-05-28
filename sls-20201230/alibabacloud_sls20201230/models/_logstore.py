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
        shard_count: int = None,
        sharding_policy: main_models.ShardingPolicy = None,
        telemetry_type: str = None,
        ttl: int = None,
    ):
        # Specifies whether to record public IP addresses. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.append_meta = append_meta
        # Specifies whether to enable automatic sharding. Valid values:
        # 
        # *   true
        # *   false
        self.auto_split = auto_split
        # The time at which the Logstore was created. The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # Specifies whether to enable the web tracking feature. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.enable_tracking = enable_tracking
        # The configuration of data encryption.
        self.encrypt_conf = encrypt_conf
        # The retention period of data in the hot storage tier of the Logstore. Minimum value: 30. Unit: days.
        self.hot_ttl = hot_ttl
        # The retention period of data in the Infrequent Access (IA) storage tier of the Logstore.
        self.infrequent_access_ttl = infrequent_access_ttl
        # The time at which the Logstore was last modified. The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_modify_time = last_modify_time
        # The name of the Logstore.
        # 
        # This parameter is required.
        self.logstore_name = logstore_name
        # The maximum number of shards into which existing shards can be automatically split. Valid values: 1 to 64.
        self.max_split_shard = max_split_shard
        # The type of the Logstore. Simple Log Service provides two types of Logstores: Standard Logstores and Query Logstores. Valid values:
        # 
        # *   **standard**: Standard Logstore. This type of Logstore supports the log analysis feature and is suitable for scenarios such as real-time monitoring and interactive analysis. You can also use this type of Logstore to build a comprehensive observability system.
        # *   **query**: Query Logstore. This type of Logstore supports high-performance queries. The index traffic fee of a Query Logstore is approximately half that of a Standard Logstore. Query Logstores do not support SQL analysis. Query Logstores are suitable for scenarios in which the amount of data is large, the log retention period is long, or log analysis is not required. If logs are stored for weeks or months, the log retention period is considered long.
        self.mode = mode
        # The ingest processor ID.
        self.processor_id = processor_id
        # The type of the service to which the logs belong.
        self.product_type = product_type
        # The number of shards.
        # 
        # This parameter is required.
        self.shard_count = shard_count
        self.sharding_policy = sharding_policy
        # The type of the data that you want to query. Valid values:
        # 
        # *   Metrics: metric data.
        # *   None: non-metric data.
        self.telemetry_type = telemetry_type
        # The log retention period. Unit: days. Valid values: 1 to 3650. If you set this parameter to 3650, logs are permanently stored.
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

