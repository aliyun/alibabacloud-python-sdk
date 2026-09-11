# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGraphInfoResponseBody(DaraModel):
    def __init__(
        self,
        business_profile: str = None,
        code: str = None,
        display_name: str = None,
        graph_name: str = None,
        message: str = None,
        request_id: str = None,
        updated: bool = None,
    ):
        # 更新后的业务说明，未设置时为空
        self.business_profile = business_profile
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 更新后的图谱展示名，未设置时为空
        self.display_name = display_name
        # 图谱名称
        self.graph_name = graph_name
        # 错误描述，成功时为空
        self.message = message
        # 请求追踪 ID
        self.request_id = request_id
        # 是否更新成功
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_profile is not None:
            result['businessProfile'] = self.business_profile

        if self.code is not None:
            result['code'] = self.code

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessProfile') is not None:
            self.business_profile = m.get('businessProfile')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

