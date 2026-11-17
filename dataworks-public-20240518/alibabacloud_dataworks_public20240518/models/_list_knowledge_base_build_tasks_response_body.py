# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListKnowledgeBaseBuildTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListKnowledgeBaseBuildTasksResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business error code. You can use this code to determine the error type when a request fails.
        self.code = code
        # The business data returned when the request is successful.
        self.data = data
        # The maximum number of entries per page.
        self.max_results = max_results
        # The error message returned when the request fails.
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
            temp_model = main_models.ListKnowledgeBaseBuildTasksResponseBodyData()
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

class ListKnowledgeBaseBuildTasksResponseBodyData(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        tasks: List[main_models.ListKnowledgeBaseBuildTasksResponseBodyDataTasks] = None,
    ):
        # The cursor for the next page. If there is no next page, the value is null.
        self.next_token = next_token
        # The knowledge objects that you have permission to read on the current page.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.ListKnowledgeBaseBuildTasksResponseBodyDataTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class ListKnowledgeBaseBuildTasksResponseBodyDataTasks(DaraModel):
    def __init__(
        self,
        content_locale: str = None,
        create_time: int = None,
        description: str = None,
        input: main_models.ListKnowledgeBaseBuildTasksResponseBodyDataTasksInput = None,
        knowledge_base_id: str = None,
        llm_model: str = None,
        modify_time: int = None,
        name: str = None,
        project_id: int = None,
        runtime_resource: main_models.ListKnowledgeBaseBuildTasksResponseBodyDataTasksRuntimeResource = None,
        task_id: str = None,
        trigger: main_models.ListKnowledgeBaseBuildTasksResponseBodyDataTasksTrigger = None,
        type: str = None,
    ):
        # The content language of the task. This field is optional and is explicitly selected when the task is created.
        self.content_locale = content_locale
        # The creation time.
        self.create_time = create_time
        # The description of the task. This field is optional.
        self.description = description
        # The typed input scope selected for the task. System-managed upload build tasks do not have fixed inputs, and this field is omitted when reading.
        self.input = input
        # The knowledge base to which the task belongs.
        self.knowledge_base_id = knowledge_base_id
        # The model configured for tasks that require a model. You can specify a model ID or set this parameter to AUTO. If this parameter is omitted during creation, the default value AUTO is used. Do not configure this parameter for tasks that do not call a model.
        self.llm_model = llm_model
        # The time when the definition was last modified.
        self.modify_time = modify_time
        # The name of the task.
        self.name = name
        # The ID of the DataWorks workspace where the task runs. This is different from the build asset scope specified by Input.ProjectIds.
        self.project_id = project_id
        # The resource group and Builder compute specifications for running the task.
        self.runtime_resource = runtime_resource
        # The stable task ID.
        self.task_id = task_id
        # The manual or periodic trigger configuration.
        self.trigger = trigger
        # The task type. Valid values: PROJECT_SPACE_BUILD, SEMANTIC_GRAPH, DOCUMENT_GRAPH, DOCUMENT_SYNC, DOCUMENT_SYNC_AND_GRAPH, and SEMANTIC_MODEL. The SEMANTIC_MODEL value is used only for YAML import.
        self.type = type

    def validate(self):
        if self.input:
            self.input.validate()
        if self.runtime_resource:
            self.runtime_resource.validate()
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_locale is not None:
            result['ContentLocale'] = self.content_locale

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.llm_model is not None:
            result['LlmModel'] = self.llm_model

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentLocale') is not None:
            self.content_locale = m.get('ContentLocale')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Input') is not None:
            temp_model = main_models.ListKnowledgeBaseBuildTasksResponseBodyDataTasksInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('LlmModel') is not None:
            self.llm_model = m.get('LlmModel')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.ListKnowledgeBaseBuildTasksResponseBodyDataTasksRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Trigger') is not None:
            temp_model = main_models.ListKnowledgeBaseBuildTasksResponseBodyDataTasksTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListKnowledgeBaseBuildTasksResponseBodyDataTasksTrigger(DaraModel):
    def __init__(
        self,
        cron: str = None,
        enabled: bool = None,
        mode: str = None,
    ):
        # The DataWorks scheduling cron expression. This field is provided only when the trigger mode is PERIODIC.
        self.cron = cron
        # Specifies whether periodic automatic triggering is enabled. This field is provided only when the trigger mode is PERIODIC and does not indicate the instance status.
        self.enabled = enabled
        # The trigger mode. Valid values: MANUAL and PERIODIC. Manual tasks do not create instances automatically.
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron is not None:
            result['Cron'] = self.cron

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cron') is not None:
            self.cron = m.get('Cron')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

class ListKnowledgeBaseBuildTasksResponseBodyDataTasksRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: int = None,
        resource_group_id: str = None,
    ):
        # The Builder compute specifications. Valid values: 4 to 16. If this parameter is omitted during creation, the default value 4 is used. The actual value is returned when reading.
        self.cu = cu
        # The ID of the DataWorks resource group used by the actual Builder nodes. The server verifies that the resource group is available in the workspace corresponding to the top-level ProjectId of the task.
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

class ListKnowledgeBaseBuildTasksResponseBodyDataTasksInput(DaraModel):
    def __init__(
        self,
        entities: List[main_models.ListKnowledgeBaseBuildTasksResponseBodyDataTasksInputEntities] = None,
        knowledge_object_ids: List[str] = None,
        project_ids: List[int] = None,
        source_ids: List[str] = None,
        yaml_upload_id: str = None,
    ):
        # The Data Map entities such as databases, schemas, and tables selected for data asset-scoped builds. The values must be non-empty and deduplicated.
        self.entities = entities
        # The IDs of the knowledge objects. This field is required, non-empty, and deduplicated when building from document objects in the knowledge base. Each item is a KnowledgeObjectId with Type=DOCUMENT in the knowledge base. Do not mix this field with SourceIds for external connector synchronization scopes.
        self.knowledge_object_ids = knowledge_object_ids
        # The IDs of the DataWorks workspaces selected for workspace-scoped builds. The values must be non-empty and deduplicated.
        self.project_ids = project_ids
        # The IDs of the registered sources in the knowledge base. The values are deduplicated. Whether this field is required and the allowed source types depend on the task input scenario. For more information, see the following table.
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
                temp_model = main_models.ListKnowledgeBaseBuildTasksResponseBodyDataTasksInputEntities()
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

class ListKnowledgeBaseBuildTasksResponseBodyDataTasksInputEntities(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
    ):
        # The metadata entity ID returned by Data Map. The client passes this ID as is and does not concatenate database, schema, or table identifiers.
        self.entity_id = entity_id
        # The entity level, such as DATABASE, SCHEMA, or TABLE. The server verifies this against Data Map identities. The presence of an enum value does not guarantee that all engines support it.
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

