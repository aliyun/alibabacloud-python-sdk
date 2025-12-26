# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWuyingServerImageRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        product_type: str = None,
        wuying_server_id: str = None,
    ):
        # The image ID.
        self.image_id = image_id
        # The product type. Set this parameter to WuyingServer.
        self.product_type = product_type
        # The ID of the workstation.
        self.wuying_server_id = wuying_server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.wuying_server_id is not None:
            result['WuyingServerId'] = self.wuying_server_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('WuyingServerId') is not None:
            self.wuying_server_id = m.get('WuyingServerId')

        return self

