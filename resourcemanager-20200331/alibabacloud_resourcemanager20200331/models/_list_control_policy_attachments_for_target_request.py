# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListControlPolicyAttachmentsForTargetRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        target_id: str = None,
    ):
        # The language in which the control policy descriptions are returned. Valid values:
        # 
        # - zh-CN (default): Chinese.
        # - en: English.
        # - ja: Japanese.
        # 
        # > This parameter is valid only for system control policies.
        self.language = language
        # The target node. Valid values:
        # 
        # - Root ID: queries the control policies attached to the Root node.
        # - Resource folder ID: queries the control policies attached to a resource folder.
        # - Member ID: queries the control policies attached to a member.
        # 
        # This parameter is required.
        self.target_id = target_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        return self

