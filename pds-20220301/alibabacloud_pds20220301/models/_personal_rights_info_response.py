# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class PersonalRightsInfoResponse(DaraModel):
    def __init__(
        self,
        expires_time: str = None,
        history_latest_rights: main_models.PersonalRightsInfoResponse = None,
        icon: str = None,
        is_expires: bool = None,
        name: str = None,
        other_rights: main_models.PersonalRightsInfoResponse = None,
        privileges: List[main_models.DataBoxPrivileges] = None,
        spu_id: str = None,
        title: str = None,
    ):
        self.expires_time = expires_time
        self.history_latest_rights = history_latest_rights
        self.icon = icon
        self.is_expires = is_expires
        self.name = name
        self.other_rights = other_rights
        self.privileges = privileges
        self.spu_id = spu_id
        self.title = title

    def validate(self):
        if self.history_latest_rights:
            self.history_latest_rights.validate()
        if self.other_rights:
            self.other_rights.validate()
        if self.privileges:
            for v1 in self.privileges:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expires_time is not None:
            result['expires_time'] = self.expires_time

        if self.history_latest_rights is not None:
            result['history_latest_rights'] = self.history_latest_rights.to_map()

        if self.icon is not None:
            result['icon'] = self.icon

        if self.is_expires is not None:
            result['is_expires'] = self.is_expires

        if self.name is not None:
            result['name'] = self.name

        if self.other_rights is not None:
            result['other_rights'] = self.other_rights.to_map()

        result['privileges'] = []
        if self.privileges is not None:
            for k1 in self.privileges:
                result['privileges'].append(k1.to_map() if k1 else None)

        if self.spu_id is not None:
            result['spu_id'] = self.spu_id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expires_time') is not None:
            self.expires_time = m.get('expires_time')

        if m.get('history_latest_rights') is not None:
            temp_model = main_models.PersonalRightsInfoResponse()
            self.history_latest_rights = temp_model.from_map(m.get('history_latest_rights'))

        if m.get('icon') is not None:
            self.icon = m.get('icon')

        if m.get('is_expires') is not None:
            self.is_expires = m.get('is_expires')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('other_rights') is not None:
            temp_model = main_models.PersonalRightsInfoResponse()
            self.other_rights = temp_model.from_map(m.get('other_rights'))

        self.privileges = []
        if m.get('privileges') is not None:
            for k1 in m.get('privileges'):
                temp_model = main_models.DataBoxPrivileges()
                self.privileges.append(temp_model.from_map(k1))

        if m.get('spu_id') is not None:
            self.spu_id = m.get('spu_id')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

