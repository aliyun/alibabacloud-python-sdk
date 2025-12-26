# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateImageFromAppInstanceGroupRequest(DaraModel):
    def __init__(
        self,
        app_center_image_name: str = None,
        app_instance_group_id: str = None,
        product_type: str = None,
    ):
        # The image name.
        # 
        # This parameter is required.
        self.app_center_image_name = app_center_image_name
        # The ID of the delivery group. You can call the [ListAppInstanceGroup](https://help.aliyun.com/document_detail/428506.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
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
        if self.app_center_image_name is not None:
            result['AppCenterImageName'] = self.app_center_image_name

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageName') is not None:
            self.app_center_image_name = m.get('AppCenterImageName')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

