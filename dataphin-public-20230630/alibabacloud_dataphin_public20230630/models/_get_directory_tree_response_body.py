# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetDirectoryTreeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetDirectoryTreeResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetDirectoryTreeResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDirectoryTreeResponseBodyData(DaraModel):
    def __init__(
        self,
        children: main_models.GetDirectoryTreeResponseBodyDataChildren = None,
        parent: main_models.GetDirectoryTreeResponseBodyDataParent = None,
    ):
        self.children = children
        self.parent = parent

    def validate(self):
        if self.children:
            self.children.validate()
        if self.parent:
            self.parent.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.children is not None:
            result['Children'] = self.children.to_map()

        if self.parent is not None:
            result['Parent'] = self.parent.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Children') is not None:
            temp_model = main_models.GetDirectoryTreeResponseBodyDataChildren()
            self.children = temp_model.from_map(m.get('Children'))

        if m.get('Parent') is not None:
            temp_model = main_models.GetDirectoryTreeResponseBodyDataParent()
            self.parent = temp_model.from_map(m.get('Parent'))

        return self

class GetDirectoryTreeResponseBodyDataParent(DaraModel):
    def __init__(
        self,
        category_type: str = None,
        creator: str = None,
        creator_name: str = None,
        data_cell_id: int = None,
        dir_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        last_modifier: str = None,
        last_modifier_name: str = None,
        name: str = None,
        project_id: int = None,
        string_id: str = None,
        type: str = None,
    ):
        self.category_type = category_type
        self.creator = creator
        self.creator_name = creator_name
        self.data_cell_id = data_cell_id
        self.dir_name = dir_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.last_modifier = last_modifier
        self.last_modifier_name = last_modifier_name
        self.name = name
        self.project_id = project_id
        self.string_id = string_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.data_cell_id is not None:
            result['DataCellId'] = self.data_cell_id

        if self.dir_name is not None:
            result['DirName'] = self.dir_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier

        if self.last_modifier_name is not None:
            result['LastModifierName'] = self.last_modifier_name

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.string_id is not None:
            result['StringId'] = self.string_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('DataCellId') is not None:
            self.data_cell_id = m.get('DataCellId')

        if m.get('DirName') is not None:
            self.dir_name = m.get('DirName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifier') is not None:
            self.last_modifier = m.get('LastModifier')

        if m.get('LastModifierName') is not None:
            self.last_modifier_name = m.get('LastModifierName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StringId') is not None:
            self.string_id = m.get('StringId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetDirectoryTreeResponseBodyDataChildren(DaraModel):
    def __init__(
        self,
        category_type: str = None,
        creator: str = None,
        creator_name: str = None,
        data_cell_id: int = None,
        dir_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        last_modifier: str = None,
        last_modifier_name: str = None,
        name: str = None,
        project_id: int = None,
        string_id: str = None,
        type: str = None,
    ):
        self.category_type = category_type
        self.creator = creator
        self.creator_name = creator_name
        self.data_cell_id = data_cell_id
        self.dir_name = dir_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.last_modifier = last_modifier
        self.last_modifier_name = last_modifier_name
        self.name = name
        self.project_id = project_id
        self.string_id = string_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.data_cell_id is not None:
            result['DataCellId'] = self.data_cell_id

        if self.dir_name is not None:
            result['DirName'] = self.dir_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier

        if self.last_modifier_name is not None:
            result['LastModifierName'] = self.last_modifier_name

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.string_id is not None:
            result['StringId'] = self.string_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('DataCellId') is not None:
            self.data_cell_id = m.get('DataCellId')

        if m.get('DirName') is not None:
            self.dir_name = m.get('DirName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifier') is not None:
            self.last_modifier = m.get('LastModifier')

        if m.get('LastModifierName') is not None:
            self.last_modifier_name = m.get('LastModifierName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StringId') is not None:
            self.string_id = m.get('StringId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

