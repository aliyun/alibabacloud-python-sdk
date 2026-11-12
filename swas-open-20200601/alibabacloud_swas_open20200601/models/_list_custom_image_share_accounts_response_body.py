# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ListCustomImageShareAccountsResponseBody(DaraModel):
    def __init__(
        self,
        image_share_users: List[main_models.ListCustomImageShareAccountsResponseBodyImageShareUsers] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the shared custom images.
        self.image_share_users = image_share_users
        # The page number of the paged query.
        self.page_number = page_number
        # The number of entries per page for a paged query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of instances.
        self.total_count = total_count

    def validate(self):
        if self.image_share_users:
            for v1 in self.image_share_users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageShareUsers'] = []
        if self.image_share_users is not None:
            for k1 in self.image_share_users:
                result['ImageShareUsers'].append(k1.to_map() if k1 else None)

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
        self.image_share_users = []
        if m.get('ImageShareUsers') is not None:
            for k1 in m.get('ImageShareUsers'):
                temp_model = main_models.ListCustomImageShareAccountsResponseBodyImageShareUsers()
                self.image_share_users.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCustomImageShareAccountsResponseBodyImageShareUsers(DaraModel):
    def __init__(
        self,
        shared_time: str = None,
        user_id: int = None,
    ):
        # The time when the custom image was shared, in the format of YYYY-MM-DD HH:mm:ss.S.
        self.shared_time = shared_time
        # The Alibaba Cloud account ID with which the custom image is shared.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.shared_time is not None:
            result['SharedTime'] = self.shared_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SharedTime') is not None:
            self.shared_time = m.get('SharedTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

