# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTenantDirectoryRequest(DaraModel):
    def __init__(
        self,
        delete_mode: str = None,
        directory_id: str = None,
        tenant_id: str = None,
    ):
        # 删除模式：reject / recursive / move_to_root
        self.delete_mode = delete_mode
        # 目录唯一标识
        self.directory_id = directory_id
        # 租户ID，公共参数；winnexo-cli 通过 --tenant-id 显式传入
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_mode is not None:
            result['deleteMode'] = self.delete_mode

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deleteMode') is not None:
            self.delete_mode = m.get('deleteMode')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

