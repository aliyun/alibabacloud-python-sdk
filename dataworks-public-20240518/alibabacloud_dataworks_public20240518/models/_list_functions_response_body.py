# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListFunctionsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListFunctionsResponseBodyPagingInfo = None,
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
            temp_model = main_models.ListFunctionsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFunctionsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        functions: List[main_models.ListFunctionsResponseBodyPagingInfoFunctions] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The function list.
        self.functions = functions
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.functions:
            for v1 in self.functions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Functions'] = []
        if self.functions is not None:
            for k1 in self.functions:
                result['Functions'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.functions = []
        if m.get('Functions') is not None:
            for k1 in m.get('Functions'):
                temp_model = main_models.ListFunctionsResponseBodyPagingInfoFunctions()
                self.functions.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFunctionsResponseBodyPagingInfoFunctions(DaraModel):
    def __init__(
        self,
        arm_resource: str = None,
        class_name: str = None,
        command_description: str = None,
        create_time: int = None,
        data_source: main_models.ListFunctionsResponseBodyPagingInfoFunctionsDataSource = None,
        database_name: str = None,
        description: str = None,
        embedded_code: str = None,
        embedded_code_type: str = None,
        embedded_resource_type: str = None,
        example_description: str = None,
        file_resource: str = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        parameter_description: str = None,
        project_id: int = None,
        return_value_description: str = None,
        runtime_resource: main_models.ListFunctionsResponseBodyPagingInfoFunctionsRuntimeResource = None,
        script: main_models.ListFunctionsResponseBodyPagingInfoFunctionsScript = None,
        type: str = None,
    ):
        # The list of resource files for the ARM cluster.
        self.arm_resource = arm_resource
        # The fully qualified class name of the UDF.
        self.class_name = class_name
        # The command description.
        self.command_description = command_description
        # The timestamp when the UDF was created.
        self.create_time = create_time
        # Data source information of the UDF.
        self.data_source = data_source
        # The database name. This parameter is used only when the function type is EMR Function.
        self.database_name = database_name
        # The general description of the function.
        self.description = description
        # Content of the nested function code
        self.embedded_code = embedded_code
        # The nested code type.
        # 
        # Valid values:
        # 
        # *   Python2
        # *   Python3
        # *   Java8
        # *   Java11
        # *   Java17
        self.embedded_code_type = embedded_code_type
        # The nested resource type.
        # 
        # Valid values:
        # 
        # *   File: General resource file.
        # *   Embedded: Embedded resource.
        self.embedded_resource_type = embedded_resource_type
        # The example description.
        self.example_description = example_description
        # The implementation code of the function and the list of resource files.
        self.file_resource = file_resource
        # The unique identifier of the UDF.
        # 
        # >  Prior to SDK version 8.0.0, this field is of type Long. In SDK version 8.0.0 and later, it is of type String. This change does not affect the normal use of the SDK. The parameter is returned based on the type defined in the SDK. Compilation failures caused by the type change may occur only when you upgrade the SDK across version 8.0.0. In this case, you must manually update the data type.
        self.id = id
        # The modification time.
        self.modify_time = modify_time
        # The UDF name.
        self.name = name
        # The owner of the UDF.
        self.owner = owner
        # The parameter description.
        self.parameter_description = parameter_description
        # The ID of the project to which the UDF belongs.
        self.project_id = project_id
        # The return value description.
        self.return_value_description = return_value_description
        # The runtime resource group information.
        self.runtime_resource = runtime_resource
        # Script information of the UDF.
        self.script = script
        # The UDF type.
        # 
        # Valid values:
        # 
        # *   Math: Mathematical operation functions
        # *   Aggregate: Aggregation functions
        # *   String: String processing functions
        # *   Date: Date functions
        # *   Analytic: Window functions
        # *   Other: Other functions
        self.type = type

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.runtime_resource:
            self.runtime_resource.validate()
        if self.script:
            self.script.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arm_resource is not None:
            result['ArmResource'] = self.arm_resource

        if self.class_name is not None:
            result['ClassName'] = self.class_name

        if self.command_description is not None:
            result['CommandDescription'] = self.command_description

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.description is not None:
            result['Description'] = self.description

        if self.embedded_code is not None:
            result['EmbeddedCode'] = self.embedded_code

        if self.embedded_code_type is not None:
            result['EmbeddedCodeType'] = self.embedded_code_type

        if self.embedded_resource_type is not None:
            result['EmbeddedResourceType'] = self.embedded_resource_type

        if self.example_description is not None:
            result['ExampleDescription'] = self.example_description

        if self.file_resource is not None:
            result['FileResource'] = self.file_resource

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.return_value_description is not None:
            result['ReturnValueDescription'] = self.return_value_description

        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource.to_map()

        if self.script is not None:
            result['Script'] = self.script.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArmResource') is not None:
            self.arm_resource = m.get('ArmResource')

        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')

        if m.get('CommandDescription') is not None:
            self.command_description = m.get('CommandDescription')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSource') is not None:
            temp_model = main_models.ListFunctionsResponseBodyPagingInfoFunctionsDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EmbeddedCode') is not None:
            self.embedded_code = m.get('EmbeddedCode')

        if m.get('EmbeddedCodeType') is not None:
            self.embedded_code_type = m.get('EmbeddedCodeType')

        if m.get('EmbeddedResourceType') is not None:
            self.embedded_resource_type = m.get('EmbeddedResourceType')

        if m.get('ExampleDescription') is not None:
            self.example_description = m.get('ExampleDescription')

        if m.get('FileResource') is not None:
            self.file_resource = m.get('FileResource')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ReturnValueDescription') is not None:
            self.return_value_description = m.get('ReturnValueDescription')

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.ListFunctionsResponseBodyPagingInfoFunctionsRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('Script') is not None:
            temp_model = main_models.ListFunctionsResponseBodyPagingInfoFunctionsScript()
            self.script = temp_model.from_map(m.get('Script'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListFunctionsResponseBodyPagingInfoFunctionsScript(DaraModel):
    def __init__(
        self,
        id: str = None,
        path: str = None,
        runtime: main_models.ListFunctionsResponseBodyPagingInfoFunctionsScriptRuntime = None,
    ):
        # The ID of the script.
        # 
        # >  This field is of type Long in SDK versions prior to 8.0.0, and of type String in SDK version 8.0.0 and later. This change does not affect the normal use of the SDK. The parameter is returned based on the type defined in the SDK. However, compilation failures may occur due to the type change only when upgrading the SDK across version 8.0.0. In this case, you must manually update the data type.
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
            temp_model = main_models.ListFunctionsResponseBodyPagingInfoFunctionsScriptRuntime()
            self.runtime = temp_model.from_map(m.get('Runtime'))

        return self

class ListFunctionsResponseBodyPagingInfoFunctionsScriptRuntime(DaraModel):
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

class ListFunctionsResponseBodyPagingInfoFunctionsRuntimeResource(DaraModel):
    def __init__(
        self,
        resource_group_id: str = None,
    ):
        # The runtime resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

class ListFunctionsResponseBodyPagingInfoFunctionsDataSource(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the data source.
        self.name = name
        # The type of the data source.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

