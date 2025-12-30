# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRegionsRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        max_results: int = None,
        next_token: str = None,
        spec_code: str = None,
    ):
        self.accept_language = accept_language
        self.max_results = max_results
        self.next_token = next_token
        self.spec_code = spec_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')

        return self

