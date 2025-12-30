# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeletePlayInfoResponseBody(DaraModel):
    def __init__(
        self,
        forbidden_list: List[str] = None,
        ignored_list: List[str] = None,
        request_id: str = None,
    ):
        # The URLs of the media streams that cannot be deleted. Generally, media streams cannot be deleted if you do not have the required permissions.
        self.forbidden_list = forbidden_list
        # The URLs of ignored media streams. An error occurred while obtaining such media assets because the IDs or URLs of the media assets do not exist.
        self.ignored_list = ignored_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forbidden_list is not None:
            result['ForbiddenList'] = self.forbidden_list

        if self.ignored_list is not None:
            result['IgnoredList'] = self.ignored_list

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForbiddenList') is not None:
            self.forbidden_list = m.get('ForbiddenList')

        if m.get('IgnoredList') is not None:
            self.ignored_list = m.get('IgnoredList')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

