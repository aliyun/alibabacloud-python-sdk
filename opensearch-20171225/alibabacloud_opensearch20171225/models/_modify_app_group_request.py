# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAppGroupRequest(DaraModel):
    def __init__(
        self,
        current_version: str = None,
        description: str = None,
        domain: str = None,
        resource_group_id: str = None,
        dry_run: bool = None,
    ):
        # The online version of the application.
        self.current_version = current_version
        # The description of the application.
        self.description = description
        # The type of the industry. Valid values:
        # 
        # *   general: general.
        # *   ecommerce: e-commerce.
        # *   education: education.
        # *   esports: electronic sports.
        # *   community: content community.
        self.domain = domain
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # Specifies whether to verify the application before modification. Valid values: true and false.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_version is not None:
            result['currentVersion'] = self.current_version

        if self.description is not None:
            result['description'] = self.description

        if self.domain is not None:
            result['domain'] = self.domain

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

