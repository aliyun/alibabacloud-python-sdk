# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class UpdateDomainRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        domain_id: str = None,
        domain_name: str = None,
        init_drive_enable: bool = None,
        init_drive_size: int = None,
        published_app_access_strategy: main_models.AppAccessStrategy = None,
        size_quota: int = None,
        user_count_quota: int = None,
    ):
        # The description of the domain.
        self.description = description
        # The domain ID.
        # 
        # This parameter is required.
        self.domain_id = domain_id
        # The name of the domain.
        self.domain_name = domain_name
        # Specifies whether to enable the default drive feature. A value of true specifies that all users are assigned a drive by default on the first logon. Default value: false.
        self.init_drive_enable = init_drive_enable
        # The size of the default drive. Unit: bytes. You must specify init_drive_size if you set init_drive_enable to true. Default value: 0. A value of 0 specifies that the size of the default drive is 0 bytes and you cannot upload files to the drive. To initialize the default drive, set init_drive_size to 0. A value of -1 specifies that the size is unlimited.
        self.init_drive_size = init_drive_size
        # The access policy of the application.
        self.published_app_access_strategy = published_app_access_strategy
        # The total storage quota for all drives in the domain. A value of 0 specifies that the quota is unlimited.
        self.size_quota = size_quota
        # The maximum number of users that can be created in the domain.
        self.user_count_quota = user_count_quota

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()

        if self.size_quota is not None:
            result['size_quota'] = self.size_quota

        if self.user_count_quota is not None:
            result['user_count_quota'] = self.user_count_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('published_app_access_strategy') is not None:
            temp_model = main_models.AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(m.get('published_app_access_strategy'))

        if m.get('size_quota') is not None:
            self.size_quota = m.get('size_quota')

        if m.get('user_count_quota') is not None:
            self.user_count_quota = m.get('user_count_quota')

        return self

