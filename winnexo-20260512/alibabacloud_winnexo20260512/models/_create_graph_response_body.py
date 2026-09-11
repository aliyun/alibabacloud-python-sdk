# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGraphResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_source_id: int = None,
        graph_name: str = None,
        message: str = None,
        request_id: str = None,
        schema_version: str = None,
        sync_status: str = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 创建时绑定的数据源 ID
        self.data_source_id = data_source_id
        # 图谱名称
        self.graph_name = graph_name
        # 错误描述，成功时为空
        self.message = message
        # 请求追踪 ID
        self.request_id = request_id
        # Schema 版本；快建路径固定 0.0.0，正式版本经控制台发布产生
        self.schema_version = schema_version
        # 同步状态，快建成功为 SUCCESS
        self.sync_status = sync_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.schema_version is not None:
            result['schemaVersion'] = self.schema_version

        if self.sync_status is not None:
            result['syncStatus'] = self.sync_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('schemaVersion') is not None:
            self.schema_version = m.get('schemaVersion')

        if m.get('syncStatus') is not None:
            self.sync_status = m.get('syncStatus')

        return self

