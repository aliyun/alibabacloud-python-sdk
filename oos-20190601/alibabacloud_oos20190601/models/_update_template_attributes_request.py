# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTemplateAttributesRequest(DaraModel):
    def __init__(
        self,
        account_ids: str = None,
        is_favorite: bool = None,
        region_id: str = None,
        share_permission_action: str = None,
        share_template_version: str = None,
        template_name: str = None,
    ):
        self.account_ids = account_ids
        self.is_favorite = is_favorite
        self.region_id = region_id
        self.share_permission_action = share_permission_action
        self.share_template_version = share_template_version
        # This parameter is required.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.is_favorite is not None:
            result['IsFavorite'] = self.is_favorite

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.share_permission_action is not None:
            result['SharePermissionAction'] = self.share_permission_action

        if self.share_template_version is not None:
            result['ShareTemplateVersion'] = self.share_template_version

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('IsFavorite') is not None:
            self.is_favorite = m.get('IsFavorite')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SharePermissionAction') is not None:
            self.share_permission_action = m.get('SharePermissionAction')

        if m.get('ShareTemplateVersion') is not None:
            self.share_template_version = m.get('ShareTemplateVersion')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

