# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTagInfoBySelectionRequest(DaraModel):
    def __init__(
        self,
        industry_id: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scene_id: int = None,
        tag_id: int = None,
    ):
        # The industry ID.
        self.industry_id = industry_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The scene ID.
        self.scene_id = scene_id
        # The tag ID.
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.industry_id is not None:
            result['IndustryId'] = self.industry_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndustryId') is not None:
            self.industry_id = m.get('IndustryId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

