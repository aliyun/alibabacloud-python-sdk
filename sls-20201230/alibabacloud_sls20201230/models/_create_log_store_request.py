# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class CreateLogStoreRequest(DaraModel):
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
        processor_id: str = None,
        resource_group_id: str = None,
        shard_count: int = None,
        sharding_policy: main_models.ShardingPolicy = None,
        telemetry_type: str = None,
        ttl: int = None,
    ):
        # Specifies whether to record the **public IP address** and the **log receiving time**. Default value: false. Valid values:
        # 
        # *   true: records the public IP address and the log receiving time. If you set this parameter to true, Simple Log Service automatically adds the public IP address of the device from which the log is collected and the time when Simple Log Service receives the log to the Tag field of the collected log.
        # *   false: does not record the public IP address or log receiving time.
        self.append_meta = append_meta
        # Specifies whether to enable automatic sharding. Valid values:
        # 
        # *   true
        # *   false
        self.auto_split = auto_split
        # Specifies whether to enable the web tracking feature. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.enable_tracking = enable_tracking
        # The data structure of the encryption configuration. The following parameters are included: `enable`, `encrypt_type`, and `user_cmk_info`. For more information, see [EncryptConf](https://help.aliyun.com/document_detail/409461.html).
        self.encrypt_conf = encrypt_conf
        # The data retention period for the hot storage tier. Unit: days. Minimum value: 7. The value of this parameter cannot exceed the value of ttl. If you set this parameter to -1, all data is stored in the hot storage tier.
        # 
        # After the retention period that is specified for the hot storage tier elapses, the data is moved to the Infrequent Access (IA) storage tier. For more information, see [Enable hot and cold-tiered storage for a Logstore](https://help.aliyun.com/document_detail/308645.html).
        self.hot_ttl = hot_ttl
        # The data retention period for the IA storage tier. You must set this parameter to at least 30 days. After the data retention period that you specify for the IA storage tier elapses, the data is moved to the Archive storage tier.
        self.infrequent_access_ttl = infrequent_access_ttl
        # The name of the Logstore. The name must meet the following requirements:
        # 
        # *   The name must be unique in a project.
        # *   The name can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # *   The name must start and end with a lowercase letter or digit.
        # *   The name must be 3 to 63 characters in length.
        # 
        # This parameter is required.
        self.logstore_name = logstore_name
        # The maximum number of shards into which existing shards can be automatically split. Valid values: 1 to 256.
        # 
        # >  If you set autoSplit to true, you must specify this parameter.
        self.max_split_shard = max_split_shard
        # The type of the Logstore. Simple Log Service provides two types of Logstores: Standard Logstores and Query Logstores. Valid values:
        # 
        # *   **standard**: Standard Logstore. This type of Logstore supports the log analysis feature and is suitable for scenarios such as real-time monitoring and interactive analysis. You can use this type of Logstore to build a comprehensive observability system.
        # *   **query**: Query Logstore. This type of Logstore supports high-performance query operations. The index traffic fee of a Query Logstore is approximately half that of a Standard Logstore. Query Logstores do not support SQL analysis. Query Logstores are suitable for scenarios in which the amount of data is large, the data retention period is long, or log analysis is not required. Data retention periods of weeks or months are considered long.
        self.mode = mode
        # IngestProcessor ID
        self.processor_id = processor_id
        self.resource_group_id = resource_group_id
        # The number of shards.
        # 
        # >  You cannot call the CreateLogStore operation to change the number of shards. You can call the SplitShard or MergeShards operation to change the number of shards.
        # 
        # This parameter is required.
        self.shard_count = shard_count
        self.sharding_policy = sharding_policy
        # The type of the observable data. Valid values:
        # 
        # *   **None** (default): log data
        # *   **Metrics**: metric data
        self.telemetry_type = telemetry_type
        # The data retention period. Unit: days. Valid values: 1 to 3650. If you set this parameter to 3650, data is permanently stored.
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

        if self.processor_id is not None:
            result['processorId'] = self.processor_id

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

        if m.get('processorId') is not None:
            self.processor_id = m.get('processorId')

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

