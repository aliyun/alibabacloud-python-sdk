# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListComponentsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListComponentsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID. Use this ID for troubleshooting.
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
            temp_model = main_models.ListComponentsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListComponentsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        components: List[main_models.ListComponentsResponseBodyPagingInfoComponents] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The UID of the user who created the dataset acceleration component. In Alibaba Cloud, this is the RAM user ID (or the Alibaba Cloud account ID if created by the account itself).
        self.components = components
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.ListComponentsResponseBodyPagingInfoComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListComponentsResponseBodyPagingInfoComponents(DaraModel):
    def __init__(
        self,
        component_id: str = None,
        create_time: str = None,
        description: str = None,
        inputs: List[main_models.ListComponentsResponseBodyPagingInfoComponentsInputs] = None,
        modify_time: str = None,
        name: str = None,
        outputs: List[main_models.ListComponentsResponseBodyPagingInfoComponentsOutputs] = None,
        owner: str = None,
        project_id: int = None,
        script: main_models.ListComponentsResponseBodyPagingInfoComponentsScript = None,
    ):
        # The component ID. This parameter can be used in requests to query, modify, or delete director components.
        self.component_id = component_id
        # The creation time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.create_time = create_time
        # The description.
        self.description = description
        # The input parameters.
        self.inputs = inputs
        # The timestamp when the publishing process was modified.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.modify_time = modify_time
        # The resource name.
        self.name = name
        # The output parameters.
        self.outputs = outputs
        # The owner.
        self.owner = owner
        # The DataWorks workspace ID. To obtain the workspace ID, log on to the DataWorks console and navigate to the workspace configuration page. You must specify either this parameter or ProjectIdentifier to identify the target DataWorks workspace for this API call.
        self.project_id = project_id
        # The script information.
        self.script = script

    def validate(self):
        if self.inputs:
            for v1 in self.inputs:
                 if v1:
                    v1.validate()
        if self.outputs:
            for v1 in self.outputs:
                 if v1:
                    v1.validate()
        if self.script:
            self.script.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        result['Inputs'] = []
        if self.inputs is not None:
            for k1 in self.inputs:
                result['Inputs'].append(k1.to_map() if k1 else None)

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        result['Outputs'] = []
        if self.outputs is not None:
            for k1 in self.outputs:
                result['Outputs'].append(k1.to_map() if k1 else None)

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.script is not None:
            result['Script'] = self.script.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.inputs = []
        if m.get('Inputs') is not None:
            for k1 in m.get('Inputs'):
                temp_model = main_models.ListComponentsResponseBodyPagingInfoComponentsInputs()
                self.inputs.append(temp_model.from_map(k1))

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.outputs = []
        if m.get('Outputs') is not None:
            for k1 in m.get('Outputs'):
                temp_model = main_models.ListComponentsResponseBodyPagingInfoComponentsOutputs()
                self.outputs.append(temp_model.from_map(k1))

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Script') is not None:
            temp_model = main_models.ListComponentsResponseBodyPagingInfoComponentsScript()
            self.script = temp_model.from_map(m.get('Script'))

        return self

class ListComponentsResponseBodyPagingInfoComponentsScript(DaraModel):
    def __init__(
        self,
        id: str = None,
        path: str = None,
        runtime: main_models.ListComponentsResponseBodyPagingInfoComponentsScriptRuntime = None,
    ):
        # ID
        self.id = id
        # The script path.
        self.path = path
        # The runtime.
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
            temp_model = main_models.ListComponentsResponseBodyPagingInfoComponentsScriptRuntime()
            self.runtime = temp_model.from_map(m.get('Runtime'))

        return self

class ListComponentsResponseBodyPagingInfoComponentsScriptRuntime(DaraModel):
    def __init__(
        self,
        command: str = None,
    ):
        # The command.
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

class ListComponentsResponseBodyPagingInfoComponentsOutputs(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        # The default value.
        self.default_value = default_value
        # The parameter description.
        self.description = description
        # The parameter name.
        self.name = name
        # The parameter type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListComponentsResponseBodyPagingInfoComponentsInputs(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        # The default value of the variable.
        self.default_value = default_value
        # The parameter description.
        self.description = description
        # The parameter name.
        self.name = name
        # The parameter type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

