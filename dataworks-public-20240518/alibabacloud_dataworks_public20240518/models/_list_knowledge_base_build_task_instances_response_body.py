# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListKnowledgeBaseBuildTaskInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business error code, which is used to determine the error type when the request fails.
        self.code = code
        # The business data returned when the request is successful.
        self.data = data
        # The maximum number of entries per page.
        self.max_results = max_results
        # The secure error message returned when the request fails.
        self.message = message
        # The unique identifier of the request, which can be used to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListKnowledgeBaseBuildTaskInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstances] = None,
        next_token: str = None,
    ):
        # The knowledge objects that you have permissions to read on the current page.
        self.instances = instances
        # The pagination token for the next page. This field is null if there is no next page.
        self.next_token = next_token

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstances(DaraModel):
    def __init__(
        self,
        config_snapshot: main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesConfigSnapshot = None,
        create_time: int = None,
        current_stage: str = None,
        error: main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesError = None,
        finished_time: int = None,
        generated_models: List[main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesGeneratedModels] = None,
        input_snapshot: main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesInputSnapshot = None,
        knowledge_base_id: str = None,
        started_time: int = None,
        status: str = None,
        task_id: str = None,
        task_instance_id: str = None,
        trigger_type: str = None,
    ):
        # The snapshot of the model, content language, and runtime resources for the execution. This snapshot does not change when the task is updated.
        self.config_snapshot = config_snapshot
        # The time when the instance was created.
        self.create_time = create_time
        # The current business stage, returned when reliable records are available. For standard build stages and semantic model import stages, refer to the domain model. This field does not replace the overall status.
        self.current_stage = current_stage
        # The error code and secure error message returned when the execution fails.
        self.error = error
        # The time when the execution finished. This field is optional.
        self.finished_time = finished_time
        # The confirmed ModelId and VersionNo for model imports only. For their structure, see GetKnowledgeBaseBuildTaskInstance.
        self.generated_models = generated_models
        # The non-sensitive input snapshot after selection and parsing for the execution. This snapshot does not change when the task is updated.
        self.input_snapshot = input_snapshot
        # The ID of the knowledge base to which the instance belongs. Use it for scope validation and queries.
        self.knowledge_base_id = knowledge_base_id
        # The time when the execution started. This field is optional.
        self.started_time = started_time
        # The overall status of the execution.
        self.status = status
        # The source task ID.
        self.task_id = task_id
        # The task instance ID.
        self.task_instance_id = task_instance_id
        # The trigger type of the execution, which can be manual, periodic, or a supported event.
        self.trigger_type = trigger_type

    def validate(self):
        if self.config_snapshot:
            self.config_snapshot.validate()
        if self.error:
            self.error.validate()
        if self.generated_models:
            for v1 in self.generated_models:
                 if v1:
                    v1.validate()
        if self.input_snapshot:
            self.input_snapshot.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_snapshot is not None:
            result['ConfigSnapshot'] = self.config_snapshot.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.current_stage is not None:
            result['CurrentStage'] = self.current_stage

        if self.error is not None:
            result['Error'] = self.error.to_map()

        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        result['GeneratedModels'] = []
        if self.generated_models is not None:
            for k1 in self.generated_models:
                result['GeneratedModels'].append(k1.to_map() if k1 else None)

        if self.input_snapshot is not None:
            result['InputSnapshot'] = self.input_snapshot.to_map()

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.started_time is not None:
            result['StartedTime'] = self.started_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_instance_id is not None:
            result['TaskInstanceId'] = self.task_instance_id

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigSnapshot') is not None:
            temp_model = main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesConfigSnapshot()
            self.config_snapshot = temp_model.from_map(m.get('ConfigSnapshot'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CurrentStage') is not None:
            self.current_stage = m.get('CurrentStage')

        if m.get('Error') is not None:
            temp_model = main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesError()
            self.error = temp_model.from_map(m.get('Error'))

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        self.generated_models = []
        if m.get('GeneratedModels') is not None:
            for k1 in m.get('GeneratedModels'):
                temp_model = main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesGeneratedModels()
                self.generated_models.append(temp_model.from_map(k1))

        if m.get('InputSnapshot') is not None:
            temp_model = main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesInputSnapshot()
            self.input_snapshot = temp_model.from_map(m.get('InputSnapshot'))

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskInstanceId') is not None:
            self.task_instance_id = m.get('TaskInstanceId')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

class ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesInputSnapshot(DaraModel):
    def __init__(
        self,
        document_source_count: int = None,
        file_paths: List[str] = None,
        resolved_entities: List[main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesInputSnapshotResolvedEntities] = None,
        resolved_entity_count: int = None,
        selected_input: main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesInputSnapshotSelectedInput = None,
    ):
        # The number of external document sources selected for the execution. This field is not returned when not applicable.
        self.document_source_count = document_source_count
        # The relative file paths in the knowledge base processed for page upload builds in the execution. These paths are from the frozen upload list of the instance. OSS addresses or verification information are not returned, and the current task or file list is not re-read.
        self.file_paths = file_paths
        # The actual Data Map entities resolved from the project, database, or schema scope for the execution. This field is not returned when not applicable.
        self.resolved_entities = resolved_entities
        # The total number of resolved entities. An accurate count is returned even if the array is omitted due to its size.
        self.resolved_entity_count = resolved_entity_count
        # The snapshot of the selection conditions in the task definition when the instance was created. This snapshot does not change when the task is updated. This field is omitted if no fixed object is selected for page upload builds.
        self.selected_input = selected_input

    def validate(self):
        if self.resolved_entities:
            for v1 in self.resolved_entities:
                 if v1:
                    v1.validate()
        if self.selected_input:
            self.selected_input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_source_count is not None:
            result['DocumentSourceCount'] = self.document_source_count

        if self.file_paths is not None:
            result['FilePaths'] = self.file_paths

        result['ResolvedEntities'] = []
        if self.resolved_entities is not None:
            for k1 in self.resolved_entities:
                result['ResolvedEntities'].append(k1.to_map() if k1 else None)

        if self.resolved_entity_count is not None:
            result['ResolvedEntityCount'] = self.resolved_entity_count

        if self.selected_input is not None:
            result['SelectedInput'] = self.selected_input.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentSourceCount') is not None:
            self.document_source_count = m.get('DocumentSourceCount')

        if m.get('FilePaths') is not None:
            self.file_paths = m.get('FilePaths')

        self.resolved_entities = []
        if m.get('ResolvedEntities') is not None:
            for k1 in m.get('ResolvedEntities'):
                temp_model = main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesInputSnapshotResolvedEntities()
                self.resolved_entities.append(temp_model.from_map(k1))

        if m.get('ResolvedEntityCount') is not None:
            self.resolved_entity_count = m.get('ResolvedEntityCount')

        if m.get('SelectedInput') is not None:
            temp_model = main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesInputSnapshotSelectedInput()
            self.selected_input = temp_model.from_map(m.get('SelectedInput'))

        return self

class ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesInputSnapshotSelectedInput(DaraModel):
    def __init__(
        self,
        entities: List[main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesInputSnapshotSelectedInputEntities] = None,
        knowledge_object_ids: List[str] = None,
        project_ids: List[int] = None,
        source_ids: List[str] = None,
        yaml_upload_id: str = None,
    ):
        # The Data Map entities, such as databases, schemas, and tables, selected for data asset-scoped builds. The list is non-empty and deduplicated.
        self.entities = entities
        # Required, non-empty, and deduplicated when building from document objects in the knowledge base. Each item is a KnowledgeObjectId with Type=DOCUMENT in the knowledge base. This field cannot be mixed with SourceIds used for external connector synchronization scopes.
        self.knowledge_object_ids = knowledge_object_ids
        # The DataWorks workspace IDs selected for workspace-scoped builds. The list is non-empty and deduplicated.
        self.project_ids = project_ids
        # The IDs of the registered sources in the knowledge base. The list is deduplicated. Whether this field is required and the allowed source types depend on the task input scenario. Refer to the following table.
        self.source_ids = source_ids
        # The YAML upload session ID in the knowledge base used for SEMANTIC_MODEL import tasks. This ID is bound when the task is created and cannot be mixed with other input scopes.
        self.yaml_upload_id = yaml_upload_id

    def validate(self):
        if self.entities:
            for v1 in self.entities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Entities'] = []
        if self.entities is not None:
            for k1 in self.entities:
                result['Entities'].append(k1.to_map() if k1 else None)

        if self.knowledge_object_ids is not None:
            result['KnowledgeObjectIds'] = self.knowledge_object_ids

        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids

        if self.source_ids is not None:
            result['SourceIds'] = self.source_ids

        if self.yaml_upload_id is not None:
            result['YamlUploadId'] = self.yaml_upload_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entities = []
        if m.get('Entities') is not None:
            for k1 in m.get('Entities'):
                temp_model = main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesInputSnapshotSelectedInputEntities()
                self.entities.append(temp_model.from_map(k1))

        if m.get('KnowledgeObjectIds') is not None:
            self.knowledge_object_ids = m.get('KnowledgeObjectIds')

        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')

        if m.get('SourceIds') is not None:
            self.source_ids = m.get('SourceIds')

        if m.get('YamlUploadId') is not None:
            self.yaml_upload_id = m.get('YamlUploadId')

        return self

class ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesInputSnapshotSelectedInputEntities(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
    ):
        # The metadata entity ID returned by Data Map. The client must pass this ID as is without concatenating database, schema, or table identifiers.
        self.entity_id = entity_id
        # The entity level, such as DATABASE, SCHEMA, or TABLE. The server validates this based on Data Map identities. The presence of an enum value does not guarantee that all engines support it.
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        return self

class ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesInputSnapshotResolvedEntities(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
    ):
        # The metadata entity ID returned by Data Map. The client must pass this ID as is without concatenating database, schema, or table identifiers.
        self.entity_id = entity_id
        # The entity level, such as DATABASE, SCHEMA, or TABLE. The server validates this based on Data Map identities. The presence of an enum value does not guarantee that all engines support it.
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        return self

class ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesGeneratedModels(DaraModel):
    def __init__(
        self,
        model_id: str = None,
        version_no: int = None,
    ):
        # The model ID generated by the semantic layer. You can use it as a KnowledgeObjectId to read the corresponding semantic model.
        self.model_id = model_id
        # The current version of the SEMANTIC_MODEL being read. Pass this value when updating content. The version can be edited in place.
        self.version_no = version_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.version_no is not None:
            result['VersionNo'] = self.version_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('VersionNo') is not None:
            self.version_no = m.get('VersionNo')

        return self

class ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The business error code, which is used to determine the error type when the request fails.
        self.code = code
        # The secure error message returned when the request fails.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

class ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesConfigSnapshot(DaraModel):
    def __init__(
        self,
        content_locale: str = None,
        llm_model: str = None,
        project_id: int = None,
        runtime_resource: main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesConfigSnapshotRuntimeResource = None,
    ):
        # The content language used for the execution.
        self.content_locale = content_locale
        # The specific model ID actually used and frozen for the execution. AUTO is not returned. This field can be empty for tasks that do not call models, such as pure synchronization tasks.
        self.llm_model = llm_model
        # The DataWorks workspace ID used for the execution, frozen from the task definition when the instance was created.
        self.project_id = project_id
        # The resource group and Builder CUs actually used for the execution.
        self.runtime_resource = runtime_resource

    def validate(self):
        if self.runtime_resource:
            self.runtime_resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_locale is not None:
            result['ContentLocale'] = self.content_locale

        if self.llm_model is not None:
            result['LlmModel'] = self.llm_model

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentLocale') is not None:
            self.content_locale = m.get('ContentLocale')

        if m.get('LlmModel') is not None:
            self.llm_model = m.get('LlmModel')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesConfigSnapshotRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        return self

class ListKnowledgeBaseBuildTaskInstancesResponseBodyDataInstancesConfigSnapshotRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: int = None,
        resource_group_id: str = None,
    ):
        # The Builder compute specifications. Valid values: 4 to 16. If omitted during creation, the default value is 4. The read operation returns the effective value.
        self.cu = cu
        # The DataWorks resource group ID used by the actual Builder nodes. The server verifies its availability in the workspace corresponding to the top-level ProjectId of the task.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['Cu'] = self.cu

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

