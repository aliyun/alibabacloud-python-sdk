# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClientDTO(DaraModel):
    def __init__(
        self,
        address: str = None,
        allowed_models: str = None,
        client_uuid: str = None,
        contact: str = None,
        delete_tag: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        main: int = None,
        name: str = None,
        remark: str = None,
    ):
        self.address = address
        self.allowed_models = allowed_models
        self.client_uuid = client_uuid
        self.contact = contact
        self.delete_tag = delete_tag
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.main = main
        self.name = name
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.allowed_models is not None:
            result['allowedModels'] = self.allowed_models

        if self.client_uuid is not None:
            result['clientUuid'] = self.client_uuid

        if self.contact is not None:
            result['contact'] = self.contact

        if self.delete_tag is not None:
            result['deleteTag'] = self.delete_tag

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.main is not None:
            result['main'] = self.main

        if self.name is not None:
            result['name'] = self.name

        if self.remark is not None:
            result['remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('allowedModels') is not None:
            self.allowed_models = m.get('allowedModels')

        if m.get('clientUuid') is not None:
            self.client_uuid = m.get('clientUuid')

        if m.get('contact') is not None:
            self.contact = m.get('contact')

        if m.get('deleteTag') is not None:
            self.delete_tag = m.get('deleteTag')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('main') is not None:
            self.main = m.get('main')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        return self

