# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckImageExistsRequest(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        pic_name: str = None,
        product_id: str = None,
    ):
        # Image Search instance name. Supports up to 20 characters.  
        # If you have already purchased an Image Search instance, you can logon to the [Image Search console](https://imagesearch.console.aliyun.com/) to view it.  
        # If you have not purchased an Image Search instance, see [Activate the service](https://help.aliyun.com/document_detail/179178.html) and [Create an instance](https://help.aliyun.com/document_detail/66569.html).  
        # > The instance name here is not the instance ID. Please distinguish between them when using.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # Image name.
        # 
        # This parameter is required.
        self.pic_name = pic_name
        # Product ID.
        # 
        # This parameter is required.
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.pic_name is not None:
            result['PicName'] = self.pic_name

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        return self

