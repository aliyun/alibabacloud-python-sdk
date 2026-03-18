# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ApiKeyDTO(DaraModel):
    def __init__(
        self,
        client: main_models.ClientDTO = None,
        client_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        key_preview: str = None,
        name: str = None,
    ):
        self.client = client
        self.client_id = client_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.key_preview = key_preview
        self.name = name

    def validate(self):
        if self.client:
            self.client.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client is not None:
            result['client'] = self.client.to_map()

        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.key_preview is not None:
            result['keyPreview'] = self.key_preview

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client') is not None:
            temp_model = main_models.ClientDTO()
            self.client = temp_model.from_map(m.get('client'))

        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('keyPreview') is not None:
            self.key_preview = m.get('keyPreview')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

