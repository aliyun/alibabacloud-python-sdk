# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUdfFileRequest(DaraModel):
    def __init__(
        self,
        class_name: str = None,
        cmd_description: str = None,
        create_folder_if_not_exists: bool = None,
        example: str = None,
        file_folder_path: str = None,
        file_name: str = None,
        function_type: str = None,
        parameter_description: str = None,
        project_id: int = None,
        project_identifier: str = None,
        resources: str = None,
        return_value: str = None,
        udf_description: str = None,
    ):
        # The name of the class in which the function is defined, which corresponds to the Class Name field in the Create Function form.
        # 
        # This parameter is required.
        self.class_name = class_name
        # The command format for invoking the function, which corresponds to the Command Format field in the Create Function form.
        self.cmd_description = cmd_description
        # Specifies whether to enable automatic creation of the directory specified by the FileFolderPath parameter if it does not exist. Valid values:
        # 
        # - true: Automatically creates the directory if it does not exist.
        # 
        # - false: The invocation fails if the directory does not exist.
        self.create_folder_if_not_exists = create_folder_if_not_exists
        # The function invocation example, which corresponds to the Example field in the Create Function form.
        self.example = example
        # The path of the folder where the function file is stored.
        self.file_folder_path = file_folder_path
        # The name of the function.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The categorization of the function, which corresponds to the Function Type field in the Create Function form. Valid values: MATH (mathematical operation function), AGGREGATE (aggregate functions), STRING (character string processing function), DATE (date processing function), ANALYTIC (window function), and OTHER (other function).
        # 
        # This parameter is required.
        self.function_type = function_type
        # The description of the function input parameters, which corresponds to the Parameter Description field in the Create Function form.
        self.parameter_description = parameter_description
        # The ID of the DataWorks workspace. You can click the small wrench icon in the upper-right corner of the page to go to the storage management page and view the ID.
        self.project_id = project_id
        # The unique identifier of the DataWorks workspace, which is the English identifier displayed in the workspace switcher at the top of the DataStudio page.
        self.project_identifier = project_identifier
        # The resources referenced by the function, which corresponds to the Resources field in the Create Function form. Separate multiple resource names with commas (,).
        # 
        # This parameter is required.
        self.resources = resources
        # The description of the return value of the function, which corresponds to the Return Value field in the Create Function form.
        self.return_value = return_value
        # The description of the function purpose, which corresponds to the Description field in the Create Function form.
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

        if self.create_folder_if_not_exists is not None:
            result['CreateFolderIfNotExists'] = self.create_folder_if_not_exists

        if self.example is not None:
            result['Example'] = self.example

        if self.file_folder_path is not None:
            result['FileFolderPath'] = self.file_folder_path

        if self.file_name is not None:
            result['FileName'] = self.file_name

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

        if m.get('CreateFolderIfNotExists') is not None:
            self.create_folder_if_not_exists = m.get('CreateFolderIfNotExists')

        if m.get('Example') is not None:
            self.example = m.get('Example')

        if m.get('FileFolderPath') is not None:
            self.file_folder_path = m.get('FileFolderPath')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

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

