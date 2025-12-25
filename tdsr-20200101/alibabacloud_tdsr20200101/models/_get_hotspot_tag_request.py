# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHotspotTagRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        enabled: bool = None,
        preview_token: str = None,
        sub_scene_uuid: str = None,
        type: str = None,
    ):
        self.domain = domain
        self.enabled = enabled
        self.preview_token = preview_token
        self.sub_scene_uuid = sub_scene_uuid
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token

        if self.sub_scene_uuid is not None:
            result['SubSceneUuid'] = self.sub_scene_uuid

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')

        if m.get('SubSceneUuid') is not None:
            self.sub_scene_uuid = m.get('SubSceneUuid')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

