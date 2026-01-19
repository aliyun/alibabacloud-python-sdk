# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSampleDataRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        description: str = None,
        encrypt_type: str = None,
        name: str = None,
        reg_id: str = None,
        risk_value: str = None,
        scene: str = None,
        store_path: str = None,
        store_type: str = None,
    ):
        # Set the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Description.
        self.description = description
        # Encryption type
        self.encrypt_type = encrypt_type
        # Name
        self.name = name
        # Region code
        self.reg_id = reg_id
        # Specified risk value
        self.risk_value = risk_value
        # Scene
        self.scene = scene
        # Storage path
        self.store_path = store_path
        # Storage type
        self.store_type = store_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.description is not None:
            result['description'] = self.description

        if self.encrypt_type is not None:
            result['encryptType'] = self.encrypt_type

        if self.name is not None:
            result['name'] = self.name

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.risk_value is not None:
            result['riskValue'] = self.risk_value

        if self.scene is not None:
            result['scene'] = self.scene

        if self.store_path is not None:
            result['storePath'] = self.store_path

        if self.store_type is not None:
            result['storeType'] = self.store_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('encryptType') is not None:
            self.encrypt_type = m.get('encryptType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('riskValue') is not None:
            self.risk_value = m.get('riskValue')

        if m.get('scene') is not None:
            self.scene = m.get('scene')

        if m.get('storePath') is not None:
            self.store_path = m.get('storePath')

        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')

        return self

