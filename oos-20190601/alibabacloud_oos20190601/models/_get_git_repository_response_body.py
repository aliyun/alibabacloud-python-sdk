# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetGitRepositoryResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        html_url: str = None,
        is_private: bool = None,
        request_id: str = None,
    ):
        self.description = description
        self.html_url = html_url
        self.is_private = is_private
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.html_url is not None:
            result['HtmlUrl'] = self.html_url

        if self.is_private is not None:
            result['IsPrivate'] = self.is_private

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HtmlUrl') is not None:
            self.html_url = m.get('HtmlUrl')

        if m.get('IsPrivate') is not None:
            self.is_private = m.get('IsPrivate')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

