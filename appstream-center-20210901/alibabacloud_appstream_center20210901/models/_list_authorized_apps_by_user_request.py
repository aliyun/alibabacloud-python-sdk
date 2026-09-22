# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAuthorizedAppsByUserRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        app_name: str = None,
        end_user_id: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
    ):
        # The application ID used to filter results. Fuzzy match by containment is used. This parameter can be combined with other filter parameters. You can obtain the application ID from the Apps list returned by the [GetAppInstanceGroup](https://help.aliyun.com/document_detail/600836.html) operation.
        self.app_id = app_id
        # The delivery group ID used to filter results. Fuzzy match by containment is used. This parameter can be combined with other filter parameters. Call the [ListAppInstanceGroup](https://help.aliyun.com/document_detail/428506.html) operation to obtain the delivery group ID.
        self.app_instance_group_id = app_instance_group_id
        # The delivery group name used to filter results. Fuzzy match by name is used. This parameter can be combined with other filter parameters.
        self.app_instance_group_name = app_instance_group_name
        # The application name used to filter results. Fuzzy match by name is used. This parameter can be combined with other filter parameters.
        self.app_name = app_name
        # The username to query. **Required**. The user must already exist under the current account. Call the [DescribeUsers](https://help.aliyun.com/document_detail/436936.html) operation to obtain the username.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # The page number of the results. **Required**. The value starts from 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of records per page. **Required**. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The product type. **Required**. The value is case-insensitive.
        # 
        # This operation queries per-application authorization records. This authorization method applies to WUYING Cloud Application delivery groups. Valid values:
        # 
        # - CloudApp: WUYING Cloud Application.
        # 
        # This parameter is required.
        self.product_type = product_type

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

        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

