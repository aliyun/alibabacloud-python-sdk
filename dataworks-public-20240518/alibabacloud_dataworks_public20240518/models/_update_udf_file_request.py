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
        # The class name where the function is defined, corresponding to the class name field in the Create Function form.
        # 
        # This parameter is required.
        self.class_name = class_name
        # The command format for invoking the function, corresponding to the command format field in the Create Function form.
        self.cmd_description = cmd_description
        # An example demonstrating how to call the function, corresponding to the example field in the Create Function form.
        self.example = example
        # The path to the folder containing the function file.
        self.file_folder_path = file_folder_path
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The function category, corresponding to the function type field in the Create Function form. Valid values: MATH (mathematical functions), AGGREGATE (aggregate functions), STRING (string processing functions), DATE (date processing functions), ANALYTIC (window functions), and OTHER (other functions).
        # 
        # This parameter is required.
        self.function_type = function_type
        # The function parameter description, corresponding to the parameter description field in the Create Function form.
        # 
        # Valid values:
        # 
        # *   ALL_ALLOWD
        # *   FAILURE_ALLOWED
        # *   ALL_DENIED
        self.parameter_description = parameter_description
        # The DataWorks workspace ID. To find this, click the wrench icon in the upper-right corner and navigate to the workspace management page.
        self.project_id = project_id
        # The unique identifier of the DataWorks workspace, which is the identifier at the top of the Data Studio page where you switch workspaces.
        # 
        # Either this parameter or ProjectId must be specified to identify the target DataWorks workspace for this API call.
        self.project_identifier = project_identifier
        # A comma-separated list of resource names referenced by the function, corresponding to the resource list field in the Create Function form.
        # 
        # This parameter is required.
        self.resources = resources
        # The return value description, corresponding to the return value field in the Create Function form.
        self.return_value = return_value
        # The function purpose description, corresponding to the description field in the Create Function form.
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

