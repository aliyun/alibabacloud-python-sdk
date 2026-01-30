# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartTransferStreamRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
        transcode: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.id = id
        self.owner_id = owner_id
        self.transcode = transcode
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.transcode is not None:
            result['Transcode'] = self.transcode

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Transcode') is not None:
            self.transcode = m.get('Transcode')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

