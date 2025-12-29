# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCloudauthstSceneRequest(DaraModel):
    def __init__(
        self,
        product_code: str = None,
        scene_name: str = None,
        store_image: str = None,
    ):
        # Product code.
        # 
        # This parameter is required.
        self.product_code = product_code
        # Scene name.
        # 
        # This parameter is required.
        self.scene_name = scene_name
        # Whether to deliver the files generated from the authentication to the customer\\"s OSS:
        # - **Y**: Enable
        # - **N**: Disable
        self.store_image = store_image

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.store_image is not None:
            result['StoreImage'] = self.store_image

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('StoreImage') is not None:
            self.store_image = m.get('StoreImage')

        return self

