# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ReviewRecordResult(DaraModel):
    def __init__(
        self,
        address: str = None,
        apply_type: str = None,
        contact_name: str = None,
        phone: str = None,
        scene_desc: str = None,
        scopes: List[str] = None,
        service_type: str = None,
    ):
        self.address = address
        self.apply_type = apply_type
        self.contact_name = contact_name
        self.phone = phone
        self.scene_desc = scene_desc
        self.scopes = scopes
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.apply_type is not None:
            result['applyType'] = self.apply_type

        if self.contact_name is not None:
            result['contactName'] = self.contact_name

        if self.phone is not None:
            result['phone'] = self.phone

        if self.scene_desc is not None:
            result['sceneDesc'] = self.scene_desc

        if self.scopes is not None:
            result['scopes'] = self.scopes

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('applyType') is not None:
            self.apply_type = m.get('applyType')

        if m.get('contactName') is not None:
            self.contact_name = m.get('contactName')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('sceneDesc') is not None:
            self.scene_desc = m.get('sceneDesc')

        if m.get('scopes') is not None:
            self.scopes = m.get('scopes')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        return self

