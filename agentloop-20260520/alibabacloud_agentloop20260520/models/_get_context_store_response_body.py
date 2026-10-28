# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

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
        # The name of the associated AgentSpace.
        self.agent_space = agent_space
        # The context library configuration.
        self.config = config
        # The name of the context store.
        self.context_store_name = context_store_name
        # The type of the context store, such as experience or memory.
        self.context_type = context_type
        # The time when the context store was created, in ISO 8601 UTC format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        # The description of the context store.
        self.description = description
        # The ID of the region where the context store is located.
        self.region_id = region_id
        # The request ID used to locate the request during troubleshooting.
        self.request_id = request_id
        # The status of the context store, such as ACTIVE, INITIALIZING, or FAILED.
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
        extraction_policies: List[main_models.GetContextStoreResponseBodyConfigExtractionPolicies] = None,
        extraction_policy: main_models.GetContextStoreResponseBodyConfigExtractionPolicy = None,
        inner_source: main_models.GetContextStoreResponseBodyConfigInnerSource = None,
        metadata_field: Dict[str, str] = None,
        mining_interval: str = None,
        mining_task_name: str = None,
        observability: main_models.GetContextStoreResponseBodyConfigObservability = None,
        output_dataset: main_models.GetContextStoreResponseBodyConfigOutputDataset = None,
        scope_policy: main_models.GetContextStoreResponseBodyConfigScopePolicy = None,
        service_names: List[str] = None,
        source: main_models.GetContextStoreResponseBodyConfigSource = None,
        source_status: main_models.GetContextStoreResponseBodyConfigSourceStatus = None,
        storage_modes: List[str] = None,
        storage_policy: main_models.GetContextStoreResponseBodyConfigStoragePolicy = None,
        strategy_version: int = None,
    ):
        # The audit configuration.
        self.audit = audit
        # The extraction policies. You can configure 1 to 10 policies. The strategyVersion parameter indicates the snapshot version of the entire library configuration.
        self.extraction_policies = extraction_policies
        # The extraction policy for the memory type.
        self.extraction_policy = extraction_policy
        # The system-assigned coordinates of the event Logstore for the memory type. The Logstore is located in the Simple Log Service (SLS) project bound to the AgentSpace.
        self.inner_source = inner_source
        # The metadata field mapping. The key is the business field and the value is the storage field.
        self.metadata_field = metadata_field
        # The interval for experience mining. Valid values: 1h, 6h, 12h, and 1d. Default value: 1d.
        self.mining_interval = mining_interval
        # The name of the internal running task associated with the server. For continuous libraries, it is used to view consumption records in read-only mode. For manual libraries, it can run limited mining. It is not inferred by the client and cannot replace the ingestion and recall criteria of the native experience library.
        self.mining_task_name = mining_task_name
        # The observability resource coordinates (memory type).
        self.observability = observability
        # The location of the memory output dataset (memory type).
        self.output_dataset = output_dataset
        # The scope constraint policy.
        self.scope_policy = scope_policy
        # The list of service names used to locate the trace data source together with source.agentSpace. This parameter cannot be modified in the current phase.
        self.service_names = service_names
        # The data source configuration provided by the user, which serves only as the root identifier of the data source.
        self.source = source
        # The running status of the data source, applicable to the memory type and experience Dataset follow mode. The experience library submits a checkpoint only after it is published and automatically applied successfully. Pausing and restarting retain the checkpoint.
        self.source_status = source_status
        self.storage_modes = storage_modes
        # The storage policy for the memory type.
        self.storage_policy = storage_policy
        # The currently effective strategy version number for the memory type.
        self.strategy_version = strategy_version

    def validate(self):
        if self.audit:
            self.audit.validate()
        if self.extraction_policies:
            for v1 in self.extraction_policies:
                 if v1:
                    v1.validate()
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

        result['extractionPolicies'] = []
        if self.extraction_policies is not None:
            for k1 in self.extraction_policies:
                result['extractionPolicies'].append(k1.to_map() if k1 else None)

        if self.extraction_policy is not None:
            result['extractionPolicy'] = self.extraction_policy.to_map()

        if self.inner_source is not None:
            result['innerSource'] = self.inner_source.to_map()

        if self.metadata_field is not None:
            result['metadataField'] = self.metadata_field

        if self.mining_interval is not None:
            result['miningInterval'] = self.mining_interval

        if self.mining_task_name is not None:
            result['miningTaskName'] = self.mining_task_name

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

        if self.storage_modes is not None:
            result['storageModes'] = self.storage_modes

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

        self.extraction_policies = []
        if m.get('extractionPolicies') is not None:
            for k1 in m.get('extractionPolicies'):
                temp_model = main_models.GetContextStoreResponseBodyConfigExtractionPolicies()
                self.extraction_policies.append(temp_model.from_map(k1))

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

        if m.get('miningTaskName') is not None:
            self.mining_task_name = m.get('miningTaskName')

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

        if m.get('storageModes') is not None:
            self.storage_modes = m.get('storageModes')

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
        # The allowed storage actions. Default value: all actions. Valid values: ADD, UPDATE, MERGE, and DELETE.
        self.allowed_actions = allowed_actions
        # Specifies whether to enable deduplication in event mode. Default value: true.
        self.dedupe = dedupe
        # Specifies whether to enable human edit protection. Default value: true. When enabled, automatic extraction does not overwrite manually modified memories.
        self.human_edit_protection = human_edit_protection
        # The merge key for upsert operations. Default value: semantic. Valid values: factKey, semantic, and both.
        self.merge_key = merge_key
        # The storage mode. Default value: upsert. Valid values: event (event append) and upsert (merge update).
        self.mode = mode
        # The similarity threshold for semantic merging. Valid values: 0 to 1. Default value: 0.4.
        self.similarity_threshold = similarity_threshold
        # The number of days before memories expire. A value of 0 indicates that memories do not expire.
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
        current_window: Dict[str, str] = None,
        last_error: str = None,
        last_run_id: str = None,
        last_window_at: str = None,
        retry_count: int = None,
        state: str = None,
    ):
        # The processing progress. For memory trajectory, the format is {processTimeNs, watermarkMs}. For dataset, the format is {seq}. For manual, the format is {}. For experience Dataset follow, the seq field uses an exact int64 decimal string.
        self.checkpoint = checkpoint
        # The current reserved sequence window for experience Dataset follow, in the format of {after, until, runId}. All sequence numbers are decimal strings. If a failure occurs, the submitted checkpoint is not advanced.
        self.current_window = current_window
        # The last desensitized error message. This field is empty when the status is normal.
        self.last_error = last_error
        # The run ID of the last successful automatic application to the native experience library. This field is for audit purposes only.
        self.last_run_id = last_run_id
        # The last window processing time in ISO 8601 UTC format.
        self.last_window_at = last_window_at
        # The number of consecutive retries.
        self.retry_count = retry_count
        # The state of the data source. Valid values: Validating, Ready, Running, Retrying, Paused, SourceSchemaChanged, and Failed.
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

        if self.current_window is not None:
            result['currentWindow'] = self.current_window

        if self.last_error is not None:
            result['lastError'] = self.last_error

        if self.last_run_id is not None:
            result['lastRunId'] = self.last_run_id

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

        if m.get('currentWindow') is not None:
            self.current_window = m.get('currentWindow')

        if m.get('lastError') is not None:
            self.last_error = m.get('lastError')

        if m.get('lastRunId') is not None:
            self.last_run_id = m.get('lastRunId')

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
        binding: Dict[str, Any] = None,
        dataset: main_models.GetContextStoreResponseBodyConfigSourceDataset = None,
        dataset_name: str = None,
        format: str = None,
        max_records: int = None,
        start_time: str = None,
        trajectory: main_models.GetContextStoreResponseBodyConfigSourceTrajectory = None,
        type: str = None,
        version_policy: main_models.GetContextStoreResponseBodyConfigSourceVersionPolicy = None,
    ):
        # The AgentSpace to which the trace data source belongs, which is the same as the AgentSpace to which it belonged when it was created.
        self.agent_space = agent_space
        # The DatasetBinding v1 shared with optimization tasks, which retains fixed column validation, supplementary column usage, and all/window selection.
        self.binding = binding
        # The data source configuration for the memory type dataset. This parameter is required when the type is memory and source.type is dataset.
        self.dataset = dataset
        # The name of the source dataset for the experience type in the current AgentSpace.
        self.dataset_name = dataset_name
        # The input format of the dataset. For the experience base dataset, the source is atif.
        self.format = format
        # The maximum number of records to read from the dataset at a time. Valid values: 1 to 1000.
        self.max_records = max_records
        # The start time for data backfill in ISO 8601 UTC format.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.start_time = start_time
        # The data source configuration for the memory type trajectory. This parameter is required when the type is memory and source.type is trajectory.
        self.trajectory = trajectory
        # The source type, which can be trajectory or dataset. For experience, if not specified, the trajectory configuration is used. For Dataset, the datasetName, format, and binding at the current level are used. The default mode is manual. If versionPolicy.mode is set to follow, continuous processing is performed and automatically applied to the experience library. For memory, if not specified, the mode is manual (only written by AddContexts). Otherwise, the trajectory or dataset sub-configuration with the same name is used. This parameter cannot be modified after creation.
        self.type = type
        # The continuous consumption configuration for the native experience library Dataset. The default mode is manual. The follow mode only allows binding.selection.mode to be set to all, and consumes data by append sequence number. This parameter cannot be modified after creation.
        self.version_policy = version_policy

    def validate(self):
        if self.dataset:
            self.dataset.validate()
        if self.trajectory:
            self.trajectory.validate()
        if self.version_policy:
            self.version_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.binding is not None:
            result['binding'] = self.binding

        if self.dataset is not None:
            result['dataset'] = self.dataset.to_map()

        if self.dataset_name is not None:
            result['datasetName'] = self.dataset_name

        if self.format is not None:
            result['format'] = self.format

        if self.max_records is not None:
            result['maxRecords'] = self.max_records

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.trajectory is not None:
            result['trajectory'] = self.trajectory.to_map()

        if self.type is not None:
            result['type'] = self.type

        if self.version_policy is not None:
            result['versionPolicy'] = self.version_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('binding') is not None:
            self.binding = m.get('binding')

        if m.get('dataset') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigSourceDataset()
            self.dataset = temp_model.from_map(m.get('dataset'))

        if m.get('datasetName') is not None:
            self.dataset_name = m.get('datasetName')

        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('maxRecords') is not None:
            self.max_records = m.get('maxRecords')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('trajectory') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigSourceTrajectory()
            self.trajectory = temp_model.from_map(m.get('trajectory'))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('versionPolicy') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigSourceVersionPolicy()
            self.version_policy = temp_model.from_map(m.get('versionPolicy'))

        return self

class GetContextStoreResponseBodyConfigSourceVersionPolicy(DaraModel):
    def __init__(
        self,
        mode: str = None,
        start_seq: str = None,
    ):
        # The continuous consumption mode. The value is fixed to follow.
        self.mode = mode
        # The initial consumed append sequence number. The value is a decimal string of a non-negative int64 integer. Default value: 0. The __dataset_seq field is used, and the business timestamp is not used as the consumption checkpoint.
        self.start_seq = start_seq

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('startSeq') is not None:
            self.start_seq = m.get('startSeq')

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
        # The trajectory filter condition. Multiple conditions are combined with AND, and conditions within a list are combined with OR.
        self.filter = filter
        # The name of the trajectory Logstore. Default value: agent-trajectory. This parameter cannot be modified after creation.
        self.logstore = logstore
        # The polling interval in seconds. Valid values: 60 to 3600. Default value: 300.
        self.poll_interval_seconds = poll_interval_seconds
        # The scope field mapping. The value is a JSONPath expression. Only the $.a.b and $.a[0] formats are supported.
        self.scope_mapping = scope_mapping
        # The start time for trajectory consumption in ISO 8601 UTC format. If not specified, the default value is the creation time.
        # 
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
        # The JSONPath expression for agentId. Default value: $.agent_name.
        self.agent_id = agent_id
        # The JSONPath expression for appId. Default value: $.service_names[0].
        self.app_id = app_id
        # The JSONPath expression for runId. Default value: $.trajectory_id.
        self.run_id = run_id
        # The JSONPath expression for userId. By default, this field is not mapped.
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
        # The list of agent names. An explicit empty list returns a 400 error.
        self.agent_names = agent_names
        # Specifies whether to exclude degraded trajectories. Default value: false (includes degraded trajectories).
        self.exclude_degraded = exclude_degraded
        # The minimum step count, which must be greater than or equal to 0.
        self.min_step_count = min_step_count
        # The native Simple Log Service (SLS) query statement. This statement is combined with the preceding conditions using the AND operator.
        self.query = query
        # The list of service names. A single trailing asterisk (*) is supported. An explicit empty list returns a 400 error.
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
        # The list of custom field declarations.
        self.custom_fields = custom_fields
        # The name of the dataset in the same AgentSpace. This parameter cannot be modified after creation.
        self.dataset_name = dataset_name
        # The row filter condition.
        self.filter = filter
        # The polling interval in seconds. Valid values: 60 to 3600. Default value: 300.
        self.poll_interval_seconds = poll_interval_seconds
        # The row schema contract of the dataset. In the current phase, this parameter is fixed to MemorySourceV1.
        self.schema_contract = schema_contract
        # The version consumption policy of the dataset.
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
        # The consumption mode. Valid values: follow (incremental consumption based on __dataset_seq) and fixed (full consumption of the specified ACTIVE version at once).
        self.mode = mode
        # The starting __dataset_seq for the follow mode.
        self.start_seq = start_seq
        # The dataset version specified for the fixed mode.
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
        # The subset of the pipeline where clause, which is pushed down to SQL.
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
        # The description of the field. This parameter is required when usage is extraction-input and is appended to the extraction prompt.
        self.description = description
        # Specifies whether the field is a sensitive field.
        self.sensitive = sensitive
        # The name of the source field.
        self.source_field = source_field
        # The target path for writing, such as metadata.customerTier.
        self.target = target
        # The usage of the field. Valid values: extraction-input (participates in extraction) and ignore (ignored).
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
        # Specifies that at least one of the scope fields must be non-empty. Valid values: userId, agentId, appId, and runId.
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
        # The AgentSpace to which the dataset belongs.
        self.agent_space = agent_space
        # The name of the dataset.
        self.dataset_name = dataset_name
        # The row schema contract of the dataset.
        self.schema_contract = schema_contract
        # The schema version.
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
        # The name of the audit Logstore.
        self.audit_logstore = audit_logstore
        # The name of the event Logstore.
        self.events_logstore = events_logstore
        # The Simple Log Service (SLS) project to which both belong, which is bound to the AgentSpace.
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
        # The name of the event Logstore.
        self.logstore = logstore
        # The name of the SLS project.
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
        # The list of memory categories.
        self.categories = categories
        # The custom extraction instructions. This parameter is required when preset is set to custom. The length must be 1 to 8,000 characters.
        self.custom_instructions = custom_instructions
        # The list of exclusion rules. Content that matches these rules is not extracted.
        self.exclude_rules = exclude_rules
        # The extraction model configuration.
        self.model = model
        # The preset policy. Valid values: fact, toc-profile, tob-digital-twin, and custom. Default value: fact.
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
        # The name of the extraction model. Currently, only qwen3.8-flash is supported. Internal platform credentials are used.
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

class GetContextStoreResponseBodyConfigExtractionPolicies(DaraModel):
    def __init__(
        self,
        categories: List[str] = None,
        custom_instructions: str = None,
        enabled: bool = None,
        exclude_rules: List[str] = None,
        model: main_models.GetContextStoreResponseBodyConfigExtractionPoliciesModel = None,
        name: str = None,
        preset: str = None,
        storage_policy: main_models.GetContextStoreResponseBodyConfigExtractionPoliciesStoragePolicy = None,
        strategy_id: str = None,
    ):
        # The list of memory categories.
        self.categories = categories
        # The custom extraction instructions. This parameter is required when preset is set to custom. The length must be 1 to 8,000 characters.
        self.custom_instructions = custom_instructions
        # Specifies whether to apply this policy to new inputs. Default value: true. Disabling the policy does not delete historical memories.
        self.enabled = enabled
        # The list of exclusion rules. Content that matches these rules is not extracted.
        self.exclude_rules = exclude_rules
        # The extraction model configuration.
        self.model = model
        # The display name of the extraction policy.
        self.name = name
        # The preset policy. Valid values: fact, toc-profile, tob-digital-twin, and custom. Default value: fact.
        self.preset = preset
        self.storage_policy = storage_policy
        # The stable ID of the extraction policy. The ID must start with a letter and can contain only letters, digits, underscores, and hyphens. It can be up to 64 characters in length. The ID must be unique within the same context library. Modifying the name or instructions does not change this ID.
        # 
        # This parameter is required.
        self.strategy_id = strategy_id

    def validate(self):
        if self.model:
            self.model.validate()
        if self.storage_policy:
            self.storage_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.categories is not None:
            result['categories'] = self.categories

        if self.custom_instructions is not None:
            result['customInstructions'] = self.custom_instructions

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.exclude_rules is not None:
            result['excludeRules'] = self.exclude_rules

        if self.model is not None:
            result['model'] = self.model.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.preset is not None:
            result['preset'] = self.preset

        if self.storage_policy is not None:
            result['storagePolicy'] = self.storage_policy.to_map()

        if self.strategy_id is not None:
            result['strategyId'] = self.strategy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categories') is not None:
            self.categories = m.get('categories')

        if m.get('customInstructions') is not None:
            self.custom_instructions = m.get('customInstructions')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('excludeRules') is not None:
            self.exclude_rules = m.get('excludeRules')

        if m.get('model') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigExtractionPoliciesModel()
            self.model = temp_model.from_map(m.get('model'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('preset') is not None:
            self.preset = m.get('preset')

        if m.get('storagePolicy') is not None:
            temp_model = main_models.GetContextStoreResponseBodyConfigExtractionPoliciesStoragePolicy()
            self.storage_policy = temp_model.from_map(m.get('storagePolicy'))

        if m.get('strategyId') is not None:
            self.strategy_id = m.get('strategyId')

        return self

class GetContextStoreResponseBodyConfigExtractionPoliciesStoragePolicy(DaraModel):
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

class GetContextStoreResponseBodyConfigExtractionPoliciesModel(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the extraction model. Currently, only qwen3.8-flash is supported. Internal platform credentials are used.
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
        # Specifies whether to write item events for dropped recall candidates. Default value: false.
        self.dropped_candidates = dropped_candidates
        # The recording mode for recall queries. Valid values: raw (plaintext) and hash (HMAC only). Default value: raw.
        self.query_mode = query_mode
        # The number of days to retain audit logs. Valid values: 1 to 180. Default value: 30.
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

