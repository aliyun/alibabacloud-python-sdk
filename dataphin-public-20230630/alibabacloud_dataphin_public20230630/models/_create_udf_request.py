# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateUdfRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateUdfRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        # The create command.
        # 
        # This parameter is required.
        self.create_command = create_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateUdfRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreateUdfRequestCreateCommand(DaraModel):
    def __init__(
        self,
        category: int = None,
        class_name: str = None,
        command_help: str = None,
        comment: str = None,
        compute_engine_type: str = None,
        description: str = None,
        directory: str = None,
        name: str = None,
        project_id: int = None,
        ref_resource_id_list: List[int] = None,
    ):
        # The UDF category identifier. Valid values: 1: window function. 2: statistical function. 3: numerical function. 4: string function. 5: time function. 6: IP address utility function. 7: URL-related function. 8: encoding and decoding function. 9: business-related function. 10: other.
        # 
        # This parameter is required.
        self.category = category
        # The class name that implements the function in the resource.
        # 
        # This parameter is required.
        self.class_name = class_name
        # The command format for function calling invoke.
        # 
        # This parameter is required.
        self.command_help = command_help
        # The commit remarks.
        # 
        # This parameter is required.
        self.comment = comment
        # The compute engine type. Valid values: MAX_COMPUTE, HADOOP.
        # 
        # This parameter is required.
        self.compute_engine_type = compute_engine_type
        # The description.
        # 
        # This parameter is required.
        self.description = description
        # The directory in which the function is stored.
        self.directory = directory
        # The function name.
        # 
        # This parameter is required.
        self.name = name
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The IDs of referenced resources.
        # 
        # This parameter is required.
        self.ref_resource_id_list = ref_resource_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.class_name is not None:
            result['ClassName'] = self.class_name

        if self.command_help is not None:
            result['CommandHelp'] = self.command_help

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.compute_engine_type is not None:
            result['ComputeEngineType'] = self.compute_engine_type

        if self.description is not None:
            result['Description'] = self.description

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.ref_resource_id_list is not None:
            result['RefResourceIdList'] = self.ref_resource_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')

        if m.get('CommandHelp') is not None:
            self.command_help = m.get('CommandHelp')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('ComputeEngineType') is not None:
            self.compute_engine_type = m.get('ComputeEngineType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RefResourceIdList') is not None:
            self.ref_resource_id_list = m.get('RefResourceIdList')

        return self

