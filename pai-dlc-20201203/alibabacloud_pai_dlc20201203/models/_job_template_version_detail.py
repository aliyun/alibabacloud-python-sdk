# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class JobTemplateVersionDetail(DaraModel):
    def __init__(
        self,
        constraints: Dict[str, str] = None,
        content: str = None,
        created_by: str = None,
        gmt_created: str = None,
        version: int = None,
    ):
        self.constraints = constraints
        # 任务模板的配置内容，支持 CreateJob 接口的所有参数字段，以 JSON 对象存储
        self.content = content
        # 创建该版本的用户ID
        self.created_by = created_by
        # 该版本的创建时间
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_created = gmt_created
        # 模板版本号
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.constraints is not None:
            result['Constraints'] = self.constraints

        if self.content is not None:
            result['Content'] = self.content

        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

