# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveGraphDraftResourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        draft_change_id: int = None,
        draft_content_hash: str = None,
        element_type: str = None,
        gmt_modified: str = None,
        graph_name: str = None,
        message: str = None,
        operation_type: str = None,
        request_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 草稿变更 ID；内容与在线完全一致被跳过时为 null
        self.draft_change_id = draft_change_id
        # 草稿内容哈希；被跳过时为 null
        self.draft_content_hash = draft_content_hash
        # 资源小类：resourceType=object 时固定 object_type；resourceType=element 时为 indicator / logic / process / rule / analysis 之一
        self.element_type = element_type
        # 最后修改时间（ISO8601）；被跳过时为 null
        self.gmt_modified = gmt_modified
        # 图谱名称
        self.graph_name = graph_name
        # 错误描述，成功时为空
        self.message = message
        # 操作类型：CREATE / UPDATE（由底层判定）；被跳过时为 null
        self.operation_type = operation_type
        # 请求追踪 ID
        self.request_id = request_id
        # 资源名
        self.resource_name = resource_name
        # 资源大类：object（对象）/ element（业务元素）
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.draft_change_id is not None:
            result['draftChangeId'] = self.draft_change_id

        if self.draft_content_hash is not None:
            result['draftContentHash'] = self.draft_content_hash

        if self.element_type is not None:
            result['elementType'] = self.element_type

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.message is not None:
            result['message'] = self.message

        if self.operation_type is not None:
            result['operationType'] = self.operation_type

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.resource_name is not None:
            result['resourceName'] = self.resource_name

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('draftChangeId') is not None:
            self.draft_change_id = m.get('draftChangeId')

        if m.get('draftContentHash') is not None:
            self.draft_content_hash = m.get('draftContentHash')

        if m.get('elementType') is not None:
            self.element_type = m.get('elementType')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('operationType') is not None:
            self.operation_type = m.get('operationType')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

