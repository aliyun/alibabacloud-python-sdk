# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnvInfoDO(DaraModel):
    def __init__(
        self,
        env: str = None,
        env_type: str = None,
        org_type: str = None,
        product_id: int = None,
        product_name: str = None,
        region: str = None,
    ):
        self.env = env
        self.env_type = env_type
        self.org_type = org_type
        self.product_id = product_id
        self.product_name = product_name
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['env'] = self.env

        if self.env_type is not None:
            result['envType'] = self.env_type

        if self.org_type is not None:
            result['orgType'] = self.org_type

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.product_name is not None:
            result['productName'] = self.product_name

        if self.region is not None:
            result['region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('envType') is not None:
            self.env_type = m.get('envType')

        if m.get('orgType') is not None:
            self.org_type = m.get('orgType')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        if m.get('region') is not None:
            self.region = m.get('region')

        return self

