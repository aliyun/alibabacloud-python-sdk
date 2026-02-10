# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyImageRegistryRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        password: str = None,
        trans_per_hour: int = None,
        user_name: str = None,
    ):
        # The ID of the image repository. You can call the listImageRegistry operation to query the ID of the image repository.
        self.id = id
        # The password.
        self.password = password
        # The number of images that are scanned per hour.
        self.trans_per_hour = trans_per_hour
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.password is not None:
            result['Password'] = self.password

        if self.trans_per_hour is not None:
            result['TransPerHour'] = self.trans_per_hour

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('TransPerHour') is not None:
            self.trans_per_hour = m.get('TransPerHour')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

