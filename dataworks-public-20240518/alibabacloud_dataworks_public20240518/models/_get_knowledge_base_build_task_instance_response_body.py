# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetKnowledgeBaseBuildTaskInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business error code. You can use this code to determine the error type when a request fails.
        self.code = code
        # The business data returned when the request is successful.
        self.data = data
        # The secure error message returned when the request fails.
        self.message = message
        # The unique identifier of the request. You can use this ID to troubleshoot issues.
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
            temp_model = main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetKnowledgeBaseBuildTaskInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        config_snapshot: main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyDataConfigSnapshot = None,
        create_time: int = None,
        current_stage: str = None,
        error: main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyDataError = None,
        finished_time: int = None,
        generated_models: List[main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyDataGeneratedModels] = None,
        input_snapshot: main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyDataInputSnapshot = None,
        knowledge_base_id: str = None,
        started_time: int = None,
        status: str = None,
        task_id: str = None,
        task_instance_id: str = None,
        trigger_type: str = None,
    ):
        # The snapshot of the model, content language, and runtime resources for the current run. This snapshot does not change when the task is updated.
        self.config_snapshot = config_snapshot
        # The time when the instance was created.
        self.create_time = create_time
        # The current business stage. This field is returned when reliable records are available. For common build stages and semantic model import stages, refer to the domain model. This field does not replace the overall status.
        self.current_stage = current_stage
        # The error code and secure error message returned when the request fails.
        self.error = error
        # The time when the execution finished. This field is optional.
        self.finished_time = finished_time
        # The confirmed materialization results of the semantic model import instance. For the structures of ModelId and VersionNo, refer to the YAML import results section.
        self.generated_models = generated_models
        # The non-sensitive input snapshot after selection and parsing for the current run. This snapshot does not change when the task is updated.
        self.input_snapshot = input_snapshot
        # The ID of the associated knowledge base, which facilitates scope validation and queries.
        self.knowledge_base_id = knowledge_base_id
        # The time when the execution started. This field is optional.
        self.started_time = started_time
        # The overall status. Valid values: PENDING, RUNNING, SUCCEEDED, FAILED, and STOPPED. The STOPPED status includes instances that are manually stopped or terminated because they are replaced by subsequent builds. The system no longer waits for these instances to succeed.
        self.status = status
        # The ID of the source task.
        self.task_id = task_id
        # The execution ID.
        self.task_instance_id = task_instance_id
        # The trigger type of the current run, such as manual, periodic, or a supported event.
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
            temp_model = main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyDataConfigSnapshot()
            self.config_snapshot = temp_model.from_map(m.get('ConfigSnapshot'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CurrentStage') is not None:
            self.current_stage = m.get('CurrentStage')

        if m.get('Error') is not None:
            temp_model = main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyDataError()
            self.error = temp_model.from_map(m.get('Error'))

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        self.generated_models = []
        if m.get('GeneratedModels') is not None:
            for k1 in m.get('GeneratedModels'):
                temp_model = main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyDataGeneratedModels()
                self.generated_models.append(temp_model.from_map(k1))

        if m.get('InputSnapshot') is not None:
            temp_model = main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyDataInputSnapshot()
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

class GetKnowledgeBaseBuildTaskInstanceResponseBodyDataInputSnapshot(DaraModel):
    def __init__(
        self,
        document_source_count: int = None,
        file_paths: List[str] = None,
        resolved_entities: List[main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyDataInputSnapshotResolvedEntities] = None,
        resolved_entity_count: int = None,
        selected_input: main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyDataInputSnapshotSelectedInput = None,
    ):
        # The number of external document sources selected for the current run. This field is not returned when it is not applicable.
        self.document_source_count = document_source_count
        # The relative file paths within the knowledge base processed for the current page upload build. These paths are from the frozen upload list of the instance. OSS addresses or verification information is not returned, and the current task or file list is not re-read.
        self.file_paths = file_paths
        # The actual Data Map entities resolved from the project, database, or schema scope for the current run. This field is not returned when it is not applicable.
        self.resolved_entities = resolved_entities
        # The total number of resolved entities. An accurate count is returned even if the array is not returned due to its size.
        self.resolved_entity_count = resolved_entity_count
        # The snapshot of the selection conditions in the task definition when the instance is created. This snapshot does not change when the task is updated. This field is omitted for page upload builds that do not have fixed object selections.
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
                temp_model = main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyDataInputSnapshotResolvedEntities()
                self.resolved_entities.append(temp_model.from_map(k1))

        if m.get('ResolvedEntityCount') is not None:
            self.resolved_entity_count = m.get('ResolvedEntityCount')

        if m.get('SelectedInput') is not None:
            temp_model = main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyDataInputSnapshotSelectedInput()
            self.selected_input = temp_model.from_map(m.get('SelectedInput'))

        return self

class GetKnowledgeBaseBuildTaskInstanceResponseBodyDataInputSnapshotSelectedInput(DaraModel):
    def __init__(
        self,
        entities: List[main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyDataInputSnapshotSelectedInputEntities] = None,
        knowledge_object_ids: List[str] = None,
        project_ids: List[int] = None,
        source_ids: List[str] = None,
        yaml_upload_id: str = None,
    ):
        # The Data Map entities such as databases, schemas, and tables selected for data asset-scoped builds. The values are non-empty and deduplicated.
        self.entities = entities
        # The knowledge object IDs required when building from document objects in the current knowledge base. The values must be non-empty and deduplicated. Each item is a KnowledgeObjectId with Type=DOCUMENT in the current knowledge base. Do not mix these IDs with the SourceIds used for external connector synchronization scopes.
        self.knowledge_object_ids = knowledge_object_ids
        # The DataWorks workspace IDs selected for workspace-scoped builds. The values are non-empty and deduplicated.
        self.project_ids = project_ids
        # The IDs of the registered sources in the current knowledge base. The values are deduplicated. Whether this field is required and the allowed source types depend on the task input scenario. Refer to the following table.
        self.source_ids = source_ids
        # The YAML upload session ID in the current knowledge base used for SEMANTIC_MODEL import tasks. This ID is bound when the task is created and cannot be mixed with other input scopes.
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
                temp_model = main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyDataInputSnapshotSelectedInputEntities()
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

class GetKnowledgeBaseBuildTaskInstanceResponseBodyDataInputSnapshotSelectedInputEntities(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
    ):
        # The metadata entity ID returned by Data Map. The client passes this ID as is and does not concatenate database, schema, or table identifiers.
        self.entity_id = entity_id
        # The entity level, such as DATABASE, SCHEMA, or TABLE. The server validates this field based on the Data Map identity. The presence of an enumeration value does not guarantee that all engines support it.
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

class GetKnowledgeBaseBuildTaskInstanceResponseBodyDataInputSnapshotResolvedEntities(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
    ):
        # The metadata entity ID returned by Data Map. The client passes this ID as is and does not concatenate database, schema, or table identifiers.
        self.entity_id = entity_id
        # The entity level, such as DATABASE, SCHEMA, or TABLE. The server validates this field based on the Data Map identity. The presence of an enumeration value does not guarantee that all engines support it.
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

class GetKnowledgeBaseBuildTaskInstanceResponseBodyDataGeneratedModels(DaraModel):
    def __init__(
        self,
        model_id: str = None,
        version_no: int = None,
    ):
        # The stable model ID in the semantic layer, which can be used as a KnowledgeObjectId.
        self.model_id = model_id
        # The materialization version for the current run. The same version can be edited later and does not represent an immutable file snapshot.
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

class GetKnowledgeBaseBuildTaskInstanceResponseBodyDataError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The business error code. You can use this code to determine the error type when a request fails.
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

class GetKnowledgeBaseBuildTaskInstanceResponseBodyDataConfigSnapshot(DaraModel):
    def __init__(
        self,
        content_locale: str = None,
        llm_model: str = None,
        project_id: int = None,
        runtime_resource: main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyDataConfigSnapshotRuntimeResource = None,
    ):
        # The content language used for the current run.
        self.content_locale = content_locale
        # The specific model ID actually used and frozen for the current run. The value AUTO is not returned. This field can be empty for tasks that do not call models, such as pure synchronization tasks.
        self.llm_model = llm_model
        # The DataWorks workspace ID used for the current run. This ID is frozen from the task definition when the instance is created.
        self.project_id = project_id
        # The resource group and Builder compute units (CUs) actually used for the current run.
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
            temp_model = main_models.GetKnowledgeBaseBuildTaskInstanceResponseBodyDataConfigSnapshotRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        return self

class GetKnowledgeBaseBuildTaskInstanceResponseBodyDataConfigSnapshotRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: int = None,
        resource_group_id: str = None,
    ):
        # The Builder compute specifications. Valid values: 4 to 16. If this field is omitted during creation, the valid value is 4. The read operation returns the valid value.
        self.cu = cu
        # The DataWorks resource group ID used by the actual Builder nodes. The server verifies that this resource group is available in the workspace corresponding to the top-level ProjectId of the task.
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

