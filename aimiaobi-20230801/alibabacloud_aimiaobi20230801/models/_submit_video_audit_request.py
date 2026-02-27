# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitVideoAuditRequest(DaraModel):
    def __init__(
        self,
        ext: str = None,
        file_key: str = None,
        snapshot_interval: float = None,
        url: str = None,
        workspace_id: str = None,
    ):
        # 扩展参数JSON字符串
        self.ext = ext
        # OSS文件Key，与url参数二选一
        self.file_key = file_key
        # 抽帧间隔时间（秒）
        self.snapshot_interval = snapshot_interval
        # 视频URL地址，与fileKey参数二选一
        self.url = url
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext is not None:
            result['Ext'] = self.ext

        if self.file_key is not None:
            result['FileKey'] = self.file_key

        if self.snapshot_interval is not None:
            result['SnapshotInterval'] = self.snapshot_interval

        if self.url is not None:
            result['Url'] = self.url

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        if m.get('SnapshotInterval') is not None:
            self.snapshot_interval = m.get('SnapshotInterval')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

