# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetMetaTableThemeLevelResponseBody(DaraModel):
    def __init__(
        self,
        entity: main_models.GetMetaTableThemeLevelResponseBodyEntity = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned data.
        self.entity = entity
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID. You can troubleshoot issues based on the ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.entity:
            self.entity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity is not None:
            result['Entity'] = self.entity.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entity') is not None:
            temp_model = main_models.GetMetaTableThemeLevelResponseBodyEntity()
            self.entity = temp_model.from_map(m.get('Entity'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMetaTableThemeLevelResponseBodyEntity(DaraModel):
    def __init__(
        self,
        level: List[main_models.GetMetaTableThemeLevelResponseBodyEntityLevel] = None,
        theme: List[main_models.GetMetaTableThemeLevelResponseBodyEntityTheme] = None,
    ):
        # The information about the levels of the metatable.
        self.level = level
        # The information about the themes of the metatable.
        self.theme = theme

    def validate(self):
        if self.level:
            for v1 in self.level:
                 if v1:
                    v1.validate()
        if self.theme:
            for v1 in self.theme:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Level'] = []
        if self.level is not None:
            for k1 in self.level:
                result['Level'].append(k1.to_map() if k1 else None)

        result['Theme'] = []
        if self.theme is not None:
            for k1 in self.theme:
                result['Theme'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.level = []
        if m.get('Level') is not None:
            for k1 in m.get('Level'):
                temp_model = main_models.GetMetaTableThemeLevelResponseBodyEntityLevel()
                self.level.append(temp_model.from_map(k1))

        self.theme = []
        if m.get('Theme') is not None:
            for k1 in m.get('Theme'):
                temp_model = main_models.GetMetaTableThemeLevelResponseBodyEntityTheme()
                self.theme.append(temp_model.from_map(k1))

        return self

class GetMetaTableThemeLevelResponseBodyEntityTheme(DaraModel):
    def __init__(
        self,
        level: int = None,
        name: str = None,
        parent_id: int = None,
        theme_id: int = None,
    ):
        # The level of the theme. Valid values:
        # 
        # *   1
        # *   2
        self.level = level
        # The name of the theme.
        self.name = name
        # The ID of the parent theme.
        self.parent_id = parent_id
        # The ID of the theme.
        self.theme_id = theme_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['Level'] = self.level

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.theme_id is not None:
            result['ThemeId'] = self.theme_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('ThemeId') is not None:
            self.theme_id = m.get('ThemeId')

        return self

class GetMetaTableThemeLevelResponseBodyEntityLevel(DaraModel):
    def __init__(
        self,
        description: str = None,
        level_id: int = None,
        name: str = None,
        type: int = None,
    ):
        # The description of the level.
        self.description = description
        # The ID of the level.
        self.level_id = level_id
        # The name of the level.
        self.name = name
        # The type of the level. Valid values:
        # 
        # *   1: indicates the logical level.
        # *   2: indicates the physical level.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.level_id is not None:
            result['LevelId'] = self.level_id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LevelId') is not None:
            self.level_id = m.get('LevelId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

