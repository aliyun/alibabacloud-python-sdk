# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeImageSharePermissionResponseBody(DaraModel):
    def __init__(
        self,
        accounts: main_models.DescribeImageSharePermissionResponseBodyAccounts = None,
        image_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        request_id: str = None,
        share_groups: main_models.DescribeImageSharePermissionResponseBodyShareGroups = None,
        total_count: int = None,
    ):
        # The Alibaba Cloud accounts.
        self.accounts = accounts
        # The ID of the custom image.
        self.image_id = image_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID of the custom image.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The shared groups.
        self.share_groups = share_groups
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.accounts:
            self.accounts.validate()
        if self.share_groups:
            self.share_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.share_groups is not None:
            result['ShareGroups'] = self.share_groups.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = main_models.DescribeImageSharePermissionResponseBodyAccounts()
            self.accounts = temp_model.from_map(m.get('Accounts'))

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShareGroups') is not None:
            temp_model = main_models.DescribeImageSharePermissionResponseBodyShareGroups()
            self.share_groups = temp_model.from_map(m.get('ShareGroups'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeImageSharePermissionResponseBodyShareGroups(DaraModel):
    def __init__(
        self,
        share_group: List[main_models.DescribeImageSharePermissionResponseBodyShareGroupsShareGroup] = None,
    ):
        self.share_group = share_group

    def validate(self):
        if self.share_group:
            for v1 in self.share_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ShareGroup'] = []
        if self.share_group is not None:
            for k1 in self.share_group:
                result['ShareGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.share_group = []
        if m.get('ShareGroup') is not None:
            for k1 in m.get('ShareGroup'):
                temp_model = main_models.DescribeImageSharePermissionResponseBodyShareGroupsShareGroup()
                self.share_group.append(temp_model.from_map(k1))

        return self

class DescribeImageSharePermissionResponseBodyShareGroupsShareGroup(DaraModel):
    def __init__(
        self,
        group: str = None,
    ):
        # The shared group.
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['Group'] = self.group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')

        return self

class DescribeImageSharePermissionResponseBodyAccounts(DaraModel):
    def __init__(
        self,
        account: List[main_models.DescribeImageSharePermissionResponseBodyAccountsAccount] = None,
    ):
        self.account = account

    def validate(self):
        if self.account:
            for v1 in self.account:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Account'] = []
        if self.account is not None:
            for k1 in self.account:
                result['Account'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k1 in m.get('Account'):
                temp_model = main_models.DescribeImageSharePermissionResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k1))

        return self

class DescribeImageSharePermissionResponseBodyAccountsAccount(DaraModel):
    def __init__(
        self,
        aliyun_id: str = None,
        shared_time: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.aliyun_id = aliyun_id
        # The time when the image was shared. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.shared_time = shared_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id

        if self.shared_time is not None:
            result['SharedTime'] = self.shared_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')

        if m.get('SharedTime') is not None:
            self.shared_time = m.get('SharedTime')

        return self

