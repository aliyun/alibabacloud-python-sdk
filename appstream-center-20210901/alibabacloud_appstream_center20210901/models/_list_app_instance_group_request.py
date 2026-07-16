# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListAppInstanceGroupRequest(DaraModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        biz_region_id: str = None,
        excluded_user_group_ids: List[str] = None,
        node_instance_type: str = None,
        office_site_id: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        region_id: str = None,
        status: List[str] = None,
        tag: List[main_models.ListAppInstanceGroupRequestTag] = None,
        user_group_ids: List[str] = None,
    ):
        # The application image ID. You can obtain this value from the Image Management page in the WUYING Cloud Application console.
        self.app_center_image_id = app_center_image_id
        # The delivery group ID.
        self.app_instance_group_id = app_instance_group_id
        # The delivery group name. Fuzzy match is used for the query. For example, if you set the delivery group name to `Office App`, all delivery groups whose names contain `Office App` are returned, such as `My Office App` and `Office App A`.
        self.app_instance_group_name = app_instance_group_name
        # The region ID of the delivery group. For more information about supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        self.biz_region_id = biz_region_id
        self.excluded_user_group_ids = excluded_user_group_ids
        # The specification type ID of the purchased resources. You can call the [ListNodeInstanceType](~~ListNodeInstanceType~~) operation to obtain this value.
        self.node_instance_type = node_instance_type
        # The office network ID.
        self.office_site_id = office_site_id
        # The page number of the query results to display.
        self.page_number = page_number
        # The number of query results per page. Maximum value: `100`.
        self.page_size = page_size
        # The product type.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The region ID.
        self.region_id = region_id
        # The list of delivery group statuses.
        self.status = status
        # The tags.
        self.tag = tag
        self.user_group_ids = user_group_ids

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.excluded_user_group_ids is not None:
            result['ExcludedUserGroupIds'] = self.excluded_user_group_ids

        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ExcludedUserGroupIds') is not None:
            self.excluded_user_group_ids = m.get('ExcludedUserGroupIds')

        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListAppInstanceGroupRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        return self

class ListAppInstanceGroupRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

