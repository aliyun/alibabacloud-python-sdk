# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReplaceGroupSourceFileRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_path: str = None,
        file_public_url: str = None,
        file_record_id: str = None,
        force_sync: bool = None,
        group_id: str = None,
        source_id: str = None,
        tenant_id: str = None,
    ):
        # 新文件名；省略或空字符串保留原文件名，用户自定义展示名沿用现有保护规则
        self.file_name = file_name
        # 已上传新文件的 OSS 持久化地址，使用上传接口返回值
        # 
        # This parameter is required.
        self.file_path = file_path
        # 已上传新文件的访问 URL，可能携带临时签名
        # 
        # This parameter is required.
        self.file_public_url = file_public_url
        # 已上传新文件的文件记录 ID
        # 
        # This parameter is required.
        self.file_record_id = file_record_id
        # 是否等待解析完成；默认 false 异步受理，true 同步等待，网关超时 300000ms
        self.force_sync = force_sync
        # 资料所属协作空间 ID
        # 
        # This parameter is required.
        self.group_id = group_id
        # 当前空间物理 GROUP 资料 ID；引用资料只读
        # 
        # This parameter is required.
        self.source_id = source_id
        # 租户ID，公共参数；缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_path is not None:
            result['filePath'] = self.file_path

        if self.file_public_url is not None:
            result['filePublicUrl'] = self.file_public_url

        if self.file_record_id is not None:
            result['fileRecordId'] = self.file_record_id

        if self.force_sync is not None:
            result['forceSync'] = self.force_sync

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')

        if m.get('filePublicUrl') is not None:
            self.file_public_url = m.get('filePublicUrl')

        if m.get('fileRecordId') is not None:
            self.file_record_id = m.get('fileRecordId')

        if m.get('forceSync') is not None:
            self.force_sync = m.get('forceSync')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

