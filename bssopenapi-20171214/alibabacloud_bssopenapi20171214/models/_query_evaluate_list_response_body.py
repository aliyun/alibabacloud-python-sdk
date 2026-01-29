# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryEvaluateListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryEvaluateListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = main_models.QueryEvaluateListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryEvaluateListResponseBodyData(DaraModel):
    def __init__(
        self,
        evaluate_list: main_models.QueryEvaluateListResponseBodyDataEvaluateList = None,
        host_id: str = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
        total_invoice_amount: int = None,
        total_un_applied_invoice_amount: int = None,
    ):
        # The data returned.
        self.evaluate_list = evaluate_list
        # The ID of the host.
        self.host_id = host_id
        # The number of the page returned.
        self.page_num = page_num
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of returned entries.
        self.total_count = total_count
        # The invoiced amount that meets the query conditions. Unit: Cent.
        self.total_invoice_amount = total_invoice_amount
        # The invoiceable amount that meets the query conditions. Unit: Cent.
        self.total_un_applied_invoice_amount = total_un_applied_invoice_amount

    def validate(self):
        if self.evaluate_list:
            self.evaluate_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.evaluate_list is not None:
            result['EvaluateList'] = self.evaluate_list.to_map()

        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_invoice_amount is not None:
            result['TotalInvoiceAmount'] = self.total_invoice_amount

        if self.total_un_applied_invoice_amount is not None:
            result['TotalUnAppliedInvoiceAmount'] = self.total_un_applied_invoice_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluateList') is not None:
            temp_model = main_models.QueryEvaluateListResponseBodyDataEvaluateList()
            self.evaluate_list = temp_model.from_map(m.get('EvaluateList'))

        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalInvoiceAmount') is not None:
            self.total_invoice_amount = m.get('TotalInvoiceAmount')

        if m.get('TotalUnAppliedInvoiceAmount') is not None:
            self.total_un_applied_invoice_amount = m.get('TotalUnAppliedInvoiceAmount')

        return self

class QueryEvaluateListResponseBodyDataEvaluateList(DaraModel):
    def __init__(
        self,
        evaluate: List[main_models.QueryEvaluateListResponseBodyDataEvaluateListEvaluate] = None,
    ):
        self.evaluate = evaluate

    def validate(self):
        if self.evaluate:
            for v1 in self.evaluate:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Evaluate'] = []
        if self.evaluate is not None:
            for k1 in self.evaluate:
                result['Evaluate'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.evaluate = []
        if m.get('Evaluate') is not None:
            for k1 in m.get('Evaluate'):
                temp_model = main_models.QueryEvaluateListResponseBodyDataEvaluateListEvaluate()
                self.evaluate.append(temp_model.from_map(k1))

        return self

class QueryEvaluateListResponseBodyDataEvaluateListEvaluate(DaraModel):
    def __init__(
        self,
        bill_cycle: str = None,
        bill_id: int = None,
        biz_time: str = None,
        biz_type: str = None,
        can_invoice_amount: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        invoiced_amount: int = None,
        item_id: int = None,
        name: str = None,
        offset_accept_amount: int = None,
        offset_cost_amount: int = None,
        op_id: str = None,
        original_amount: int = None,
        out_biz_id: str = None,
        present_amount: int = None,
        status: int = None,
        type: int = None,
        user_id: int = None,
        user_nick: str = None,
    ):
        # The billing cycle.
        self.bill_cycle = bill_cycle
        # The ID of the bill.
        self.bill_id = bill_id
        # The time.
        self.biz_time = biz_time
        # The market type in the invoice. Valid values:
        # 
        # *   ALIYUN: Alibaba Cloud
        # *   MARKETPLACE: Alibaba Cloud Marketplace
        self.biz_type = biz_type
        # The invoiceable amount.
        self.can_invoice_amount = can_invoice_amount
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The ID of the invoice.
        self.id = id
        # The invoiced amount.
        self.invoiced_amount = invoiced_amount
        # The ID of the item.
        self.item_id = item_id
        # The name of the object to be invoiced.
        self.name = name
        # If a refund is issued due to an order such as an unsubscription order or a configuration downgrade order, the refund amount is used to offset the amount of the invoice. The value is consistent with the value of the **OffsetCostAmount** parameter.
        self.offset_accept_amount = offset_accept_amount
        # The refund amount used to offset the amount of the invoice. If a refund is issued due to an order such as an unsubscription order or a configuration downgrade order, the refund amount is used to offset the amount of the invoice. The value is consistent with the value of the **OffsetAcceptAmount** parameter.
        self.offset_cost_amount = offset_cost_amount
        # The ID of the external object.
        self.op_id = op_id
        # The original amount.
        self.original_amount = original_amount
        # The ID of the external order.
        self.out_biz_id = out_biz_id
        # The balance.
        self.present_amount = present_amount
        # The status of the invoiceable amount.
        self.status = status
        # The type of orders that are queried. Valid values:
        # 
        # *   1: the orders in which the invoiceable amount is negative.
        # *   2: the orders in which the invoiceable amount is positive.
        # *   3: the orders in which the invoiceable amount is not 0.
        # *   4: the orders in which the amount that has been invoiced is greater than 0.
        # 
        # >  By default, this parameter is left empty. If this parameter is left empty, all orders are queried.
        self.type = type
        # The ID of the user.
        self.user_id = user_id
        # The nickname of the user.
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_cycle is not None:
            result['BillCycle'] = self.bill_cycle

        if self.bill_id is not None:
            result['BillId'] = self.bill_id

        if self.biz_time is not None:
            result['BizTime'] = self.biz_time

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.can_invoice_amount is not None:
            result['CanInvoiceAmount'] = self.can_invoice_amount

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.invoiced_amount is not None:
            result['InvoicedAmount'] = self.invoiced_amount

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.name is not None:
            result['Name'] = self.name

        if self.offset_accept_amount is not None:
            result['OffsetAcceptAmount'] = self.offset_accept_amount

        if self.offset_cost_amount is not None:
            result['OffsetCostAmount'] = self.offset_cost_amount

        if self.op_id is not None:
            result['OpId'] = self.op_id

        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount

        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id

        if self.present_amount is not None:
            result['PresentAmount'] = self.present_amount

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_nick is not None:
            result['UserNick'] = self.user_nick

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillCycle') is not None:
            self.bill_cycle = m.get('BillCycle')

        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')

        if m.get('BizTime') is not None:
            self.biz_time = m.get('BizTime')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CanInvoiceAmount') is not None:
            self.can_invoice_amount = m.get('CanInvoiceAmount')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InvoicedAmount') is not None:
            self.invoiced_amount = m.get('InvoicedAmount')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OffsetAcceptAmount') is not None:
            self.offset_accept_amount = m.get('OffsetAcceptAmount')

        if m.get('OffsetCostAmount') is not None:
            self.offset_cost_amount = m.get('OffsetCostAmount')

        if m.get('OpId') is not None:
            self.op_id = m.get('OpId')

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')

        if m.get('PresentAmount') is not None:
            self.present_amount = m.get('PresentAmount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')

        return self

