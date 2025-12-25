# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceAttributeRequest(DaraModel):
    def __init__(
        self,
        attribute_type: str = None,
        attribute_value: str = None,
        dbinstance_id: str = None,
        product: str = None,
        region_id: str = None,
    ):
        # The configuration that you want to modify.
        # 
        # *   MaintainTime: the O\\&M time
        # *   DBInstanceDescription: the cluster name
        # 
        # This parameter is required.
        self.attribute_type = attribute_type
        # The new value of the configuration.
        # 
        # This parameter is required.
        self.attribute_value = attribute_value
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The code of the cloud service.
        self.product = product
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_type is not None:
            result['AttributeType'] = self.attribute_type

        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.product is not None:
            result['Product'] = self.product

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeType') is not None:
            self.attribute_type = m.get('AttributeType')

        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

