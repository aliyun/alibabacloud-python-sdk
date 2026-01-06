# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListWorkflowDefinitionsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListWorkflowDefinitionsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListWorkflowDefinitionsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListWorkflowDefinitionsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        workflow_definitions: List[main_models.ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitions] = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count
        # The workflows.
        self.workflow_definitions = workflow_definitions

    def validate(self):
        if self.workflow_definitions:
            for v1 in self.workflow_definitions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['WorkflowDefinitions'] = []
        if self.workflow_definitions is not None:
            for k1 in self.workflow_definitions:
                result['WorkflowDefinitions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.workflow_definitions = []
        if m.get('WorkflowDefinitions') is not None:
            for k1 in m.get('WorkflowDefinitions'):
                temp_model = main_models.ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitions()
                self.workflow_definitions.append(temp_model.from_map(k1))

        return self

class ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitions(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        project_id: int = None,
        script: main_models.ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitionsScript = None,
        type: str = None,
    ):
        # The timestamp when the workflow was created.
        self.create_time = create_time
        # Description
        self.description = description
        # The unique identifier of the workflow.
        # 
        # >  Prior to SDK version 8.0.0, this field is of type Long. In SDK version 8.0.0 and later, it is of type String. This change does not affect the normal use of the SDK. The parameter is returned based on the type defined in the SDK. Compilation failures caused by the type change may occur only when you upgrade the SDK across version 8.0.0. In this case, you must manually update the data type.
        self.id = id
        # The timestamp when the workflow was last modified.
        self.modify_time = modify_time
        # The name of the workflow.
        self.name = name
        # Owner
        self.owner = owner
        # The ID of the DataWorks workspace to which the workflow belongs.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The script information.
        self.script = script
        # The type of the workflow.
        # 
        # Valid values:
        # 
        # *   CycleWorkflow
        # *   ManualWorkflow
        self.type = type

    def validate(self):
        if self.script:
            self.script.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.script is not None:
            result['Script'] = self.script.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Script') is not None:
            temp_model = main_models.ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitionsScript()
            self.script = temp_model.from_map(m.get('Script'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitionsScript(DaraModel):
    def __init__(
        self,
        id: str = None,
        path: str = None,
        runtime: main_models.ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitionsScriptRuntime = None,
    ):
        # The ID of the script.
        # 
        # >  This field is of type Long in SDK versions prior to 8.0.0, and of type String in SDK version 8.0.0 and later. This change does not affect the normal use of the SDK. The parameter is returned based on the type defined in the SDK. Compilation failures due to the type change may occur only when upgrading the SDK across version 8.0.0, in which case users need to manually correct the data type.
        self.id = id
        # The script path.
        self.path = path
        # Runtime
        self.runtime = runtime

    def validate(self):
        if self.runtime:
            self.runtime.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.path is not None:
            result['Path'] = self.path

        if self.runtime is not None:
            result['Runtime'] = self.runtime.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Runtime') is not None:
            temp_model = main_models.ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitionsScriptRuntime()
            self.runtime = temp_model.from_map(m.get('Runtime'))

        return self

class ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitionsScriptRuntime(DaraModel):
    def __init__(
        self,
        command: str = None,
    ):
        # Command
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')

        return self

