# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSkillBizTagsRequest(DaraModel):
    def __init__(
        self,
        biz_tags: str = None,
        namespace_id: str = None,
        skill_name: str = None,
    ):
        # This parameter is required.
        self.biz_tags = biz_tags
        # This parameter is required.
        self.namespace_id = namespace_id
        # This parameter is required.
        self.skill_name = skill_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_tags is not None:
            result['BizTags'] = self.biz_tags

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTags') is not None:
            self.biz_tags = m.get('BizTags')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        return self

