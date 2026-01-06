# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CreateOrgHonorTemplateRequest(DaraModel):
    def __init__(
        self,
        tenant_context: main_models.CreateOrgHonorTemplateRequestTenantContext = None,
        avatar_frame_media_id: str = None,
        default_bg_color: str = None,
        medal_desc: str = None,
        medal_media_id: str = None,
        medal_name: str = None,
        org_id: int = None,
        user_id: str = None,
    ):
        self.tenant_context = tenant_context
        # This parameter is required.
        self.avatar_frame_media_id = avatar_frame_media_id
        # This parameter is required.
        self.default_bg_color = default_bg_color
        # This parameter is required.
        self.medal_desc = medal_desc
        # This parameter is required.
        self.medal_media_id = medal_media_id
        # This parameter is required.
        self.medal_name = medal_name
        # This parameter is required.
        self.org_id = org_id
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.avatar_frame_media_id is not None:
            result['avatarFrameMediaId'] = self.avatar_frame_media_id

        if self.default_bg_color is not None:
            result['defaultBgColor'] = self.default_bg_color

        if self.medal_desc is not None:
            result['medalDesc'] = self.medal_desc

        if self.medal_media_id is not None:
            result['medalMediaId'] = self.medal_media_id

        if self.medal_name is not None:
            result['medalName'] = self.medal_name

        if self.org_id is not None:
            result['orgId'] = self.org_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            temp_model = main_models.CreateOrgHonorTemplateRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('avatarFrameMediaId') is not None:
            self.avatar_frame_media_id = m.get('avatarFrameMediaId')

        if m.get('defaultBgColor') is not None:
            self.default_bg_color = m.get('defaultBgColor')

        if m.get('medalDesc') is not None:
            self.medal_desc = m.get('medalDesc')

        if m.get('medalMediaId') is not None:
            self.medal_media_id = m.get('medalMediaId')

        if m.get('medalName') is not None:
            self.medal_name = m.get('medalName')

        if m.get('orgId') is not None:
            self.org_id = m.get('orgId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class CreateOrgHonorTemplateRequestTenantContext(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

