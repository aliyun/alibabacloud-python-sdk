# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListProductsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        products: List[main_models.ListProductsResponseBodyProducts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.products = products
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.products:
            for v1 in self.products:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Products'] = []
        if self.products is not None:
            for k1 in self.products:
                result['Products'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.products = []
        if m.get('Products') is not None:
            for k1 in m.get('Products'):
                temp_model = main_models.ListProductsResponseBodyProducts()
                self.products.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProductsResponseBodyProducts(DaraModel):
    def __init__(
        self,
        abnormal_data_ingestion_count: int = None,
        active_time: int = None,
        allow_add_data_ingestion: bool = None,
        create_time: int = None,
        data_ingestion_status: bool = None,
        enabled_data_ingestion_count: int = None,
        product_alias: str = None,
        product_id: str = None,
        product_name: str = None,
        product_type: str = None,
        total_data_ingestion_count: int = None,
        update_time: int = None,
        vendor_id: str = None,
        vendor_name: str = None,
    ):
        self.abnormal_data_ingestion_count = abnormal_data_ingestion_count
        self.active_time = active_time
        self.allow_add_data_ingestion = allow_add_data_ingestion
        self.create_time = create_time
        self.data_ingestion_status = data_ingestion_status
        self.enabled_data_ingestion_count = enabled_data_ingestion_count
        self.product_alias = product_alias
        self.product_id = product_id
        self.product_name = product_name
        self.product_type = product_type
        self.total_data_ingestion_count = total_data_ingestion_count
        self.update_time = update_time
        self.vendor_id = vendor_id
        self.vendor_name = vendor_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormal_data_ingestion_count is not None:
            result['AbnormalDataIngestionCount'] = self.abnormal_data_ingestion_count

        if self.active_time is not None:
            result['ActiveTime'] = self.active_time

        if self.allow_add_data_ingestion is not None:
            result['AllowAddDataIngestion'] = self.allow_add_data_ingestion

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_ingestion_status is not None:
            result['DataIngestionStatus'] = self.data_ingestion_status

        if self.enabled_data_ingestion_count is not None:
            result['EnabledDataIngestionCount'] = self.enabled_data_ingestion_count

        if self.product_alias is not None:
            result['ProductAlias'] = self.product_alias

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.total_data_ingestion_count is not None:
            result['TotalDataIngestionCount'] = self.total_data_ingestion_count

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id

        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalDataIngestionCount') is not None:
            self.abnormal_data_ingestion_count = m.get('AbnormalDataIngestionCount')

        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')

        if m.get('AllowAddDataIngestion') is not None:
            self.allow_add_data_ingestion = m.get('AllowAddDataIngestion')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataIngestionStatus') is not None:
            self.data_ingestion_status = m.get('DataIngestionStatus')

        if m.get('EnabledDataIngestionCount') is not None:
            self.enabled_data_ingestion_count = m.get('EnabledDataIngestionCount')

        if m.get('ProductAlias') is not None:
            self.product_alias = m.get('ProductAlias')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('TotalDataIngestionCount') is not None:
            self.total_data_ingestion_count = m.get('TotalDataIngestionCount')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')

        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')

        return self

