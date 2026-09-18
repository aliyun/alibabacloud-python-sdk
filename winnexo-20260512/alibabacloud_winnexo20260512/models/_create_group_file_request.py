# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGroupFileRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory_id: str = None,
        file_record_id: str = None,
        group_id: str = None,
        name: str = None,
        source_tags: str = None,
        tenant_id: str = None,
    ):
        # 资料描述
        self.description = description
        # 当前空间物理目录ID；省略/root使用空间根，首次可能初始化根目录；引用目录不可写
        self.directory_id = directory_id
        # 当前用户在当前租户上传的SOURCE/OSS文件记录ID；须先完成文件PUT
        # 
        # This parameter is required.
        self.file_record_id = file_record_id
        # 协作空间 ID
        # 
        # This parameter is required.
        self.group_id = group_id
        # 资料显示名；最终名称沿用Provider规则
        # 
        # This parameter is required.
        self.name = name
        # 资料标签，JSON字符串列表
        self.source_tags = source_tags
        # 租户ID，公共参数；缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.file_record_id is not None:
            result['fileRecordId'] = self.file_record_id

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.name is not None:
            result['name'] = self.name

        if self.source_tags is not None:
            result['sourceTags'] = self.source_tags

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('fileRecordId') is not None:
            self.file_record_id = m.get('fileRecordId')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

