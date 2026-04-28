# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class Domain(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        data_hash_name: str = None,
        description: str = None,
        domain_id: str = None,
        domain_name: str = None,
        init_drive_enable: bool = None,
        init_drive_size: int = None,
        parent_domain_id: str = None,
        published_app_access_strategy: main_models.AppAccessStrategy = None,
        sharable: bool = None,
        size_quota: int = None,
        size_quota_used: int = None,
        status: int = None,
        store_redundancy_type: str = None,
        updated_at: str = None,
        used_size: int = None,
        user_count_quota: int = None,
    ):
        # The time when the domain was created. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.created_at = created_at
        # The method used to calculate the hash value of the data.
        self.data_hash_name = data_hash_name
        # The description of the domain.
        self.description = description
        # domain ID
        self.domain_id = domain_id
        # The name of the domain.
        self.domain_name = domain_name
        # Specifies whether to enable the default drive feature. Valid values: true and false. A value of true specifies that all users are assigned a drive by default on the first logon. Default value: false.
        self.init_drive_enable = init_drive_enable
        # The size of the default drive. Unit: bytes. This parameter is required if you set init_drive_enable to true. Default value: 0. A value of 0 indicates that the size of the default drive is 0 byte and you cannot upload files to the drive. To initialize the default drive, set init_drive_size to a positive number or -1. A value of -1 indicates that the size is unlimited.
        self.init_drive_size = init_drive_size
        # The ID of the parent domain. If the parent domain exists, the current domain is a child domain. Otherwise, the current domain is a common domain.
        self.parent_domain_id = parent_domain_id
        # The access policy of the application.
        self.published_app_access_strategy = published_app_access_strategy
        # Specifies whether to enable sharing.
        self.sharable = sharable
        # The total storage quota for all drives in the domain. A value of 0 indicates that the quota is unlimited.
        self.size_quota = size_quota
        # The used storage quota of all drives in the domain.
        self.size_quota_used = size_quota_used
        # The status of the domain. 1: The domain runs normally. 2: The domain is being created. 6: The domain has expired.
        self.status = status
        self.store_redundancy_type = store_redundancy_type
        # The time when the domain was last modified. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.updated_at = updated_at
        # The usage of the logic space. Unit: bytes.
        self.used_size = used_size
        # The maximum allowed number of users.
        self.user_count_quota = user_count_quota

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

        if self.data_hash_name is not None:
            result['data_hash_name'] = self.data_hash_name

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

        if self.sharable is not None:
            result['sharable'] = self.sharable

        if self.size_quota is not None:
            result['size_quota'] = self.size_quota

        if self.size_quota_used is not None:
            result['size_quota_used'] = self.size_quota_used

        if self.status is not None:
            result['status'] = self.status

        if self.store_redundancy_type is not None:
            result['store_redundancy_type'] = self.store_redundancy_type

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        if self.used_size is not None:
            result['used_size'] = self.used_size

        if self.user_count_quota is not None:
            result['user_count_quota'] = self.user_count_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('data_hash_name') is not None:
            self.data_hash_name = m.get('data_hash_name')

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

        if m.get('sharable') is not None:
            self.sharable = m.get('sharable')

        if m.get('size_quota') is not None:
            self.size_quota = m.get('size_quota')

        if m.get('size_quota_used') is not None:
            self.size_quota_used = m.get('size_quota_used')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('store_redundancy_type') is not None:
            self.store_redundancy_type = m.get('store_redundancy_type')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        if m.get('used_size') is not None:
            self.used_size = m.get('used_size')

        if m.get('user_count_quota') is not None:
            self.user_count_quota = m.get('user_count_quota')

        return self

