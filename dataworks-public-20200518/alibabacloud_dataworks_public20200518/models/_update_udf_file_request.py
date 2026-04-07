# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUdfFileRequest(DaraModel):
    def __init__(
        self,
        class_name: str = None,
        cmd_description: str = None,
        example: str = None,
        file_folder_path: str = None,
        file_id: str = None,
        function_type: str = None,
        parameter_description: str = None,
        project_id: int = None,
        project_identifier: str = None,
        resources: str = None,
        return_value: str = None,
        udf_description: str = None,
    ):
        # The name of the class in which the function is defined. This parameter corresponds to the Class Name parameter in the Register Function section of the configuration tab of the function in the DataWorks console.
        # 
        # This parameter is required.
        self.class_name = class_name
        # The syntax used for calling the function. This parameter corresponds to the Expression Syntax parameter in the Register Function section of the configuration tab of the function in the DataWorks console.
        self.cmd_description = cmd_description
        # The example for calling the function. This parameter corresponds to the Example parameter in the Register Function section of the configuration tab of the function in the DataWorks console.
        self.example = example
        # The path of the folder in which the function file is stored.
        self.file_folder_path = file_folder_path
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The type of the function. Valid values: MATH, AGGREGATE, STRING, DATE, ANALYTIC, and OTHER. This parameter corresponds to the Function Type parameter in the Register Function section of the configuration tab of the function on the DataStudio page.
        # 
        # This parameter is required.
        self.function_type = function_type
        # The description of the input parameters of the function. This parameter corresponds to the Parameter Description parameter in the Register Function section of the configuration tab of the function on the DataStudio page.
        # 
        # Valid values:
        # 
        # *   ALL_ALLOWD
        # *   FAILURE_ALLOWED
        # *   ALL_DENIED
        self.parameter_description = parameter_description
        # The ID of the DataWorks workspace. You can click the Workspace Manage icon in the upper-right corner of the DataStudio page to go to the Workspace Management page and view the workspace ID.
        self.project_id = project_id
        # The unique identifier of the DataWorks workspace. You can click the identifier in the upper-left corner of the DataStudio page to switch to another workspace.
        # 
        # You must specify either this parameter or ProjectId to determine the DataWorks workspace to which the operation is applied.
        self.project_identifier = project_identifier
        # The names of the resources that are referenced by the function. This parameter corresponds to the Resources parameter in the Register Function section of the configuration tab of the function in the DataWorks console. Separate multiple resource names with commas (,).
        # 
        # This parameter is required.
        self.resources = resources
        # The description of the return value of the function. This parameter corresponds to the Return Value parameter in the Register Function section of the configuration tab of the function on the DataStudio page.
        self.return_value = return_value
        # The description of the function. This parameter corresponds to the Description parameter in the Register Function section of the configuration tab of the function on the DataStudio page.
        self.udf_description = udf_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_name is not None:
            result['ClassName'] = self.class_name

        if self.cmd_description is not None:
            result['CmdDescription'] = self.cmd_description

        if self.example is not None:
            result['Example'] = self.example

        if self.file_folder_path is not None:
            result['FileFolderPath'] = self.file_folder_path

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.function_type is not None:
            result['FunctionType'] = self.function_type

        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.return_value is not None:
            result['ReturnValue'] = self.return_value

        if self.udf_description is not None:
            result['UdfDescription'] = self.udf_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')

        if m.get('CmdDescription') is not None:
            self.cmd_description = m.get('CmdDescription')

        if m.get('Example') is not None:
            self.example = m.get('Example')

        if m.get('FileFolderPath') is not None:
            self.file_folder_path = m.get('FileFolderPath')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('ReturnValue') is not None:
            self.return_value = m.get('ReturnValue')

        if m.get('UdfDescription') is not None:
            self.udf_description = m.get('UdfDescription')

        return self

