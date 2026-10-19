# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetMemoryDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        groups: List[main_models.GetMemoryDetailResponseBodyGroups] = None,
        message: str = None,
        profile: main_models.GetMemoryDetailResponseBodyProfile = None,
        request_id: str = None,
    ):
        # 业务状态码；成功为 200，失败时为对应错误码
        self.code = code
        # 自动拾取记忆的分组列表；无自动记忆时为空数组
        self.groups = groups
        # 错误描述；成功时为空字符串，失败时返回具体原因
        self.message = message
        # 手动添加的记忆，来自 profile.md；包含完整内容、存在状态和修改时间
        self.profile = profile
        # 请求追踪 ID，用于定位本次调用
        self.request_id = request_id

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()
        if self.profile:
            self.profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['groups'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.profile is not None:
            result['profile'] = self.profile.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.groups = []
        if m.get('groups') is not None:
            for k1 in m.get('groups'):
                temp_model = main_models.GetMemoryDetailResponseBodyGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('profile') is not None:
            temp_model = main_models.GetMemoryDetailResponseBodyProfile()
            self.profile = temp_model.from_map(m.get('profile'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetMemoryDetailResponseBodyProfile(DaraModel):
    def __init__(
        self,
        content: str = None,
        exists: bool = None,
        gmt_modified: int = None,
    ):
        # 手动记忆的完整正文；未保存过时为空字符串
        self.content = content
        # profile.md 是否存在；未保存过时为 false
        self.exists = exists
        # profile.md 最近修改时间，Unix 秒级时间戳；文件不存在或无法取得元数据时为 null
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.exists is not None:
            result['exists'] = self.exists

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('exists') is not None:
            self.exists = m.get('exists')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        return self

class GetMemoryDetailResponseBodyGroups(DaraModel):
    def __init__(
        self,
        gmt_modified: int = None,
        items: List[main_models.GetMemoryDetailResponseBodyGroupsItems] = None,
        type: str = None,
    ):
        # 该分组最近修改时间，Unix 秒级时间戳；无文件时为 null
        self.gmt_modified = gmt_modified
        # 该类型下的自动记忆条目列表；没有条目时为空数组
        self.items = items
        # 自动记忆类型：user、feedback、reference 或 project
        self.type = type

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.GetMemoryDetailResponseBodyGroupsItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetMemoryDetailResponseBodyGroupsItems(DaraModel):
    def __init__(
        self,
        content: str = None,
        description: str = None,
        id: str = None,
        title: str = None,
    ):
        # 自动记忆正文，不包含 YAML frontmatter
        self.content = content
        # 自动记忆的附加描述；没有时为空字符串
        self.description = description
        # 自动记忆条目的唯一标识，为相对 OSS 路径
        self.id = id
        # 自动记忆标题，来自文件元数据或文件名
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

