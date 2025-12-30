# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserVpcAuthorizationsRequest(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        authorized_user_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The authorization scope. Valid values:
        # 
        # *   NORMAL: general authorization
        # *   CLOUD_PRODUCT: cloud service-related authorization
        self.auth_type = auth_type
        # The ID of the Alibaba Cloud account to which the permissions on the resources are granted.
        self.authorized_user_id = authorized_user_id
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

