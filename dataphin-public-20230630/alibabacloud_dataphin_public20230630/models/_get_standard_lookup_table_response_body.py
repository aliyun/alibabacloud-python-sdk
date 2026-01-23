# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetStandardLookupTableResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        lookup_table_info: main_models.GetStandardLookupTableResponseBodyLookupTableInfo = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.lookup_table_info = lookup_table_info
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.lookup_table_info:
            self.lookup_table_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.lookup_table_info is not None:
            result['LookupTableInfo'] = self.lookup_table_info.to_map()

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

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('LookupTableInfo') is not None:
            temp_model = main_models.GetStandardLookupTableResponseBodyLookupTableInfo()
            self.lookup_table_info = temp_model.from_map(m.get('LookupTableInfo'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetStandardLookupTableResponseBodyLookupTableInfo(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_time: str = None,
        creator: str = None,
        creator_name: str = None,
        description: str = None,
        directory_reference: main_models.GetStandardLookupTableResponseBodyLookupTableInfoDirectoryReference = None,
        id: int = None,
        last_modifier: str = None,
        last_modifier_name: str = None,
        lookup_table_value_list: List[main_models.GetStandardLookupTableResponseBodyLookupTableInfoLookupTableValueList] = None,
        modify_time: str = None,
        name: str = None,
        owner: str = None,
        owner_name: str = None,
    ):
        self.code = code
        self.create_time = create_time
        self.creator = creator
        self.creator_name = creator_name
        self.description = description
        self.directory_reference = directory_reference
        self.id = id
        self.last_modifier = last_modifier
        self.last_modifier_name = last_modifier_name
        self.lookup_table_value_list = lookup_table_value_list
        self.modify_time = modify_time
        self.name = name
        self.owner = owner
        self.owner_name = owner_name

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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.description is not None:
            result['Description'] = self.description

        if self.directory_reference is not None:
            result['DirectoryReference'] = self.directory_reference.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier

        if self.last_modifier_name is not None:
            result['LastModifierName'] = self.last_modifier_name

        result['LookupTableValueList'] = []
        if self.lookup_table_value_list is not None:
            for k1 in self.lookup_table_value_list:
                result['LookupTableValueList'].append(k1.to_map() if k1 else None)

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DirectoryReference') is not None:
            temp_model = main_models.GetStandardLookupTableResponseBodyLookupTableInfoDirectoryReference()
            self.directory_reference = temp_model.from_map(m.get('DirectoryReference'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifier') is not None:
            self.last_modifier = m.get('LastModifier')

        if m.get('LastModifierName') is not None:
            self.last_modifier_name = m.get('LastModifierName')

        self.lookup_table_value_list = []
        if m.get('LookupTableValueList') is not None:
            for k1 in m.get('LookupTableValueList'):
                temp_model = main_models.GetStandardLookupTableResponseBodyLookupTableInfoLookupTableValueList()
                self.lookup_table_value_list.append(temp_model.from_map(k1))

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        return self

class GetStandardLookupTableResponseBodyLookupTableInfoLookupTableValueList(DaraModel):
    def __init__(
        self,
        description: str = None,
        english_name: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.english_name = english_name
        self.name = name
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

class GetStandardLookupTableResponseBodyLookupTableInfoDirectoryReference(DaraModel):
    def __init__(
        self,
        directory: str = None,
    ):
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

