# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class CssInstanceCommodity(DaraModel):
    def __init__(
        self,
        activity_id: int = None,
        aliyun_produce_code: str = None,
        charge_type: str = None,
        commodity_code: str = None,
        components: List[main_models.CssInstanceComponent] = None,
        duration: int = None,
        instance_id: str = None,
        is_free: bool = None,
        is_pre_pay_post_charge: bool = None,
        is_renew_change: bool = None,
        is_sync_to_subscription: bool = None,
        order_params: Dict[str, str] = None,
        order_type: str = None,
        plan_item_id: int = None,
        pricing_cycle: str = None,
        quantity: int = None,
        redeem_no_list: List[str] = None,
        redeem_order_type: str = None,
        refund_spec_code: str = None,
        spec_code: str = None,
        spec_upgrade_origin_spec_codes: List[str] = None,
        specify_start_date: int = None,
        upgrade_inquire_financial_value: bool = None,
    ):
        self.activity_id = activity_id
        self.aliyun_produce_code = aliyun_produce_code
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.components = components
        self.duration = duration
        self.instance_id = instance_id
        self.is_free = is_free
        self.is_pre_pay_post_charge = is_pre_pay_post_charge
        self.is_renew_change = is_renew_change
        self.is_sync_to_subscription = is_sync_to_subscription
        self.order_params = order_params
        self.order_type = order_type
        self.plan_item_id = plan_item_id
        self.pricing_cycle = pricing_cycle
        self.quantity = quantity
        self.redeem_no_list = redeem_no_list
        self.redeem_order_type = redeem_order_type
        self.refund_spec_code = refund_spec_code
        self.spec_code = spec_code
        self.spec_upgrade_origin_spec_codes = spec_upgrade_origin_spec_codes
        self.specify_start_date = specify_start_date
        self.upgrade_inquire_financial_value = upgrade_inquire_financial_value

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['activityId'] = self.activity_id

        if self.aliyun_produce_code is not None:
            result['aliyunProduceCode'] = self.aliyun_produce_code

        if self.charge_type is not None:
            result['chargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code

        result['components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['components'].append(k1.to_map() if k1 else None)

        if self.duration is not None:
            result['duration'] = self.duration

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.is_free is not None:
            result['isFree'] = self.is_free

        if self.is_pre_pay_post_charge is not None:
            result['isPrePayPostCharge'] = self.is_pre_pay_post_charge

        if self.is_renew_change is not None:
            result['isRenewChange'] = self.is_renew_change

        if self.is_sync_to_subscription is not None:
            result['isSyncToSubscription'] = self.is_sync_to_subscription

        if self.order_params is not None:
            result['orderParams'] = self.order_params

        if self.order_type is not None:
            result['orderType'] = self.order_type

        if self.plan_item_id is not None:
            result['planItemId'] = self.plan_item_id

        if self.pricing_cycle is not None:
            result['pricingCycle'] = self.pricing_cycle

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.redeem_no_list is not None:
            result['redeemNoList'] = self.redeem_no_list

        if self.redeem_order_type is not None:
            result['redeemOrderType'] = self.redeem_order_type

        if self.refund_spec_code is not None:
            result['refundSpecCode'] = self.refund_spec_code

        if self.spec_code is not None:
            result['specCode'] = self.spec_code

        if self.spec_upgrade_origin_spec_codes is not None:
            result['specUpgradeOriginSpecCodes'] = self.spec_upgrade_origin_spec_codes

        if self.specify_start_date is not None:
            result['specifyStartDate'] = self.specify_start_date

        if self.upgrade_inquire_financial_value is not None:
            result['upgradeInquireFinancialValue'] = self.upgrade_inquire_financial_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activityId') is not None:
            self.activity_id = m.get('activityId')

        if m.get('aliyunProduceCode') is not None:
            self.aliyun_produce_code = m.get('aliyunProduceCode')

        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')

        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')

        self.components = []
        if m.get('components') is not None:
            for k1 in m.get('components'):
                temp_model = main_models.CssInstanceComponent()
                self.components.append(temp_model.from_map(k1))

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('isFree') is not None:
            self.is_free = m.get('isFree')

        if m.get('isPrePayPostCharge') is not None:
            self.is_pre_pay_post_charge = m.get('isPrePayPostCharge')

        if m.get('isRenewChange') is not None:
            self.is_renew_change = m.get('isRenewChange')

        if m.get('isSyncToSubscription') is not None:
            self.is_sync_to_subscription = m.get('isSyncToSubscription')

        if m.get('orderParams') is not None:
            self.order_params = m.get('orderParams')

        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')

        if m.get('planItemId') is not None:
            self.plan_item_id = m.get('planItemId')

        if m.get('pricingCycle') is not None:
            self.pricing_cycle = m.get('pricingCycle')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('redeemNoList') is not None:
            self.redeem_no_list = m.get('redeemNoList')

        if m.get('redeemOrderType') is not None:
            self.redeem_order_type = m.get('redeemOrderType')

        if m.get('refundSpecCode') is not None:
            self.refund_spec_code = m.get('refundSpecCode')

        if m.get('specCode') is not None:
            self.spec_code = m.get('specCode')

        if m.get('specUpgradeOriginSpecCodes') is not None:
            self.spec_upgrade_origin_spec_codes = m.get('specUpgradeOriginSpecCodes')

        if m.get('specifyStartDate') is not None:
            self.specify_start_date = m.get('specifyStartDate')

        if m.get('upgradeInquireFinancialValue') is not None:
            self.upgrade_inquire_financial_value = m.get('upgradeInquireFinancialValue')

        return self

