# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeSafDeOrderResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeSafDeOrderResponseBodyResultObject = None,
    ):
        # Request ID
        self.request_id = request_id
        # Return object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeSafDeOrderResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeSafDeOrderResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        expiration_date: int = None,
        open_user_type: int = None,
        regions: List[main_models.DescribeSafDeOrderResponseBodyResultObjectRegions] = None,
    ):
        # Expiration time
        self.expiration_date = expiration_date
        # Based on the product type subscribed by the customer, the console permissions are divided into three categories:
        # 
        #      1. New Customer: Has not purchased/subscribed to any service.
        #      2. Old Customer (Subscription): Customers who have purchased the SAF product.
        #      3. Pay-As-You-Go: Customers who have purchased the SAF_BAG product or activated SAF_POS.
        self.open_user_type = open_user_type
        # Activated region permission addresses.
        self.regions = regions

    def validate(self):
        if self.regions:
            for v1 in self.regions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expiration_date is not None:
            result['expirationDate'] = self.expiration_date

        if self.open_user_type is not None:
            result['openUserType'] = self.open_user_type

        result['regions'] = []
        if self.regions is not None:
            for k1 in self.regions:
                result['regions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expirationDate') is not None:
            self.expiration_date = m.get('expirationDate')

        if m.get('openUserType') is not None:
            self.open_user_type = m.get('openUserType')

        self.regions = []
        if m.get('regions') is not None:
            for k1 in m.get('regions'):
                temp_model = main_models.DescribeSafDeOrderResponseBodyResultObjectRegions()
                self.regions.append(temp_model.from_map(k1))

        return self

class DescribeSafDeOrderResponseBodyResultObjectRegions(DaraModel):
    def __init__(
        self,
        expiration_date: int = None,
        region: str = None,
        specification: int = None,
    ):
        # Expiration date (timestamp).
        self.expiration_date = expiration_date
        # Region ID.
        self.region = region
        # Specification model:
        # 
        # 1: Basic Edition 
        # 2: Advanced Edition 
        # 3: Premium Edition 
        # 4: Flagship Edition
        self.specification = specification

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expiration_date is not None:
            result['expirationDate'] = self.expiration_date

        if self.region is not None:
            result['region'] = self.region

        if self.specification is not None:
            result['specification'] = self.specification

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expirationDate') is not None:
            self.expiration_date = m.get('expirationDate')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('specification') is not None:
            self.specification = m.get('specification')

        return self

