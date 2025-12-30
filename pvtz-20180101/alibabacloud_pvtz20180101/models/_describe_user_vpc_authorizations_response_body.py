# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribeUserVpcAuthorizationsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        users: List[main_models.DescribeUserVpcAuthorizationsResponseBodyUsers] = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_items = total_items
        # The total number of returned pages.
        self.total_pages = total_pages
        # The Alibaba Cloud accounts to which the permissions on the resources are granted.
        self.users = users

    def validate(self):
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.DescribeUserVpcAuthorizationsResponseBodyUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class DescribeUserVpcAuthorizationsResponseBodyUsers(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        authorized_aliyun_id: str = None,
        authorized_user_id: int = None,
        create_time: str = None,
        create_timestamp: int = None,
    ):
        # The authorization scope. Valid values:
        # 
        # *   NORMAL: general authorization
        # *   CLOUD_PRODUCT: cloud service-related authorization
        self.auth_type = auth_type
        # The name of the Alibaba Cloud account to which the permissions on the resources are granted.
        self.authorized_aliyun_id = authorized_aliyun_id
        # The ID of the Alibaba Cloud account to which the permissions on the resources are granted.
        self.authorized_user_id = authorized_user_id
        # The time when the authorization was performed. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the authorization was performed. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.authorized_aliyun_id is not None:
            result['AuthorizedAliyunId'] = self.authorized_aliyun_id

        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('AuthorizedAliyunId') is not None:
            self.authorized_aliyun_id = m.get('AuthorizedAliyunId')

        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        return self

