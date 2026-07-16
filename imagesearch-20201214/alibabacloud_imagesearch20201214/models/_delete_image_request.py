# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteImageRequest(DaraModel):
    def __init__(
        self,
        filter: str = None,
        instance_name: str = None,
        is_delete_by_filter: bool = None,
        pic_name: str = None,
        product_id: str = None,
    ):
        # The filter condition. The operators supported for int_attr include greater than (>), greater than or equal to (>=), less than (<), less than or equal to (<=), and equal to (=). The operators supported for str_attr include equal to (=) and not equal to (!=). Multiple conditions can be connected by using AND and OR.
        # Examples:
        # - int_attr >= 100.
        # - str_attr != "value1".
        # - int_attr = 1000 AND str_attr = "value1".
        # >A maximum of 4096 characters are supported.
        self.filter = filter
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # If you have purchased an Image Search instance, log on to the [Image Search console](https://imagesearch.console.aliyun.com/) to view the instance name.
        # If you have not purchased an Image Search instance, refer to [Activate the service](https://help.aliyun.com/document_detail/179178.html) and [Create an instance](https://help.aliyun.com/document_detail/66569.html).
        # >The instance name is not the instance ID. The instance name must be unique within the same region. Make sure that you use the correct value.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # Specifies whether to delete images based on the Filter parameter.
        # > 1. If this parameter is set to true, images are deleted based on the Filter parameter, and Filter is required.   
        #  2. If this parameter is set to false, images are deleted based on ProductId or the combination of ProductId and PicName. ProductId is required.
        self.is_delete_by_filter = is_delete_by_filter
        # The image name.
        #  - If you do not specify this parameter, all images under the specified ProductId are deleted.
        #  - If you specify this parameter, the image specified by the combination of ProductId and PicName is deleted.
        self.pic_name = pic_name
        # The product ID.
        # 
        # > 1. A product can have multiple images. 2. If IsDeleteByFilter is set to false, this parameter is required.
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.is_delete_by_filter is not None:
            result['IsDeleteByFilter'] = self.is_delete_by_filter

        if self.pic_name is not None:
            result['PicName'] = self.pic_name

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IsDeleteByFilter') is not None:
            self.is_delete_by_filter = m.get('IsDeleteByFilter')

        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        return self

