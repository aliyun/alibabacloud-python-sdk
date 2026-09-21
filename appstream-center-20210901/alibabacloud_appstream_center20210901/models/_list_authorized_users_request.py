# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAuthorizedUsersRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_group_set_id: str = None,
        app_instance_persistent_id: str = None,
        end_user_id: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        user_id_fuzzy: str = None,
    ):
        # The application ID used to filter authorization relationships.
        # 
        # Set this parameter when querying authorized users of a specific application. This parameter is not required when querying cloud browser groups or delivery group sets.
        self.app_id = app_id
        # The delivery group ID. When querying cloud browsers, set this parameter to the browser group ID.
        # 
        # Specify either this parameter or `AppInstanceGroupSetId`, but not both.
        self.app_instance_group_id = app_instance_group_id
        # The delivery group set ID.
        # 
        # Specify either this parameter or `AppInstanceGroupId`, but not both. When querying by set, omit `AppId` and `AppInstancePersistentId`.
        self.app_instance_group_set_id = app_instance_group_set_id
        # The persistent session ID used to filter authorization relationships. This parameter applies to delivery groups that use session-based authorization.
        # 
        # This parameter is not required when querying delivery group sets.
        self.app_instance_persistent_id = app_instance_persistent_id
        # Performs an exact match by authorized username. If this parameter is not specified, results are not filtered by exact username.
        self.end_user_id = end_user_id
        # The page number. This parameter is required. Pages start from page 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The maximum number of records per page. This parameter is required. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The product type. Set this parameter to `CloudBrowser` when querying authorized users of cloud browsers.
        # 
        # This parameter is required.
        self.product_type = product_type
        # Performs a fuzzy match by text contained in the authorized username.
        self.user_id_fuzzy = user_id_fuzzy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_set_id is not None:
            result['AppInstanceGroupSetId'] = self.app_instance_group_set_id

        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.user_id_fuzzy is not None:
            result['UserIdFuzzy'] = self.user_id_fuzzy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupSetId') is not None:
            self.app_instance_group_set_id = m.get('AppInstanceGroupSetId')

        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('UserIdFuzzy') is not None:
            self.user_id_fuzzy = m.get('UserIdFuzzy')

        return self

