# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class RefundResult(DaraModel):
    def __init__(
        self,
        apply_dispute_desc: str = None,
        apply_reason: main_models.ApplyReason = None,
        biz_claim_type: int = None,
        dispute_create_time: str = None,
        dispute_desc: str = None,
        dispute_end_time: str = None,
        dispute_id: str = None,
        dispute_status: int = None,
        order_id: str = None,
        order_line_id: str = None,
        order_logistics_status: int = None,
        refund_fee: int = None,
        refund_fee_data: main_models.RefundFeeData = None,
        refunder_address: str = None,
        refunder_name: str = None,
        refunder_tel: str = None,
        refunder_zip_code: str = None,
        request_id: str = None,
        return_good_logistics_status: int = None,
        seller_agree_msg: str = None,
        seller_refuse_agreement_message: str = None,
        seller_refuse_reason: str = None,
    ):
        self.apply_dispute_desc = apply_dispute_desc
        self.apply_reason = apply_reason
        self.biz_claim_type = biz_claim_type
        self.dispute_create_time = dispute_create_time
        self.dispute_desc = dispute_desc
        self.dispute_end_time = dispute_end_time
        self.dispute_id = dispute_id
        self.dispute_status = dispute_status
        self.order_id = order_id
        self.order_line_id = order_line_id
        self.order_logistics_status = order_logistics_status
        self.refund_fee = refund_fee
        self.refund_fee_data = refund_fee_data
        self.refunder_address = refunder_address
        self.refunder_name = refunder_name
        self.refunder_tel = refunder_tel
        self.refunder_zip_code = refunder_zip_code
        self.request_id = request_id
        self.return_good_logistics_status = return_good_logistics_status
        self.seller_agree_msg = seller_agree_msg
        self.seller_refuse_agreement_message = seller_refuse_agreement_message
        self.seller_refuse_reason = seller_refuse_reason

    def validate(self):
        if self.apply_reason:
            self.apply_reason.validate()
        if self.refund_fee_data:
            self.refund_fee_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_dispute_desc is not None:
            result['applyDisputeDesc'] = self.apply_dispute_desc

        if self.apply_reason is not None:
            result['applyReason'] = self.apply_reason.to_map()

        if self.biz_claim_type is not None:
            result['bizClaimType'] = self.biz_claim_type

        if self.dispute_create_time is not None:
            result['disputeCreateTime'] = self.dispute_create_time

        if self.dispute_desc is not None:
            result['disputeDesc'] = self.dispute_desc

        if self.dispute_end_time is not None:
            result['disputeEndTime'] = self.dispute_end_time

        if self.dispute_id is not None:
            result['disputeId'] = self.dispute_id

        if self.dispute_status is not None:
            result['disputeStatus'] = self.dispute_status

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.order_line_id is not None:
            result['orderLineId'] = self.order_line_id

        if self.order_logistics_status is not None:
            result['orderLogisticsStatus'] = self.order_logistics_status

        if self.refund_fee is not None:
            result['refundFee'] = self.refund_fee

        if self.refund_fee_data is not None:
            result['refundFeeData'] = self.refund_fee_data.to_map()

        if self.refunder_address is not None:
            result['refunderAddress'] = self.refunder_address

        if self.refunder_name is not None:
            result['refunderName'] = self.refunder_name

        if self.refunder_tel is not None:
            result['refunderTel'] = self.refunder_tel

        if self.refunder_zip_code is not None:
            result['refunderZipCode'] = self.refunder_zip_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.return_good_logistics_status is not None:
            result['returnGoodLogisticsStatus'] = self.return_good_logistics_status

        if self.seller_agree_msg is not None:
            result['sellerAgreeMsg'] = self.seller_agree_msg

        if self.seller_refuse_agreement_message is not None:
            result['sellerRefuseAgreementMessage'] = self.seller_refuse_agreement_message

        if self.seller_refuse_reason is not None:
            result['sellerRefuseReason'] = self.seller_refuse_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyDisputeDesc') is not None:
            self.apply_dispute_desc = m.get('applyDisputeDesc')

        if m.get('applyReason') is not None:
            temp_model = main_models.ApplyReason()
            self.apply_reason = temp_model.from_map(m.get('applyReason'))

        if m.get('bizClaimType') is not None:
            self.biz_claim_type = m.get('bizClaimType')

        if m.get('disputeCreateTime') is not None:
            self.dispute_create_time = m.get('disputeCreateTime')

        if m.get('disputeDesc') is not None:
            self.dispute_desc = m.get('disputeDesc')

        if m.get('disputeEndTime') is not None:
            self.dispute_end_time = m.get('disputeEndTime')

        if m.get('disputeId') is not None:
            self.dispute_id = m.get('disputeId')

        if m.get('disputeStatus') is not None:
            self.dispute_status = m.get('disputeStatus')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('orderLineId') is not None:
            self.order_line_id = m.get('orderLineId')

        if m.get('orderLogisticsStatus') is not None:
            self.order_logistics_status = m.get('orderLogisticsStatus')

        if m.get('refundFee') is not None:
            self.refund_fee = m.get('refundFee')

        if m.get('refundFeeData') is not None:
            temp_model = main_models.RefundFeeData()
            self.refund_fee_data = temp_model.from_map(m.get('refundFeeData'))

        if m.get('refunderAddress') is not None:
            self.refunder_address = m.get('refunderAddress')

        if m.get('refunderName') is not None:
            self.refunder_name = m.get('refunderName')

        if m.get('refunderTel') is not None:
            self.refunder_tel = m.get('refunderTel')

        if m.get('refunderZipCode') is not None:
            self.refunder_zip_code = m.get('refunderZipCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('returnGoodLogisticsStatus') is not None:
            self.return_good_logistics_status = m.get('returnGoodLogisticsStatus')

        if m.get('sellerAgreeMsg') is not None:
            self.seller_agree_msg = m.get('sellerAgreeMsg')

        if m.get('sellerRefuseAgreementMessage') is not None:
            self.seller_refuse_agreement_message = m.get('sellerRefuseAgreementMessage')

        if m.get('sellerRefuseReason') is not None:
            self.seller_refuse_reason = m.get('sellerRefuseReason')

        return self

