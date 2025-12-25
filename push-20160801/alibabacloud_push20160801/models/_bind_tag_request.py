# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindTagRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        client_key: str = None,
        key_type: str = None,
        tag_name: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.client_key = client_key
        # This parameter is required.
        self.key_type = key_type
        # This parameter is required.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.client_key is not None:
            result['ClientKey'] = self.client_key

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('ClientKey') is not None:
            self.client_key = m.get('ClientKey')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

