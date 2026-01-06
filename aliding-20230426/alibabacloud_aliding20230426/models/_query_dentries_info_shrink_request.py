# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDentriesInfoShrinkRequest(DaraModel):
    def __init__(
        self,
        app_ids_for_app_properties_shrink: str = None,
        dentry_id: str = None,
        space_id: str = None,
        tenant_context_shrink: str = None,
        with_thumbnail: bool = None,
    ):
        self.app_ids_for_app_properties_shrink = app_ids_for_app_properties_shrink
        # This parameter is required.
        self.dentry_id = dentry_id
        # This parameter is required.
        self.space_id = space_id
        self.tenant_context_shrink = tenant_context_shrink
        self.with_thumbnail = with_thumbnail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ids_for_app_properties_shrink is not None:
            result['AppIdsForAppProperties'] = self.app_ids_for_app_properties_shrink

        if self.dentry_id is not None:
            result['DentryId'] = self.dentry_id

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.with_thumbnail is not None:
            result['WithThumbnail'] = self.with_thumbnail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdsForAppProperties') is not None:
            self.app_ids_for_app_properties_shrink = m.get('AppIdsForAppProperties')

        if m.get('DentryId') is not None:
            self.dentry_id = m.get('DentryId')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('WithThumbnail') is not None:
            self.with_thumbnail = m.get('WithThumbnail')

        return self

