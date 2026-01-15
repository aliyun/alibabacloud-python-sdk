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
        self.filter = filter
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        self.is_delete_by_filter = is_delete_by_filter
        # The name of the image.
        # 
        # *   If this parameter is not set, the system deletes all the images that correspond to the specified ProductId parameter.
        # *   If this parameter is set, the system deletes only the image that is specified by the ProductId and PicName parameters.
        self.pic_name = pic_name
        # The ID of the commodity.
        # 
        # >  A commodity may have multiple images.
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

