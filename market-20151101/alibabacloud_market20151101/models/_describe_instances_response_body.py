# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_market20151101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instance_items: main_models.DescribeInstancesResponseBodyInstanceItems = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instance_items = instance_items
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.instance_items:
            self.instance_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_items is not None:
            result['InstanceItems'] = self.instance_items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceItems') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstanceItems()
            self.instance_items = temp_model.from_map(m.get('InstanceItems'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstancesResponseBodyInstanceItems(DaraModel):
    def __init__(
        self,
        instance_item: List[main_models.DescribeInstancesResponseBodyInstanceItemsInstanceItem] = None,
    ):
        self.instance_item = instance_item

    def validate(self):
        if self.instance_item:
            for v1 in self.instance_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceItem'] = []
        if self.instance_item is not None:
            for k1 in self.instance_item:
                result['InstanceItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_item = []
        if m.get('InstanceItem') is not None:
            for k1 in m.get('InstanceItem'):
                temp_model = main_models.DescribeInstancesResponseBodyInstanceItemsInstanceItem()
                self.instance_item.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstanceItemsInstanceItem(DaraModel):
    def __init__(
        self,
        api_json: str = None,
        app_json: str = None,
        began_on: int = None,
        created_on: int = None,
        end_on: int = None,
        extend_json: str = None,
        host_json: str = None,
        idaas_json: str = None,
        image_json: str = None,
        instance_id: int = None,
        order_id: int = None,
        product_code: str = None,
        product_name: str = None,
        product_sku_code: str = None,
        product_type: str = None,
        status: str = None,
        supplier_name: str = None,
    ):
        self.api_json = api_json
        self.app_json = app_json
        self.began_on = began_on
        self.created_on = created_on
        self.end_on = end_on
        self.extend_json = extend_json
        self.host_json = host_json
        self.idaas_json = idaas_json
        self.image_json = image_json
        self.instance_id = instance_id
        self.order_id = order_id
        self.product_code = product_code
        self.product_name = product_name
        self.product_sku_code = product_sku_code
        self.product_type = product_type
        self.status = status
        self.supplier_name = supplier_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_json is not None:
            result['ApiJson'] = self.api_json

        if self.app_json is not None:
            result['AppJson'] = self.app_json

        if self.began_on is not None:
            result['BeganOn'] = self.began_on

        if self.created_on is not None:
            result['CreatedOn'] = self.created_on

        if self.end_on is not None:
            result['EndOn'] = self.end_on

        if self.extend_json is not None:
            result['ExtendJson'] = self.extend_json

        if self.host_json is not None:
            result['HostJson'] = self.host_json

        if self.idaas_json is not None:
            result['IdaasJson'] = self.idaas_json

        if self.image_json is not None:
            result['ImageJson'] = self.image_json

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_sku_code is not None:
            result['ProductSkuCode'] = self.product_sku_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.status is not None:
            result['Status'] = self.status

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiJson') is not None:
            self.api_json = m.get('ApiJson')

        if m.get('AppJson') is not None:
            self.app_json = m.get('AppJson')

        if m.get('BeganOn') is not None:
            self.began_on = m.get('BeganOn')

        if m.get('CreatedOn') is not None:
            self.created_on = m.get('CreatedOn')

        if m.get('EndOn') is not None:
            self.end_on = m.get('EndOn')

        if m.get('ExtendJson') is not None:
            self.extend_json = m.get('ExtendJson')

        if m.get('HostJson') is not None:
            self.host_json = m.get('HostJson')

        if m.get('IdaasJson') is not None:
            self.idaas_json = m.get('IdaasJson')

        if m.get('ImageJson') is not None:
            self.image_json = m.get('ImageJson')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductSkuCode') is not None:
            self.product_sku_code = m.get('ProductSkuCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        return self

