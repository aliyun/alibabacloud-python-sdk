# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAppInstanceGroupImageRequest(DaraModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        product_type: str = None,
    ):
        # The application image ID. You can obtain this ID from the Image Management page in the WUYING Cloud Application console.
        # 
        # This parameter is required.
        self.app_center_image_id = app_center_image_id
        # The delivery group ID.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The region ID of the delivery group. For more information about supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The product type.
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
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

