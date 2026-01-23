# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateStandardLookupTableRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateStandardLookupTableRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_command = create_command
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
            temp_model = main_models.CreateStandardLookupTableRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreateStandardLookupTableRequestCreateCommand(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        directory_reference: main_models.CreateStandardLookupTableRequestCreateCommandDirectoryReference = None,
        lookup_table_value_list: List[main_models.CreateStandardLookupTableRequestCreateCommandLookupTableValueList] = None,
        name: str = None,
        owner: str = None,
    ):
        # This parameter is required.
        self.code = code
        self.description = description
        self.directory_reference = directory_reference
        self.lookup_table_value_list = lookup_table_value_list
        # This parameter is required.
        self.name = name
        self.owner = owner

    def validate(self):
        if self.directory_reference:
            self.directory_reference.validate()
        if self.lookup_table_value_list:
            for v1 in self.lookup_table_value_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.description is not None:
            result['Description'] = self.description

        if self.directory_reference is not None:
            result['DirectoryReference'] = self.directory_reference.to_map()

        result['LookupTableValueList'] = []
        if self.lookup_table_value_list is not None:
            for k1 in self.lookup_table_value_list:
                result['LookupTableValueList'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DirectoryReference') is not None:
            temp_model = main_models.CreateStandardLookupTableRequestCreateCommandDirectoryReference()
            self.directory_reference = temp_model.from_map(m.get('DirectoryReference'))

        self.lookup_table_value_list = []
        if m.get('LookupTableValueList') is not None:
            for k1 in m.get('LookupTableValueList'):
                temp_model = main_models.CreateStandardLookupTableRequestCreateCommandLookupTableValueList()
                self.lookup_table_value_list.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        return self

class CreateStandardLookupTableRequestCreateCommandLookupTableValueList(DaraModel):
    def __init__(
        self,
        description: str = None,
        english_name: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.english_name = english_name
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.english_name is not None:
            result['EnglishName'] = self.english_name

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnglishName') is not None:
            self.english_name = m.get('EnglishName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateStandardLookupTableRequestCreateCommandDirectoryReference(DaraModel):
    def __init__(
        self,
        directory: str = None,
    ):
        # This parameter is required.
        self.directory = directory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory is not None:
            result['Directory'] = self.directory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        return self

