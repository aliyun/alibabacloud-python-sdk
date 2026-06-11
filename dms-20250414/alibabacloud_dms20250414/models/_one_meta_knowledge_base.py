# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OneMetaKnowledgeBase(DaraModel):
    def __init__(
        self,
        creator: str = None,
        description: str = None,
        domain: str = None,
        extra_info: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        kb_uuid: str = None,
        name: str = None,
        state: int = None,
        tag: str = None,
    ):
        # The creator of the knowledge base.
        self.creator = creator
        # The description of the knowledge base.
        self.description = description
        # The domain of the knowledge base.
        self.domain = domain
        # Additional information about the knowledge base.
        self.extra_info = extra_info
        # The time when the knowledge base was created.
        self.gmt_create = gmt_create
        # The time when the knowledge base was last modified.
        self.gmt_modified = gmt_modified
        # The UUID of the knowledge base.
        self.kb_uuid = kb_uuid
        # The name of the knowledge base.
        self.name = name
        # The state of the knowledge base. Valid values include 0 (No data) and 1 (Available).
        self.state = state
        # The tag of the knowledge base.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.kb_uuid is not None:
            result['KbUuid'] = self.kb_uuid

        if self.name is not None:
            result['Name'] = self.name

        if self.state is not None:
            result['State'] = self.state

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('KbUuid') is not None:
            self.kb_uuid = m.get('KbUuid')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

