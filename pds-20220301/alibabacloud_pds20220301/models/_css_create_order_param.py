# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class CssCreateOrderParam(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        auto_pay: bool = None,
        auto_use_coupon: bool = None,
        bid: str = None,
        buyer_id: int = None,
        certificate: str = None,
        child_id: int = None,
        cilent_ip: str = None,
        commodities: List[main_models.CssInstanceCommodity] = None,
        creater_nick: str = None,
        css_auth_request_param: Any = None,
        from_app: str = None,
        language: str = None,
        market_type: int = None,
        memo: str = None,
        order_origin: str = None,
        order_params: Dict[str, str] = None,
        payer_id: int = None,
        plan_group_id: int = None,
        plan_id: int = None,
        plan_instance_id: str = None,
        promotion_code: str = None,
        promotion_input_param: Any = None,
        request_id: str = None,
        skip_channel: bool = None,
        token: str = None,
        transient_access: Any = None,
        umid_token: str = None,
        user_id: int = None,
    ):
        self.agent_id = agent_id
        self.auto_pay = auto_pay
        self.auto_use_coupon = auto_use_coupon
        self.bid = bid
        self.buyer_id = buyer_id
        self.certificate = certificate
        self.child_id = child_id
        self.cilent_ip = cilent_ip
        self.commodities = commodities
        self.creater_nick = creater_nick
        self.css_auth_request_param = css_auth_request_param
        self.from_app = from_app
        self.language = language
        self.market_type = market_type
        self.memo = memo
        self.order_origin = order_origin
        self.order_params = order_params
        self.payer_id = payer_id
        self.plan_group_id = plan_group_id
        self.plan_id = plan_id
        self.plan_instance_id = plan_instance_id
        self.promotion_code = promotion_code
        self.promotion_input_param = promotion_input_param
        self.request_id = request_id
        self.skip_channel = skip_channel
        self.token = token
        self.transient_access = transient_access
        self.umid_token = umid_token
        self.user_id = user_id

    def validate(self):
        if self.commodities:
            for v1 in self.commodities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.auto_pay is not None:
            result['autoPay'] = self.auto_pay

        if self.auto_use_coupon is not None:
            result['autoUseCoupon'] = self.auto_use_coupon

        if self.bid is not None:
            result['bid'] = self.bid

        if self.buyer_id is not None:
            result['buyerId'] = self.buyer_id

        if self.certificate is not None:
            result['certificate'] = self.certificate

        if self.child_id is not None:
            result['childId'] = self.child_id

        if self.cilent_ip is not None:
            result['cilentIp'] = self.cilent_ip

        result['commodities'] = []
        if self.commodities is not None:
            for k1 in self.commodities:
                result['commodities'].append(k1.to_map() if k1 else None)

        if self.creater_nick is not None:
            result['createrNick'] = self.creater_nick

        if self.css_auth_request_param is not None:
            result['cssAuthRequestParam'] = self.css_auth_request_param

        if self.from_app is not None:
            result['fromApp'] = self.from_app

        if self.language is not None:
            result['language'] = self.language

        if self.market_type is not None:
            result['marketType'] = self.market_type

        if self.memo is not None:
            result['memo'] = self.memo

        if self.order_origin is not None:
            result['orderOrigin'] = self.order_origin

        if self.order_params is not None:
            result['orderParams'] = self.order_params

        if self.payer_id is not None:
            result['payerId'] = self.payer_id

        if self.plan_group_id is not None:
            result['planGroupId'] = self.plan_group_id

        if self.plan_id is not None:
            result['planId'] = self.plan_id

        if self.plan_instance_id is not None:
            result['planInstanceId'] = self.plan_instance_id

        if self.promotion_code is not None:
            result['promotionCode'] = self.promotion_code

        if self.promotion_input_param is not None:
            result['promotionInputParam'] = self.promotion_input_param

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.skip_channel is not None:
            result['skipChannel'] = self.skip_channel

        if self.token is not None:
            result['token'] = self.token

        if self.transient_access is not None:
            result['transientAccess'] = self.transient_access

        if self.umid_token is not None:
            result['umidToken'] = self.umid_token

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('autoPay') is not None:
            self.auto_pay = m.get('autoPay')

        if m.get('autoUseCoupon') is not None:
            self.auto_use_coupon = m.get('autoUseCoupon')

        if m.get('bid') is not None:
            self.bid = m.get('bid')

        if m.get('buyerId') is not None:
            self.buyer_id = m.get('buyerId')

        if m.get('certificate') is not None:
            self.certificate = m.get('certificate')

        if m.get('childId') is not None:
            self.child_id = m.get('childId')

        if m.get('cilentIp') is not None:
            self.cilent_ip = m.get('cilentIp')

        self.commodities = []
        if m.get('commodities') is not None:
            for k1 in m.get('commodities'):
                temp_model = main_models.CssInstanceCommodity()
                self.commodities.append(temp_model.from_map(k1))

        if m.get('createrNick') is not None:
            self.creater_nick = m.get('createrNick')

        if m.get('cssAuthRequestParam') is not None:
            self.css_auth_request_param = m.get('cssAuthRequestParam')

        if m.get('fromApp') is not None:
            self.from_app = m.get('fromApp')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('marketType') is not None:
            self.market_type = m.get('marketType')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('orderOrigin') is not None:
            self.order_origin = m.get('orderOrigin')

        if m.get('orderParams') is not None:
            self.order_params = m.get('orderParams')

        if m.get('payerId') is not None:
            self.payer_id = m.get('payerId')

        if m.get('planGroupId') is not None:
            self.plan_group_id = m.get('planGroupId')

        if m.get('planId') is not None:
            self.plan_id = m.get('planId')

        if m.get('planInstanceId') is not None:
            self.plan_instance_id = m.get('planInstanceId')

        if m.get('promotionCode') is not None:
            self.promotion_code = m.get('promotionCode')

        if m.get('promotionInputParam') is not None:
            self.promotion_input_param = m.get('promotionInputParam')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('skipChannel') is not None:
            self.skip_channel = m.get('skipChannel')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('transientAccess') is not None:
            self.transient_access = m.get('transientAccess')

        if m.get('umidToken') is not None:
            self.umid_token = m.get('umidToken')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

