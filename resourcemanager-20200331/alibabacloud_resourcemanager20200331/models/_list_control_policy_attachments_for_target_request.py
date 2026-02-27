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
        # The language in which you want to return the descriptions of the access control policies. Valid values:
        # 
        # *   zh-CN (default value): Chinese
        # *   en: English
        # *   ja: Japanese
        # 
        # >  This parameter is valid only for system access control policies.
        self.language = language
        # The ID of the object whose access control policies you want to query. Access control policies can be attached to the following objects:
        # 
        # *   Root folder
        # *   Subfolders of the Root folder
        # *   Members
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

