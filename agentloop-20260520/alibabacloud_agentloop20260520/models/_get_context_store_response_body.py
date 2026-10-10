# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class GetContextStoreResponseBody(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        config: main_models.GetContextStoreResponseBodyConfig = None,
        context_store_name: str = None,
        context_type: str = None,
        create_time: str = None,
        description: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
        update_time: str = None,
    ):
        # The name of the AgentSpace to which the context store belongs.
        self.agent_space = agent_space
        # The configuration of the context store.
        self.config = config
        # The context store name.
        self.context_store_name = context_store_name
        # The type of the context store, such as experience or memory.
        self.context_type = context_type
        # The time when the context store was created, in ISO 8601 UTC format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        # The description of the context store.
        self.description = description
        # The region ID of the context store.
        self.region_id = region_id
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The status of the context store. Valid values:
        # - ACTIVE
        # - INITIALIZING
        # - FAILED
        self.status = status
        # The time when the context store was last updated, in ISO 8601 UTC format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.context_store_name is not None:
            result['contextStoreName'] = self.context_store_name

        if self.context_type is not None:
            result['contextType'] = self.context_type

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.status is not None:
            result['status'] = self.status

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('config') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('contextStoreName') is not None:
            self.context_store_name = m.get('contextStoreName')

        if m.get('contextType') is not None:
            self.context_type = m.get('contextType')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class GetContextStoreResponseBodyConfig(DaraModel):
    def __init__(
        self,
        audit: main_models.GetContextStoreResponseBodyConfigAudit = None,
        extraction_policy: main_models.GetContextStoreResponseBodyConfigExtractionPolicy = None,
        inner_source: main_models.GetContextStoreResponseBodyConfigInnerSource = None,
        metadata_field: Dict[str, str] = None,
        mining_interval: str = None,
        observability: main_models.GetContextStoreResponseBodyConfigObservability = None,
        output_dataset: main_models.GetContextStoreResponseBodyConfigOutputDataset = None,
        scope_policy: main_models.GetContextStoreResponseBodyConfigScopePolicy = None,
        service_names: List[str] = None,
        source: main_models.GetContextStoreResponseBodyConfigSource = None,
        source_status: main_models.GetContextStoreResponseBodyConfigSourceStatus = None,
        storage_policy: main_models.GetContextStoreResponseBodyConfigStoragePolicy = None,
        strategy_version: int = None,
    ):
        self.audit = audit
        self.extraction_policy = extraction_policy
        self.inner_source = inner_source
        # The metadata field mapping. The key is the business field and the value is the storage field.
        self.metadata_field = metadata_field
        # The experience mining interval. Valid values: 1h, 6h, 12h, and 1d. Default value: 1d.
        self.mining_interval = mining_interval
        self.observability = observability
        self.output_dataset = output_dataset
        self.scope_policy = scope_policy
        # The list of service names. This works together with source.agentSpace to locate the trace data source. This value cannot be changed in the current version.
        self.service_names = service_names
        # The datasource config passed in by the user. This serves only as the root identifier of the data source.
        self.source = source
        self.source_status = source_status
        self.storage_policy = storage_policy
        self.strategy_version = strategy_version

    def validate(self):
        if self.audit:
            self.audit.validate()
        if self.extraction_policy:
            self.extraction_policy.validate()
        if self.inner_source:
            self.inner_source.validate()
        if self.observability:
            self.observability.validate()
        if self.output_dataset:
            self.output_dataset.validate()
        if self.scope_policy:
            self.scope_policy.validate()
        if self.source:
            self.source.validate()
        if self.source_status:
            self.source_status.validate()
        if self.storage_policy:
            self.storage_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit is not None:
            result['audit'] = self.audit.to_map()

        if self.extraction_policy is not None:
            result['extractionPolicy'] = self.extraction_policy.to_map()

        if self.inner_source is not None:
            result['innerSource'] = self.inner_source.to_map()

        if self.metadata_field is not None:
            result['metadataField'] = self.metadata_field

        if self.mining_interval is not None:
            result['miningInterval'] = self.mining_interval

        if self.observability is not None:
            result['observability'] = self.observability.to_map()

        if self.output_dataset is not None:
            result['outputDataset'] = self.output_dataset.to_map()

        if self.scope_policy is not None:
            result['scopePolicy'] = self.scope_policy.to_map()

        if self.service_names is not None:
            result['serviceNames'] = self.service_names

        if self.source is not None:
            result['source'] = self.source.to_map()

        if self.source_status is not None:
            result['sourceStatus'] = self.source_status.to_map()

        if self.storage_policy is not None:
            result['storagePolicy'] = self.storage_policy.to_map()

        if self.strategy_version is not None:
            result['strategyVersion'] = self.strategy_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audit') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigAudit()
            self.audit = temp_model.from_map(m.get('audit'))

        if m.get('extractionPolicy') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigExtractionPolicy()
            self.extraction_policy = temp_model.from_map(m.get('extractionPolicy'))

        if m.get('innerSource') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigInnerSource()
            self.inner_source = temp_model.from_map(m.get('innerSource'))

        if m.get('metadataField') is not None:
            self.metadata_field = m.get('metadataField')

        if m.get('miningInterval') is not None:
            self.mining_interval = m.get('miningInterval')

        if m.get('observability') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigObservability()
            self.observability = temp_model.from_map(m.get('observability'))

        if m.get('outputDataset') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigOutputDataset()
            self.output_dataset = temp_model.from_map(m.get('outputDataset'))

        if m.get('scopePolicy') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigScopePolicy()
            self.scope_policy = temp_model.from_map(m.get('scopePolicy'))

        if m.get('serviceNames') is not None:
            self.service_names = m.get('serviceNames')

        if m.get('source') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigSource()
            self.source = temp_model.from_map(m.get('source'))

        if m.get('sourceStatus') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigSourceStatus()
            self.source_status = temp_model.from_map(m.get('sourceStatus'))

        if m.get('storagePolicy') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigStoragePolicy()
            self.storage_policy = temp_model.from_map(m.get('storagePolicy'))

        if m.get('strategyVersion') is not None:
            self.strategy_version = m.get('strategyVersion')

        return self

class GetContextStoreResponseBodyConfigStoragePolicy(DaraModel):
    def __init__(
        self,
        allowed_actions: List[str] = None,
        dedupe: bool = None,
        human_edit_protection: bool = None,
        merge_key: str = None,
        mode: str = None,
        similarity_threshold: float = None,
        ttl_days: int = None,
    ):
        self.allowed_actions = allowed_actions
        self.dedupe = dedupe
        self.human_edit_protection = human_edit_protection
        self.merge_key = merge_key
        self.mode = mode
        self.similarity_threshold = similarity_threshold
        self.ttl_days = ttl_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_actions is not None:
            result['allowedActions'] = self.allowed_actions

        if self.dedupe is not None:
            result['dedupe'] = self.dedupe

        if self.human_edit_protection is not None:
            result['humanEditProtection'] = self.human_edit_protection

        if self.merge_key is not None:
            result['mergeKey'] = self.merge_key

        if self.mode is not None:
            result['mode'] = self.mode

        if self.similarity_threshold is not None:
            result['similarityThreshold'] = self.similarity_threshold

        if self.ttl_days is not None:
            result['ttlDays'] = self.ttl_days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowedActions') is not None:
            self.allowed_actions = m.get('allowedActions')

        if m.get('dedupe') is not None:
            self.dedupe = m.get('dedupe')

        if m.get('humanEditProtection') is not None:
            self.human_edit_protection = m.get('humanEditProtection')

        if m.get('mergeKey') is not None:
            self.merge_key = m.get('mergeKey')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('similarityThreshold') is not None:
            self.similarity_threshold = m.get('similarityThreshold')

        if m.get('ttlDays') is not None:
            self.ttl_days = m.get('ttlDays')

        return self

class GetContextStoreResponseBodyConfigSourceStatus(DaraModel):
    def __init__(
        self,
        checkpoint: Dict[str, Any] = None,
        last_error: str = None,
        last_window_at: str = None,
        retry_count: int = None,
        state: str = None,
    ):
        self.checkpoint = checkpoint
        self.last_error = last_error
        self.last_window_at = last_window_at
        self.retry_count = retry_count
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkpoint is not None:
            result['checkpoint'] = self.checkpoint

        if self.last_error is not None:
            result['lastError'] = self.last_error

        if self.last_window_at is not None:
            result['lastWindowAt'] = self.last_window_at

        if self.retry_count is not None:
            result['retryCount'] = self.retry_count

        if self.state is not None:
            result['state'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkpoint') is not None:
            self.checkpoint = m.get('checkpoint')

        if m.get('lastError') is not None:
            self.last_error = m.get('lastError')

        if m.get('lastWindowAt') is not None:
            self.last_window_at = m.get('lastWindowAt')

        if m.get('retryCount') is not None:
            self.retry_count = m.get('retryCount')

        if m.get('state') is not None:
            self.state = m.get('state')

        return self

class GetContextStoreResponseBodyConfigSource(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        dataset: main_models.GetContextStoreResponseBodyConfigSourceDataset = None,
        start_time: str = None,
        trajectory: main_models.GetContextStoreResponseBodyConfigSourceTrajectory = None,
        type: str = None,
    ):
        # The AgentSpace where the trace data source resides. This is the same as the AgentSpace specified during creation.
        self.agent_space = agent_space
        self.dataset = dataset
        # The start time for data backfill, in ISO 8601 UTC format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.start_time = start_time
        self.trajectory = trajectory
        self.type = type

    def validate(self):
        if self.dataset:
            self.dataset.validate()
        if self.trajectory:
            self.trajectory.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.dataset is not None:
            result['dataset'] = self.dataset.to_map()

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.trajectory is not None:
            result['trajectory'] = self.trajectory.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('dataset') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigSourceDataset()
            self.dataset = temp_model.from_map(m.get('dataset'))

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('trajectory') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigSourceTrajectory()
            self.trajectory = temp_model.from_map(m.get('trajectory'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetContextStoreResponseBodyConfigSourceTrajectory(DaraModel):
    def __init__(
        self,
        filter: main_models.GetContextStoreResponseBodyConfigSourceTrajectoryFilter = None,
        logstore: str = None,
        poll_interval_seconds: int = None,
        scope_mapping: main_models.GetContextStoreResponseBodyConfigSourceTrajectoryScopeMapping = None,
        start_time: str = None,
    ):
        self.filter = filter
        self.logstore = logstore
        self.poll_interval_seconds = poll_interval_seconds
        self.scope_mapping = scope_mapping
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.start_time = start_time

    def validate(self):
        if self.filter:
            self.filter.validate()
        if self.scope_mapping:
            self.scope_mapping.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['filter'] = self.filter.to_map()

        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.poll_interval_seconds is not None:
            result['pollIntervalSeconds'] = self.poll_interval_seconds

        if self.scope_mapping is not None:
            result['scopeMapping'] = self.scope_mapping.to_map()

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigSourceTrajectoryFilter()
            self.filter = temp_model.from_map(m.get('filter'))

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('pollIntervalSeconds') is not None:
            self.poll_interval_seconds = m.get('pollIntervalSeconds')

        if m.get('scopeMapping') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigSourceTrajectoryScopeMapping()
            self.scope_mapping = temp_model.from_map(m.get('scopeMapping'))

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

class GetContextStoreResponseBodyConfigSourceTrajectoryScopeMapping(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        app_id: str = None,
        run_id: str = None,
        user_id: str = None,
    ):
        self.agent_id = agent_id
        self.app_id = app_id
        self.run_id = run_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class GetContextStoreResponseBodyConfigSourceTrajectoryFilter(DaraModel):
    def __init__(
        self,
        agent_names: List[str] = None,
        exclude_degraded: bool = None,
        min_step_count: int = None,
        query: str = None,
        service_names: List[str] = None,
    ):
        self.agent_names = agent_names
        self.exclude_degraded = exclude_degraded
        self.min_step_count = min_step_count
        self.query = query
        self.service_names = service_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_names is not None:
            result['agentNames'] = self.agent_names

        if self.exclude_degraded is not None:
            result['excludeDegraded'] = self.exclude_degraded

        if self.min_step_count is not None:
            result['minStepCount'] = self.min_step_count

        if self.query is not None:
            result['query'] = self.query

        if self.service_names is not None:
            result['serviceNames'] = self.service_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentNames') is not None:
            self.agent_names = m.get('agentNames')

        if m.get('excludeDegraded') is not None:
            self.exclude_degraded = m.get('excludeDegraded')

        if m.get('minStepCount') is not None:
            self.min_step_count = m.get('minStepCount')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('serviceNames') is not None:
            self.service_names = m.get('serviceNames')

        return self

class GetContextStoreResponseBodyConfigSourceDataset(DaraModel):
    def __init__(
        self,
        custom_fields: List[main_models.GetContextStoreResponseBodyConfigSourceDatasetCustomFields] = None,
        dataset_name: str = None,
        filter: main_models.GetContextStoreResponseBodyConfigSourceDatasetFilter = None,
        poll_interval_seconds: int = None,
        schema_contract: str = None,
        version_policy: main_models.GetContextStoreResponseBodyConfigSourceDatasetVersionPolicy = None,
    ):
        self.custom_fields = custom_fields
        self.dataset_name = dataset_name
        self.filter = filter
        self.poll_interval_seconds = poll_interval_seconds
        self.schema_contract = schema_contract
        self.version_policy = version_policy

    def validate(self):
        if self.custom_fields:
            for v1 in self.custom_fields:
                 if v1:
                    v1.validate()
        if self.filter:
            self.filter.validate()
        if self.version_policy:
            self.version_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['customFields'] = []
        if self.custom_fields is not None:
            for k1 in self.custom_fields:
                result['customFields'].append(k1.to_map() if k1 else None)

        if self.dataset_name is not None:
            result['datasetName'] = self.dataset_name

        if self.filter is not None:
            result['filter'] = self.filter.to_map()

        if self.poll_interval_seconds is not None:
            result['pollIntervalSeconds'] = self.poll_interval_seconds

        if self.schema_contract is not None:
            result['schemaContract'] = self.schema_contract

        if self.version_policy is not None:
            result['versionPolicy'] = self.version_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_fields = []
        if m.get('customFields') is not None:
            for k1 in m.get('customFields'):
                temp_model = main_models.GetContextStoreResponseBodyConfigSourceDatasetCustomFields()
                self.custom_fields.append(temp_model.from_map(k1))

        if m.get('datasetName') is not None:
            self.dataset_name = m.get('datasetName')

        if m.get('filter') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigSourceDatasetFilter()
            self.filter = temp_model.from_map(m.get('filter'))

        if m.get('pollIntervalSeconds') is not None:
            self.poll_interval_seconds = m.get('pollIntervalSeconds')

        if m.get('schemaContract') is not None:
            self.schema_contract = m.get('schemaContract')

        if m.get('versionPolicy') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigSourceDatasetVersionPolicy()
            self.version_policy = temp_model.from_map(m.get('versionPolicy'))

        return self

class GetContextStoreResponseBodyConfigSourceDatasetVersionPolicy(DaraModel):
    def __init__(
        self,
        mode: str = None,
        start_seq: int = None,
        version: str = None,
    ):
        self.mode = mode
        self.start_seq = start_seq
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['mode'] = self.mode

        if self.start_seq is not None:
            result['startSeq'] = self.start_seq

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('startSeq') is not None:
            self.start_seq = m.get('startSeq')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class GetContextStoreResponseBodyConfigSourceDatasetFilter(DaraModel):
    def __init__(
        self,
        where: str = None,
    ):
        self.where = where

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.where is not None:
            result['where'] = self.where

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('where') is not None:
            self.where = m.get('where')

        return self

class GetContextStoreResponseBodyConfigSourceDatasetCustomFields(DaraModel):
    def __init__(
        self,
        description: str = None,
        sensitive: bool = None,
        source_field: str = None,
        target: str = None,
        usage: str = None,
    ):
        self.description = description
        self.sensitive = sensitive
        self.source_field = source_field
        self.target = target
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.sensitive is not None:
            result['sensitive'] = self.sensitive

        if self.source_field is not None:
            result['sourceField'] = self.source_field

        if self.target is not None:
            result['target'] = self.target

        if self.usage is not None:
            result['usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('sensitive') is not None:
            self.sensitive = m.get('sensitive')

        if m.get('sourceField') is not None:
            self.source_field = m.get('sourceField')

        if m.get('target') is not None:
            self.target = m.get('target')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self

class GetContextStoreResponseBodyConfigScopePolicy(DaraModel):
    def __init__(
        self,
        required_any_of: List[str] = None,
    ):
        self.required_any_of = required_any_of

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.required_any_of is not None:
            result['requiredAnyOf'] = self.required_any_of

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requiredAnyOf') is not None:
            self.required_any_of = m.get('requiredAnyOf')

        return self

class GetContextStoreResponseBodyConfigOutputDataset(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        dataset_name: str = None,
        schema_contract: str = None,
        schema_version: int = None,
    ):
        self.agent_space = agent_space
        self.dataset_name = dataset_name
        self.schema_contract = schema_contract
        self.schema_version = schema_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.dataset_name is not None:
            result['datasetName'] = self.dataset_name

        if self.schema_contract is not None:
            result['schemaContract'] = self.schema_contract

        if self.schema_version is not None:
            result['schemaVersion'] = self.schema_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('datasetName') is not None:
            self.dataset_name = m.get('datasetName')

        if m.get('schemaContract') is not None:
            self.schema_contract = m.get('schemaContract')

        if m.get('schemaVersion') is not None:
            self.schema_version = m.get('schemaVersion')

        return self

class GetContextStoreResponseBodyConfigObservability(DaraModel):
    def __init__(
        self,
        audit_logstore: str = None,
        events_logstore: str = None,
        project: str = None,
    ):
        self.audit_logstore = audit_logstore
        self.events_logstore = events_logstore
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_logstore is not None:
            result['auditLogstore'] = self.audit_logstore

        if self.events_logstore is not None:
            result['eventsLogstore'] = self.events_logstore

        if self.project is not None:
            result['project'] = self.project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auditLogstore') is not None:
            self.audit_logstore = m.get('auditLogstore')

        if m.get('eventsLogstore') is not None:
            self.events_logstore = m.get('eventsLogstore')

        if m.get('project') is not None:
            self.project = m.get('project')

        return self

class GetContextStoreResponseBodyConfigInnerSource(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
    ):
        self.logstore = logstore
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.project is not None:
            result['project'] = self.project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('project') is not None:
            self.project = m.get('project')

        return self

class GetContextStoreResponseBodyConfigExtractionPolicy(DaraModel):
    def __init__(
        self,
        categories: List[str] = None,
        custom_instructions: str = None,
        exclude_rules: List[str] = None,
        model: main_models.GetContextStoreResponseBodyConfigExtractionPolicyModel = None,
        preset: str = None,
    ):
        self.categories = categories
        self.custom_instructions = custom_instructions
        self.exclude_rules = exclude_rules
        self.model = model
        self.preset = preset

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.categories is not None:
            result['categories'] = self.categories

        if self.custom_instructions is not None:
            result['customInstructions'] = self.custom_instructions

        if self.exclude_rules is not None:
            result['excludeRules'] = self.exclude_rules

        if self.model is not None:
            result['model'] = self.model.to_map()

        if self.preset is not None:
            result['preset'] = self.preset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categories') is not None:
            self.categories = m.get('categories')

        if m.get('customInstructions') is not None:
            self.custom_instructions = m.get('customInstructions')

        if m.get('excludeRules') is not None:
            self.exclude_rules = m.get('excludeRules')

        if m.get('model') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigExtractionPolicyModel()
            self.model = temp_model.from_map(m.get('model'))

        if m.get('preset') is not None:
            self.preset = m.get('preset')

        return self

class GetContextStoreResponseBodyConfigExtractionPolicyModel(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class GetContextStoreResponseBodyConfigAudit(DaraModel):
    def __init__(
        self,
        dropped_candidates: bool = None,
        query_mode: str = None,
        retention_days: int = None,
    ):
        self.dropped_candidates = dropped_candidates
        self.query_mode = query_mode
        self.retention_days = retention_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dropped_candidates is not None:
            result['droppedCandidates'] = self.dropped_candidates

        if self.query_mode is not None:
            result['queryMode'] = self.query_mode

        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('droppedCandidates') is not None:
            self.dropped_candidates = m.get('droppedCandidates')

        if m.get('queryMode') is not None:
            self.query_mode = m.get('queryMode')

        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')

        return self

