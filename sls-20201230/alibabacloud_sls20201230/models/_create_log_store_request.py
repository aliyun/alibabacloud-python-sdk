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
        enable_modify: bool = None,
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
        # Specifies whether to record the source **public IP address** and the **server reception time**. Default value: false.
        # 
        # - true: Log Service automatically appends the public IP address of the source device and the server reception time to the Tag field of logs.
        # 
        # - false: Log Service does not append the source public IP address or the server reception time.
        self.append_meta = append_meta
        # Specifies whether to enable automatic shard splitting. If you set this parameter to true, Log Service automatically splits a shard to increase write throughput when the write traffic to the shard continuously exceeds the service limit. If you enable automatic shard splitting, you must also specify `maxSplitShard`.
        self.auto_split = auto_split
        self.enable_modify = enable_modify
        # Specifies whether to enable WebTracking. The default value is false. This feature lets you collect and analyze user behavior data from browsers or mini programs, such as page views, purchase history, and dwell time.
        self.enable_tracking = enable_tracking
        # The encryption configuration. This data structure includes the `enable`, `encrypt_type`, and `user_cmk_info` parameters. For more information, see [EncryptConf](https://help.aliyun.com/document_detail/409461.html).
        # 
        # Example 1 (Enable default encryption):
        # 
        # ```
        # {
        #     "enable": true,
        #     "encrypt_conf": "default"
        # }
        # ```
        # 
        # Example 2 (Enable BYOK encryption):
        # 
        # ```
        # {
        #     "enable": true,
        #     "encrypt_conf": "default",
        #     "user_cmk_info": {
        #         "cmk_key_id": "xxxxx",
        #         "arn": "acs:ram::112340000000:role/rolename",
        #         "region": "cn-hangzhou"
        #     }
        # }
        # ```
        self.encrypt_conf = encrypt_conf
        # The retention period of data in the hot storage tier of the Logstore, in days. The value must be an integer from 7 to the value of `ttl`. If you do not specify this parameter, data is stored in the hot storage tier for the entire data retention period specified by `ttl`.
        # 
        # After the hot storage retention period expires, data is moved to the Infrequent Access (IA) storage tier. To enable IA storage, you must set the hot storage retention period to at least 7 days. For more information, see [Smart Tiered Storage](https://help.aliyun.com/document_detail/308645.html).
        # 
        # Examples:
        # 
        # - Scenario 1 (Store data in the hot storage tier for 30 days): `{"ttl": 30}` or `{"ttl": 30, "hot_ttl": 30}`
        # 
        # - Scenario 2 (Store data in the hot storage tier for 7 days and in the IA storage tier for 23 days): `{"ttl": 30, "hot_ttl": 7}`
        self.hot_ttl = hot_ttl
        # The retention period for Infrequent Access (IA) storage, in days. While this parameter has no minimum value, data must remain in the IA storage tier for at least 30 days before it can be moved to archive storage.
        # 
        # If the total retention period (`ttl`) is longer than the sum of the hot storage period (`hot_ttl`) and the IA storage period (`infrequentAccessTTL`), the remaining time is the archive storage period.
        # 
        # Examples:
        # 
        # - Scenario 1 (Store data in the hot storage tier for 7 days and in the IA storage tier for 23 days): `{"ttl": 30, "hot_ttl": 7}`
        # 
        # - Scenario 2 (Store data in the hot storage tier for 7 days, in the IA storage tier for 30 days, and in the archive storage tier for 60 days): `{"ttl": 97, "hot_ttl": 7, "infrequentAccessTTL": 30}`
        # 
        # - Scenario 3 (Store data in the hot storage tier for 60 days and in the archive storage tier for 60 days, with the IA storage period being 0 days): `{"ttl": 120, "hot_ttl": 60, "infrequentAccessTTL": 0}`
        self.infrequent_access_ttl = infrequent_access_ttl
        # The name of the Logstore. The name must meet the following requirements:
        # 
        # - The name must be unique within a project.
        # 
        # - The name can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # 
        # - The name must start and end with a lowercase letter or a digit.
        # 
        # - The name must be 2 to 63 characters long.
        # 
        # This parameter is required.
        self.logstore_name = logstore_name
        # The maximum number of shards after an automatic split. The value must be an integer from 1 to 256.
        # 
        # > This parameter is required if you set `autoSplit` to true.
        self.max_split_shard = max_split_shard
        # Log Service provides two types of Logstores: standard and query.
        # 
        # - **standard**: Supports end-to-end data analytics. This mode is suitable for scenarios such as real-time monitoring, interactive analysis, and building a complete observability system.
        # 
        # - **query**: Supports high-performance queries. The index traffic cost is approximately half that of the standard mode, but SQL analysis is not supported. This mode is suitable for scenarios that involve large volumes of data, long retention periods such as weeks or months, and do not require SQL-based analysis.
        self.mode = mode
        # The ID of the IngestProcessor.
        self.processor_id = processor_id
        # The ID of the resource group to which the Logstore belongs.
        self.resource_group_id = resource_group_id
        # The number of shards.
        # 
        # > You cannot update the shard count with this operation. To do so, call the SplitShard or MergeShards operation.
        # 
        # This parameter is required.
        self.shard_count = shard_count
        # The configuration for hash-based writes. When you write data, logs are stored in a shard that is selected based on the configured hash-based sharding policy. Before you configure this parameter, make sure that the hash ranges of the shards are evenly distributed. Improper configuration may affect write performance. Configure this parameter with caution.
        self.sharding_policy = sharding_policy
        # The type of observable data. Default value: log data. Valid values:
        # 
        # - **None**: log data. This is the default value.
        # 
        # - **Metrics**: Metrics data.
        self.telemetry_type = telemetry_type
        # The data retention period in days. Valid values: 1 to 3,650. If you set this parameter to 3,650, data is stored permanently.
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

