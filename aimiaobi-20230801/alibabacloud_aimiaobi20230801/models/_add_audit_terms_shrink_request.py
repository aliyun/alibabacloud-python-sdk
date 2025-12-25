# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddAuditTermsShrinkRequest(DaraModel):
    def __init__(
        self,
        exception_word_shrink: str = None,
        keyword: str = None,
        suggest_word: str = None,
        terms_desc: str = None,
        terms_name: str = None,
        workspace_id: str = None,
    ):
        self.exception_word_shrink = exception_word_shrink
        self.keyword = keyword
        self.suggest_word = suggest_word
        self.terms_desc = terms_desc
        self.terms_name = terms_name
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exception_word_shrink is not None:
            result['ExceptionWord'] = self.exception_word_shrink

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.suggest_word is not None:
            result['SuggestWord'] = self.suggest_word

        if self.terms_desc is not None:
            result['TermsDesc'] = self.terms_desc

        if self.terms_name is not None:
            result['TermsName'] = self.terms_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionWord') is not None:
            self.exception_word_shrink = m.get('ExceptionWord')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('SuggestWord') is not None:
            self.suggest_word = m.get('SuggestWord')

        if m.get('TermsDesc') is not None:
            self.terms_desc = m.get('TermsDesc')

        if m.get('TermsName') is not None:
            self.terms_name = m.get('TermsName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

