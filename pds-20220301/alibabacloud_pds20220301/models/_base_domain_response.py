# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class BaseDomainResponse(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        domain_id: str = None,
        domain_name: str = None,
        init_drive_enable: bool = None,
        init_drive_size: int = None,
        parent_domain_id: str = None,
        published_app_access_strategy: main_models.AppAccessStrategy = None,
        share_link_enabled: bool = None,
        size_quota: int = None,
        size_quota_used: int = None,
        status: int = None,
        updated_at: str = None,
        used_size: int = None,
    ):
        self.created_at = created_at
        self.description = description
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.init_drive_enable = init_drive_enable
        self.init_drive_size = init_drive_size
        self.parent_domain_id = parent_domain_id
        self.published_app_access_strategy = published_app_access_strategy
        self.share_link_enabled = share_link_enabled
        self.size_quota = size_quota
        self.size_quota_used = size_quota_used
        self.status = status
        self.updated_at = updated_at
        self.used_size = used_size

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.domain_name is not None:
            result['domain_name'] = self.domain_name

        if self.init_drive_enable is not None:
            result['init_drive_enable'] = self.init_drive_enable

        if self.init_drive_size is not None:
            result['init_drive_size'] = self.init_drive_size

        if self.parent_domain_id is not None:
            result['parent_domain_id'] = self.parent_domain_id

        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()

        if self.share_link_enabled is not None:
            result['share_link_enabled'] = self.share_link_enabled

        if self.size_quota is not None:
            result['size_quota'] = self.size_quota

        if self.size_quota_used is not None:
            result['size_quota_used'] = self.size_quota_used

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        if self.used_size is not None:
            result['used_size'] = self.used_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('domain_name') is not None:
            self.domain_name = m.get('domain_name')

        if m.get('init_drive_enable') is not None:
            self.init_drive_enable = m.get('init_drive_enable')

        if m.get('init_drive_size') is not None:
            self.init_drive_size = m.get('init_drive_size')

        if m.get('parent_domain_id') is not None:
            self.parent_domain_id = m.get('parent_domain_id')

        if m.get('published_app_access_strategy') is not None:
            temp_model = main_models.AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(m.get('published_app_access_strategy'))

        if m.get('share_link_enabled') is not None:
            self.share_link_enabled = m.get('share_link_enabled')

        if m.get('size_quota') is not None:
            self.size_quota = m.get('size_quota')

        if m.get('size_quota_used') is not None:
            self.size_quota_used = m.get('size_quota_used')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        if m.get('used_size') is not None:
            self.used_size = m.get('used_size')

        return self

