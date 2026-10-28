# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyShareImageRequest(DaraModel):
    def __init__(
        self,
        add_account: List[int] = None,
        biz_type: int = None,
        image_id: str = None,
        product_type: str = None,
        remove_account: List[int] = None,
    ):
        self.add_account = add_account
        self.biz_type = biz_type
        self.image_id = image_id
        self.product_type = product_type
        self.remove_account = remove_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_account is not None:
            result['AddAccount'] = self.add_account

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.remove_account is not None:
            result['RemoveAccount'] = self.remove_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddAccount') is not None:
            self.add_account = m.get('AddAccount')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RemoveAccount') is not None:
            self.remove_account = m.get('RemoveAccount')

        return self

