# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryRIUtilizationDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryRIUtilizationDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryRIUtilizationDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryRIUtilizationDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        detail_list: main_models.QueryRIUtilizationDetailResponseBodyDataDetailList = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.detail_list = detail_list
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.detail_list:
            self.detail_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail_list is not None:
            result['DetailList'] = self.detail_list.to_map()

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailList') is not None:
            temp_model = main_models.QueryRIUtilizationDetailResponseBodyDataDetailList()
            self.detail_list = temp_model.from_map(m.get('DetailList'))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryRIUtilizationDetailResponseBodyDataDetailList(DaraModel):
    def __init__(
        self,
        detail_list: List[main_models.QueryRIUtilizationDetailResponseBodyDataDetailListDetailList] = None,
    ):
        self.detail_list = detail_list

    def validate(self):
        if self.detail_list:
            for v1 in self.detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DetailList'] = []
        if self.detail_list is not None:
            for k1 in self.detail_list:
                result['DetailList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_list = []
        if m.get('DetailList') is not None:
            for k1 in m.get('DetailList'):
                temp_model = main_models.QueryRIUtilizationDetailResponseBodyDataDetailListDetailList()
                self.detail_list.append(temp_model.from_map(k1))

        return self

class QueryRIUtilizationDetailResponseBodyDataDetailListDetailList(DaraModel):
    def __init__(
        self,
        deduct_date: str = None,
        deduct_factor_total: float = None,
        deduct_hours: str = None,
        deduct_quantity: float = None,
        deducted_commodity_code: str = None,
        deducted_instance_id: str = None,
        deducted_product_detail: str = None,
        instance_spec: str = None,
        riinstance_id: str = None,
    ):
        self.deduct_date = deduct_date
        self.deduct_factor_total = deduct_factor_total
        self.deduct_hours = deduct_hours
        self.deduct_quantity = deduct_quantity
        self.deducted_commodity_code = deducted_commodity_code
        self.deducted_instance_id = deducted_instance_id
        self.deducted_product_detail = deducted_product_detail
        self.instance_spec = instance_spec
        self.riinstance_id = riinstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deduct_date is not None:
            result['DeductDate'] = self.deduct_date

        if self.deduct_factor_total is not None:
            result['DeductFactorTotal'] = self.deduct_factor_total

        if self.deduct_hours is not None:
            result['DeductHours'] = self.deduct_hours

        if self.deduct_quantity is not None:
            result['DeductQuantity'] = self.deduct_quantity

        if self.deducted_commodity_code is not None:
            result['DeductedCommodityCode'] = self.deducted_commodity_code

        if self.deducted_instance_id is not None:
            result['DeductedInstanceId'] = self.deducted_instance_id

        if self.deducted_product_detail is not None:
            result['DeductedProductDetail'] = self.deducted_product_detail

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.riinstance_id is not None:
            result['RIInstanceId'] = self.riinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeductDate') is not None:
            self.deduct_date = m.get('DeductDate')

        if m.get('DeductFactorTotal') is not None:
            self.deduct_factor_total = m.get('DeductFactorTotal')

        if m.get('DeductHours') is not None:
            self.deduct_hours = m.get('DeductHours')

        if m.get('DeductQuantity') is not None:
            self.deduct_quantity = m.get('DeductQuantity')

        if m.get('DeductedCommodityCode') is not None:
            self.deducted_commodity_code = m.get('DeductedCommodityCode')

        if m.get('DeductedInstanceId') is not None:
            self.deducted_instance_id = m.get('DeductedInstanceId')

        if m.get('DeductedProductDetail') is not None:
            self.deducted_product_detail = m.get('DeductedProductDetail')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('RIInstanceId') is not None:
            self.riinstance_id = m.get('RIInstanceId')

        return self

