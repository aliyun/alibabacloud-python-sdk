# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class RunSkillRequest(DaraModel):
    def __init__(
        self,
        arguments: Dict[str, Any] = None,
        client_token: str = None,
        model: str = None,
        operating_object_name: str = None,
        skill_code: str = None,
        skill_name: str = None,
        tenant_id: str = None,
    ):
        self.arguments = arguments
        # 幂等 token，调用方自行生成；当前版本仅记录到 metadata，未做去重
        self.client_token = client_token
        # 抽象模型名（模型档位），不传默认 standard
        self.model = model
        # 数字员工名称；用于按绑定关系计算 CodeAgent allowedSkills 白名单
        self.operating_object_name = operating_object_name
        # 技能编码（全局唯一），优先级高于 skillName
        self.skill_code = skill_code
        # 技能名称，未传 skillCode 时使用；租户范围内必须唯一
        self.skill_name = skill_name
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arguments is not None:
            result['arguments'] = self.arguments

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.model is not None:
            result['model'] = self.model

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.skill_code is not None:
            result['skillCode'] = self.skill_code

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arguments') is not None:
            self.arguments = m.get('arguments')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

