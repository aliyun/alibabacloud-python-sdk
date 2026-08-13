# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePersonalVoiceMeetingRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory_id: str = None,
        file_url: str = None,
        name: str = None,
        operating_object_name: str = None,
        tenant_id: str = None,
    ):
        # 资源描述（可选）
        self.description = description
        # 目标个人目录 ID；不传时自动绑定到当前数字员工默认根目录，传入时必须是当前用户在当前数字员工下的已有个人目录
        self.directory_id = directory_id
        # 离线会议音频文件 URL（必填）
        # 
        # This parameter is required.
        self.file_url = file_url
        # 资源显示名称
        # 
        # This parameter is required.
        self.name = name
        # 数字员工名称（已废弃：不再作为个人资源隔离条件，仅保留用于来源追溯）
        self.operating_object_name = operating_object_name
        # 租户ID，公共参数，缺省时使用调用方默认租户
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

        if self.file_url is not None:
            result['fileUrl'] = self.file_url

        if self.name is not None:
            result['name'] = self.name

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

