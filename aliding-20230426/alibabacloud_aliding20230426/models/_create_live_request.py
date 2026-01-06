# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CreateLiveRequest(DaraModel):
    def __init__(
        self,
        cover_url: str = None,
        introduction: str = None,
        pre_end_time: int = None,
        pre_start_time: int = None,
        public_type: int = None,
        tenant_context: main_models.CreateLiveRequestTenantContext = None,
        title: str = None,
    ):
        self.cover_url = cover_url
        self.introduction = introduction
        # This parameter is required.
        self.pre_end_time = pre_end_time
        # This parameter is required.
        self.pre_start_time = pre_start_time
        self.public_type = public_type
        self.tenant_context = tenant_context
        # This parameter is required.
        self.title = title

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url

        if self.introduction is not None:
            result['Introduction'] = self.introduction

        if self.pre_end_time is not None:
            result['PreEndTime'] = self.pre_end_time

        if self.pre_start_time is not None:
            result['PreStartTime'] = self.pre_start_time

        if self.public_type is not None:
            result['PublicType'] = self.public_type

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')

        if m.get('PreEndTime') is not None:
            self.pre_end_time = m.get('PreEndTime')

        if m.get('PreStartTime') is not None:
            self.pre_start_time = m.get('PreStartTime')

        if m.get('PublicType') is not None:
            self.public_type = m.get('PublicType')

        if m.get('TenantContext') is not None:
            temp_model = main_models.CreateLiveRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class CreateLiveRequestTenantContext(DaraModel):
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

