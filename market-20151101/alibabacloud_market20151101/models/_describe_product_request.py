# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeProductRequest(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        code: str = None,
        query_draft: bool = None,
    ):
        # AliUid
        self.ali_uid = ali_uid
        # This parameter is required.
        self.code = code
        self.query_draft = query_draft

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.code is not None:
            result['Code'] = self.code

        if self.query_draft is not None:
            result['QueryDraft'] = self.query_draft

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('QueryDraft') is not None:
            self.query_draft = m.get('QueryDraft')

        return self

