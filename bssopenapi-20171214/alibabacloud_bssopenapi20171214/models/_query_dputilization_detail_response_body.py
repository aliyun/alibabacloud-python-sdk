# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryDPUtilizationDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryDPUtilizationDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
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
            temp_model = main_models.QueryDPUtilizationDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryDPUtilizationDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        detail_list: main_models.QueryDPUtilizationDetailResponseBodyDataDetailList = None,
        next_token: str = None,
    ):
        # The detailed resource plan usage.
        self.detail_list = detail_list
        # The token that is used to retrieve the next page of results. You can set the LastToken parameter to this value in the next request. If null is returned, all results are queried.
        self.next_token = next_token

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

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailList') is not None:
            temp_model = main_models.QueryDPUtilizationDetailResponseBodyDataDetailList()
            self.detail_list = temp_model.from_map(m.get('DetailList'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class QueryDPUtilizationDetailResponseBodyDataDetailList(DaraModel):
    def __init__(
        self,
        detail_list: List[main_models.QueryDPUtilizationDetailResponseBodyDataDetailListDetailList] = None,
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
                temp_model = main_models.QueryDPUtilizationDetailResponseBodyDataDetailListDetailList()
                self.detail_list.append(temp_model.from_map(k1))

        return self

class QueryDPUtilizationDetailResponseBodyDataDetailListDetailList(DaraModel):
    def __init__(
        self,
        deduct_date: str = None,
        deduct_factor_total: float = None,
        deduct_hours: float = None,
        deduct_measure: float = None,
        deduct_quantity: float = None,
        deducted_commodity_code: str = None,
        deducted_instance_id: str = None,
        deducted_product_detail: str = None,
        instance_id: str = None,
        instance_spec: str = None,
        region: str = None,
        res_code: str = None,
        share_uid: int = None,
        uid: int = None,
    ):
        # The deduction date.
        self.deduct_date = deduct_date
        # The total computing capacity or storage capacity of the RI or SCU during the deduction.
        self.deduct_factor_total = deduct_factor_total
        # The deduct factor. This parameter is returned only if the CommodityCode parameter is set to ecsRi.
        self.deduct_hours = deduct_hours
        # The original measured amount.
        self.deduct_measure = deduct_measure
        # The computing capacity or storage capacity that is deducted in a pay-as-you-go instance.
        self.deduct_quantity = deduct_quantity
        # The code of the deducted service.
        self.deducted_commodity_code = deducted_commodity_code
        # The ID of the deducted instance.
        self.deducted_instance_id = deducted_instance_id
        # The name of the deducted service.
        self.deducted_product_detail = deducted_product_detail
        # The ID of the RI.
        self.instance_id = instance_id
        # The instance type of the deducted instance.
        self.instance_spec = instance_spec
        # The region in which the instance resides. This parameter can be left empty.
        self.region = region
        # The billable item.
        self.res_code = res_code
        # The UID of the deducted instance.
        # 
        # *   If the deduction is shared, the value of this parameter indicates the UID of the deducted instance.
        # *   If the deduction is not shared, the value of this parameter is the same as that of the uid parameter.
        self.share_uid = share_uid
        # The UID of the deducted instance.
        self.uid = uid

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

        if self.deduct_measure is not None:
            result['DeductMeasure'] = self.deduct_measure

        if self.deduct_quantity is not None:
            result['DeductQuantity'] = self.deduct_quantity

        if self.deducted_commodity_code is not None:
            result['DeductedCommodityCode'] = self.deducted_commodity_code

        if self.deducted_instance_id is not None:
            result['DeductedInstanceId'] = self.deducted_instance_id

        if self.deducted_product_detail is not None:
            result['DeductedProductDetail'] = self.deducted_product_detail

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.region is not None:
            result['Region'] = self.region

        if self.res_code is not None:
            result['ResCode'] = self.res_code

        if self.share_uid is not None:
            result['ShareUid'] = self.share_uid

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeductDate') is not None:
            self.deduct_date = m.get('DeductDate')

        if m.get('DeductFactorTotal') is not None:
            self.deduct_factor_total = m.get('DeductFactorTotal')

        if m.get('DeductHours') is not None:
            self.deduct_hours = m.get('DeductHours')

        if m.get('DeductMeasure') is not None:
            self.deduct_measure = m.get('DeductMeasure')

        if m.get('DeductQuantity') is not None:
            self.deduct_quantity = m.get('DeductQuantity')

        if m.get('DeductedCommodityCode') is not None:
            self.deducted_commodity_code = m.get('DeductedCommodityCode')

        if m.get('DeductedInstanceId') is not None:
            self.deducted_instance_id = m.get('DeductedInstanceId')

        if m.get('DeductedProductDetail') is not None:
            self.deducted_product_detail = m.get('DeductedProductDetail')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResCode') is not None:
            self.res_code = m.get('ResCode')

        if m.get('ShareUid') is not None:
            self.share_uid = m.get('ShareUid')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

