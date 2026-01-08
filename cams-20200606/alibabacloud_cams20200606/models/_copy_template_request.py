# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyTemplateRequest(DaraModel):
    def __init__(
        self,
        cust_space_id: str = None,
        language: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scene_template_code: str = None,
        scene_template_name: str = None,
    ):
        self.cust_space_id = cust_space_id
        self.language = language
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.scene_template_code = scene_template_code
        # This parameter is required.
        self.scene_template_name = scene_template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.language is not None:
            result['Language'] = self.language

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scene_template_code is not None:
            result['SceneTemplateCode'] = self.scene_template_code

        if self.scene_template_name is not None:
            result['SceneTemplateName'] = self.scene_template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SceneTemplateCode') is not None:
            self.scene_template_code = m.get('SceneTemplateCode')

        if m.get('SceneTemplateName') is not None:
            self.scene_template_name = m.get('SceneTemplateName')

        return self

