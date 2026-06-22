# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetaStoreConf(DaraModel):
    def __init__(
        self,
        db_password: str = None,
        db_url: str = None,
        db_user_name: str = None,
    ):
        self.db_password = db_password
        self.db_url = db_url
        self.db_user_name = db_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_password is not None:
            result['DbPassword'] = self.db_password

        if self.db_url is not None:
            result['DbUrl'] = self.db_url

        if self.db_user_name is not None:
            result['DbUserName'] = self.db_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbPassword') is not None:
            self.db_password = m.get('DbPassword')

        if m.get('DbUrl') is not None:
            self.db_url = m.get('DbUrl')

        if m.get('DbUserName') is not None:
            self.db_user_name = m.get('DbUserName')

        return self

