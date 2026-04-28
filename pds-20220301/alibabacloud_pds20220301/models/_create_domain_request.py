# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDomainRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        domain_name: str = None,
        init_drive_enable: bool = None,
        init_drive_size: int = None,
        parent_domain_id: str = None,
        size_quota: int = None,
        store_redundancy_type: str = None,
        user_count_quota: int = None,
    ):
        # The description of the domain.
        self.description = description
        # The name of the domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Specifies whether to enable the default drive feature. A value of true specifies that all users are assigned a drive by default on the first logon. Default value: false.
        self.init_drive_enable = init_drive_enable
        # This parameter is required when the init_drive_enable is set to true. The size of the default drive. Unit: bytes. The default is 0, meaning the created drive size is 0, and files cannot be uploaded. If you need to initialize the drive, set this value. A value of -1 indicates that the size is unlimited.
        self.init_drive_size = init_drive_size
        # The ID of the parent domain. If you want to create a child domain, specify parent_domain_id. In most cases, you do not need to create a child domain. If you want to perform secondary operations based on Drive and Photo Service, contact the customer service.
        self.parent_domain_id = parent_domain_id
        # The total storage quota for all drives in the domain. A value of 0 indicates that the quota is unlimited.
        self.size_quota = size_quota
        # Specifies the storage redundancy type. Valid values:
        # 
        # *   LRS: locally redundant storage
        # *   ZRS: zone-redundant storage
        self.store_redundancy_type = store_redundancy_type
        # The largest number of users that can be created in the domain. A value of 0 specifies that the number is unlimited.
        self.user_count_quota = user_count_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.domain_name is not None:
            result['domain_name'] = self.domain_name

        if self.init_drive_enable is not None:
            result['init_drive_enable'] = self.init_drive_enable

        if self.init_drive_size is not None:
            result['init_drive_size'] = self.init_drive_size

        if self.parent_domain_id is not None:
            result['parent_domain_id'] = self.parent_domain_id

        if self.size_quota is not None:
            result['size_quota'] = self.size_quota

        if self.store_redundancy_type is not None:
            result['store_redundancy_type'] = self.store_redundancy_type

        if self.user_count_quota is not None:
            result['user_count_quota'] = self.user_count_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domain_name') is not None:
            self.domain_name = m.get('domain_name')

        if m.get('init_drive_enable') is not None:
            self.init_drive_enable = m.get('init_drive_enable')

        if m.get('init_drive_size') is not None:
            self.init_drive_size = m.get('init_drive_size')

        if m.get('parent_domain_id') is not None:
            self.parent_domain_id = m.get('parent_domain_id')

        if m.get('size_quota') is not None:
            self.size_quota = m.get('size_quota')

        if m.get('store_redundancy_type') is not None:
            self.store_redundancy_type = m.get('store_redundancy_type')

        if m.get('user_count_quota') is not None:
            self.user_count_quota = m.get('user_count_quota')

        return self

