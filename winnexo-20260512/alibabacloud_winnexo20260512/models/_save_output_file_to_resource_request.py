# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SaveOutputFileToResourceRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        item_ids: List[str] = None,
        mode: str = None,
        tenant_id: str = None,
    ):
        # 目标个人目录 ID；不传则自动解析用户默认目录。
        self.directory_id = directory_id
        # itemIds
        # 
        # This parameter is required.
        self.item_ids = item_ids
        # 保存方式：link=链接（1:1 幂等，编辑产出会同步资源） / copy=复制（不限次，快照）
        self.mode = mode
        # 租户ID，公共参数；winnexo-cli 通过 --tenant-id 显式传入
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.item_ids is not None:
            result['itemIds'] = self.item_ids

        if self.mode is not None:
            result['mode'] = self.mode

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('itemIds') is not None:
            self.item_ids = m.get('itemIds')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

