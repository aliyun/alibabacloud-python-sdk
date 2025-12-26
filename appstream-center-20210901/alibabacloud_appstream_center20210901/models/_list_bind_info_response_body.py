# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListBindInfoResponseBody(DaraModel):
    def __init__(
        self,
        bind_info_models: List[main_models.ListBindInfoResponseBodyBindInfoModels] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The bindings.
        self.bind_info_models = bind_info_models
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.bind_info_models:
            for v1 in self.bind_info_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BindInfoModels'] = []
        if self.bind_info_models is not None:
            for k1 in self.bind_info_models:
                result['BindInfoModels'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bind_info_models = []
        if m.get('BindInfoModels') is not None:
            for k1 in m.get('BindInfoModels'):
                temp_model = main_models.ListBindInfoResponseBodyBindInfoModels()
                self.bind_info_models.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBindInfoResponseBodyBindInfoModels(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_version: str = None,
        product_type: str = None,
        region_id: str = None,
        user_id: str = None,
        wy_id: str = None,
    ):
        # The account type.
        # 
        # Valid values:
        # 
        # *   ad: Active Directory (AD) account
        # *   simple: convenience account
        self.account_type = account_type
        # The app ID.
        self.app_id = app_id
        # The ID of the delivery group.
        self.app_instance_group_id = app_instance_group_id
        # The ID of the app instance.
        self.app_instance_id = app_instance_id
        # The app version.
        self.app_version = app_version
        # The product type.
        # 
        # Valid values:
        # 
        # *   CloudApp: App Streaming
        # *   CloudBrowser: Cloud-based Browser
        # *   AndroidCloud: Cloud Phone
        self.product_type = product_type
        # The region ID.
        self.region_id = region_id
        # The user ID.
        self.user_id = user_id
        # The ID of the Alibaba Cloud Workspace user.
        self.wy_id = wy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.wy_id is not None:
            result['WyId'] = self.wy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')

        return self

