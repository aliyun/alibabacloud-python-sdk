# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WebofficeUser(DaraModel):
    def __init__(
        self,
        avatar: str = None,
        id: str = None,
        name: str = None,
    ):
        # The custom URL of the avatar picture. The avatar picture is displayed on the WebOffice page.
        self.avatar = avatar
        # The custom user ID. The user ID is displayed on the WebOffice page. A user ID can contain letters and digits and cannot exceed 15 characters in length.
        self.id = id
        # The custom username. The username is displayed on the WebOffice page. The username must meet the following requirements:
        # 
        # *   A username can contain digits, letters, hyphens (-), underscores (_), plus signs (+), forward slashes (/), equal signs (=), and at signs (@).
        # *   A username can contain up to 32 characters.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar is not None:
            result['Avatar'] = self.avatar

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

