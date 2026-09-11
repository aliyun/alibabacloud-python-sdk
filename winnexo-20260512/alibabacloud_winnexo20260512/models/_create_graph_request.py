# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGraphRequest(DaraModel):
    def __init__(
        self,
        business_profile: str = None,
        data_source_id: int = None,
        display_name: str = None,
        graph_name: str = None,
        tenant_id: str = None,
    ):
        # 业务说明（可选）
        self.business_profile = business_profile
        # 绑定的数据源 ID（控制台已创建的 RDB 类数据源）
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # 图谱展示名（可选，租户内大小写不敏感唯一，最多200字）
        self.display_name = display_name
        # 图谱名称，字母开头+字母/数字/下划线，长度不超过64，租户内唯一
        # 
        # This parameter is required.
        self.graph_name = graph_name
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_profile is not None:
            result['businessProfile'] = self.business_profile

        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessProfile') is not None:
            self.business_profile = m.get('businessProfile')

        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

