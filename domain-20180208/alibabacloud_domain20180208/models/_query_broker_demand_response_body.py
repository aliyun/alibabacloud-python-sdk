# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class QueryBrokerDemandResponseBody(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[main_models.QueryBrokerDemandResponseBodyData] = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryBrokerDemandResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class QueryBrokerDemandResponseBodyData(DaraModel):
    def __init__(
        self,
        audit_status: int = None,
        bargain_seller_mobile: str = None,
        bargain_seller_price: float = None,
        biz_id: str = None,
        demand_domain: str = None,
        demand_price: float = None,
        description: str = None,
        email: str = None,
        mobile: str = None,
        order_type: int = None,
        partner_domain: str = None,
        pay_domain: str = None,
        pay_price: float = None,
        pay_time: int = None,
        produce_type: int = None,
        publish_time: int = None,
        purchase_status: int = None,
        service_pay_price: float = None,
        settle_base_price: float = None,
        status: str = None,
    ):
        self.audit_status = audit_status
        self.bargain_seller_mobile = bargain_seller_mobile
        self.bargain_seller_price = bargain_seller_price
        self.biz_id = biz_id
        self.demand_domain = demand_domain
        self.demand_price = demand_price
        self.description = description
        self.email = email
        self.mobile = mobile
        self.order_type = order_type
        self.partner_domain = partner_domain
        self.pay_domain = pay_domain
        self.pay_price = pay_price
        self.pay_time = pay_time
        self.produce_type = produce_type
        self.publish_time = publish_time
        self.purchase_status = purchase_status
        self.service_pay_price = service_pay_price
        self.settle_base_price = settle_base_price
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.bargain_seller_mobile is not None:
            result['BargainSellerMobile'] = self.bargain_seller_mobile

        if self.bargain_seller_price is not None:
            result['BargainSellerPrice'] = self.bargain_seller_price

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.demand_domain is not None:
            result['DemandDomain'] = self.demand_domain

        if self.demand_price is not None:
            result['DemandPrice'] = self.demand_price

        if self.description is not None:
            result['Description'] = self.description

        if self.email is not None:
            result['Email'] = self.email

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.partner_domain is not None:
            result['PartnerDomain'] = self.partner_domain

        if self.pay_domain is not None:
            result['PayDomain'] = self.pay_domain

        if self.pay_price is not None:
            result['PayPrice'] = self.pay_price

        if self.pay_time is not None:
            result['PayTime'] = self.pay_time

        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.purchase_status is not None:
            result['PurchaseStatus'] = self.purchase_status

        if self.service_pay_price is not None:
            result['ServicePayPrice'] = self.service_pay_price

        if self.settle_base_price is not None:
            result['SettleBasePrice'] = self.settle_base_price

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('BargainSellerMobile') is not None:
            self.bargain_seller_mobile = m.get('BargainSellerMobile')

        if m.get('BargainSellerPrice') is not None:
            self.bargain_seller_price = m.get('BargainSellerPrice')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DemandDomain') is not None:
            self.demand_domain = m.get('DemandDomain')

        if m.get('DemandPrice') is not None:
            self.demand_price = m.get('DemandPrice')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PartnerDomain') is not None:
            self.partner_domain = m.get('PartnerDomain')

        if m.get('PayDomain') is not None:
            self.pay_domain = m.get('PayDomain')

        if m.get('PayPrice') is not None:
            self.pay_price = m.get('PayPrice')

        if m.get('PayTime') is not None:
            self.pay_time = m.get('PayTime')

        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('PurchaseStatus') is not None:
            self.purchase_status = m.get('PurchaseStatus')

        if m.get('ServicePayPrice') is not None:
            self.service_pay_price = m.get('ServicePayPrice')

        if m.get('SettleBasePrice') is not None:
            self.settle_base_price = m.get('SettleBasePrice')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

