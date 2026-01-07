# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunScriptContinueRequest(DaraModel):
    def __init__(
        self,
        script_summary: str = None,
        script_type_keyword: str = None,
        user_provided_content: str = None,
    ):
        self.script_summary = script_summary
        self.script_type_keyword = script_type_keyword
        # This parameter is required.
        self.user_provided_content = user_provided_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.script_summary is not None:
            result['scriptSummary'] = self.script_summary

        if self.script_type_keyword is not None:
            result['scriptTypeKeyword'] = self.script_type_keyword

        if self.user_provided_content is not None:
            result['userProvidedContent'] = self.user_provided_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scriptSummary') is not None:
            self.script_summary = m.get('scriptSummary')

        if m.get('scriptTypeKeyword') is not None:
            self.script_type_keyword = m.get('scriptTypeKeyword')

        if m.get('userProvidedContent') is not None:
            self.user_provided_content = m.get('userProvidedContent')

        return self

