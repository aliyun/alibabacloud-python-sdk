# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class ApplyCreateDistributionOrderRequestItemInfoLists(TeaModel):
    def __init__(
        self,
        distribution_mall_id: str = None,
        lm_item_id: str = None,
        price: int = None,
        quantity: int = None,
        sku_id: str = None,
    ):
        self.distribution_mall_id = distribution_mall_id
        self.lm_item_id = lm_item_id
        self.price = price
        self.quantity = quantity
        # SKU
        self.sku_id = sku_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.price is not None:
            result['Price'] = self.price
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        return self


class ApplyCreateDistributionOrderRequest(TeaModel):
    def __init__(
        self,
        buyer_id: str = None,
        delivery_address: str = None,
        distribution_out_trade_id: str = None,
        distribution_supplier_id: str = None,
        distributor_id: str = None,
        ext_info: str = None,
        item_info_lists: List[ApplyCreateDistributionOrderRequestItemInfoLists] = None,
        tenant_id: str = None,
    ):
        self.buyer_id = buyer_id
        self.delivery_address = delivery_address
        self.distribution_out_trade_id = distribution_out_trade_id
        self.distribution_supplier_id = distribution_supplier_id
        self.distributor_id = distributor_id
        self.ext_info = ext_info
        self.item_info_lists = item_info_lists
        self.tenant_id = tenant_id

    def validate(self):
        if self.item_info_lists:
            for k in self.item_info_lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_id is not None:
            result['BuyerId'] = self.buyer_id
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address
        if self.distribution_out_trade_id is not None:
            result['DistributionOutTradeId'] = self.distribution_out_trade_id
        if self.distribution_supplier_id is not None:
            result['DistributionSupplierId'] = self.distribution_supplier_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        result['ItemInfoLists'] = []
        if self.item_info_lists is not None:
            for k in self.item_info_lists:
                result['ItemInfoLists'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyerId') is not None:
            self.buyer_id = m.get('BuyerId')
        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')
        if m.get('DistributionOutTradeId') is not None:
            self.distribution_out_trade_id = m.get('DistributionOutTradeId')
        if m.get('DistributionSupplierId') is not None:
            self.distribution_supplier_id = m.get('DistributionSupplierId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        self.item_info_lists = []
        if m.get('ItemInfoLists') is not None:
            for k in m.get('ItemInfoLists'):
                temp_model = ApplyCreateDistributionOrderRequestItemInfoLists()
                self.item_info_lists.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ApplyCreateDistributionOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        buyer_id: str = None,
        delivery_address: str = None,
        distribution_out_trade_id: str = None,
        distribution_supplier_id: str = None,
        distributor_id: str = None,
        ext_info: str = None,
        item_info_lists_shrink: str = None,
        tenant_id: str = None,
    ):
        self.buyer_id = buyer_id
        self.delivery_address = delivery_address
        self.distribution_out_trade_id = distribution_out_trade_id
        self.distribution_supplier_id = distribution_supplier_id
        self.distributor_id = distributor_id
        self.ext_info = ext_info
        self.item_info_lists_shrink = item_info_lists_shrink
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_id is not None:
            result['BuyerId'] = self.buyer_id
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address
        if self.distribution_out_trade_id is not None:
            result['DistributionOutTradeId'] = self.distribution_out_trade_id
        if self.distribution_supplier_id is not None:
            result['DistributionSupplierId'] = self.distribution_supplier_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.item_info_lists_shrink is not None:
            result['ItemInfoLists'] = self.item_info_lists_shrink
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyerId') is not None:
            self.buyer_id = m.get('BuyerId')
        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')
        if m.get('DistributionOutTradeId') is not None:
            self.distribution_out_trade_id = m.get('DistributionOutTradeId')
        if m.get('DistributionSupplierId') is not None:
            self.distribution_supplier_id = m.get('DistributionSupplierId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('ItemInfoLists') is not None:
            self.item_info_lists_shrink = m.get('ItemInfoLists')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ApplyCreateDistributionOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ApplyCreateDistributionOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyCreateDistributionOrderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyCreateDistributionOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyRefund4DistributionRequestLeavePictureLists(TeaModel):
    def __init__(
        self,
        desc: str = None,
        picture: str = None,
    ):
        self.desc = desc
        self.picture = picture

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.picture is not None:
            result['Picture'] = self.picture
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Picture') is not None:
            self.picture = m.get('Picture')
        return self


class ApplyRefund4DistributionRequest(TeaModel):
    def __init__(
        self,
        apply_reason_text_id: int = None,
        apply_refund_count: int = None,
        apply_refund_fee: int = None,
        biz_claim_type: int = None,
        distributor_id: str = None,
        goods_status: int = None,
        leave_message: str = None,
        leave_picture_lists: List[ApplyRefund4DistributionRequestLeavePictureLists] = None,
        sub_distribution_order_id: str = None,
        tenant_id: str = None,
    ):
        self.apply_reason_text_id = apply_reason_text_id
        self.apply_refund_count = apply_refund_count
        self.apply_refund_fee = apply_refund_fee
        self.biz_claim_type = biz_claim_type
        self.distributor_id = distributor_id
        self.goods_status = goods_status
        self.leave_message = leave_message
        self.leave_picture_lists = leave_picture_lists
        self.sub_distribution_order_id = sub_distribution_order_id
        self.tenant_id = tenant_id

    def validate(self):
        if self.leave_picture_lists:
            for k in self.leave_picture_lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_reason_text_id is not None:
            result['ApplyReasonTextId'] = self.apply_reason_text_id
        if self.apply_refund_count is not None:
            result['ApplyRefundCount'] = self.apply_refund_count
        if self.apply_refund_fee is not None:
            result['ApplyRefundFee'] = self.apply_refund_fee
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.goods_status is not None:
            result['GoodsStatus'] = self.goods_status
        if self.leave_message is not None:
            result['LeaveMessage'] = self.leave_message
        result['LeavePictureLists'] = []
        if self.leave_picture_lists is not None:
            for k in self.leave_picture_lists:
                result['LeavePictureLists'].append(k.to_map() if k else None)
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyReasonTextId') is not None:
            self.apply_reason_text_id = m.get('ApplyReasonTextId')
        if m.get('ApplyRefundCount') is not None:
            self.apply_refund_count = m.get('ApplyRefundCount')
        if m.get('ApplyRefundFee') is not None:
            self.apply_refund_fee = m.get('ApplyRefundFee')
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('GoodsStatus') is not None:
            self.goods_status = m.get('GoodsStatus')
        if m.get('LeaveMessage') is not None:
            self.leave_message = m.get('LeaveMessage')
        self.leave_picture_lists = []
        if m.get('LeavePictureLists') is not None:
            for k in m.get('LeavePictureLists'):
                temp_model = ApplyRefund4DistributionRequestLeavePictureLists()
                self.leave_picture_lists.append(temp_model.from_map(k))
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ApplyRefund4DistributionShrinkRequest(TeaModel):
    def __init__(
        self,
        apply_reason_text_id: int = None,
        apply_refund_count: int = None,
        apply_refund_fee: int = None,
        biz_claim_type: int = None,
        distributor_id: str = None,
        goods_status: int = None,
        leave_message: str = None,
        leave_picture_lists_shrink: str = None,
        sub_distribution_order_id: str = None,
        tenant_id: str = None,
    ):
        self.apply_reason_text_id = apply_reason_text_id
        self.apply_refund_count = apply_refund_count
        self.apply_refund_fee = apply_refund_fee
        self.biz_claim_type = biz_claim_type
        self.distributor_id = distributor_id
        self.goods_status = goods_status
        self.leave_message = leave_message
        self.leave_picture_lists_shrink = leave_picture_lists_shrink
        self.sub_distribution_order_id = sub_distribution_order_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_reason_text_id is not None:
            result['ApplyReasonTextId'] = self.apply_reason_text_id
        if self.apply_refund_count is not None:
            result['ApplyRefundCount'] = self.apply_refund_count
        if self.apply_refund_fee is not None:
            result['ApplyRefundFee'] = self.apply_refund_fee
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.goods_status is not None:
            result['GoodsStatus'] = self.goods_status
        if self.leave_message is not None:
            result['LeaveMessage'] = self.leave_message
        if self.leave_picture_lists_shrink is not None:
            result['LeavePictureLists'] = self.leave_picture_lists_shrink
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyReasonTextId') is not None:
            self.apply_reason_text_id = m.get('ApplyReasonTextId')
        if m.get('ApplyRefundCount') is not None:
            self.apply_refund_count = m.get('ApplyRefundCount')
        if m.get('ApplyRefundFee') is not None:
            self.apply_refund_fee = m.get('ApplyRefundFee')
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('GoodsStatus') is not None:
            self.goods_status = m.get('GoodsStatus')
        if m.get('LeaveMessage') is not None:
            self.leave_message = m.get('LeaveMessage')
        if m.get('LeavePictureLists') is not None:
            self.leave_picture_lists_shrink = m.get('LeavePictureLists')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ApplyRefund4DistributionResponseBodyModel(TeaModel):
    def __init__(
        self,
        dispute_id: int = None,
        dispute_status: int = None,
        dispute_type: int = None,
        sub_distribution_order_id: str = None,
    ):
        self.dispute_id = dispute_id
        self.dispute_status = dispute_status
        self.dispute_type = dispute_type
        self.sub_distribution_order_id = sub_distribution_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.dispute_status is not None:
            result['DisputeStatus'] = self.dispute_status
        if self.dispute_type is not None:
            result['DisputeType'] = self.dispute_type
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DisputeStatus') is not None:
            self.dispute_status = m.get('DisputeStatus')
        if m.get('DisputeType') is not None:
            self.dispute_type = m.get('DisputeType')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        return self


class ApplyRefund4DistributionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: ApplyRefund4DistributionResponseBodyModel = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = ApplyRefund4DistributionResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ApplyRefund4DistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyRefund4DistributionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyRefund4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelDistributionTradeRequest(TeaModel):
    def __init__(
        self,
        distribution_trade_id: str = None,
        distributor_id: str = None,
        tenant_id: str = None,
    ):
        self.distribution_trade_id = distribution_trade_id
        self.distributor_id = distributor_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_trade_id is not None:
            result['DistributionTradeId'] = self.distribution_trade_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributionTradeId') is not None:
            self.distribution_trade_id = m.get('DistributionTradeId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CancelDistributionTradeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CancelDistributionTradeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelDistributionTradeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelDistributionTradeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelRefund4DistributionRequest(TeaModel):
    def __init__(
        self,
        dispute_id: int = None,
        distributor_id: str = None,
        sub_distribution_order_id: str = None,
        tenant_id: str = None,
    ):
        self.dispute_id = dispute_id
        self.distributor_id = distributor_id
        self.sub_distribution_order_id = sub_distribution_order_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CancelRefund4DistributionResponseBodyModel(TeaModel):
    def __init__(
        self,
        dispute_id: int = None,
        dispute_status: int = None,
        dispute_type: int = None,
        sub_distribution_order_id: str = None,
    ):
        self.dispute_id = dispute_id
        self.dispute_status = dispute_status
        self.dispute_type = dispute_type
        self.sub_distribution_order_id = sub_distribution_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.dispute_status is not None:
            result['DisputeStatus'] = self.dispute_status
        if self.dispute_type is not None:
            result['DisputeType'] = self.dispute_type
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DisputeStatus') is not None:
            self.dispute_status = m.get('DisputeStatus')
        if m.get('DisputeType') is not None:
            self.dispute_type = m.get('DisputeType')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        return self


class CancelRefund4DistributionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: CancelRefund4DistributionResponseBodyModel = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = CancelRefund4DistributionResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CancelRefund4DistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelRefund4DistributionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelRefund4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmDisburse4DistributionRequest(TeaModel):
    def __init__(
        self,
        distribution_trade_id: str = None,
        distributor_id: str = None,
        main_distribution_order_id: str = None,
        tenant_id: str = None,
    ):
        self.distribution_trade_id = distribution_trade_id
        self.distributor_id = distributor_id
        self.main_distribution_order_id = main_distribution_order_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_trade_id is not None:
            result['DistributionTradeId'] = self.distribution_trade_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.main_distribution_order_id is not None:
            result['MainDistributionOrderId'] = self.main_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributionTradeId') is not None:
            self.distribution_trade_id = m.get('DistributionTradeId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('MainDistributionOrderId') is not None:
            self.main_distribution_order_id = m.get('MainDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ConfirmDisburse4DistributionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ConfirmDisburse4DistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfirmDisburse4DistributionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ConfirmDisburse4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitApplyRefund4DistributionRequest(TeaModel):
    def __init__(
        self,
        biz_claim_type: int = None,
        distributor_id: str = None,
        goods_status: int = None,
        sub_distribution_order_id: str = None,
        tenant_id: str = None,
    ):
        self.biz_claim_type = biz_claim_type
        self.distributor_id = distributor_id
        self.goods_status = goods_status
        self.sub_distribution_order_id = sub_distribution_order_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.goods_status is not None:
            result['GoodsStatus'] = self.goods_status
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('GoodsStatus') is not None:
            self.goods_status = m.get('GoodsStatus')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class InitApplyRefund4DistributionResponseBodyModelMaxRefundFeeData(TeaModel):
    def __init__(
        self,
        max_refund_fee: int = None,
        min_refund_fee: int = None,
    ):
        self.max_refund_fee = max_refund_fee
        self.min_refund_fee = min_refund_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_refund_fee is not None:
            result['MaxRefundFee'] = self.max_refund_fee
        if self.min_refund_fee is not None:
            result['MinRefundFee'] = self.min_refund_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxRefundFee') is not None:
            self.max_refund_fee = m.get('MaxRefundFee')
        if m.get('MinRefundFee') is not None:
            self.min_refund_fee = m.get('MinRefundFee')
        return self


class InitApplyRefund4DistributionResponseBodyModelRefundReasonList(TeaModel):
    def __init__(
        self,
        proof_required: bool = None,
        reason_text_id: str = None,
        reason_tips: str = None,
        refund_desc_required: bool = None,
    ):
        self.proof_required = proof_required
        self.reason_text_id = reason_text_id
        self.reason_tips = reason_tips
        self.refund_desc_required = refund_desc_required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.proof_required is not None:
            result['ProofRequired'] = self.proof_required
        if self.reason_text_id is not None:
            result['ReasonTextId'] = self.reason_text_id
        if self.reason_tips is not None:
            result['ReasonTips'] = self.reason_tips
        if self.refund_desc_required is not None:
            result['RefundDescRequired'] = self.refund_desc_required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProofRequired') is not None:
            self.proof_required = m.get('ProofRequired')
        if m.get('ReasonTextId') is not None:
            self.reason_text_id = m.get('ReasonTextId')
        if m.get('ReasonTips') is not None:
            self.reason_tips = m.get('ReasonTips')
        if m.get('RefundDescRequired') is not None:
            self.refund_desc_required = m.get('RefundDescRequired')
        return self


class InitApplyRefund4DistributionResponseBodyModel(TeaModel):
    def __init__(
        self,
        biz_claim_type: int = None,
        main_order_refund: bool = None,
        max_refund_fee_data: InitApplyRefund4DistributionResponseBodyModelMaxRefundFeeData = None,
        refund_reason_list: List[InitApplyRefund4DistributionResponseBodyModelRefundReasonList] = None,
        sub_distribution_order_id: str = None,
    ):
        self.biz_claim_type = biz_claim_type
        self.main_order_refund = main_order_refund
        self.max_refund_fee_data = max_refund_fee_data
        self.refund_reason_list = refund_reason_list
        self.sub_distribution_order_id = sub_distribution_order_id

    def validate(self):
        if self.max_refund_fee_data:
            self.max_refund_fee_data.validate()
        if self.refund_reason_list:
            for k in self.refund_reason_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.main_order_refund is not None:
            result['MainOrderRefund'] = self.main_order_refund
        if self.max_refund_fee_data is not None:
            result['MaxRefundFeeData'] = self.max_refund_fee_data.to_map()
        result['RefundReasonList'] = []
        if self.refund_reason_list is not None:
            for k in self.refund_reason_list:
                result['RefundReasonList'].append(k.to_map() if k else None)
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('MainOrderRefund') is not None:
            self.main_order_refund = m.get('MainOrderRefund')
        if m.get('MaxRefundFeeData') is not None:
            temp_model = InitApplyRefund4DistributionResponseBodyModelMaxRefundFeeData()
            self.max_refund_fee_data = temp_model.from_map(m['MaxRefundFeeData'])
        self.refund_reason_list = []
        if m.get('RefundReasonList') is not None:
            for k in m.get('RefundReasonList'):
                temp_model = InitApplyRefund4DistributionResponseBodyModelRefundReasonList()
                self.refund_reason_list.append(temp_model.from_map(k))
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        return self


class InitApplyRefund4DistributionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: InitApplyRefund4DistributionResponseBodyModel = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = InitApplyRefund4DistributionResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class InitApplyRefund4DistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitApplyRefund4DistributionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InitApplyRefund4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitModifyRefund4DistributionRequest(TeaModel):
    def __init__(
        self,
        biz_claim_type: int = None,
        dispute_id: int = None,
        distributor_id: str = None,
        sub_distribution_order_id: str = None,
        tenant_id: str = None,
    ):
        self.biz_claim_type = biz_claim_type
        self.dispute_id = dispute_id
        self.distributor_id = distributor_id
        self.sub_distribution_order_id = sub_distribution_order_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class InitModifyRefund4DistributionResponseBodyModelMaxRefundFeeData(TeaModel):
    def __init__(
        self,
        max_refund_fee: int = None,
        min_refund_fee: int = None,
    ):
        self.max_refund_fee = max_refund_fee
        self.min_refund_fee = min_refund_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_refund_fee is not None:
            result['MaxRefundFee'] = self.max_refund_fee
        if self.min_refund_fee is not None:
            result['MinRefundFee'] = self.min_refund_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxRefundFee') is not None:
            self.max_refund_fee = m.get('MaxRefundFee')
        if m.get('MinRefundFee') is not None:
            self.min_refund_fee = m.get('MinRefundFee')
        return self


class InitModifyRefund4DistributionResponseBodyModelRefundReasonList(TeaModel):
    def __init__(
        self,
        proof_required: bool = None,
        reason_text_id: str = None,
        reason_tips: str = None,
        refund_desc_required: bool = None,
    ):
        self.proof_required = proof_required
        self.reason_text_id = reason_text_id
        self.reason_tips = reason_tips
        self.refund_desc_required = refund_desc_required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.proof_required is not None:
            result['ProofRequired'] = self.proof_required
        if self.reason_text_id is not None:
            result['ReasonTextId'] = self.reason_text_id
        if self.reason_tips is not None:
            result['ReasonTips'] = self.reason_tips
        if self.refund_desc_required is not None:
            result['RefundDescRequired'] = self.refund_desc_required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProofRequired') is not None:
            self.proof_required = m.get('ProofRequired')
        if m.get('ReasonTextId') is not None:
            self.reason_text_id = m.get('ReasonTextId')
        if m.get('ReasonTips') is not None:
            self.reason_tips = m.get('ReasonTips')
        if m.get('RefundDescRequired') is not None:
            self.refund_desc_required = m.get('RefundDescRequired')
        return self


class InitModifyRefund4DistributionResponseBodyModel(TeaModel):
    def __init__(
        self,
        biz_claim_type: int = None,
        main_order_refund: bool = None,
        max_refund_fee_data: InitModifyRefund4DistributionResponseBodyModelMaxRefundFeeData = None,
        refund_reason_list: List[InitModifyRefund4DistributionResponseBodyModelRefundReasonList] = None,
        sub_distribution_order_id: str = None,
    ):
        self.biz_claim_type = biz_claim_type
        self.main_order_refund = main_order_refund
        self.max_refund_fee_data = max_refund_fee_data
        self.refund_reason_list = refund_reason_list
        self.sub_distribution_order_id = sub_distribution_order_id

    def validate(self):
        if self.max_refund_fee_data:
            self.max_refund_fee_data.validate()
        if self.refund_reason_list:
            for k in self.refund_reason_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.main_order_refund is not None:
            result['MainOrderRefund'] = self.main_order_refund
        if self.max_refund_fee_data is not None:
            result['MaxRefundFeeData'] = self.max_refund_fee_data.to_map()
        result['RefundReasonList'] = []
        if self.refund_reason_list is not None:
            for k in self.refund_reason_list:
                result['RefundReasonList'].append(k.to_map() if k else None)
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('MainOrderRefund') is not None:
            self.main_order_refund = m.get('MainOrderRefund')
        if m.get('MaxRefundFeeData') is not None:
            temp_model = InitModifyRefund4DistributionResponseBodyModelMaxRefundFeeData()
            self.max_refund_fee_data = temp_model.from_map(m['MaxRefundFeeData'])
        self.refund_reason_list = []
        if m.get('RefundReasonList') is not None:
            for k in m.get('RefundReasonList'):
                temp_model = InitModifyRefund4DistributionResponseBodyModelRefundReasonList()
                self.refund_reason_list.append(temp_model.from_map(k))
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        return self


class InitModifyRefund4DistributionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: InitModifyRefund4DistributionResponseBodyModel = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = InitModifyRefund4DistributionResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class InitModifyRefund4DistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitModifyRefund4DistributionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InitModifyRefund4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDistributionItemRequest(TeaModel):
    def __init__(
        self,
        distribution_mall_id: str = None,
        distributor_id: str = None,
        item_status: int = None,
        lm_item_id: str = None,
        page_number: int = None,
        page_size: int = None,
        tenant_id: str = None,
    ):
        self.distribution_mall_id = distribution_mall_id
        self.distributor_id = distributor_id
        self.item_status = item_status
        self.lm_item_id = lm_item_id
        self.page_number = page_number
        self.page_size = page_size
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.item_status is not None:
            result['ItemStatus'] = self.item_status
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('ItemStatus') is not None:
            self.item_status = m.get('ItemStatus')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListDistributionItemResponseBodyModelCategoryChain(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        leaf: bool = None,
        level: int = None,
        name: str = None,
        parent_id: int = None,
    ):
        self.category_id = category_id
        self.leaf = leaf
        self.level = level
        self.name = name
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.leaf is not None:
            result['Leaf'] = self.leaf
        if self.level is not None:
            result['Level'] = self.level
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Leaf') is not None:
            self.leaf = m.get('Leaf')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class ListDistributionItemResponseBodyModelLmAttributeModels(TeaModel):
    def __init__(
        self,
        attr_id: int = None,
        category: int = None,
        data_type: str = None,
        description: str = None,
        name: str = None,
        restriction: str = None,
        scope_list: List[str] = None,
        value: str = None,
    ):
        self.attr_id = attr_id
        self.category = category
        self.data_type = data_type
        self.description = description
        self.name = name
        self.restriction = restriction
        self.scope_list = scope_list
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attr_id is not None:
            result['AttrId'] = self.attr_id
        if self.category is not None:
            result['Category'] = self.category
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.restriction is not None:
            result['Restriction'] = self.restriction
        if self.scope_list is not None:
            result['ScopeList'] = self.scope_list
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttrId') is not None:
            self.attr_id = m.get('AttrId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Restriction') is not None:
            self.restriction = m.get('Restriction')
        if m.get('ScopeList') is not None:
            self.scope_list = m.get('ScopeList')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListDistributionItemResponseBodyModelSkuListLmAttributeModels(TeaModel):
    def __init__(
        self,
        attr_id: int = None,
        category: int = None,
        data_type: str = None,
        description: str = None,
        name: str = None,
        restriction: str = None,
        scope_list: List[str] = None,
        value: str = None,
    ):
        self.attr_id = attr_id
        self.category = category
        self.data_type = data_type
        self.description = description
        self.name = name
        self.restriction = restriction
        self.scope_list = scope_list
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attr_id is not None:
            result['AttrId'] = self.attr_id
        if self.category is not None:
            result['Category'] = self.category
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.restriction is not None:
            result['Restriction'] = self.restriction
        if self.scope_list is not None:
            result['ScopeList'] = self.scope_list
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttrId') is not None:
            self.attr_id = m.get('AttrId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Restriction') is not None:
            self.restriction = m.get('Restriction')
        if m.get('ScopeList') is not None:
            self.scope_list = m.get('ScopeList')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListDistributionItemResponseBodyModelSkuList(TeaModel):
    def __init__(
        self,
        can_sell: bool = None,
        customized_attribute_map: Dict[str, str] = None,
        ext_info: str = None,
        gmt_modified: str = None,
        has_quantity: bool = None,
        item_id: int = None,
        lm_attribute_models: List[ListDistributionItemResponseBodyModelSkuListLmAttributeModels] = None,
        lm_item_id: str = None,
        price_cent: int = None,
        quantity: int = None,
        reserved_price: int = None,
        simple_quantity: str = None,
        sku_desc: str = None,
        sku_id: int = None,
        sku_pic_url: str = None,
        sku_properties: Dict[str, str] = None,
        sku_properties_json: str = None,
        sku_title: str = None,
        status: int = None,
        tips: str = None,
        lm_sku_attribute_map: Dict[str, str] = None,
    ):
        self.can_sell = can_sell
        self.customized_attribute_map = customized_attribute_map
        self.ext_info = ext_info
        self.gmt_modified = gmt_modified
        self.has_quantity = has_quantity
        self.item_id = item_id
        self.lm_attribute_models = lm_attribute_models
        self.lm_item_id = lm_item_id
        self.price_cent = price_cent
        self.quantity = quantity
        self.reserved_price = reserved_price
        self.simple_quantity = simple_quantity
        self.sku_desc = sku_desc
        self.sku_id = sku_id
        self.sku_pic_url = sku_pic_url
        self.sku_properties = sku_properties
        self.sku_properties_json = sku_properties_json
        self.sku_title = sku_title
        self.status = status
        self.tips = tips
        self.lm_sku_attribute_map = lm_sku_attribute_map

    def validate(self):
        if self.lm_attribute_models:
            for k in self.lm_attribute_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.has_quantity is not None:
            result['HasQuantity'] = self.has_quantity
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        result['LmAttributeModels'] = []
        if self.lm_attribute_models is not None:
            for k in self.lm_attribute_models:
                result['LmAttributeModels'].append(k.to_map() if k else None)
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.simple_quantity is not None:
            result['SimpleQuantity'] = self.simple_quantity
        if self.sku_desc is not None:
            result['SkuDesc'] = self.sku_desc
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_pic_url is not None:
            result['SkuPicUrl'] = self.sku_pic_url
        if self.sku_properties is not None:
            result['SkuProperties'] = self.sku_properties
        if self.sku_properties_json is not None:
            result['SkuPropertiesJson'] = self.sku_properties_json
        if self.sku_title is not None:
            result['SkuTitle'] = self.sku_title
        if self.status is not None:
            result['Status'] = self.status
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.lm_sku_attribute_map is not None:
            result['lmSkuAttributeMap'] = self.lm_sku_attribute_map
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HasQuantity') is not None:
            self.has_quantity = m.get('HasQuantity')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        self.lm_attribute_models = []
        if m.get('LmAttributeModels') is not None:
            for k in m.get('LmAttributeModels'):
                temp_model = ListDistributionItemResponseBodyModelSkuListLmAttributeModels()
                self.lm_attribute_models.append(temp_model.from_map(k))
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('SimpleQuantity') is not None:
            self.simple_quantity = m.get('SimpleQuantity')
        if m.get('SkuDesc') is not None:
            self.sku_desc = m.get('SkuDesc')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuPicUrl') is not None:
            self.sku_pic_url = m.get('SkuPicUrl')
        if m.get('SkuProperties') is not None:
            self.sku_properties = m.get('SkuProperties')
        if m.get('SkuPropertiesJson') is not None:
            self.sku_properties_json = m.get('SkuPropertiesJson')
        if m.get('SkuTitle') is not None:
            self.sku_title = m.get('SkuTitle')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('lmSkuAttributeMap') is not None:
            self.lm_sku_attribute_map = m.get('lmSkuAttributeMap')
        return self


class ListDistributionItemResponseBodyModel(TeaModel):
    def __init__(
        self,
        category: str = None,
        category_chain: List[ListDistributionItemResponseBodyModelCategoryChain] = None,
        category_id: int = None,
        desc_option: str = None,
        distribution_mall_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        has_quantity: bool = None,
        is_can_sell: bool = None,
        item_desc: str = None,
        item_id: int = None,
        item_id_str: str = None,
        item_images: List[str] = None,
        item_name: str = None,
        item_title: str = None,
        lm_attribute_map: Dict[str, str] = None,
        lm_attribute_models: List[ListDistributionItemResponseBodyModelLmAttributeModels] = None,
        lm_item_id: str = None,
        main_pic_url: str = None,
        pic_url: str = None,
        price_cent_scope: str = None,
        properties_json: str = None,
        quantity: int = None,
        reserved_price: int = None,
        reserved_price_scope: str = None,
        simple_quantity: str = None,
        simple_total_sold_quantity: str = None,
        sku_list: List[ListDistributionItemResponseBodyModelSkuList] = None,
        status: int = None,
        tips: str = None,
        total_sold_quantity: int = None,
    ):
        self.category = category
        self.category_chain = category_chain
        self.category_id = category_id
        self.desc_option = desc_option
        self.distribution_mall_id = distribution_mall_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.has_quantity = has_quantity
        self.is_can_sell = is_can_sell
        self.item_desc = item_desc
        self.item_id = item_id
        self.item_id_str = item_id_str
        self.item_images = item_images
        self.item_name = item_name
        self.item_title = item_title
        self.lm_attribute_map = lm_attribute_map
        self.lm_attribute_models = lm_attribute_models
        self.lm_item_id = lm_item_id
        self.main_pic_url = main_pic_url
        self.pic_url = pic_url
        self.price_cent_scope = price_cent_scope
        self.properties_json = properties_json
        self.quantity = quantity
        self.reserved_price = reserved_price
        self.reserved_price_scope = reserved_price_scope
        self.simple_quantity = simple_quantity
        self.simple_total_sold_quantity = simple_total_sold_quantity
        self.sku_list = sku_list
        self.status = status
        self.tips = tips
        self.total_sold_quantity = total_sold_quantity

    def validate(self):
        if self.category_chain:
            for k in self.category_chain:
                if k:
                    k.validate()
        if self.lm_attribute_models:
            for k in self.lm_attribute_models:
                if k:
                    k.validate()
        if self.sku_list:
            for k in self.sku_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        result['CategoryChain'] = []
        if self.category_chain is not None:
            for k in self.category_chain:
                result['CategoryChain'].append(k.to_map() if k else None)
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.desc_option is not None:
            result['DescOption'] = self.desc_option
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.has_quantity is not None:
            result['HasQuantity'] = self.has_quantity
        if self.is_can_sell is not None:
            result['IsCanSell'] = self.is_can_sell
        if self.item_desc is not None:
            result['ItemDesc'] = self.item_desc
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_id_str is not None:
            result['ItemIdStr'] = self.item_id_str
        if self.item_images is not None:
            result['ItemImages'] = self.item_images
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.lm_attribute_map is not None:
            result['LmAttributeMap'] = self.lm_attribute_map
        result['LmAttributeModels'] = []
        if self.lm_attribute_models is not None:
            for k in self.lm_attribute_models:
                result['LmAttributeModels'].append(k.to_map() if k else None)
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.main_pic_url is not None:
            result['MainPicUrl'] = self.main_pic_url
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.price_cent_scope is not None:
            result['PriceCentScope'] = self.price_cent_scope
        if self.properties_json is not None:
            result['PropertiesJson'] = self.properties_json
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.reserved_price_scope is not None:
            result['ReservedPriceScope'] = self.reserved_price_scope
        if self.simple_quantity is not None:
            result['SimpleQuantity'] = self.simple_quantity
        if self.simple_total_sold_quantity is not None:
            result['SimpleTotalSoldQuantity'] = self.simple_total_sold_quantity
        result['SkuList'] = []
        if self.sku_list is not None:
            for k in self.sku_list:
                result['SkuList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.total_sold_quantity is not None:
            result['TotalSoldQuantity'] = self.total_sold_quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        self.category_chain = []
        if m.get('CategoryChain') is not None:
            for k in m.get('CategoryChain'):
                temp_model = ListDistributionItemResponseBodyModelCategoryChain()
                self.category_chain.append(temp_model.from_map(k))
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('DescOption') is not None:
            self.desc_option = m.get('DescOption')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HasQuantity') is not None:
            self.has_quantity = m.get('HasQuantity')
        if m.get('IsCanSell') is not None:
            self.is_can_sell = m.get('IsCanSell')
        if m.get('ItemDesc') is not None:
            self.item_desc = m.get('ItemDesc')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemIdStr') is not None:
            self.item_id_str = m.get('ItemIdStr')
        if m.get('ItemImages') is not None:
            self.item_images = m.get('ItemImages')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('LmAttributeMap') is not None:
            self.lm_attribute_map = m.get('LmAttributeMap')
        self.lm_attribute_models = []
        if m.get('LmAttributeModels') is not None:
            for k in m.get('LmAttributeModels'):
                temp_model = ListDistributionItemResponseBodyModelLmAttributeModels()
                self.lm_attribute_models.append(temp_model.from_map(k))
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('MainPicUrl') is not None:
            self.main_pic_url = m.get('MainPicUrl')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('PriceCentScope') is not None:
            self.price_cent_scope = m.get('PriceCentScope')
        if m.get('PropertiesJson') is not None:
            self.properties_json = m.get('PropertiesJson')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('ReservedPriceScope') is not None:
            self.reserved_price_scope = m.get('ReservedPriceScope')
        if m.get('SimpleQuantity') is not None:
            self.simple_quantity = m.get('SimpleQuantity')
        if m.get('SimpleTotalSoldQuantity') is not None:
            self.simple_total_sold_quantity = m.get('SimpleTotalSoldQuantity')
        self.sku_list = []
        if m.get('SkuList') is not None:
            for k in m.get('SkuList'):
                temp_model = ListDistributionItemResponseBodyModelSkuList()
                self.sku_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('TotalSoldQuantity') is not None:
            self.total_sold_quantity = m.get('TotalSoldQuantity')
        return self


class ListDistributionItemResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: List[ListDistributionItemResponseBodyModel] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = ListDistributionItemResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDistributionItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDistributionItemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDistributionItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDistributionItemWithoutCacheRequest(TeaModel):
    def __init__(
        self,
        distribution_mall_id: str = None,
        distributor_id: str = None,
        item_status: int = None,
        lm_item_id: str = None,
        page_number: int = None,
        page_size: int = None,
        tenant_id: str = None,
    ):
        self.distribution_mall_id = distribution_mall_id
        self.distributor_id = distributor_id
        self.item_status = item_status
        self.lm_item_id = lm_item_id
        self.page_number = page_number
        self.page_size = page_size
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.item_status is not None:
            result['ItemStatus'] = self.item_status
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('ItemStatus') is not None:
            self.item_status = m.get('ItemStatus')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListDistributionItemWithoutCacheResponseBodyModelSkuModels(TeaModel):
    def __init__(
        self,
        customized_attribute_map: Dict[str, str] = None,
        distribution_mall_id: str = None,
        ext_json: str = None,
        has_quantity: bool = None,
        invoice_type: int = None,
        is_can_not_be_sold_code: str = None,
        is_can_not_be_sold_message: str = None,
        item_id: int = None,
        lm_item_id: str = None,
        lm_sku_attribute_map: Dict[str, str] = None,
        price_cent: int = None,
        quantity: int = None,
        reserved_price: int = None,
        simple_quantity: str = None,
        sku_id: int = None,
        sku_pic_url: str = None,
        sku_pvs: str = None,
        sku_title: str = None,
        status: int = None,
        supplier_price: int = None,
    ):
        self.customized_attribute_map = customized_attribute_map
        self.distribution_mall_id = distribution_mall_id
        self.ext_json = ext_json
        self.has_quantity = has_quantity
        self.invoice_type = invoice_type
        self.is_can_not_be_sold_code = is_can_not_be_sold_code
        self.is_can_not_be_sold_message = is_can_not_be_sold_message
        self.item_id = item_id
        self.lm_item_id = lm_item_id
        self.lm_sku_attribute_map = lm_sku_attribute_map
        self.price_cent = price_cent
        self.quantity = quantity
        self.reserved_price = reserved_price
        self.simple_quantity = simple_quantity
        self.sku_id = sku_id
        self.sku_pic_url = sku_pic_url
        self.sku_pvs = sku_pvs
        self.sku_title = sku_title
        self.status = status
        self.supplier_price = supplier_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.has_quantity is not None:
            result['HasQuantity'] = self.has_quantity
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.is_can_not_be_sold_code is not None:
            result['IsCanNotBeSoldCode'] = self.is_can_not_be_sold_code
        if self.is_can_not_be_sold_message is not None:
            result['IsCanNotBeSoldMessage'] = self.is_can_not_be_sold_message
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.lm_sku_attribute_map is not None:
            result['LmSkuAttributeMap'] = self.lm_sku_attribute_map
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.simple_quantity is not None:
            result['SimpleQuantity'] = self.simple_quantity
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_pic_url is not None:
            result['SkuPicUrl'] = self.sku_pic_url
        if self.sku_pvs is not None:
            result['SkuPvs'] = self.sku_pvs
        if self.sku_title is not None:
            result['SkuTitle'] = self.sku_title
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_price is not None:
            result['SupplierPrice'] = self.supplier_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('HasQuantity') is not None:
            self.has_quantity = m.get('HasQuantity')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('IsCanNotBeSoldCode') is not None:
            self.is_can_not_be_sold_code = m.get('IsCanNotBeSoldCode')
        if m.get('IsCanNotBeSoldMessage') is not None:
            self.is_can_not_be_sold_message = m.get('IsCanNotBeSoldMessage')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LmSkuAttributeMap') is not None:
            self.lm_sku_attribute_map = m.get('LmSkuAttributeMap')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('SimpleQuantity') is not None:
            self.simple_quantity = m.get('SimpleQuantity')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuPicUrl') is not None:
            self.sku_pic_url = m.get('SkuPicUrl')
        if m.get('SkuPvs') is not None:
            self.sku_pvs = m.get('SkuPvs')
        if m.get('SkuTitle') is not None:
            self.sku_title = m.get('SkuTitle')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierPrice') is not None:
            self.supplier_price = m.get('SupplierPrice')
        return self


class ListDistributionItemWithoutCacheResponseBodyModelSkuPropertysValues(TeaModel):
    def __init__(
        self,
        id: int = None,
        text: str = None,
    ):
        self.id = id
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class ListDistributionItemWithoutCacheResponseBodyModelSkuPropertys(TeaModel):
    def __init__(
        self,
        id: int = None,
        text: str = None,
        values: List[ListDistributionItemWithoutCacheResponseBodyModelSkuPropertysValues] = None,
    ):
        self.id = id
        self.text = text
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.text is not None:
            result['Text'] = self.text
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = ListDistributionItemWithoutCacheResponseBodyModelSkuPropertysValues()
                self.values.append(temp_model.from_map(k))
        return self


class ListDistributionItemWithoutCacheResponseBodyModel(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        category_ids: List[int] = None,
        city: str = None,
        current: str = None,
        customized_attribute_map: Dict[str, str] = None,
        desc_option: str = None,
        desc_path: str = None,
        distribution_mall_id: str = None,
        features: Dict[str, str] = None,
        first_pic_url: str = None,
        has_quantity: bool = None,
        iforest_props: List[Dict[str, str]] = None,
        invoice_type: int = None,
        is_can_not_be_sold_code: str = None,
        is_can_not_be_sold_message: str = None,
        is_can_sell: bool = None,
        is_seller_pay_postfee: bool = None,
        item_id: int = None,
        item_images: List[str] = None,
        item_title: str = None,
        item_total_simple_value: str = None,
        item_total_value: int = None,
        lm_item_attribute_map: Dict[str, str] = None,
        lm_item_category: str = None,
        lm_item_id: str = None,
        main_pic_url: str = None,
        min_price: int = None,
        properties: Dict[str, List[str]] = None,
        prov: str = None,
        quantity: int = None,
        reserved_price: int = None,
        secured_transactions: int = None,
        simple_quantity: str = None,
        sku_models: List[ListDistributionItemWithoutCacheResponseBodyModelSkuModels] = None,
        sku_propertys: List[ListDistributionItemWithoutCacheResponseBodyModelSkuPropertys] = None,
        third_party_item_id: str = None,
        third_party_name: str = None,
        user_type: int = None,
        video_pic_url: str = None,
        video_url: str = None,
        virtual_item_type: str = None,
    ):
        self.category_id = category_id
        self.category_ids = category_ids
        self.city = city
        self.current = current
        self.customized_attribute_map = customized_attribute_map
        self.desc_option = desc_option
        self.desc_path = desc_path
        self.distribution_mall_id = distribution_mall_id
        self.features = features
        self.first_pic_url = first_pic_url
        self.has_quantity = has_quantity
        self.iforest_props = iforest_props
        self.invoice_type = invoice_type
        self.is_can_not_be_sold_code = is_can_not_be_sold_code
        self.is_can_not_be_sold_message = is_can_not_be_sold_message
        self.is_can_sell = is_can_sell
        self.is_seller_pay_postfee = is_seller_pay_postfee
        self.item_id = item_id
        self.item_images = item_images
        self.item_title = item_title
        self.item_total_simple_value = item_total_simple_value
        self.item_total_value = item_total_value
        self.lm_item_attribute_map = lm_item_attribute_map
        self.lm_item_category = lm_item_category
        self.lm_item_id = lm_item_id
        self.main_pic_url = main_pic_url
        self.min_price = min_price
        self.properties = properties
        self.prov = prov
        self.quantity = quantity
        self.reserved_price = reserved_price
        self.secured_transactions = secured_transactions
        self.simple_quantity = simple_quantity
        self.sku_models = sku_models
        self.sku_propertys = sku_propertys
        self.third_party_item_id = third_party_item_id
        self.third_party_name = third_party_name
        self.user_type = user_type
        self.video_pic_url = video_pic_url
        self.video_url = video_url
        self.virtual_item_type = virtual_item_type

    def validate(self):
        if self.sku_models:
            for k in self.sku_models:
                if k:
                    k.validate()
        if self.sku_propertys:
            for k in self.sku_propertys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.city is not None:
            result['City'] = self.city
        if self.current is not None:
            result['Current'] = self.current
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.desc_option is not None:
            result['DescOption'] = self.desc_option
        if self.desc_path is not None:
            result['DescPath'] = self.desc_path
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.features is not None:
            result['Features'] = self.features
        if self.first_pic_url is not None:
            result['FirstPicUrl'] = self.first_pic_url
        if self.has_quantity is not None:
            result['HasQuantity'] = self.has_quantity
        if self.iforest_props is not None:
            result['IforestProps'] = self.iforest_props
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.is_can_not_be_sold_code is not None:
            result['IsCanNotBeSoldCode'] = self.is_can_not_be_sold_code
        if self.is_can_not_be_sold_message is not None:
            result['IsCanNotBeSoldMessage'] = self.is_can_not_be_sold_message
        if self.is_can_sell is not None:
            result['IsCanSell'] = self.is_can_sell
        if self.is_seller_pay_postfee is not None:
            result['IsSellerPayPostfee'] = self.is_seller_pay_postfee
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_images is not None:
            result['ItemImages'] = self.item_images
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.item_total_simple_value is not None:
            result['ItemTotalSimpleValue'] = self.item_total_simple_value
        if self.item_total_value is not None:
            result['ItemTotalValue'] = self.item_total_value
        if self.lm_item_attribute_map is not None:
            result['LmItemAttributeMap'] = self.lm_item_attribute_map
        if self.lm_item_category is not None:
            result['LmItemCategory'] = self.lm_item_category
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.main_pic_url is not None:
            result['MainPicUrl'] = self.main_pic_url
        if self.min_price is not None:
            result['MinPrice'] = self.min_price
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.prov is not None:
            result['Prov'] = self.prov
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.secured_transactions is not None:
            result['SecuredTransactions'] = self.secured_transactions
        if self.simple_quantity is not None:
            result['SimpleQuantity'] = self.simple_quantity
        result['SkuModels'] = []
        if self.sku_models is not None:
            for k in self.sku_models:
                result['SkuModels'].append(k.to_map() if k else None)
        result['SkuPropertys'] = []
        if self.sku_propertys is not None:
            for k in self.sku_propertys:
                result['SkuPropertys'].append(k.to_map() if k else None)
        if self.third_party_item_id is not None:
            result['ThirdPartyItemId'] = self.third_party_item_id
        if self.third_party_name is not None:
            result['ThirdPartyName'] = self.third_party_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.video_pic_url is not None:
            result['VideoPicUrl'] = self.video_pic_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.virtual_item_type is not None:
            result['VirtualItemType'] = self.virtual_item_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('DescOption') is not None:
            self.desc_option = m.get('DescOption')
        if m.get('DescPath') is not None:
            self.desc_path = m.get('DescPath')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('FirstPicUrl') is not None:
            self.first_pic_url = m.get('FirstPicUrl')
        if m.get('HasQuantity') is not None:
            self.has_quantity = m.get('HasQuantity')
        if m.get('IforestProps') is not None:
            self.iforest_props = m.get('IforestProps')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('IsCanNotBeSoldCode') is not None:
            self.is_can_not_be_sold_code = m.get('IsCanNotBeSoldCode')
        if m.get('IsCanNotBeSoldMessage') is not None:
            self.is_can_not_be_sold_message = m.get('IsCanNotBeSoldMessage')
        if m.get('IsCanSell') is not None:
            self.is_can_sell = m.get('IsCanSell')
        if m.get('IsSellerPayPostfee') is not None:
            self.is_seller_pay_postfee = m.get('IsSellerPayPostfee')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemImages') is not None:
            self.item_images = m.get('ItemImages')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('ItemTotalSimpleValue') is not None:
            self.item_total_simple_value = m.get('ItemTotalSimpleValue')
        if m.get('ItemTotalValue') is not None:
            self.item_total_value = m.get('ItemTotalValue')
        if m.get('LmItemAttributeMap') is not None:
            self.lm_item_attribute_map = m.get('LmItemAttributeMap')
        if m.get('LmItemCategory') is not None:
            self.lm_item_category = m.get('LmItemCategory')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('MainPicUrl') is not None:
            self.main_pic_url = m.get('MainPicUrl')
        if m.get('MinPrice') is not None:
            self.min_price = m.get('MinPrice')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Prov') is not None:
            self.prov = m.get('Prov')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('SecuredTransactions') is not None:
            self.secured_transactions = m.get('SecuredTransactions')
        if m.get('SimpleQuantity') is not None:
            self.simple_quantity = m.get('SimpleQuantity')
        self.sku_models = []
        if m.get('SkuModels') is not None:
            for k in m.get('SkuModels'):
                temp_model = ListDistributionItemWithoutCacheResponseBodyModelSkuModels()
                self.sku_models.append(temp_model.from_map(k))
        self.sku_propertys = []
        if m.get('SkuPropertys') is not None:
            for k in m.get('SkuPropertys'):
                temp_model = ListDistributionItemWithoutCacheResponseBodyModelSkuPropertys()
                self.sku_propertys.append(temp_model.from_map(k))
        if m.get('ThirdPartyItemId') is not None:
            self.third_party_item_id = m.get('ThirdPartyItemId')
        if m.get('ThirdPartyName') is not None:
            self.third_party_name = m.get('ThirdPartyName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('VideoPicUrl') is not None:
            self.video_pic_url = m.get('VideoPicUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('VirtualItemType') is not None:
            self.virtual_item_type = m.get('VirtualItemType')
        return self


class ListDistributionItemWithoutCacheResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: List[ListDistributionItemWithoutCacheResponseBodyModel] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = ListDistributionItemWithoutCacheResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDistributionItemWithoutCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDistributionItemWithoutCacheResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDistributionItemWithoutCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDistributionMallRequest(TeaModel):
    def __init__(
        self,
        channel_supplier_id: str = None,
        distribution_mall_id: str = None,
        distribution_mall_name: str = None,
        distributor_id: str = None,
        end_date: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: str = None,
        tenant_id: str = None,
    ):
        self.channel_supplier_id = channel_supplier_id
        self.distribution_mall_id = distribution_mall_id
        self.distribution_mall_name = distribution_mall_name
        self.distributor_id = distributor_id
        self.end_date = end_date
        self.page_number = page_number
        self.page_size = page_size
        self.start_date = start_date
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_supplier_id is not None:
            result['ChannelSupplierId'] = self.channel_supplier_id
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distribution_mall_name is not None:
            result['DistributionMallName'] = self.distribution_mall_name
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelSupplierId') is not None:
            self.channel_supplier_id = m.get('ChannelSupplierId')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributionMallName') is not None:
            self.distribution_mall_name = m.get('DistributionMallName')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListDistributionMallResponseBodyModel(TeaModel):
    def __init__(
        self,
        channel_supplier_id: str = None,
        distribution_mall_id: str = None,
        distribution_mall_name: str = None,
        distribution_mall_type: str = None,
        end_date: str = None,
        start_date: str = None,
        status: str = None,
    ):
        self.channel_supplier_id = channel_supplier_id
        self.distribution_mall_id = distribution_mall_id
        self.distribution_mall_name = distribution_mall_name
        self.distribution_mall_type = distribution_mall_type
        self.end_date = end_date
        self.start_date = start_date
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_supplier_id is not None:
            result['ChannelSupplierId'] = self.channel_supplier_id
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distribution_mall_name is not None:
            result['DistributionMallName'] = self.distribution_mall_name
        if self.distribution_mall_type is not None:
            result['DistributionMallType'] = self.distribution_mall_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelSupplierId') is not None:
            self.channel_supplier_id = m.get('ChannelSupplierId')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributionMallName') is not None:
            self.distribution_mall_name = m.get('DistributionMallName')
        if m.get('DistributionMallType') is not None:
            self.distribution_mall_type = m.get('DistributionMallType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDistributionMallResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: List[ListDistributionMallResponseBodyModel] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = ListDistributionMallResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDistributionMallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDistributionMallResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDistributionMallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRefund4DistributionRequestLeavePictureLists(TeaModel):
    def __init__(
        self,
        desc: str = None,
        picture: str = None,
    ):
        self.desc = desc
        self.picture = picture

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.picture is not None:
            result['Picture'] = self.picture
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Picture') is not None:
            self.picture = m.get('Picture')
        return self


class ModifyRefund4DistributionRequest(TeaModel):
    def __init__(
        self,
        apply_reason_text_id: int = None,
        apply_refund_count: int = None,
        apply_refund_fee: int = None,
        biz_claim_type: int = None,
        dispute_id: int = None,
        distributor_id: str = None,
        goods_status: int = None,
        leave_message: str = None,
        leave_picture_lists: List[ModifyRefund4DistributionRequestLeavePictureLists] = None,
        sub_distribution_order_id: str = None,
        tenant_id: str = None,
    ):
        self.apply_reason_text_id = apply_reason_text_id
        self.apply_refund_count = apply_refund_count
        self.apply_refund_fee = apply_refund_fee
        self.biz_claim_type = biz_claim_type
        self.dispute_id = dispute_id
        self.distributor_id = distributor_id
        self.goods_status = goods_status
        self.leave_message = leave_message
        self.leave_picture_lists = leave_picture_lists
        self.sub_distribution_order_id = sub_distribution_order_id
        self.tenant_id = tenant_id

    def validate(self):
        if self.leave_picture_lists:
            for k in self.leave_picture_lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_reason_text_id is not None:
            result['ApplyReasonTextId'] = self.apply_reason_text_id
        if self.apply_refund_count is not None:
            result['ApplyRefundCount'] = self.apply_refund_count
        if self.apply_refund_fee is not None:
            result['ApplyRefundFee'] = self.apply_refund_fee
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.goods_status is not None:
            result['GoodsStatus'] = self.goods_status
        if self.leave_message is not None:
            result['LeaveMessage'] = self.leave_message
        result['LeavePictureLists'] = []
        if self.leave_picture_lists is not None:
            for k in self.leave_picture_lists:
                result['LeavePictureLists'].append(k.to_map() if k else None)
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyReasonTextId') is not None:
            self.apply_reason_text_id = m.get('ApplyReasonTextId')
        if m.get('ApplyRefundCount') is not None:
            self.apply_refund_count = m.get('ApplyRefundCount')
        if m.get('ApplyRefundFee') is not None:
            self.apply_refund_fee = m.get('ApplyRefundFee')
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('GoodsStatus') is not None:
            self.goods_status = m.get('GoodsStatus')
        if m.get('LeaveMessage') is not None:
            self.leave_message = m.get('LeaveMessage')
        self.leave_picture_lists = []
        if m.get('LeavePictureLists') is not None:
            for k in m.get('LeavePictureLists'):
                temp_model = ModifyRefund4DistributionRequestLeavePictureLists()
                self.leave_picture_lists.append(temp_model.from_map(k))
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ModifyRefund4DistributionShrinkRequest(TeaModel):
    def __init__(
        self,
        apply_reason_text_id: int = None,
        apply_refund_count: int = None,
        apply_refund_fee: int = None,
        biz_claim_type: int = None,
        dispute_id: int = None,
        distributor_id: str = None,
        goods_status: int = None,
        leave_message: str = None,
        leave_picture_lists_shrink: str = None,
        sub_distribution_order_id: str = None,
        tenant_id: str = None,
    ):
        self.apply_reason_text_id = apply_reason_text_id
        self.apply_refund_count = apply_refund_count
        self.apply_refund_fee = apply_refund_fee
        self.biz_claim_type = biz_claim_type
        self.dispute_id = dispute_id
        self.distributor_id = distributor_id
        self.goods_status = goods_status
        self.leave_message = leave_message
        self.leave_picture_lists_shrink = leave_picture_lists_shrink
        self.sub_distribution_order_id = sub_distribution_order_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_reason_text_id is not None:
            result['ApplyReasonTextId'] = self.apply_reason_text_id
        if self.apply_refund_count is not None:
            result['ApplyRefundCount'] = self.apply_refund_count
        if self.apply_refund_fee is not None:
            result['ApplyRefundFee'] = self.apply_refund_fee
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.goods_status is not None:
            result['GoodsStatus'] = self.goods_status
        if self.leave_message is not None:
            result['LeaveMessage'] = self.leave_message
        if self.leave_picture_lists_shrink is not None:
            result['LeavePictureLists'] = self.leave_picture_lists_shrink
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyReasonTextId') is not None:
            self.apply_reason_text_id = m.get('ApplyReasonTextId')
        if m.get('ApplyRefundCount') is not None:
            self.apply_refund_count = m.get('ApplyRefundCount')
        if m.get('ApplyRefundFee') is not None:
            self.apply_refund_fee = m.get('ApplyRefundFee')
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('GoodsStatus') is not None:
            self.goods_status = m.get('GoodsStatus')
        if m.get('LeaveMessage') is not None:
            self.leave_message = m.get('LeaveMessage')
        if m.get('LeavePictureLists') is not None:
            self.leave_picture_lists_shrink = m.get('LeavePictureLists')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ModifyRefund4DistributionResponseBodyModel(TeaModel):
    def __init__(
        self,
        dispute_id: int = None,
        dispute_status: int = None,
        dispute_type: int = None,
        sub_distribution_order_id: str = None,
    ):
        self.dispute_id = dispute_id
        self.dispute_status = dispute_status
        self.dispute_type = dispute_type
        self.sub_distribution_order_id = sub_distribution_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.dispute_status is not None:
            result['DisputeStatus'] = self.dispute_status
        if self.dispute_type is not None:
            result['DisputeType'] = self.dispute_type
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DisputeStatus') is not None:
            self.dispute_status = m.get('DisputeStatus')
        if m.get('DisputeType') is not None:
            self.dispute_type = m.get('DisputeType')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        return self


class ModifyRefund4DistributionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: ModifyRefund4DistributionResponseBodyModel = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = ModifyRefund4DistributionResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ModifyRefund4DistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyRefund4DistributionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyRefund4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryChildDivisionCodeByIdRequest(TeaModel):
    def __init__(
        self,
        distributor_id: str = None,
        division_code: str = None,
        tenant_id: str = None,
    ):
        self.distributor_id = distributor_id
        self.division_code = division_code
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryChildDivisionCodeByIdResponseBodyModelDivisionList(TeaModel):
    def __init__(
        self,
        division_code: int = None,
        division_level: int = None,
        division_name: str = None,
        parent_id: int = None,
        pinyin: str = None,
    ):
        self.division_code = division_code
        self.division_level = division_level
        self.division_name = division_name
        self.parent_id = parent_id
        self.pinyin = pinyin

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        if self.division_level is not None:
            result['DivisionLevel'] = self.division_level
        if self.division_name is not None:
            result['DivisionName'] = self.division_name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.pinyin is not None:
            result['Pinyin'] = self.pinyin
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        if m.get('DivisionLevel') is not None:
            self.division_level = m.get('DivisionLevel')
        if m.get('DivisionName') is not None:
            self.division_name = m.get('DivisionName')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Pinyin') is not None:
            self.pinyin = m.get('Pinyin')
        return self


class QueryChildDivisionCodeByIdResponseBodyModel(TeaModel):
    def __init__(
        self,
        division_list: List[QueryChildDivisionCodeByIdResponseBodyModelDivisionList] = None,
    ):
        self.division_list = division_list

    def validate(self):
        if self.division_list:
            for k in self.division_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DivisionList'] = []
        if self.division_list is not None:
            for k in self.division_list:
                result['DivisionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.division_list = []
        if m.get('DivisionList') is not None:
            for k in m.get('DivisionList'):
                temp_model = QueryChildDivisionCodeByIdResponseBodyModelDivisionList()
                self.division_list.append(temp_model.from_map(k))
        return self


class QueryChildDivisionCodeByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: QueryChildDivisionCodeByIdResponseBodyModel = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryChildDivisionCodeByIdResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryChildDivisionCodeByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryChildDivisionCodeByIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryChildDivisionCodeByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDistributionBillDetailRequest(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        bill_period: str = None,
        bill_status: str = None,
        distribution_mall_id: str = None,
        distribution_mall_name: str = None,
        distributor_id: str = None,
        page_number: int = None,
        page_size: int = None,
        tenant_id: str = None,
    ):
        self.bill_id = bill_id
        self.bill_period = bill_period
        self.bill_status = bill_status
        self.distribution_mall_id = distribution_mall_id
        self.distribution_mall_name = distribution_mall_name
        self.distributor_id = distributor_id
        self.page_number = page_number
        self.page_size = page_size
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.bill_period is not None:
            result['BillPeriod'] = self.bill_period
        if self.bill_status is not None:
            result['BillStatus'] = self.bill_status
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distribution_mall_name is not None:
            result['DistributionMallName'] = self.distribution_mall_name
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('BillPeriod') is not None:
            self.bill_period = m.get('BillPeriod')
        if m.get('BillStatus') is not None:
            self.bill_status = m.get('BillStatus')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributionMallName') is not None:
            self.distribution_mall_name = m.get('DistributionMallName')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryDistributionBillDetailResponseBodyModel(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryDistributionBillDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: QueryDistributionBillDetailResponseBodyModel = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryDistributionBillDetailResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDistributionBillDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDistributionBillDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryDistributionBillDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDistributionMallRequest(TeaModel):
    def __init__(
        self,
        distribution_mall_id: str = None,
        tenant_id: str = None,
    ):
        self.distribution_mall_id = distribution_mall_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryDistributionMallResponseBodyModel(TeaModel):
    def __init__(
        self,
        channel_supplier_id: str = None,
        distribution_mall_id: str = None,
        distribution_mall_name: str = None,
        distribution_mall_type: str = None,
        distributor_id: str = None,
        end_date: str = None,
        start_date: str = None,
        status: str = None,
    ):
        self.channel_supplier_id = channel_supplier_id
        self.distribution_mall_id = distribution_mall_id
        self.distribution_mall_name = distribution_mall_name
        self.distribution_mall_type = distribution_mall_type
        self.distributor_id = distributor_id
        self.end_date = end_date
        self.start_date = start_date
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_supplier_id is not None:
            result['ChannelSupplierId'] = self.channel_supplier_id
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distribution_mall_name is not None:
            result['DistributionMallName'] = self.distribution_mall_name
        if self.distribution_mall_type is not None:
            result['DistributionMallType'] = self.distribution_mall_type
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelSupplierId') is not None:
            self.channel_supplier_id = m.get('ChannelSupplierId')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributionMallName') is not None:
            self.distribution_mall_name = m.get('DistributionMallName')
        if m.get('DistributionMallType') is not None:
            self.distribution_mall_type = m.get('DistributionMallType')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryDistributionMallResponseBody(TeaModel):
    def __init__(
        self,
        biz_view_data: Dict[str, Any] = None,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: QueryDistributionMallResponseBodyModel = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.biz_view_data = biz_view_data
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_view_data is not None:
            result['BizViewData'] = self.biz_view_data
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizViewData') is not None:
            self.biz_view_data = m.get('BizViewData')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryDistributionMallResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryDistributionMallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDistributionMallResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryDistributionMallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDistributionTradeStatusRequest(TeaModel):
    def __init__(
        self,
        distribution_supplier_id: str = None,
        distribution_trade_id: str = None,
        distributor_id: str = None,
        tenant_id: str = None,
    ):
        self.distribution_supplier_id = distribution_supplier_id
        self.distribution_trade_id = distribution_trade_id
        self.distributor_id = distributor_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_supplier_id is not None:
            result['DistributionSupplierId'] = self.distribution_supplier_id
        if self.distribution_trade_id is not None:
            result['DistributionTradeId'] = self.distribution_trade_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributionSupplierId') is not None:
            self.distribution_supplier_id = m.get('DistributionSupplierId')
        if m.get('DistributionTradeId') is not None:
            self.distribution_trade_id = m.get('DistributionTradeId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryDistributionTradeStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryDistributionTradeStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDistributionTradeStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryDistributionTradeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryItemDetailRequest(TeaModel):
    def __init__(
        self,
        distribution_mall_id: str = None,
        distributor_id: str = None,
        lm_item_id: str = None,
        tenant_id: str = None,
    ):
        self.distribution_mall_id = distribution_mall_id
        self.distributor_id = distributor_id
        self.lm_item_id = lm_item_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryItemDetailResponseBodyModelSkuModels(TeaModel):
    def __init__(
        self,
        can_not_be_sold_code: str = None,
        can_not_be_sold_message: str = None,
        customized_attribute_map: Dict[str, str] = None,
        distribution_mall_id: str = None,
        ext_json: str = None,
        has_quantity: bool = None,
        invoice_type: int = None,
        item_id: int = None,
        lm_item_id: str = None,
        lm_sku_attribute_map: Dict[str, str] = None,
        price_cent: int = None,
        quantity: int = None,
        reserved_price: int = None,
        simple_quantity: str = None,
        sku_id: int = None,
        sku_pic_url: str = None,
        sku_pvs: str = None,
        sku_title: str = None,
        status: int = None,
    ):
        self.can_not_be_sold_code = can_not_be_sold_code
        self.can_not_be_sold_message = can_not_be_sold_message
        self.customized_attribute_map = customized_attribute_map
        self.distribution_mall_id = distribution_mall_id
        self.ext_json = ext_json
        self.has_quantity = has_quantity
        self.invoice_type = invoice_type
        self.item_id = item_id
        self.lm_item_id = lm_item_id
        self.lm_sku_attribute_map = lm_sku_attribute_map
        self.price_cent = price_cent
        self.quantity = quantity
        self.reserved_price = reserved_price
        self.simple_quantity = simple_quantity
        self.sku_id = sku_id
        self.sku_pic_url = sku_pic_url
        self.sku_pvs = sku_pvs
        self.sku_title = sku_title
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_not_be_sold_code is not None:
            result['CanNotBeSoldCode'] = self.can_not_be_sold_code
        if self.can_not_be_sold_message is not None:
            result['CanNotBeSoldMessage'] = self.can_not_be_sold_message
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.has_quantity is not None:
            result['HasQuantity'] = self.has_quantity
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.lm_sku_attribute_map is not None:
            result['LmSkuAttributeMap'] = self.lm_sku_attribute_map
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.simple_quantity is not None:
            result['SimpleQuantity'] = self.simple_quantity
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_pic_url is not None:
            result['SkuPicUrl'] = self.sku_pic_url
        if self.sku_pvs is not None:
            result['SkuPvs'] = self.sku_pvs
        if self.sku_title is not None:
            result['SkuTitle'] = self.sku_title
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanNotBeSoldCode') is not None:
            self.can_not_be_sold_code = m.get('CanNotBeSoldCode')
        if m.get('CanNotBeSoldMessage') is not None:
            self.can_not_be_sold_message = m.get('CanNotBeSoldMessage')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('HasQuantity') is not None:
            self.has_quantity = m.get('HasQuantity')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LmSkuAttributeMap') is not None:
            self.lm_sku_attribute_map = m.get('LmSkuAttributeMap')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('SimpleQuantity') is not None:
            self.simple_quantity = m.get('SimpleQuantity')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuPicUrl') is not None:
            self.sku_pic_url = m.get('SkuPicUrl')
        if m.get('SkuPvs') is not None:
            self.sku_pvs = m.get('SkuPvs')
        if m.get('SkuTitle') is not None:
            self.sku_title = m.get('SkuTitle')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryItemDetailResponseBodyModelSkuPropertysValues(TeaModel):
    def __init__(
        self,
        id: int = None,
        text: str = None,
    ):
        self.id = id
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class QueryItemDetailResponseBodyModelSkuPropertys(TeaModel):
    def __init__(
        self,
        id: int = None,
        text: str = None,
        values: List[QueryItemDetailResponseBodyModelSkuPropertysValues] = None,
    ):
        self.id = id
        self.text = text
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.text is not None:
            result['Text'] = self.text
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = QueryItemDetailResponseBodyModelSkuPropertysValues()
                self.values.append(temp_model.from_map(k))
        return self


class QueryItemDetailResponseBodyModel(TeaModel):
    def __init__(
        self,
        can_not_be_sold_code: str = None,
        can_not_be_sold_message: str = None,
        category_id: int = None,
        category_ids: List[int] = None,
        city: str = None,
        current: str = None,
        customized_attribute_map: Dict[str, str] = None,
        desc_option: str = None,
        desc_path: str = None,
        distribution_mall_id: str = None,
        features: Dict[str, str] = None,
        first_pic_url: str = None,
        has_quantity: bool = None,
        iforest_props: List[Dict[str, str]] = None,
        invoice_type: int = None,
        is_can_sell: bool = None,
        is_seller_pay_postfee: bool = None,
        item_id: int = None,
        item_images: List[str] = None,
        item_title: str = None,
        item_total_simple_value: str = None,
        item_total_value: int = None,
        lm_item_attribute_map: Dict[str, str] = None,
        lm_item_category: str = None,
        lm_item_id: str = None,
        main_pic_url: str = None,
        min_price: int = None,
        properties: Dict[str, List[str]] = None,
        prov: str = None,
        quantity: int = None,
        reserved_price: int = None,
        simple_quantity: str = None,
        sku_models: List[QueryItemDetailResponseBodyModelSkuModels] = None,
        sku_propertys: List[QueryItemDetailResponseBodyModelSkuPropertys] = None,
        third_party_item_id: str = None,
        third_party_name: str = None,
        video_pic_url: str = None,
        video_url: str = None,
        virtual_item_type: str = None,
    ):
        self.can_not_be_sold_code = can_not_be_sold_code
        self.can_not_be_sold_message = can_not_be_sold_message
        self.category_id = category_id
        self.category_ids = category_ids
        self.city = city
        self.current = current
        self.customized_attribute_map = customized_attribute_map
        self.desc_option = desc_option
        self.desc_path = desc_path
        self.distribution_mall_id = distribution_mall_id
        self.features = features
        self.first_pic_url = first_pic_url
        self.has_quantity = has_quantity
        self.iforest_props = iforest_props
        self.invoice_type = invoice_type
        self.is_can_sell = is_can_sell
        self.is_seller_pay_postfee = is_seller_pay_postfee
        self.item_id = item_id
        self.item_images = item_images
        self.item_title = item_title
        self.item_total_simple_value = item_total_simple_value
        self.item_total_value = item_total_value
        self.lm_item_attribute_map = lm_item_attribute_map
        self.lm_item_category = lm_item_category
        self.lm_item_id = lm_item_id
        self.main_pic_url = main_pic_url
        self.min_price = min_price
        self.properties = properties
        self.prov = prov
        self.quantity = quantity
        self.reserved_price = reserved_price
        self.simple_quantity = simple_quantity
        # sku list
        self.sku_models = sku_models
        self.sku_propertys = sku_propertys
        self.third_party_item_id = third_party_item_id
        self.third_party_name = third_party_name
        self.video_pic_url = video_pic_url
        self.video_url = video_url
        self.virtual_item_type = virtual_item_type

    def validate(self):
        if self.sku_models:
            for k in self.sku_models:
                if k:
                    k.validate()
        if self.sku_propertys:
            for k in self.sku_propertys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_not_be_sold_code is not None:
            result['CanNotBeSoldCode'] = self.can_not_be_sold_code
        if self.can_not_be_sold_message is not None:
            result['CanNotBeSoldMessage'] = self.can_not_be_sold_message
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.city is not None:
            result['City'] = self.city
        if self.current is not None:
            result['Current'] = self.current
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.desc_option is not None:
            result['DescOption'] = self.desc_option
        if self.desc_path is not None:
            result['DescPath'] = self.desc_path
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.features is not None:
            result['Features'] = self.features
        if self.first_pic_url is not None:
            result['FirstPicUrl'] = self.first_pic_url
        if self.has_quantity is not None:
            result['HasQuantity'] = self.has_quantity
        if self.iforest_props is not None:
            result['IforestProps'] = self.iforest_props
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.is_can_sell is not None:
            result['IsCanSell'] = self.is_can_sell
        if self.is_seller_pay_postfee is not None:
            result['IsSellerPayPostfee'] = self.is_seller_pay_postfee
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_images is not None:
            result['ItemImages'] = self.item_images
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.item_total_simple_value is not None:
            result['ItemTotalSimpleValue'] = self.item_total_simple_value
        if self.item_total_value is not None:
            result['ItemTotalValue'] = self.item_total_value
        if self.lm_item_attribute_map is not None:
            result['LmItemAttributeMap'] = self.lm_item_attribute_map
        if self.lm_item_category is not None:
            result['LmItemCategory'] = self.lm_item_category
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.main_pic_url is not None:
            result['MainPicUrl'] = self.main_pic_url
        if self.min_price is not None:
            result['MinPrice'] = self.min_price
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.prov is not None:
            result['Prov'] = self.prov
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.simple_quantity is not None:
            result['SimpleQuantity'] = self.simple_quantity
        result['SkuModels'] = []
        if self.sku_models is not None:
            for k in self.sku_models:
                result['SkuModels'].append(k.to_map() if k else None)
        result['SkuPropertys'] = []
        if self.sku_propertys is not None:
            for k in self.sku_propertys:
                result['SkuPropertys'].append(k.to_map() if k else None)
        if self.third_party_item_id is not None:
            result['ThirdPartyItemId'] = self.third_party_item_id
        if self.third_party_name is not None:
            result['ThirdPartyName'] = self.third_party_name
        if self.video_pic_url is not None:
            result['VideoPicUrl'] = self.video_pic_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.virtual_item_type is not None:
            result['VirtualItemType'] = self.virtual_item_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanNotBeSoldCode') is not None:
            self.can_not_be_sold_code = m.get('CanNotBeSoldCode')
        if m.get('CanNotBeSoldMessage') is not None:
            self.can_not_be_sold_message = m.get('CanNotBeSoldMessage')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('DescOption') is not None:
            self.desc_option = m.get('DescOption')
        if m.get('DescPath') is not None:
            self.desc_path = m.get('DescPath')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('FirstPicUrl') is not None:
            self.first_pic_url = m.get('FirstPicUrl')
        if m.get('HasQuantity') is not None:
            self.has_quantity = m.get('HasQuantity')
        if m.get('IforestProps') is not None:
            self.iforest_props = m.get('IforestProps')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('IsCanSell') is not None:
            self.is_can_sell = m.get('IsCanSell')
        if m.get('IsSellerPayPostfee') is not None:
            self.is_seller_pay_postfee = m.get('IsSellerPayPostfee')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemImages') is not None:
            self.item_images = m.get('ItemImages')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('ItemTotalSimpleValue') is not None:
            self.item_total_simple_value = m.get('ItemTotalSimpleValue')
        if m.get('ItemTotalValue') is not None:
            self.item_total_value = m.get('ItemTotalValue')
        if m.get('LmItemAttributeMap') is not None:
            self.lm_item_attribute_map = m.get('LmItemAttributeMap')
        if m.get('LmItemCategory') is not None:
            self.lm_item_category = m.get('LmItemCategory')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('MainPicUrl') is not None:
            self.main_pic_url = m.get('MainPicUrl')
        if m.get('MinPrice') is not None:
            self.min_price = m.get('MinPrice')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Prov') is not None:
            self.prov = m.get('Prov')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('SimpleQuantity') is not None:
            self.simple_quantity = m.get('SimpleQuantity')
        self.sku_models = []
        if m.get('SkuModels') is not None:
            for k in m.get('SkuModels'):
                temp_model = QueryItemDetailResponseBodyModelSkuModels()
                self.sku_models.append(temp_model.from_map(k))
        self.sku_propertys = []
        if m.get('SkuPropertys') is not None:
            for k in m.get('SkuPropertys'):
                temp_model = QueryItemDetailResponseBodyModelSkuPropertys()
                self.sku_propertys.append(temp_model.from_map(k))
        if m.get('ThirdPartyItemId') is not None:
            self.third_party_item_id = m.get('ThirdPartyItemId')
        if m.get('ThirdPartyName') is not None:
            self.third_party_name = m.get('ThirdPartyName')
        if m.get('VideoPicUrl') is not None:
            self.video_pic_url = m.get('VideoPicUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('VirtualItemType') is not None:
            self.virtual_item_type = m.get('VirtualItemType')
        return self


class QueryItemDetailResponseBody(TeaModel):
    def __init__(
        self,
        biz_view_data: Dict[str, Any] = None,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: QueryItemDetailResponseBodyModel = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.biz_view_data = biz_view_data
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_view_data is not None:
            result['BizViewData'] = self.biz_view_data
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizViewData') is not None:
            self.biz_view_data = m.get('BizViewData')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryItemDetailResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryItemDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryItemDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryItemDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryItemDetailWithDivisionRequest(TeaModel):
    def __init__(
        self,
        distribution_mall_id: str = None,
        distributor_id: str = None,
        division_code: str = None,
        lm_item_id: str = None,
        tenant_id: str = None,
    ):
        self.distribution_mall_id = distribution_mall_id
        self.distributor_id = distributor_id
        self.division_code = division_code
        self.lm_item_id = lm_item_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryItemDetailWithDivisionResponseBodyModelSkuModels(TeaModel):
    def __init__(
        self,
        can_not_be_sold_code: str = None,
        can_not_be_sold_massage: str = None,
        customized_attribute_map: Dict[str, str] = None,
        distribution_mall_id: str = None,
        ext_json: str = None,
        has_quantity: bool = None,
        invoice_type: int = None,
        item_id: int = None,
        lm_item_id: str = None,
        lm_sku_attribute_map: Dict[str, str] = None,
        price_cent: int = None,
        quantity: int = None,
        reserve_price: int = None,
        simple_quantity: str = None,
        sku_id: int = None,
        sku_pic_url: str = None,
        sku_pvs: str = None,
        sku_title: str = None,
        status: int = None,
        supplier_price: int = None,
    ):
        self.can_not_be_sold_code = can_not_be_sold_code
        self.can_not_be_sold_massage = can_not_be_sold_massage
        self.customized_attribute_map = customized_attribute_map
        self.distribution_mall_id = distribution_mall_id
        self.ext_json = ext_json
        self.has_quantity = has_quantity
        self.invoice_type = invoice_type
        self.item_id = item_id
        self.lm_item_id = lm_item_id
        self.lm_sku_attribute_map = lm_sku_attribute_map
        self.price_cent = price_cent
        self.quantity = quantity
        self.reserve_price = reserve_price
        self.simple_quantity = simple_quantity
        self.sku_id = sku_id
        self.sku_pic_url = sku_pic_url
        self.sku_pvs = sku_pvs
        self.sku_title = sku_title
        self.status = status
        self.supplier_price = supplier_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_not_be_sold_code is not None:
            result['CanNotBeSoldCode'] = self.can_not_be_sold_code
        if self.can_not_be_sold_massage is not None:
            result['CanNotBeSoldMassage'] = self.can_not_be_sold_massage
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.has_quantity is not None:
            result['HasQuantity'] = self.has_quantity
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.lm_sku_attribute_map is not None:
            result['LmSkuAttributeMap'] = self.lm_sku_attribute_map
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.simple_quantity is not None:
            result['SimpleQuantity'] = self.simple_quantity
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_pic_url is not None:
            result['SkuPicUrl'] = self.sku_pic_url
        if self.sku_pvs is not None:
            result['SkuPvs'] = self.sku_pvs
        if self.sku_title is not None:
            result['SkuTitle'] = self.sku_title
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_price is not None:
            result['SupplierPrice'] = self.supplier_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanNotBeSoldCode') is not None:
            self.can_not_be_sold_code = m.get('CanNotBeSoldCode')
        if m.get('CanNotBeSoldMassage') is not None:
            self.can_not_be_sold_massage = m.get('CanNotBeSoldMassage')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('HasQuantity') is not None:
            self.has_quantity = m.get('HasQuantity')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LmSkuAttributeMap') is not None:
            self.lm_sku_attribute_map = m.get('LmSkuAttributeMap')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('SimpleQuantity') is not None:
            self.simple_quantity = m.get('SimpleQuantity')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuPicUrl') is not None:
            self.sku_pic_url = m.get('SkuPicUrl')
        if m.get('SkuPvs') is not None:
            self.sku_pvs = m.get('SkuPvs')
        if m.get('SkuTitle') is not None:
            self.sku_title = m.get('SkuTitle')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierPrice') is not None:
            self.supplier_price = m.get('SupplierPrice')
        return self


class QueryItemDetailWithDivisionResponseBodyModelSkuPropertysValues(TeaModel):
    def __init__(
        self,
        id: int = None,
        text: str = None,
    ):
        self.id = id
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class QueryItemDetailWithDivisionResponseBodyModelSkuPropertys(TeaModel):
    def __init__(
        self,
        id: int = None,
        text: str = None,
        values: List[QueryItemDetailWithDivisionResponseBodyModelSkuPropertysValues] = None,
    ):
        self.id = id
        self.text = text
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.text is not None:
            result['Text'] = self.text
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = QueryItemDetailWithDivisionResponseBodyModelSkuPropertysValues()
                self.values.append(temp_model.from_map(k))
        return self


class QueryItemDetailWithDivisionResponseBodyModel(TeaModel):
    def __init__(
        self,
        can_not_be_sold_code: str = None,
        can_not_be_sold_massage: str = None,
        can_sell: bool = None,
        category_id: int = None,
        category_ids: List[int] = None,
        city: str = None,
        current: str = None,
        customized_attribute_map: Dict[str, str] = None,
        desc_option: str = None,
        desc_path: str = None,
        distribution_mall_id: str = None,
        features: Dict[str, str] = None,
        first_pic_url: str = None,
        has_quantity: bool = None,
        iforest_props: List[Dict[str, str]] = None,
        invoice_type: int = None,
        item_id: int = None,
        item_images: List[str] = None,
        item_title: str = None,
        item_total_simple_value: str = None,
        item_total_value: int = None,
        lm_item_attribute_map: Dict[str, str] = None,
        lm_item_category: str = None,
        lm_item_id: str = None,
        main_pic_url: str = None,
        min_price: int = None,
        properties: Dict[str, List[str]] = None,
        prov: str = None,
        quantity: int = None,
        reserve_price: int = None,
        secured_transactions: int = None,
        seller_pay_postfee: bool = None,
        simple_quantity: str = None,
        sku_models: List[QueryItemDetailWithDivisionResponseBodyModelSkuModels] = None,
        sku_propertys: List[QueryItemDetailWithDivisionResponseBodyModelSkuPropertys] = None,
        third_party_item_id: str = None,
        third_party_name: str = None,
        user_type: int = None,
        video_pic_url: str = None,
        video_url: str = None,
        virtual_item_type: str = None,
    ):
        self.can_not_be_sold_code = can_not_be_sold_code
        self.can_not_be_sold_massage = can_not_be_sold_massage
        self.can_sell = can_sell
        self.category_id = category_id
        self.category_ids = category_ids
        self.city = city
        self.current = current
        self.customized_attribute_map = customized_attribute_map
        self.desc_option = desc_option
        self.desc_path = desc_path
        self.distribution_mall_id = distribution_mall_id
        self.features = features
        self.first_pic_url = first_pic_url
        self.has_quantity = has_quantity
        self.iforest_props = iforest_props
        self.invoice_type = invoice_type
        self.item_id = item_id
        self.item_images = item_images
        self.item_title = item_title
        self.item_total_simple_value = item_total_simple_value
        self.item_total_value = item_total_value
        self.lm_item_attribute_map = lm_item_attribute_map
        self.lm_item_category = lm_item_category
        self.lm_item_id = lm_item_id
        self.main_pic_url = main_pic_url
        self.min_price = min_price
        self.properties = properties
        self.prov = prov
        self.quantity = quantity
        self.reserve_price = reserve_price
        self.secured_transactions = secured_transactions
        self.seller_pay_postfee = seller_pay_postfee
        self.simple_quantity = simple_quantity
        # sku list
        self.sku_models = sku_models
        self.sku_propertys = sku_propertys
        self.third_party_item_id = third_party_item_id
        self.third_party_name = third_party_name
        self.user_type = user_type
        self.video_pic_url = video_pic_url
        self.video_url = video_url
        self.virtual_item_type = virtual_item_type

    def validate(self):
        if self.sku_models:
            for k in self.sku_models:
                if k:
                    k.validate()
        if self.sku_propertys:
            for k in self.sku_propertys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_not_be_sold_code is not None:
            result['CanNotBeSoldCode'] = self.can_not_be_sold_code
        if self.can_not_be_sold_massage is not None:
            result['CanNotBeSoldMassage'] = self.can_not_be_sold_massage
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.city is not None:
            result['City'] = self.city
        if self.current is not None:
            result['Current'] = self.current
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.desc_option is not None:
            result['DescOption'] = self.desc_option
        if self.desc_path is not None:
            result['DescPath'] = self.desc_path
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.features is not None:
            result['Features'] = self.features
        if self.first_pic_url is not None:
            result['FirstPicUrl'] = self.first_pic_url
        if self.has_quantity is not None:
            result['HasQuantity'] = self.has_quantity
        if self.iforest_props is not None:
            result['IforestProps'] = self.iforest_props
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_images is not None:
            result['ItemImages'] = self.item_images
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.item_total_simple_value is not None:
            result['ItemTotalSimpleValue'] = self.item_total_simple_value
        if self.item_total_value is not None:
            result['ItemTotalValue'] = self.item_total_value
        if self.lm_item_attribute_map is not None:
            result['LmItemAttributeMap'] = self.lm_item_attribute_map
        if self.lm_item_category is not None:
            result['LmItemCategory'] = self.lm_item_category
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.main_pic_url is not None:
            result['MainPicUrl'] = self.main_pic_url
        if self.min_price is not None:
            result['MinPrice'] = self.min_price
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.prov is not None:
            result['Prov'] = self.prov
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.secured_transactions is not None:
            result['SecuredTransactions'] = self.secured_transactions
        if self.seller_pay_postfee is not None:
            result['SellerPayPostfee'] = self.seller_pay_postfee
        if self.simple_quantity is not None:
            result['SimpleQuantity'] = self.simple_quantity
        result['SkuModels'] = []
        if self.sku_models is not None:
            for k in self.sku_models:
                result['SkuModels'].append(k.to_map() if k else None)
        result['SkuPropertys'] = []
        if self.sku_propertys is not None:
            for k in self.sku_propertys:
                result['SkuPropertys'].append(k.to_map() if k else None)
        if self.third_party_item_id is not None:
            result['ThirdPartyItemId'] = self.third_party_item_id
        if self.third_party_name is not None:
            result['ThirdPartyName'] = self.third_party_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.video_pic_url is not None:
            result['VideoPicUrl'] = self.video_pic_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.virtual_item_type is not None:
            result['VirtualItemType'] = self.virtual_item_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanNotBeSoldCode') is not None:
            self.can_not_be_sold_code = m.get('CanNotBeSoldCode')
        if m.get('CanNotBeSoldMassage') is not None:
            self.can_not_be_sold_massage = m.get('CanNotBeSoldMassage')
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('DescOption') is not None:
            self.desc_option = m.get('DescOption')
        if m.get('DescPath') is not None:
            self.desc_path = m.get('DescPath')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('FirstPicUrl') is not None:
            self.first_pic_url = m.get('FirstPicUrl')
        if m.get('HasQuantity') is not None:
            self.has_quantity = m.get('HasQuantity')
        if m.get('IforestProps') is not None:
            self.iforest_props = m.get('IforestProps')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemImages') is not None:
            self.item_images = m.get('ItemImages')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('ItemTotalSimpleValue') is not None:
            self.item_total_simple_value = m.get('ItemTotalSimpleValue')
        if m.get('ItemTotalValue') is not None:
            self.item_total_value = m.get('ItemTotalValue')
        if m.get('LmItemAttributeMap') is not None:
            self.lm_item_attribute_map = m.get('LmItemAttributeMap')
        if m.get('LmItemCategory') is not None:
            self.lm_item_category = m.get('LmItemCategory')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('MainPicUrl') is not None:
            self.main_pic_url = m.get('MainPicUrl')
        if m.get('MinPrice') is not None:
            self.min_price = m.get('MinPrice')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Prov') is not None:
            self.prov = m.get('Prov')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('SecuredTransactions') is not None:
            self.secured_transactions = m.get('SecuredTransactions')
        if m.get('SellerPayPostfee') is not None:
            self.seller_pay_postfee = m.get('SellerPayPostfee')
        if m.get('SimpleQuantity') is not None:
            self.simple_quantity = m.get('SimpleQuantity')
        self.sku_models = []
        if m.get('SkuModels') is not None:
            for k in m.get('SkuModels'):
                temp_model = QueryItemDetailWithDivisionResponseBodyModelSkuModels()
                self.sku_models.append(temp_model.from_map(k))
        self.sku_propertys = []
        if m.get('SkuPropertys') is not None:
            for k in m.get('SkuPropertys'):
                temp_model = QueryItemDetailWithDivisionResponseBodyModelSkuPropertys()
                self.sku_propertys.append(temp_model.from_map(k))
        if m.get('ThirdPartyItemId') is not None:
            self.third_party_item_id = m.get('ThirdPartyItemId')
        if m.get('ThirdPartyName') is not None:
            self.third_party_name = m.get('ThirdPartyName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('VideoPicUrl') is not None:
            self.video_pic_url = m.get('VideoPicUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('VirtualItemType') is not None:
            self.virtual_item_type = m.get('VirtualItemType')
        return self


class QueryItemDetailWithDivisionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: QueryItemDetailWithDivisionResponseBodyModel = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryItemDetailWithDivisionResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryItemDetailWithDivisionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryItemDetailWithDivisionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryItemDetailWithDivisionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryItemGuideRetailPriceRequest(TeaModel):
    def __init__(
        self,
        distribution_mall_id: str = None,
        distributor_id: str = None,
        lm_item_ids: List[str] = None,
        tenant_id: str = None,
    ):
        self.distribution_mall_id = distribution_mall_id
        self.distributor_id = distributor_id
        self.lm_item_ids = lm_item_ids
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.lm_item_ids is not None:
            result['LmItemIds'] = self.lm_item_ids
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('LmItemIds') is not None:
            self.lm_item_ids = m.get('LmItemIds')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryItemGuideRetailPriceShrinkRequest(TeaModel):
    def __init__(
        self,
        distribution_mall_id: str = None,
        distributor_id: str = None,
        lm_item_ids_shrink: str = None,
        tenant_id: str = None,
    ):
        self.distribution_mall_id = distribution_mall_id
        self.distributor_id = distributor_id
        self.lm_item_ids_shrink = lm_item_ids_shrink
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.lm_item_ids_shrink is not None:
            result['LmItemIds'] = self.lm_item_ids_shrink
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('LmItemIds') is not None:
            self.lm_item_ids_shrink = m.get('LmItemIds')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryItemGuideRetailPriceResponseBodyModelSkuModels(TeaModel):
    def __init__(
        self,
        distribution_mall_id: str = None,
        guide_retail_price: int = None,
        item_id: int = None,
        lm_item_id: str = None,
        low_guide_retail_price: int = None,
        price_cent: int = None,
        reserved_price: int = None,
        sku_id: int = None,
        sku_title: str = None,
        status: int = None,
    ):
        self.distribution_mall_id = distribution_mall_id
        self.guide_retail_price = guide_retail_price
        self.item_id = item_id
        self.lm_item_id = lm_item_id
        self.low_guide_retail_price = low_guide_retail_price
        self.price_cent = price_cent
        self.reserved_price = reserved_price
        self.sku_id = sku_id
        self.sku_title = sku_title
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.guide_retail_price is not None:
            result['GuideRetailPrice'] = self.guide_retail_price
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.low_guide_retail_price is not None:
            result['LowGuideRetailPrice'] = self.low_guide_retail_price
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_title is not None:
            result['SkuTitle'] = self.sku_title
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('GuideRetailPrice') is not None:
            self.guide_retail_price = m.get('GuideRetailPrice')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LowGuideRetailPrice') is not None:
            self.low_guide_retail_price = m.get('LowGuideRetailPrice')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuTitle') is not None:
            self.sku_title = m.get('SkuTitle')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryItemGuideRetailPriceResponseBodyModel(TeaModel):
    def __init__(
        self,
        distribution_mall_id: str = None,
        guide_retail_price_scope: str = None,
        item_id: int = None,
        item_title: str = None,
        lm_item_id: str = None,
        low_guide_retail_price_scope: str = None,
        reserved_price: int = None,
        reserved_price_scope: str = None,
        sku_models: List[QueryItemGuideRetailPriceResponseBodyModelSkuModels] = None,
    ):
        self.distribution_mall_id = distribution_mall_id
        self.guide_retail_price_scope = guide_retail_price_scope
        self.item_id = item_id
        self.item_title = item_title
        self.lm_item_id = lm_item_id
        self.low_guide_retail_price_scope = low_guide_retail_price_scope
        self.reserved_price = reserved_price
        self.reserved_price_scope = reserved_price_scope
        self.sku_models = sku_models

    def validate(self):
        if self.sku_models:
            for k in self.sku_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.guide_retail_price_scope is not None:
            result['GuideRetailPriceScope'] = self.guide_retail_price_scope
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.low_guide_retail_price_scope is not None:
            result['LowGuideRetailPriceScope'] = self.low_guide_retail_price_scope
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.reserved_price_scope is not None:
            result['ReservedPriceScope'] = self.reserved_price_scope
        result['SkuModels'] = []
        if self.sku_models is not None:
            for k in self.sku_models:
                result['SkuModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('GuideRetailPriceScope') is not None:
            self.guide_retail_price_scope = m.get('GuideRetailPriceScope')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LowGuideRetailPriceScope') is not None:
            self.low_guide_retail_price_scope = m.get('LowGuideRetailPriceScope')
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('ReservedPriceScope') is not None:
            self.reserved_price_scope = m.get('ReservedPriceScope')
        self.sku_models = []
        if m.get('SkuModels') is not None:
            for k in m.get('SkuModels'):
                temp_model = QueryItemGuideRetailPriceResponseBodyModelSkuModels()
                self.sku_models.append(temp_model.from_map(k))
        return self


class QueryItemGuideRetailPriceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: List[QueryItemGuideRetailPriceResponseBodyModel] = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = QueryItemGuideRetailPriceResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryItemGuideRetailPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryItemGuideRetailPriceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryItemGuideRetailPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLogistics4DistributionRequest(TeaModel):
    def __init__(
        self,
        distributor_id: str = None,
        main_distribution_order_id: str = None,
        request_id: str = None,
        tenant_id: str = None,
    ):
        self.distributor_id = distributor_id
        self.main_distribution_order_id = main_distribution_order_id
        self.request_id = request_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.main_distribution_order_id is not None:
            result['MainDistributionOrderId'] = self.main_distribution_order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('MainDistributionOrderId') is not None:
            self.main_distribution_order_id = m.get('MainDistributionOrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryLogistics4DistributionResponseBodyModelGoods(TeaModel):
    def __init__(
        self,
        good_name: str = None,
        item_id: str = None,
        quantity: int = None,
        sku_id: str = None,
    ):
        self.good_name = good_name
        self.item_id = item_id
        self.quantity = quantity
        self.sku_id = sku_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.good_name is not None:
            result['GoodName'] = self.good_name
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GoodName') is not None:
            self.good_name = m.get('GoodName')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        return self


class QueryLogistics4DistributionResponseBodyModelLogisticsDetailList(TeaModel):
    def __init__(
        self,
        ocurr_time_str: str = None,
        standerd_desc: str = None,
    ):
        self.ocurr_time_str = ocurr_time_str
        self.standerd_desc = standerd_desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ocurr_time_str is not None:
            result['OcurrTimeStr'] = self.ocurr_time_str
        if self.standerd_desc is not None:
            result['StanderdDesc'] = self.standerd_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OcurrTimeStr') is not None:
            self.ocurr_time_str = m.get('OcurrTimeStr')
        if m.get('StanderdDesc') is not None:
            self.standerd_desc = m.get('StanderdDesc')
        return self


class QueryLogistics4DistributionResponseBodyModel(TeaModel):
    def __init__(
        self,
        data_provider: str = None,
        data_provider_title: str = None,
        goods: List[QueryLogistics4DistributionResponseBodyModelGoods] = None,
        logistics_company_code: str = None,
        logistics_company_name: str = None,
        logistics_detail_list: List[QueryLogistics4DistributionResponseBodyModelLogisticsDetailList] = None,
        mail_no: str = None,
    ):
        self.data_provider = data_provider
        self.data_provider_title = data_provider_title
        self.goods = goods
        self.logistics_company_code = logistics_company_code
        self.logistics_company_name = logistics_company_name
        self.logistics_detail_list = logistics_detail_list
        self.mail_no = mail_no

    def validate(self):
        if self.goods:
            for k in self.goods:
                if k:
                    k.validate()
        if self.logistics_detail_list:
            for k in self.logistics_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_provider is not None:
            result['DataProvider'] = self.data_provider
        if self.data_provider_title is not None:
            result['DataProviderTitle'] = self.data_provider_title
        result['Goods'] = []
        if self.goods is not None:
            for k in self.goods:
                result['Goods'].append(k.to_map() if k else None)
        if self.logistics_company_code is not None:
            result['LogisticsCompanyCode'] = self.logistics_company_code
        if self.logistics_company_name is not None:
            result['LogisticsCompanyName'] = self.logistics_company_name
        result['LogisticsDetailList'] = []
        if self.logistics_detail_list is not None:
            for k in self.logistics_detail_list:
                result['LogisticsDetailList'].append(k.to_map() if k else None)
        if self.mail_no is not None:
            result['MailNo'] = self.mail_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataProvider') is not None:
            self.data_provider = m.get('DataProvider')
        if m.get('DataProviderTitle') is not None:
            self.data_provider_title = m.get('DataProviderTitle')
        self.goods = []
        if m.get('Goods') is not None:
            for k in m.get('Goods'):
                temp_model = QueryLogistics4DistributionResponseBodyModelGoods()
                self.goods.append(temp_model.from_map(k))
        if m.get('LogisticsCompanyCode') is not None:
            self.logistics_company_code = m.get('LogisticsCompanyCode')
        if m.get('LogisticsCompanyName') is not None:
            self.logistics_company_name = m.get('LogisticsCompanyName')
        self.logistics_detail_list = []
        if m.get('LogisticsDetailList') is not None:
            for k in m.get('LogisticsDetailList'):
                temp_model = QueryLogistics4DistributionResponseBodyModelLogisticsDetailList()
                self.logistics_detail_list.append(temp_model.from_map(k))
        if m.get('MailNo') is not None:
            self.mail_no = m.get('MailNo')
        return self


class QueryLogistics4DistributionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: List[QueryLogistics4DistributionResponseBodyModel] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = QueryLogistics4DistributionResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryLogistics4DistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryLogistics4DistributionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryLogistics4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMallCategoryListRequest(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        distribution_mall_id: str = None,
        distributor_id: str = None,
        tenant_id: str = None,
    ):
        self.category_id = category_id
        self.distribution_mall_id = distribution_mall_id
        self.distributor_id = distributor_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryMallCategoryListResponseBodyModel(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        leaf: bool = None,
        name: str = None,
        parent_id: int = None,
    ):
        self.category_id = category_id
        self.leaf = leaf
        self.name = name
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.leaf is not None:
            result['Leaf'] = self.leaf
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Leaf') is not None:
            self.leaf = m.get('Leaf')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class QueryMallCategoryListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: List[QueryMallCategoryListResponseBodyModel] = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = QueryMallCategoryListResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMallCategoryListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMallCategoryListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryMallCategoryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderDetail4DistributionRequest(TeaModel):
    def __init__(
        self,
        distributor_id: str = None,
        main_distribution_order_id: str = None,
        tenant_id: str = None,
    ):
        self.distributor_id = distributor_id
        self.main_distribution_order_id = main_distribution_order_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.main_distribution_order_id is not None:
            result['MainDistributionOrderId'] = self.main_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('MainDistributionOrderId') is not None:
            self.main_distribution_order_id = m.get('MainDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryOrderDetail4DistributionResponseBodyModelSubOrderListItemPrice(TeaModel):
    def __init__(
        self,
        fund_amount_money: str = None,
    ):
        self.fund_amount_money = fund_amount_money

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_amount_money is not None:
            result['FundAmountMoney'] = self.fund_amount_money
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAmountMoney') is not None:
            self.fund_amount_money = m.get('FundAmountMoney')
        return self


class QueryOrderDetail4DistributionResponseBodyModelSubOrderList(TeaModel):
    def __init__(
        self,
        item_id: str = None,
        item_pic: str = None,
        item_price: List[QueryOrderDetail4DistributionResponseBodyModelSubOrderListItemPrice] = None,
        item_title: str = None,
        logistics_status: str = None,
        main_distribution_order_id: str = None,
        number: str = None,
        order_status: str = None,
        sku_id: str = None,
        sku_name: str = None,
        sub_distribution_order_id: str = None,
    ):
        self.item_id = item_id
        self.item_pic = item_pic
        self.item_price = item_price
        self.item_title = item_title
        self.logistics_status = logistics_status
        self.main_distribution_order_id = main_distribution_order_id
        self.number = number
        self.order_status = order_status
        self.sku_id = sku_id
        self.sku_name = sku_name
        self.sub_distribution_order_id = sub_distribution_order_id

    def validate(self):
        if self.item_price:
            for k in self.item_price:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_pic is not None:
            result['ItemPic'] = self.item_pic
        result['ItemPrice'] = []
        if self.item_price is not None:
            for k in self.item_price:
                result['ItemPrice'].append(k.to_map() if k else None)
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.logistics_status is not None:
            result['LogisticsStatus'] = self.logistics_status
        if self.main_distribution_order_id is not None:
            result['MainDistributionOrderId'] = self.main_distribution_order_id
        if self.number is not None:
            result['Number'] = self.number
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_name is not None:
            result['SkuName'] = self.sku_name
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemPic') is not None:
            self.item_pic = m.get('ItemPic')
        self.item_price = []
        if m.get('ItemPrice') is not None:
            for k in m.get('ItemPrice'):
                temp_model = QueryOrderDetail4DistributionResponseBodyModelSubOrderListItemPrice()
                self.item_price.append(temp_model.from_map(k))
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('LogisticsStatus') is not None:
            self.logistics_status = m.get('LogisticsStatus')
        if m.get('MainDistributionOrderId') is not None:
            self.main_distribution_order_id = m.get('MainDistributionOrderId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        return self


class QueryOrderDetail4DistributionResponseBodyModel(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        distribution_order_id: str = None,
        distributor_id: str = None,
        logistics_status: str = None,
        order_amount: str = None,
        order_status: str = None,
        sub_order_list: List[QueryOrderDetail4DistributionResponseBodyModelSubOrderList] = None,
    ):
        self.create_date = create_date
        self.distribution_order_id = distribution_order_id
        self.distributor_id = distributor_id
        self.logistics_status = logistics_status
        self.order_amount = order_amount
        self.order_status = order_status
        self.sub_order_list = sub_order_list

    def validate(self):
        if self.sub_order_list:
            for k in self.sub_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.distribution_order_id is not None:
            result['DistributionOrderId'] = self.distribution_order_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.logistics_status is not None:
            result['LogisticsStatus'] = self.logistics_status
        if self.order_amount is not None:
            result['OrderAmount'] = self.order_amount
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        result['SubOrderList'] = []
        if self.sub_order_list is not None:
            for k in self.sub_order_list:
                result['SubOrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DistributionOrderId') is not None:
            self.distribution_order_id = m.get('DistributionOrderId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('LogisticsStatus') is not None:
            self.logistics_status = m.get('LogisticsStatus')
        if m.get('OrderAmount') is not None:
            self.order_amount = m.get('OrderAmount')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        self.sub_order_list = []
        if m.get('SubOrderList') is not None:
            for k in m.get('SubOrderList'):
                temp_model = QueryOrderDetail4DistributionResponseBodyModelSubOrderList()
                self.sub_order_list.append(temp_model.from_map(k))
        return self


class QueryOrderDetail4DistributionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: QueryOrderDetail4DistributionResponseBodyModel = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryOrderDetail4DistributionResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryOrderDetail4DistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryOrderDetail4DistributionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryOrderDetail4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderList4DistributionRequest(TeaModel):
    def __init__(
        self,
        distributor_id: str = None,
        filter_option: str = None,
        page_number: int = None,
        page_size: int = None,
        tenant_id: str = None,
    ):
        self.distributor_id = distributor_id
        self.filter_option = filter_option
        self.page_number = page_number
        self.page_size = page_size
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.filter_option is not None:
            result['FilterOption'] = self.filter_option
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('FilterOption') is not None:
            self.filter_option = m.get('FilterOption')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryOrderList4DistributionResponseBodyModelSubOrderListItemPrice(TeaModel):
    def __init__(
        self,
        fund_amount_money: str = None,
    ):
        self.fund_amount_money = fund_amount_money

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_amount_money is not None:
            result['FundAmountMoney'] = self.fund_amount_money
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAmountMoney') is not None:
            self.fund_amount_money = m.get('FundAmountMoney')
        return self


class QueryOrderList4DistributionResponseBodyModelSubOrderList(TeaModel):
    def __init__(
        self,
        item_id: str = None,
        item_pic: str = None,
        item_price: List[QueryOrderList4DistributionResponseBodyModelSubOrderListItemPrice] = None,
        item_title: str = None,
        logistics_status: str = None,
        main_distribution_order_id: str = None,
        number: str = None,
        order_status: str = None,
        sku_id: str = None,
        sku_name: str = None,
        sub_distribution_order_id: str = None,
    ):
        self.item_id = item_id
        self.item_pic = item_pic
        self.item_price = item_price
        self.item_title = item_title
        self.logistics_status = logistics_status
        self.main_distribution_order_id = main_distribution_order_id
        self.number = number
        self.order_status = order_status
        self.sku_id = sku_id
        self.sku_name = sku_name
        self.sub_distribution_order_id = sub_distribution_order_id

    def validate(self):
        if self.item_price:
            for k in self.item_price:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_pic is not None:
            result['ItemPic'] = self.item_pic
        result['ItemPrice'] = []
        if self.item_price is not None:
            for k in self.item_price:
                result['ItemPrice'].append(k.to_map() if k else None)
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.logistics_status is not None:
            result['LogisticsStatus'] = self.logistics_status
        if self.main_distribution_order_id is not None:
            result['MainDistributionOrderId'] = self.main_distribution_order_id
        if self.number is not None:
            result['Number'] = self.number
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_name is not None:
            result['SkuName'] = self.sku_name
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemPic') is not None:
            self.item_pic = m.get('ItemPic')
        self.item_price = []
        if m.get('ItemPrice') is not None:
            for k in m.get('ItemPrice'):
                temp_model = QueryOrderList4DistributionResponseBodyModelSubOrderListItemPrice()
                self.item_price.append(temp_model.from_map(k))
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('LogisticsStatus') is not None:
            self.logistics_status = m.get('LogisticsStatus')
        if m.get('MainDistributionOrderId') is not None:
            self.main_distribution_order_id = m.get('MainDistributionOrderId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        return self


class QueryOrderList4DistributionResponseBodyModel(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        distribution_order_id: str = None,
        distributor_id: str = None,
        logistics_status: str = None,
        order_amount: str = None,
        order_status: str = None,
        sub_order_list: List[QueryOrderList4DistributionResponseBodyModelSubOrderList] = None,
    ):
        self.create_date = create_date
        self.distribution_order_id = distribution_order_id
        self.distributor_id = distributor_id
        self.logistics_status = logistics_status
        self.order_amount = order_amount
        self.order_status = order_status
        self.sub_order_list = sub_order_list

    def validate(self):
        if self.sub_order_list:
            for k in self.sub_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.distribution_order_id is not None:
            result['DistributionOrderId'] = self.distribution_order_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.logistics_status is not None:
            result['LogisticsStatus'] = self.logistics_status
        if self.order_amount is not None:
            result['OrderAmount'] = self.order_amount
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        result['SubOrderList'] = []
        if self.sub_order_list is not None:
            for k in self.sub_order_list:
                result['SubOrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DistributionOrderId') is not None:
            self.distribution_order_id = m.get('DistributionOrderId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('LogisticsStatus') is not None:
            self.logistics_status = m.get('LogisticsStatus')
        if m.get('OrderAmount') is not None:
            self.order_amount = m.get('OrderAmount')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        self.sub_order_list = []
        if m.get('SubOrderList') is not None:
            for k in m.get('SubOrderList'):
                temp_model = QueryOrderList4DistributionResponseBodyModelSubOrderList()
                self.sub_order_list.append(temp_model.from_map(k))
        return self


class QueryOrderList4DistributionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: List[QueryOrderList4DistributionResponseBodyModel] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = QueryOrderList4DistributionResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryOrderList4DistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryOrderList4DistributionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryOrderList4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRefundApplicationDetail4DistributionRequest(TeaModel):
    def __init__(
        self,
        distributor_id: str = None,
        sub_distribution_order_id: str = None,
        tenant_id: str = None,
    ):
        self.distributor_id = distributor_id
        self.sub_distribution_order_id = sub_distribution_order_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryRefundApplicationDetail4DistributionResponseBodyModelApplyReason(TeaModel):
    def __init__(
        self,
        reason_text_id: int = None,
        reason_tips: str = None,
    ):
        self.reason_text_id = reason_text_id
        self.reason_tips = reason_tips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason_text_id is not None:
            result['ReasonTextId'] = self.reason_text_id
        if self.reason_tips is not None:
            result['ReasonTips'] = self.reason_tips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReasonTextId') is not None:
            self.reason_text_id = m.get('ReasonTextId')
        if m.get('ReasonTips') is not None:
            self.reason_tips = m.get('ReasonTips')
        return self


class QueryRefundApplicationDetail4DistributionResponseBodyModelRefundFeeData(TeaModel):
    def __init__(
        self,
        max_refund_fee: int = None,
        min_refund_fee: int = None,
    ):
        self.max_refund_fee = max_refund_fee
        self.min_refund_fee = min_refund_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_refund_fee is not None:
            result['MaxRefundFee'] = self.max_refund_fee
        if self.min_refund_fee is not None:
            result['MinRefundFee'] = self.min_refund_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxRefundFee') is not None:
            self.max_refund_fee = m.get('MaxRefundFee')
        if m.get('MinRefundFee') is not None:
            self.min_refund_fee = m.get('MinRefundFee')
        return self


class QueryRefundApplicationDetail4DistributionResponseBodyModel(TeaModel):
    def __init__(
        self,
        apply_dispute_desc: str = None,
        apply_reason: QueryRefundApplicationDetail4DistributionResponseBodyModelApplyReason = None,
        biz_claim_type: int = None,
        dispute_create_time: str = None,
        dispute_desc: str = None,
        dispute_end_time: str = None,
        dispute_id: int = None,
        dispute_status: int = None,
        dispute_type: int = None,
        distribution_order_id: str = None,
        order_logistics_status: int = None,
        real_refund_fee: int = None,
        refund_fee: int = None,
        refund_fee_data: QueryRefundApplicationDetail4DistributionResponseBodyModelRefundFeeData = None,
        refunder_address: str = None,
        refunder_name: str = None,
        refunder_tel: str = None,
        refunder_zip_code: str = None,
        return_good_count: int = None,
        return_good_logistics_status: int = None,
        seller_agree_msg: str = None,
        seller_refuse_agreement_message: str = None,
        seller_refuse_reason: str = None,
        sub_distribution_order_id: str = None,
    ):
        self.apply_dispute_desc = apply_dispute_desc
        self.apply_reason = apply_reason
        self.biz_claim_type = biz_claim_type
        self.dispute_create_time = dispute_create_time
        self.dispute_desc = dispute_desc
        self.dispute_end_time = dispute_end_time
        self.dispute_id = dispute_id
        self.dispute_status = dispute_status
        self.dispute_type = dispute_type
        self.distribution_order_id = distribution_order_id
        self.order_logistics_status = order_logistics_status
        self.real_refund_fee = real_refund_fee
        self.refund_fee = refund_fee
        self.refund_fee_data = refund_fee_data
        self.refunder_address = refunder_address
        self.refunder_name = refunder_name
        self.refunder_tel = refunder_tel
        self.refunder_zip_code = refunder_zip_code
        self.return_good_count = return_good_count
        self.return_good_logistics_status = return_good_logistics_status
        self.seller_agree_msg = seller_agree_msg
        self.seller_refuse_agreement_message = seller_refuse_agreement_message
        self.seller_refuse_reason = seller_refuse_reason
        self.sub_distribution_order_id = sub_distribution_order_id

    def validate(self):
        if self.apply_reason:
            self.apply_reason.validate()
        if self.refund_fee_data:
            self.refund_fee_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_dispute_desc is not None:
            result['ApplyDisputeDesc'] = self.apply_dispute_desc
        if self.apply_reason is not None:
            result['ApplyReason'] = self.apply_reason.to_map()
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.dispute_create_time is not None:
            result['DisputeCreateTime'] = self.dispute_create_time
        if self.dispute_desc is not None:
            result['DisputeDesc'] = self.dispute_desc
        if self.dispute_end_time is not None:
            result['DisputeEndTime'] = self.dispute_end_time
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.dispute_status is not None:
            result['DisputeStatus'] = self.dispute_status
        if self.dispute_type is not None:
            result['DisputeType'] = self.dispute_type
        if self.distribution_order_id is not None:
            result['DistributionOrderId'] = self.distribution_order_id
        if self.order_logistics_status is not None:
            result['OrderLogisticsStatus'] = self.order_logistics_status
        if self.real_refund_fee is not None:
            result['RealRefundFee'] = self.real_refund_fee
        if self.refund_fee is not None:
            result['RefundFee'] = self.refund_fee
        if self.refund_fee_data is not None:
            result['RefundFeeData'] = self.refund_fee_data.to_map()
        if self.refunder_address is not None:
            result['RefunderAddress'] = self.refunder_address
        if self.refunder_name is not None:
            result['RefunderName'] = self.refunder_name
        if self.refunder_tel is not None:
            result['RefunderTel'] = self.refunder_tel
        if self.refunder_zip_code is not None:
            result['RefunderZipCode'] = self.refunder_zip_code
        if self.return_good_count is not None:
            result['ReturnGoodCount'] = self.return_good_count
        if self.return_good_logistics_status is not None:
            result['ReturnGoodLogisticsStatus'] = self.return_good_logistics_status
        if self.seller_agree_msg is not None:
            result['SellerAgreeMsg'] = self.seller_agree_msg
        if self.seller_refuse_agreement_message is not None:
            result['SellerRefuseAgreementMessage'] = self.seller_refuse_agreement_message
        if self.seller_refuse_reason is not None:
            result['SellerRefuseReason'] = self.seller_refuse_reason
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyDisputeDesc') is not None:
            self.apply_dispute_desc = m.get('ApplyDisputeDesc')
        if m.get('ApplyReason') is not None:
            temp_model = QueryRefundApplicationDetail4DistributionResponseBodyModelApplyReason()
            self.apply_reason = temp_model.from_map(m['ApplyReason'])
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('DisputeCreateTime') is not None:
            self.dispute_create_time = m.get('DisputeCreateTime')
        if m.get('DisputeDesc') is not None:
            self.dispute_desc = m.get('DisputeDesc')
        if m.get('DisputeEndTime') is not None:
            self.dispute_end_time = m.get('DisputeEndTime')
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DisputeStatus') is not None:
            self.dispute_status = m.get('DisputeStatus')
        if m.get('DisputeType') is not None:
            self.dispute_type = m.get('DisputeType')
        if m.get('DistributionOrderId') is not None:
            self.distribution_order_id = m.get('DistributionOrderId')
        if m.get('OrderLogisticsStatus') is not None:
            self.order_logistics_status = m.get('OrderLogisticsStatus')
        if m.get('RealRefundFee') is not None:
            self.real_refund_fee = m.get('RealRefundFee')
        if m.get('RefundFee') is not None:
            self.refund_fee = m.get('RefundFee')
        if m.get('RefundFeeData') is not None:
            temp_model = QueryRefundApplicationDetail4DistributionResponseBodyModelRefundFeeData()
            self.refund_fee_data = temp_model.from_map(m['RefundFeeData'])
        if m.get('RefunderAddress') is not None:
            self.refunder_address = m.get('RefunderAddress')
        if m.get('RefunderName') is not None:
            self.refunder_name = m.get('RefunderName')
        if m.get('RefunderTel') is not None:
            self.refunder_tel = m.get('RefunderTel')
        if m.get('RefunderZipCode') is not None:
            self.refunder_zip_code = m.get('RefunderZipCode')
        if m.get('ReturnGoodCount') is not None:
            self.return_good_count = m.get('ReturnGoodCount')
        if m.get('ReturnGoodLogisticsStatus') is not None:
            self.return_good_logistics_status = m.get('ReturnGoodLogisticsStatus')
        if m.get('SellerAgreeMsg') is not None:
            self.seller_agree_msg = m.get('SellerAgreeMsg')
        if m.get('SellerRefuseAgreementMessage') is not None:
            self.seller_refuse_agreement_message = m.get('SellerRefuseAgreementMessage')
        if m.get('SellerRefuseReason') is not None:
            self.seller_refuse_reason = m.get('SellerRefuseReason')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        return self


class QueryRefundApplicationDetail4DistributionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: QueryRefundApplicationDetail4DistributionResponseBodyModel = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryRefundApplicationDetail4DistributionResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryRefundApplicationDetail4DistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRefundApplicationDetail4DistributionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryRefundApplicationDetail4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenderDistributionOrderRequestItemInfoLists(TeaModel):
    def __init__(
        self,
        distribution_mall_id: str = None,
        lm_item_id: str = None,
        quantity: int = None,
        sku_id: str = None,
    ):
        self.distribution_mall_id = distribution_mall_id
        self.lm_item_id = lm_item_id
        self.quantity = quantity
        self.sku_id = sku_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        return self


class RenderDistributionOrderRequest(TeaModel):
    def __init__(
        self,
        buyer_id: str = None,
        delivery_address: str = None,
        distribution_supplier_id: str = None,
        distributor_id: str = None,
        ext_info: str = None,
        item_info_lists: List[RenderDistributionOrderRequestItemInfoLists] = None,
        tenant_id: str = None,
    ):
        self.buyer_id = buyer_id
        self.delivery_address = delivery_address
        self.distribution_supplier_id = distribution_supplier_id
        self.distributor_id = distributor_id
        self.ext_info = ext_info
        self.item_info_lists = item_info_lists
        self.tenant_id = tenant_id

    def validate(self):
        if self.item_info_lists:
            for k in self.item_info_lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_id is not None:
            result['BuyerId'] = self.buyer_id
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address
        if self.distribution_supplier_id is not None:
            result['DistributionSupplierId'] = self.distribution_supplier_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        result['ItemInfoLists'] = []
        if self.item_info_lists is not None:
            for k in self.item_info_lists:
                result['ItemInfoLists'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyerId') is not None:
            self.buyer_id = m.get('BuyerId')
        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')
        if m.get('DistributionSupplierId') is not None:
            self.distribution_supplier_id = m.get('DistributionSupplierId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        self.item_info_lists = []
        if m.get('ItemInfoLists') is not None:
            for k in m.get('ItemInfoLists'):
                temp_model = RenderDistributionOrderRequestItemInfoLists()
                self.item_info_lists.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class RenderDistributionOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        buyer_id: str = None,
        delivery_address: str = None,
        distribution_supplier_id: str = None,
        distributor_id: str = None,
        ext_info: str = None,
        item_info_lists_shrink: str = None,
        tenant_id: str = None,
    ):
        self.buyer_id = buyer_id
        self.delivery_address = delivery_address
        self.distribution_supplier_id = distribution_supplier_id
        self.distributor_id = distributor_id
        self.ext_info = ext_info
        self.item_info_lists_shrink = item_info_lists_shrink
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_id is not None:
            result['BuyerId'] = self.buyer_id
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address
        if self.distribution_supplier_id is not None:
            result['DistributionSupplierId'] = self.distribution_supplier_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.item_info_lists_shrink is not None:
            result['ItemInfoLists'] = self.item_info_lists_shrink
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyerId') is not None:
            self.buyer_id = m.get('BuyerId')
        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')
        if m.get('DistributionSupplierId') is not None:
            self.distribution_supplier_id = m.get('DistributionSupplierId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('ItemInfoLists') is not None:
            self.item_info_lists_shrink = m.get('ItemInfoLists')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class RenderDistributionOrderResponseBodyModelAddressInfos(TeaModel):
    def __init__(
        self,
        address_detail: str = None,
        address_id: int = None,
        division_code: str = None,
        is_default: bool = None,
        receiver: str = None,
        receiver_phone: str = None,
        town_division_code: str = None,
    ):
        self.address_detail = address_detail
        self.address_id = address_id
        self.division_code = division_code
        self.is_default = is_default
        self.receiver = receiver
        self.receiver_phone = receiver_phone
        self.town_division_code = town_division_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail
        if self.address_id is not None:
            result['AddressId'] = self.address_id
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.receiver is not None:
            result['Receiver'] = self.receiver
        if self.receiver_phone is not None:
            result['ReceiverPhone'] = self.receiver_phone
        if self.town_division_code is not None:
            result['TownDivisionCode'] = self.town_division_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressDetail') is not None:
            self.address_detail = m.get('AddressDetail')
        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Receiver') is not None:
            self.receiver = m.get('Receiver')
        if m.get('ReceiverPhone') is not None:
            self.receiver_phone = m.get('ReceiverPhone')
        if m.get('TownDivisionCode') is not None:
            self.town_division_code = m.get('TownDivisionCode')
        return self


class RenderDistributionOrderResponseBodyModelRenderOrderInfosDeliveryInfos(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        post_fee: int = None,
        service_type: int = None,
    ):
        self.display_name = display_name
        self.id = id
        self.post_fee = post_fee
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.post_fee is not None:
            result['PostFee'] = self.post_fee
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PostFee') is not None:
            self.post_fee = m.get('PostFee')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class RenderDistributionOrderResponseBodyModelRenderOrderInfosInvoiceInfo(TeaModel):
    def __init__(
        self,
        desc: str = None,
        type: str = None,
    ):
        self.desc = desc
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfosItemPromInstVOSAvailableItems(TeaModel):
    def __init__(
        self,
        item_id: int = None,
        lm_item_id: str = None,
        lm_shop_id: int = None,
        number: int = None,
        points: int = None,
        points_amount: int = None,
        price_cent: int = None,
        removed: bool = None,
        sku_id: int = None,
        tb_seller_id: int = None,
        user_pay_fee: int = None,
    ):
        self.item_id = item_id
        self.lm_item_id = lm_item_id
        self.lm_shop_id = lm_shop_id
        self.number = number
        self.points = points
        self.points_amount = points_amount
        self.price_cent = price_cent
        self.removed = removed
        self.sku_id = sku_id
        self.tb_seller_id = tb_seller_id
        self.user_pay_fee = user_pay_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.lm_shop_id is not None:
            result['LmShopId'] = self.lm_shop_id
        if self.number is not None:
            result['Number'] = self.number
        if self.points is not None:
            result['Points'] = self.points
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.removed is not None:
            result['Removed'] = self.removed
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.user_pay_fee is not None:
            result['UserPayFee'] = self.user_pay_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LmShopId') is not None:
            self.lm_shop_id = m.get('LmShopId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Removed') is not None:
            self.removed = m.get('Removed')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('UserPayFee') is not None:
            self.user_pay_fee = m.get('UserPayFee')
        return self


class RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfosItemPromInstVOS(TeaModel):
    def __init__(
        self,
        available_items: List[RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfosItemPromInstVOSAvailableItems] = None,
        can_use: bool = None,
        discount_price: int = None,
        expire_time: int = None,
        instance_id: str = None,
        level: str = None,
        lm_item_id: str = None,
        promotion_name: str = None,
        promotion_type: str = None,
        reason: str = None,
        selected: bool = None,
        sku_ids: List[int] = None,
        special_price: int = None,
        sub_biz_code: str = None,
        tb_seller_id: int = None,
        threshold_price: int = None,
        use_start_time: int = None,
    ):
        self.available_items = available_items
        self.can_use = can_use
        self.discount_price = discount_price
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.level = level
        self.lm_item_id = lm_item_id
        self.promotion_name = promotion_name
        self.promotion_type = promotion_type
        self.reason = reason
        self.selected = selected
        self.sku_ids = sku_ids
        self.special_price = special_price
        self.sub_biz_code = sub_biz_code
        self.tb_seller_id = tb_seller_id
        self.threshold_price = threshold_price
        self.use_start_time = use_start_time

    def validate(self):
        if self.available_items:
            for k in self.available_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableItems'] = []
        if self.available_items is not None:
            for k in self.available_items:
                result['AvailableItems'].append(k.to_map() if k else None)
        if self.can_use is not None:
            result['CanUse'] = self.can_use
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.level is not None:
            result['Level'] = self.level
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_type is not None:
            result['PromotionType'] = self.promotion_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.selected is not None:
            result['Selected'] = self.selected
        if self.sku_ids is not None:
            result['SkuIds'] = self.sku_ids
        if self.special_price is not None:
            result['SpecialPrice'] = self.special_price
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.threshold_price is not None:
            result['ThresholdPrice'] = self.threshold_price
        if self.use_start_time is not None:
            result['UseStartTime'] = self.use_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_items = []
        if m.get('AvailableItems') is not None:
            for k in m.get('AvailableItems'):
                temp_model = RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfosItemPromInstVOSAvailableItems()
                self.available_items.append(temp_model.from_map(k))
        if m.get('CanUse') is not None:
            self.can_use = m.get('CanUse')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionType') is not None:
            self.promotion_type = m.get('PromotionType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        if m.get('SkuIds') is not None:
            self.sku_ids = m.get('SkuIds')
        if m.get('SpecialPrice') is not None:
            self.special_price = m.get('SpecialPrice')
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('ThresholdPrice') is not None:
            self.threshold_price = m.get('ThresholdPrice')
        if m.get('UseStartTime') is not None:
            self.use_start_time = m.get('UseStartTime')
        return self


class RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfos(TeaModel):
    def __init__(
        self,
        can_sell: bool = None,
        distribution_mall_id: str = None,
        distribution_supplier_id: str = None,
        distributor_id: str = None,
        features: Dict[str, str] = None,
        item_id: str = None,
        item_name: str = None,
        item_pic_url: str = None,
        item_prom_inst_vos: List[RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfosItemPromInstVOS] = None,
        item_url: str = None,
        message: str = None,
        price: int = None,
        promotion_fee: int = None,
        quantity: int = None,
        reserve_price: int = None,
        sku_id: int = None,
        sku_name: str = None,
        virtual_item_type: str = None,
    ):
        self.can_sell = can_sell
        self.distribution_mall_id = distribution_mall_id
        self.distribution_supplier_id = distribution_supplier_id
        self.distributor_id = distributor_id
        self.features = features
        self.item_id = item_id
        self.item_name = item_name
        self.item_pic_url = item_pic_url
        self.item_prom_inst_vos = item_prom_inst_vos
        self.item_url = item_url
        self.message = message
        self.price = price
        self.promotion_fee = promotion_fee
        self.quantity = quantity
        self.reserve_price = reserve_price
        self.sku_id = sku_id
        self.sku_name = sku_name
        self.virtual_item_type = virtual_item_type

    def validate(self):
        if self.item_prom_inst_vos:
            for k in self.item_prom_inst_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distribution_supplier_id is not None:
            result['DistributionSupplierId'] = self.distribution_supplier_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.features is not None:
            result['Features'] = self.features
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.item_pic_url is not None:
            result['ItemPicUrl'] = self.item_pic_url
        result['ItemPromInstVOS'] = []
        if self.item_prom_inst_vos is not None:
            for k in self.item_prom_inst_vos:
                result['ItemPromInstVOS'].append(k.to_map() if k else None)
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.message is not None:
            result['Message'] = self.message
        if self.price is not None:
            result['Price'] = self.price
        if self.promotion_fee is not None:
            result['PromotionFee'] = self.promotion_fee
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_name is not None:
            result['SkuName'] = self.sku_name
        if self.virtual_item_type is not None:
            result['VirtualItemType'] = self.virtual_item_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributionSupplierId') is not None:
            self.distribution_supplier_id = m.get('DistributionSupplierId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('ItemPicUrl') is not None:
            self.item_pic_url = m.get('ItemPicUrl')
        self.item_prom_inst_vos = []
        if m.get('ItemPromInstVOS') is not None:
            for k in m.get('ItemPromInstVOS'):
                temp_model = RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfosItemPromInstVOS()
                self.item_prom_inst_vos.append(temp_model.from_map(k))
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('PromotionFee') is not None:
            self.promotion_fee = m.get('PromotionFee')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')
        if m.get('VirtualItemType') is not None:
            self.virtual_item_type = m.get('VirtualItemType')
        return self


class RenderDistributionOrderResponseBodyModelRenderOrderInfosShopPromInstVOSAvailableItems(TeaModel):
    def __init__(
        self,
        item_id: int = None,
        lm_item_id: str = None,
        lm_shop_id: int = None,
        number: int = None,
        points: int = None,
        points_amount: int = None,
        price_cent: int = None,
        removed: bool = None,
        sku_id: int = None,
        tb_seller_id: int = None,
        user_pay_fee: int = None,
    ):
        self.item_id = item_id
        self.lm_item_id = lm_item_id
        self.lm_shop_id = lm_shop_id
        self.number = number
        self.points = points
        self.points_amount = points_amount
        self.price_cent = price_cent
        self.removed = removed
        self.sku_id = sku_id
        self.tb_seller_id = tb_seller_id
        self.user_pay_fee = user_pay_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.lm_shop_id is not None:
            result['LmShopId'] = self.lm_shop_id
        if self.number is not None:
            result['Number'] = self.number
        if self.points is not None:
            result['Points'] = self.points
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.removed is not None:
            result['Removed'] = self.removed
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.user_pay_fee is not None:
            result['UserPayFee'] = self.user_pay_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LmShopId') is not None:
            self.lm_shop_id = m.get('LmShopId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Removed') is not None:
            self.removed = m.get('Removed')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('UserPayFee') is not None:
            self.user_pay_fee = m.get('UserPayFee')
        return self


class RenderDistributionOrderResponseBodyModelRenderOrderInfosShopPromInstVOS(TeaModel):
    def __init__(
        self,
        available_items: List[RenderDistributionOrderResponseBodyModelRenderOrderInfosShopPromInstVOSAvailableItems] = None,
        can_use: bool = None,
        discount_price: int = None,
        expire_time: int = None,
        instance_id: str = None,
        level: str = None,
        lm_item_id: str = None,
        promotion_name: str = None,
        promotion_type: str = None,
        reason: str = None,
        selected: bool = None,
        sku_ids: List[int] = None,
        special_price: int = None,
        sub_biz_code: str = None,
        tb_seller_id: int = None,
        threshold_price: int = None,
        use_start_time: int = None,
    ):
        self.available_items = available_items
        self.can_use = can_use
        self.discount_price = discount_price
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.level = level
        self.lm_item_id = lm_item_id
        self.promotion_name = promotion_name
        self.promotion_type = promotion_type
        self.reason = reason
        self.selected = selected
        self.sku_ids = sku_ids
        self.special_price = special_price
        self.sub_biz_code = sub_biz_code
        self.tb_seller_id = tb_seller_id
        self.threshold_price = threshold_price
        self.use_start_time = use_start_time

    def validate(self):
        if self.available_items:
            for k in self.available_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableItems'] = []
        if self.available_items is not None:
            for k in self.available_items:
                result['AvailableItems'].append(k.to_map() if k else None)
        if self.can_use is not None:
            result['CanUse'] = self.can_use
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.level is not None:
            result['Level'] = self.level
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_type is not None:
            result['PromotionType'] = self.promotion_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.selected is not None:
            result['Selected'] = self.selected
        if self.sku_ids is not None:
            result['SkuIds'] = self.sku_ids
        if self.special_price is not None:
            result['SpecialPrice'] = self.special_price
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.threshold_price is not None:
            result['ThresholdPrice'] = self.threshold_price
        if self.use_start_time is not None:
            result['UseStartTime'] = self.use_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_items = []
        if m.get('AvailableItems') is not None:
            for k in m.get('AvailableItems'):
                temp_model = RenderDistributionOrderResponseBodyModelRenderOrderInfosShopPromInstVOSAvailableItems()
                self.available_items.append(temp_model.from_map(k))
        if m.get('CanUse') is not None:
            self.can_use = m.get('CanUse')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionType') is not None:
            self.promotion_type = m.get('PromotionType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        if m.get('SkuIds') is not None:
            self.sku_ids = m.get('SkuIds')
        if m.get('SpecialPrice') is not None:
            self.special_price = m.get('SpecialPrice')
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('ThresholdPrice') is not None:
            self.threshold_price = m.get('ThresholdPrice')
        if m.get('UseStartTime') is not None:
            self.use_start_time = m.get('UseStartTime')
        return self


class RenderDistributionOrderResponseBodyModelRenderOrderInfos(TeaModel):
    def __init__(
        self,
        can_sell: bool = None,
        delivery_infos: List[RenderDistributionOrderResponseBodyModelRenderOrderInfosDeliveryInfos] = None,
        ext_info: Dict[str, str] = None,
        invoice_info: RenderDistributionOrderResponseBodyModelRenderOrderInfosInvoiceInfo = None,
        item_infos: List[RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfos] = None,
        message: str = None,
        shop_prom_inst_vos: List[RenderDistributionOrderResponseBodyModelRenderOrderInfosShopPromInstVOS] = None,
    ):
        self.can_sell = can_sell
        self.delivery_infos = delivery_infos
        self.ext_info = ext_info
        self.invoice_info = invoice_info
        self.item_infos = item_infos
        self.message = message
        self.shop_prom_inst_vos = shop_prom_inst_vos

    def validate(self):
        if self.delivery_infos:
            for k in self.delivery_infos:
                if k:
                    k.validate()
        if self.invoice_info:
            self.invoice_info.validate()
        if self.item_infos:
            for k in self.item_infos:
                if k:
                    k.validate()
        if self.shop_prom_inst_vos:
            for k in self.shop_prom_inst_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        result['DeliveryInfos'] = []
        if self.delivery_infos is not None:
            for k in self.delivery_infos:
                result['DeliveryInfos'].append(k.to_map() if k else None)
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.invoice_info is not None:
            result['InvoiceInfo'] = self.invoice_info.to_map()
        result['ItemInfos'] = []
        if self.item_infos is not None:
            for k in self.item_infos:
                result['ItemInfos'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        result['ShopPromInstVOS'] = []
        if self.shop_prom_inst_vos is not None:
            for k in self.shop_prom_inst_vos:
                result['ShopPromInstVOS'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        self.delivery_infos = []
        if m.get('DeliveryInfos') is not None:
            for k in m.get('DeliveryInfos'):
                temp_model = RenderDistributionOrderResponseBodyModelRenderOrderInfosDeliveryInfos()
                self.delivery_infos.append(temp_model.from_map(k))
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('InvoiceInfo') is not None:
            temp_model = RenderDistributionOrderResponseBodyModelRenderOrderInfosInvoiceInfo()
            self.invoice_info = temp_model.from_map(m['InvoiceInfo'])
        self.item_infos = []
        if m.get('ItemInfos') is not None:
            for k in m.get('ItemInfos'):
                temp_model = RenderDistributionOrderResponseBodyModelRenderOrderInfosItemInfos()
                self.item_infos.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.shop_prom_inst_vos = []
        if m.get('ShopPromInstVOS') is not None:
            for k in m.get('ShopPromInstVOS'):
                temp_model = RenderDistributionOrderResponseBodyModelRenderOrderInfosShopPromInstVOS()
                self.shop_prom_inst_vos.append(temp_model.from_map(k))
        return self


class RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosDeliveryInfos(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        post_fee: int = None,
        service_type: int = None,
    ):
        self.display_name = display_name
        self.id = id
        self.post_fee = post_fee
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.post_fee is not None:
            result['PostFee'] = self.post_fee
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PostFee') is not None:
            self.post_fee = m.get('PostFee')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosInvoiceInfo(TeaModel):
    def __init__(
        self,
        desc: str = None,
        type: str = None,
    ):
        self.desc = desc
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfosItemPromInstVOSAvailableItems(TeaModel):
    def __init__(
        self,
        item_id: int = None,
        lm_item_id: str = None,
        lm_shop_id: int = None,
        number: int = None,
        points: int = None,
        points_amount: int = None,
        price_cent: int = None,
        removed: bool = None,
        sku_id: int = None,
        tb_seller_id: int = None,
        user_pay_fee: int = None,
    ):
        self.item_id = item_id
        self.lm_item_id = lm_item_id
        self.lm_shop_id = lm_shop_id
        self.number = number
        self.points = points
        self.points_amount = points_amount
        self.price_cent = price_cent
        self.removed = removed
        self.sku_id = sku_id
        self.tb_seller_id = tb_seller_id
        self.user_pay_fee = user_pay_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.lm_shop_id is not None:
            result['LmShopId'] = self.lm_shop_id
        if self.number is not None:
            result['Number'] = self.number
        if self.points is not None:
            result['Points'] = self.points
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.removed is not None:
            result['Removed'] = self.removed
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.user_pay_fee is not None:
            result['UserPayFee'] = self.user_pay_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LmShopId') is not None:
            self.lm_shop_id = m.get('LmShopId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Removed') is not None:
            self.removed = m.get('Removed')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('UserPayFee') is not None:
            self.user_pay_fee = m.get('UserPayFee')
        return self


class RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfosItemPromInstVOS(TeaModel):
    def __init__(
        self,
        available_items: List[RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfosItemPromInstVOSAvailableItems] = None,
        can_use: bool = None,
        discount_price: int = None,
        expire_time: int = None,
        instance_id: str = None,
        level: str = None,
        lm_item_id: str = None,
        promotion_name: str = None,
        promotion_type: str = None,
        reason: str = None,
        selected: bool = None,
        sku_ids: List[int] = None,
        special_price: int = None,
        sub_biz_code: str = None,
        tb_seller_id: int = None,
        threshold_price: int = None,
        use_start_time: int = None,
    ):
        self.available_items = available_items
        self.can_use = can_use
        self.discount_price = discount_price
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.level = level
        self.lm_item_id = lm_item_id
        self.promotion_name = promotion_name
        self.promotion_type = promotion_type
        self.reason = reason
        self.selected = selected
        self.sku_ids = sku_ids
        self.special_price = special_price
        self.sub_biz_code = sub_biz_code
        self.tb_seller_id = tb_seller_id
        self.threshold_price = threshold_price
        self.use_start_time = use_start_time

    def validate(self):
        if self.available_items:
            for k in self.available_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableItems'] = []
        if self.available_items is not None:
            for k in self.available_items:
                result['AvailableItems'].append(k.to_map() if k else None)
        if self.can_use is not None:
            result['CanUse'] = self.can_use
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.level is not None:
            result['Level'] = self.level
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_type is not None:
            result['PromotionType'] = self.promotion_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.selected is not None:
            result['Selected'] = self.selected
        if self.sku_ids is not None:
            result['SkuIds'] = self.sku_ids
        if self.special_price is not None:
            result['SpecialPrice'] = self.special_price
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.threshold_price is not None:
            result['ThresholdPrice'] = self.threshold_price
        if self.use_start_time is not None:
            result['UseStartTime'] = self.use_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_items = []
        if m.get('AvailableItems') is not None:
            for k in m.get('AvailableItems'):
                temp_model = RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfosItemPromInstVOSAvailableItems()
                self.available_items.append(temp_model.from_map(k))
        if m.get('CanUse') is not None:
            self.can_use = m.get('CanUse')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionType') is not None:
            self.promotion_type = m.get('PromotionType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        if m.get('SkuIds') is not None:
            self.sku_ids = m.get('SkuIds')
        if m.get('SpecialPrice') is not None:
            self.special_price = m.get('SpecialPrice')
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('ThresholdPrice') is not None:
            self.threshold_price = m.get('ThresholdPrice')
        if m.get('UseStartTime') is not None:
            self.use_start_time = m.get('UseStartTime')
        return self


class RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfos(TeaModel):
    def __init__(
        self,
        can_sell: bool = None,
        distribution_mall_id: str = None,
        distribution_supplier_id: str = None,
        distributor_id: str = None,
        features: Dict[str, str] = None,
        item_id: str = None,
        item_name: str = None,
        item_pic_url: str = None,
        item_prom_inst_vos: List[RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfosItemPromInstVOS] = None,
        item_url: str = None,
        message: str = None,
        price: int = None,
        promotion_fee: int = None,
        quantity: int = None,
        reserve_price: int = None,
        sku_id: int = None,
        sku_name: str = None,
        virtual_item_type: str = None,
    ):
        self.can_sell = can_sell
        self.distribution_mall_id = distribution_mall_id
        self.distribution_supplier_id = distribution_supplier_id
        self.distributor_id = distributor_id
        self.features = features
        self.item_id = item_id
        self.item_name = item_name
        self.item_pic_url = item_pic_url
        self.item_prom_inst_vos = item_prom_inst_vos
        self.item_url = item_url
        self.message = message
        self.price = price
        self.promotion_fee = promotion_fee
        self.quantity = quantity
        self.reserve_price = reserve_price
        self.sku_id = sku_id
        self.sku_name = sku_name
        self.virtual_item_type = virtual_item_type

    def validate(self):
        if self.item_prom_inst_vos:
            for k in self.item_prom_inst_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.distribution_mall_id is not None:
            result['DistributionMallId'] = self.distribution_mall_id
        if self.distribution_supplier_id is not None:
            result['DistributionSupplierId'] = self.distribution_supplier_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.features is not None:
            result['Features'] = self.features
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.item_pic_url is not None:
            result['ItemPicUrl'] = self.item_pic_url
        result['ItemPromInstVOS'] = []
        if self.item_prom_inst_vos is not None:
            for k in self.item_prom_inst_vos:
                result['ItemPromInstVOS'].append(k.to_map() if k else None)
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.message is not None:
            result['Message'] = self.message
        if self.price is not None:
            result['Price'] = self.price
        if self.promotion_fee is not None:
            result['PromotionFee'] = self.promotion_fee
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_name is not None:
            result['SkuName'] = self.sku_name
        if self.virtual_item_type is not None:
            result['VirtualItemType'] = self.virtual_item_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('DistributionMallId') is not None:
            self.distribution_mall_id = m.get('DistributionMallId')
        if m.get('DistributionSupplierId') is not None:
            self.distribution_supplier_id = m.get('DistributionSupplierId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('ItemPicUrl') is not None:
            self.item_pic_url = m.get('ItemPicUrl')
        self.item_prom_inst_vos = []
        if m.get('ItemPromInstVOS') is not None:
            for k in m.get('ItemPromInstVOS'):
                temp_model = RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfosItemPromInstVOS()
                self.item_prom_inst_vos.append(temp_model.from_map(k))
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('PromotionFee') is not None:
            self.promotion_fee = m.get('PromotionFee')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')
        if m.get('VirtualItemType') is not None:
            self.virtual_item_type = m.get('VirtualItemType')
        return self


class RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosShopPromInstVOSAvailableItems(TeaModel):
    def __init__(
        self,
        item_id: int = None,
        lm_item_id: str = None,
        lm_shop_id: int = None,
        number: int = None,
        points: int = None,
        points_amount: int = None,
        price_cent: int = None,
        removed: bool = None,
        sku_id: int = None,
        tb_seller_id: int = None,
        user_pay_fee: int = None,
    ):
        self.item_id = item_id
        self.lm_item_id = lm_item_id
        self.lm_shop_id = lm_shop_id
        self.number = number
        self.points = points
        self.points_amount = points_amount
        self.price_cent = price_cent
        self.removed = removed
        self.sku_id = sku_id
        self.tb_seller_id = tb_seller_id
        self.user_pay_fee = user_pay_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.lm_shop_id is not None:
            result['LmShopId'] = self.lm_shop_id
        if self.number is not None:
            result['Number'] = self.number
        if self.points is not None:
            result['Points'] = self.points
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.removed is not None:
            result['Removed'] = self.removed
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.user_pay_fee is not None:
            result['UserPayFee'] = self.user_pay_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('LmShopId') is not None:
            self.lm_shop_id = m.get('LmShopId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Removed') is not None:
            self.removed = m.get('Removed')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('UserPayFee') is not None:
            self.user_pay_fee = m.get('UserPayFee')
        return self


class RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosShopPromInstVOS(TeaModel):
    def __init__(
        self,
        available_items: List[RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosShopPromInstVOSAvailableItems] = None,
        can_use: bool = None,
        discount_price: int = None,
        expire_time: int = None,
        instance_id: str = None,
        level: str = None,
        lm_item_id: str = None,
        promotion_name: str = None,
        promotion_type: str = None,
        reason: str = None,
        selected: bool = None,
        sku_ids: List[int] = None,
        special_price: int = None,
        sub_biz_code: str = None,
        tb_seller_id: int = None,
        threshold_price: int = None,
        use_start_time: int = None,
    ):
        self.available_items = available_items
        self.can_use = can_use
        self.discount_price = discount_price
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.level = level
        self.lm_item_id = lm_item_id
        self.promotion_name = promotion_name
        self.promotion_type = promotion_type
        self.reason = reason
        self.selected = selected
        self.sku_ids = sku_ids
        self.special_price = special_price
        self.sub_biz_code = sub_biz_code
        self.tb_seller_id = tb_seller_id
        self.threshold_price = threshold_price
        self.use_start_time = use_start_time

    def validate(self):
        if self.available_items:
            for k in self.available_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableItems'] = []
        if self.available_items is not None:
            for k in self.available_items:
                result['AvailableItems'].append(k.to_map() if k else None)
        if self.can_use is not None:
            result['CanUse'] = self.can_use
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.level is not None:
            result['Level'] = self.level
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_type is not None:
            result['PromotionType'] = self.promotion_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.selected is not None:
            result['Selected'] = self.selected
        if self.sku_ids is not None:
            result['SkuIds'] = self.sku_ids
        if self.special_price is not None:
            result['SpecialPrice'] = self.special_price
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.threshold_price is not None:
            result['ThresholdPrice'] = self.threshold_price
        if self.use_start_time is not None:
            result['UseStartTime'] = self.use_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_items = []
        if m.get('AvailableItems') is not None:
            for k in m.get('AvailableItems'):
                temp_model = RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosShopPromInstVOSAvailableItems()
                self.available_items.append(temp_model.from_map(k))
        if m.get('CanUse') is not None:
            self.can_use = m.get('CanUse')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionType') is not None:
            self.promotion_type = m.get('PromotionType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        if m.get('SkuIds') is not None:
            self.sku_ids = m.get('SkuIds')
        if m.get('SpecialPrice') is not None:
            self.special_price = m.get('SpecialPrice')
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('ThresholdPrice') is not None:
            self.threshold_price = m.get('ThresholdPrice')
        if m.get('UseStartTime') is not None:
            self.use_start_time = m.get('UseStartTime')
        return self


class RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfos(TeaModel):
    def __init__(
        self,
        can_sell: bool = None,
        delivery_infos: List[RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosDeliveryInfos] = None,
        ext_info: Dict[str, str] = None,
        invoice_info: RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosInvoiceInfo = None,
        item_infos: List[RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfos] = None,
        message: str = None,
        shop_prom_inst_vos: List[RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosShopPromInstVOS] = None,
    ):
        self.can_sell = can_sell
        self.delivery_infos = delivery_infos
        self.ext_info = ext_info
        self.invoice_info = invoice_info
        self.item_infos = item_infos
        self.message = message
        self.shop_prom_inst_vos = shop_prom_inst_vos

    def validate(self):
        if self.delivery_infos:
            for k in self.delivery_infos:
                if k:
                    k.validate()
        if self.invoice_info:
            self.invoice_info.validate()
        if self.item_infos:
            for k in self.item_infos:
                if k:
                    k.validate()
        if self.shop_prom_inst_vos:
            for k in self.shop_prom_inst_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        result['DeliveryInfos'] = []
        if self.delivery_infos is not None:
            for k in self.delivery_infos:
                result['DeliveryInfos'].append(k.to_map() if k else None)
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.invoice_info is not None:
            result['InvoiceInfo'] = self.invoice_info.to_map()
        result['ItemInfos'] = []
        if self.item_infos is not None:
            for k in self.item_infos:
                result['ItemInfos'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        result['ShopPromInstVOS'] = []
        if self.shop_prom_inst_vos is not None:
            for k in self.shop_prom_inst_vos:
                result['ShopPromInstVOS'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        self.delivery_infos = []
        if m.get('DeliveryInfos') is not None:
            for k in m.get('DeliveryInfos'):
                temp_model = RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosDeliveryInfos()
                self.delivery_infos.append(temp_model.from_map(k))
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('InvoiceInfo') is not None:
            temp_model = RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosInvoiceInfo()
            self.invoice_info = temp_model.from_map(m['InvoiceInfo'])
        self.item_infos = []
        if m.get('ItemInfos') is not None:
            for k in m.get('ItemInfos'):
                temp_model = RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosItemInfos()
                self.item_infos.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.shop_prom_inst_vos = []
        if m.get('ShopPromInstVOS') is not None:
            for k in m.get('ShopPromInstVOS'):
                temp_model = RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfosShopPromInstVOS()
                self.shop_prom_inst_vos.append(temp_model.from_map(k))
        return self


class RenderDistributionOrderResponseBodyModel(TeaModel):
    def __init__(
        self,
        address_infos: List[RenderDistributionOrderResponseBodyModelAddressInfos] = None,
        can_sell: bool = None,
        ext_info: Dict[str, str] = None,
        message: str = None,
        render_order_infos: List[RenderDistributionOrderResponseBodyModelRenderOrderInfos] = None,
        unsellable_render_order_infos: List[RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfos] = None,
    ):
        self.address_infos = address_infos
        self.can_sell = can_sell
        self.ext_info = ext_info
        self.message = message
        self.render_order_infos = render_order_infos
        self.unsellable_render_order_infos = unsellable_render_order_infos

    def validate(self):
        if self.address_infos:
            for k in self.address_infos:
                if k:
                    k.validate()
        if self.render_order_infos:
            for k in self.render_order_infos:
                if k:
                    k.validate()
        if self.unsellable_render_order_infos:
            for k in self.unsellable_render_order_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AddressInfos'] = []
        if self.address_infos is not None:
            for k in self.address_infos:
                result['AddressInfos'].append(k.to_map() if k else None)
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.message is not None:
            result['Message'] = self.message
        result['RenderOrderInfos'] = []
        if self.render_order_infos is not None:
            for k in self.render_order_infos:
                result['RenderOrderInfos'].append(k.to_map() if k else None)
        result['UnsellableRenderOrderInfos'] = []
        if self.unsellable_render_order_infos is not None:
            for k in self.unsellable_render_order_infos:
                result['UnsellableRenderOrderInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address_infos = []
        if m.get('AddressInfos') is not None:
            for k in m.get('AddressInfos'):
                temp_model = RenderDistributionOrderResponseBodyModelAddressInfos()
                self.address_infos.append(temp_model.from_map(k))
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.render_order_infos = []
        if m.get('RenderOrderInfos') is not None:
            for k in m.get('RenderOrderInfos'):
                temp_model = RenderDistributionOrderResponseBodyModelRenderOrderInfos()
                self.render_order_infos.append(temp_model.from_map(k))
        self.unsellable_render_order_infos = []
        if m.get('UnsellableRenderOrderInfos') is not None:
            for k in m.get('UnsellableRenderOrderInfos'):
                temp_model = RenderDistributionOrderResponseBodyModelUnsellableRenderOrderInfos()
                self.unsellable_render_order_infos.append(temp_model.from_map(k))
        return self


class RenderDistributionOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        model: RenderDistributionOrderResponseBodyModel = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.model = model
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = RenderDistributionOrderResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class RenderDistributionOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenderDistributionOrderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenderDistributionOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitReturnGoodLogistics4DistributionRequest(TeaModel):
    def __init__(
        self,
        cp_code: str = None,
        dispute_id: int = None,
        distributor_id: str = None,
        logistics_no: str = None,
        sub_distribution_order_id: str = None,
        tenant_id: str = None,
    ):
        self.cp_code = cp_code
        self.dispute_id = dispute_id
        self.distributor_id = distributor_id
        self.logistics_no = logistics_no
        self.sub_distribution_order_id = sub_distribution_order_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cp_code is not None:
            result['CpCode'] = self.cp_code
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.distributor_id is not None:
            result['DistributorId'] = self.distributor_id
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.sub_distribution_order_id is not None:
            result['SubDistributionOrderId'] = self.sub_distribution_order_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DistributorId') is not None:
            self.distributor_id = m.get('DistributorId')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('SubDistributionOrderId') is not None:
            self.sub_distribution_order_id = m.get('SubDistributionOrderId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class SubmitReturnGoodLogistics4DistributionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        logs_id: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sub_code: str = None,
        sub_message: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.logs_id = logs_id
        self.message = message
        self.page_number = page_number
        # pageSize
        self.page_size = page_size
        self.request_id = request_id
        self.sub_code = sub_code
        self.sub_message = sub_message
        self.success = success
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SubmitReturnGoodLogistics4DistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitReturnGoodLogistics4DistributionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitReturnGoodLogistics4DistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


