# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SourceFeiShuDocsParameters(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret: str = None,
        knowledge_space_name: str = None,
        load_mode: str = None,
    ):
        self.app_id = app_id
        self.app_secret = app_secret
        self.knowledge_space_name = knowledge_space_name
        self.load_mode = load_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret

        if self.knowledge_space_name is not None:
            result['KnowledgeSpaceName'] = self.knowledge_space_name

        if self.load_mode is not None:
            result['LoadMode'] = self.load_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')

        if m.get('KnowledgeSpaceName') is not None:
            self.knowledge_space_name = m.get('KnowledgeSpaceName')

        if m.get('LoadMode') is not None:
            self.load_mode = m.get('LoadMode')

        return self

