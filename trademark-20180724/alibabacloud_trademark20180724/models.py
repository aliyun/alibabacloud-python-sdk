# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class QueryTradeProduceListRequest(TeaModel):
    def __init__(
        self,
        register_number: str = None,
        page_num: int = None,
        page_size: int = None,
        pre_order_id: str = None,
        buyer_status: int = None,
        sort_order: str = None,
        sort_filed: str = None,
        biz_id: str = None,
    ):
        self.register_number = register_number
        self.page_num = page_num
        self.page_size = page_size
        self.pre_order_id = pre_order_id
        self.buyer_status = buyer_status
        self.sort_order = sort_order
        self.sort_filed = sort_filed
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_order_id is not None:
            result['PreOrderId'] = self.pre_order_id
        if self.buyer_status is not None:
            result['BuyerStatus'] = self.buyer_status
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PreOrderId') is not None:
            self.pre_order_id = m.get('PreOrderId')
        if m.get('BuyerStatus') is not None:
            self.buyer_status = m.get('BuyerStatus')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryTradeProduceListResponseBodyDataTradeProduces(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        pre_amount: float = None,
        create_time: int = None,
        user_id: str = None,
        biz_id: str = None,
        icon: str = None,
        buyer_status: int = None,
        source: int = None,
        operate_note: str = None,
        pre_order_id: str = None,
        allow_cancel: bool = None,
        register_number: str = None,
        classification: str = None,
        final_amount: float = None,
        fail_reason: int = None,
    ):
        self.update_time = update_time
        self.pre_amount = pre_amount
        self.create_time = create_time
        self.user_id = user_id
        self.biz_id = biz_id
        self.icon = icon
        self.buyer_status = buyer_status
        self.source = source
        self.operate_note = operate_note
        self.pre_order_id = pre_order_id
        self.allow_cancel = allow_cancel
        self.register_number = register_number
        self.classification = classification
        self.final_amount = final_amount
        self.fail_reason = fail_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.pre_amount is not None:
            result['PreAmount'] = self.pre_amount
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.buyer_status is not None:
            result['BuyerStatus'] = self.buyer_status
        if self.source is not None:
            result['Source'] = self.source
        if self.operate_note is not None:
            result['OperateNote'] = self.operate_note
        if self.pre_order_id is not None:
            result['PreOrderId'] = self.pre_order_id
        if self.allow_cancel is not None:
            result['AllowCancel'] = self.allow_cancel
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.final_amount is not None:
            result['FinalAmount'] = self.final_amount
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('PreAmount') is not None:
            self.pre_amount = m.get('PreAmount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('BuyerStatus') is not None:
            self.buyer_status = m.get('BuyerStatus')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('OperateNote') is not None:
            self.operate_note = m.get('OperateNote')
        if m.get('PreOrderId') is not None:
            self.pre_order_id = m.get('PreOrderId')
        if m.get('AllowCancel') is not None:
            self.allow_cancel = m.get('AllowCancel')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('FinalAmount') is not None:
            self.final_amount = m.get('FinalAmount')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        return self


class QueryTradeProduceListResponseBodyData(TeaModel):
    def __init__(
        self,
        trade_produces: List[QueryTradeProduceListResponseBodyDataTradeProduces] = None,
    ):
        self.trade_produces = trade_produces

    def validate(self):
        if self.trade_produces:
            for k in self.trade_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TradeProduces'] = []
        if self.trade_produces is not None:
            for k in self.trade_produces:
                result['TradeProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trade_produces = []
        if m.get('TradeProduces') is not None:
            for k in m.get('TradeProduces'):
                temp_model = QueryTradeProduceListResponseBodyDataTradeProduces()
                self.trade_produces.append(temp_model.from_map(k))
        return self


class QueryTradeProduceListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        total_page_num: int = None,
        request_id: str = None,
        page_size: int = None,
        total_item_num: int = None,
        data: QueryTradeProduceListResponseBodyData = None,
    ):
        self.current_page_num = current_page_num
        self.total_page_num = total_page_num
        self.request_id = request_id
        self.page_size = page_size
        self.total_item_num = total_item_num
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryTradeProduceListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTradeProduceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTradeProduceListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTradeProduceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkMonitorResultsRequest(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
        action_type: int = None,
        procedure_status: int = None,
        tm_name: str = None,
        apply_year: str = None,
        registration_number: str = None,
        classification: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.rule_id = rule_id
        self.action_type = action_type
        self.procedure_status = procedure_status
        self.tm_name = tm_name
        self.apply_year = apply_year
        self.registration_number = registration_number
        self.classification = classification
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.procedure_status is not None:
            result['ProcedureStatus'] = self.procedure_status
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.apply_year is not None:
            result['ApplyYear'] = self.apply_year
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('ProcedureStatus') is not None:
            self.procedure_status = m.get('ProcedureStatus')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('ApplyYear') is not None:
            self.apply_year = m.get('ApplyYear')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTrademarkMonitorResultsResponseBodyDataTmMonitorResult(TeaModel):
    def __init__(
        self,
        tm_procedure_status_desc: str = None,
        wuxiao_end_date: str = None,
        user_id: str = None,
        owner_en_name: str = None,
        tm_uid: str = None,
        owner_name: str = None,
        data_update_time: int = None,
        chesan_end_date: str = None,
        xuzhan_end_date: str = None,
        rule_id: str = None,
        registration_number: str = None,
        tm_name: str = None,
        tm_image: str = None,
        data_create_time: int = None,
        yiyi_end_date: str = None,
        classification: str = None,
        apply_date: str = None,
    ):
        self.tm_procedure_status_desc = tm_procedure_status_desc
        self.wuxiao_end_date = wuxiao_end_date
        self.user_id = user_id
        self.owner_en_name = owner_en_name
        self.tm_uid = tm_uid
        self.owner_name = owner_name
        self.data_update_time = data_update_time
        self.chesan_end_date = chesan_end_date
        self.xuzhan_end_date = xuzhan_end_date
        self.rule_id = rule_id
        self.registration_number = registration_number
        self.tm_name = tm_name
        self.tm_image = tm_image
        self.data_create_time = data_create_time
        self.yiyi_end_date = yiyi_end_date
        self.classification = classification
        self.apply_date = apply_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tm_procedure_status_desc is not None:
            result['TmProcedureStatusDesc'] = self.tm_procedure_status_desc
        if self.wuxiao_end_date is not None:
            result['WuxiaoEndDate'] = self.wuxiao_end_date
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.tm_uid is not None:
            result['TmUid'] = self.tm_uid
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.data_update_time is not None:
            result['DataUpdateTime'] = self.data_update_time
        if self.chesan_end_date is not None:
            result['ChesanEndDate'] = self.chesan_end_date
        if self.xuzhan_end_date is not None:
            result['XuzhanEndDate'] = self.xuzhan_end_date
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_image is not None:
            result['TmImage'] = self.tm_image
        if self.data_create_time is not None:
            result['DataCreateTime'] = self.data_create_time
        if self.yiyi_end_date is not None:
            result['YiyiEndDate'] = self.yiyi_end_date
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.apply_date is not None:
            result['ApplyDate'] = self.apply_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TmProcedureStatusDesc') is not None:
            self.tm_procedure_status_desc = m.get('TmProcedureStatusDesc')
        if m.get('WuxiaoEndDate') is not None:
            self.wuxiao_end_date = m.get('WuxiaoEndDate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('TmUid') is not None:
            self.tm_uid = m.get('TmUid')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('DataUpdateTime') is not None:
            self.data_update_time = m.get('DataUpdateTime')
        if m.get('ChesanEndDate') is not None:
            self.chesan_end_date = m.get('ChesanEndDate')
        if m.get('XuzhanEndDate') is not None:
            self.xuzhan_end_date = m.get('XuzhanEndDate')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmImage') is not None:
            self.tm_image = m.get('TmImage')
        if m.get('DataCreateTime') is not None:
            self.data_create_time = m.get('DataCreateTime')
        if m.get('YiyiEndDate') is not None:
            self.yiyi_end_date = m.get('YiyiEndDate')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('ApplyDate') is not None:
            self.apply_date = m.get('ApplyDate')
        return self


class QueryTrademarkMonitorResultsResponseBodyData(TeaModel):
    def __init__(
        self,
        tm_monitor_result: List[QueryTrademarkMonitorResultsResponseBodyDataTmMonitorResult] = None,
    ):
        self.tm_monitor_result = tm_monitor_result

    def validate(self):
        if self.tm_monitor_result:
            for k in self.tm_monitor_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmMonitorResult'] = []
        if self.tm_monitor_result is not None:
            for k in self.tm_monitor_result:
                result['TmMonitorResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tm_monitor_result = []
        if m.get('TmMonitorResult') is not None:
            for k in m.get('TmMonitorResult'):
                temp_model = QueryTrademarkMonitorResultsResponseBodyDataTmMonitorResult()
                self.tm_monitor_result.append(temp_model.from_map(k))
        return self


class QueryTrademarkMonitorResultsResponseBody(TeaModel):
    def __init__(
        self,
        next_page: bool = None,
        request_id: str = None,
        pre_page: bool = None,
        total_item_num: int = None,
        current_page_num: int = None,
        total_page_num: int = None,
        page_size: int = None,
        data: QueryTrademarkMonitorResultsResponseBodyData = None,
    ):
        self.next_page = next_page
        self.request_id = request_id
        self.pre_page = pre_page
        self.total_item_num = total_item_num
        self.current_page_num = current_page_num
        self.total_page_num = total_page_num
        self.page_size = page_size
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Data') is not None:
            temp_model = QueryTrademarkMonitorResultsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTrademarkMonitorResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTrademarkMonitorResultsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTrademarkMonitorResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelTradeOrderRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class CancelTradeOrderResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class CancelTradeOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelTradeOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CancelTradeOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTmMonitorRuleRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteTmMonitorRuleResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DeleteTmMonitorRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTmMonitorRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteTmMonitorRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadNotaryDataRequest(TeaModel):
    def __init__(
        self,
        notary_type: int = None,
        biz_order_no: str = None,
        upload_context: str = None,
    ):
        self.notary_type = notary_type
        self.biz_order_no = biz_order_no
        self.upload_context = upload_context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.biz_order_no is not None:
            result['BizOrderNo'] = self.biz_order_no
        if self.upload_context is not None:
            result['UploadContext'] = self.upload_context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('BizOrderNo') is not None:
            self.biz_order_no = m.get('BizOrderNo')
        if m.get('UploadContext') is not None:
            self.upload_context = m.get('UploadContext')
        return self


class UploadNotaryDataResponseBody(TeaModel):
    def __init__(
        self,
        user_auth_url: str = None,
        request_id: str = None,
    ):
        self.user_auth_url = user_auth_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_auth_url is not None:
            result['UserAuthUrl'] = self.user_auth_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserAuthUrl') is not None:
            self.user_auth_url = m.get('UserAuthUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadNotaryDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadNotaryDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UploadNotaryDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyApplicantRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CopyApplicantResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CopyApplicantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CopyApplicantResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CopyApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PartnerUpdateTrademarkNameRequest(TeaModel):
    def __init__(
        self,
        tm_icon: str = None,
        aliyun_kp: str = None,
        type: int = None,
        biz_id: str = None,
        caller_type: str = None,
        caller_parent_id: int = None,
        tm_comment: str = None,
        tm_name: str = None,
        bid: str = None,
        event_scene_type: str = None,
    ):
        # tmIcon
        self.tm_icon = tm_icon
        # aliyunKp
        self.aliyun_kp = aliyun_kp
        # type
        self.type = type
        # bizId
        self.biz_id = biz_id
        # callerType
        self.caller_type = caller_type
        # callerParentId
        self.caller_parent_id = caller_parent_id
        # tmComment
        self.tm_comment = tm_comment
        # tmName
        self.tm_name = tm_name
        # bid
        self.bid = bid
        self.event_scene_type = event_scene_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.type is not None:
            result['Type'] = self.type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.caller_type is not None:
            result['CallerType'] = self.caller_type
        if self.caller_parent_id is not None:
            result['CallerParentId'] = self.caller_parent_id
        if self.tm_comment is not None:
            result['TmComment'] = self.tm_comment
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.event_scene_type is not None:
            result['EventSceneType'] = self.event_scene_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')
        if m.get('CallerParentId') is not None:
            self.caller_parent_id = m.get('CallerParentId')
        if m.get('TmComment') is not None:
            self.tm_comment = m.get('TmComment')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('EventSceneType') is not None:
            self.event_scene_type = m.get('EventSceneType')
        return self


class PartnerUpdateTrademarkNameResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        request_id: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        success: bool = None,
        app_name: str = None,
    ):
        # allowRetry
        self.allow_retry = allow_retry
        # requestId
        self.request_id = request_id
        # errorMsg
        self.error_msg = error_msg
        # httpStatusCode
        self.http_status_code = http_status_code
        # dynamicCode
        self.dynamic_code = dynamic_code
        # errorCode
        self.error_code = error_code
        # dynamicMessage
        self.dynamic_message = dynamic_message
        # success
        self.success = success
        # appName
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.success is not None:
            result['Success'] = self.success
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class PartnerUpdateTrademarkNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PartnerUpdateTrademarkNameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PartnerUpdateTrademarkNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentionDetailRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryIntentionDetailResponseBody(TeaModel):
    def __init__(
        self,
        status: int = None,
        type: int = None,
        update_time: int = None,
        relation_biz_id: str = None,
        create_time: int = None,
        user_id: str = None,
        biz_id: str = None,
        partner_mobile: str = None,
        request_id: str = None,
        description: str = None,
        mobile: str = None,
        register_number: str = None,
        classification: str = None,
        user_name: str = None,
    ):
        self.status = status
        self.type = type
        self.update_time = update_time
        self.relation_biz_id = relation_biz_id
        self.create_time = create_time
        self.user_id = user_id
        self.biz_id = biz_id
        self.partner_mobile = partner_mobile
        self.request_id = request_id
        self.description = description
        self.mobile = mobile
        self.register_number = register_number
        self.classification = classification
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.relation_biz_id is not None:
            result['RelationBizId'] = self.relation_biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.partner_mobile is not None:
            result['PartnerMobile'] = self.partner_mobile
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.description is not None:
            result['Description'] = self.description
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('RelationBizId') is not None:
            self.relation_biz_id = m.get('RelationBizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('PartnerMobile') is not None:
            self.partner_mobile = m.get('PartnerMobile')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryIntentionDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryIntentionDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryIntentionDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentionPriceRequest(TeaModel):
    def __init__(
        self,
        intention_biz_id: str = None,
        channel: str = None,
    ):
        self.intention_biz_id = intention_biz_id
        self.channel = channel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.channel is not None:
            result['Channel'] = self.channel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        return self


class QueryIntentionPriceResponseBodyDataTmProducesThirdClassificationThirdClassifications(TeaModel):
    def __init__(
        self,
        classification_name: str = None,
        classification_code: str = None,
    ):
        self.classification_name = classification_name
        self.classification_code = classification_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        return self


class QueryIntentionPriceResponseBodyDataTmProducesThirdClassification(TeaModel):
    def __init__(
        self,
        third_classifications: List[QueryIntentionPriceResponseBodyDataTmProducesThirdClassificationThirdClassifications] = None,
    ):
        self.third_classifications = third_classifications

    def validate(self):
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = QueryIntentionPriceResponseBodyDataTmProducesThirdClassificationThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        return self


class QueryIntentionPriceResponseBodyDataTmProducesFirstClassification(TeaModel):
    def __init__(
        self,
        classification_name: str = None,
        classification_code: str = None,
    ):
        self.classification_name = classification_name
        self.classification_code = classification_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        return self


class QueryIntentionPriceResponseBodyDataTmProduces(TeaModel):
    def __init__(
        self,
        type: int = None,
        status: int = None,
        order_price: float = None,
        update_time: int = None,
        material_name: str = None,
        create_time: int = None,
        biz_id: str = None,
        service_price: float = None,
        tm_icon: str = None,
        tm_name: str = None,
        material_id: str = None,
        supplement_id: int = None,
        loa_url: str = None,
        tm_number: str = None,
        note: str = None,
        supplement_status: int = None,
        total_price: float = None,
        third_classification: QueryIntentionPriceResponseBodyDataTmProducesThirdClassification = None,
        first_classification: QueryIntentionPriceResponseBodyDataTmProducesFirstClassification = None,
    ):
        self.type = type
        self.status = status
        self.order_price = order_price
        self.update_time = update_time
        self.material_name = material_name
        self.create_time = create_time
        self.biz_id = biz_id
        self.service_price = service_price
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.material_id = material_id
        self.supplement_id = supplement_id
        self.loa_url = loa_url
        self.tm_number = tm_number
        self.note = note
        self.supplement_status = supplement_status
        self.total_price = total_price
        self.third_classification = third_classification
        self.first_classification = first_classification

    def validate(self):
        if self.third_classification:
            self.third_classification.validate()
        if self.first_classification:
            self.first_classification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.note is not None:
            result['Note'] = self.note
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('ThirdClassification') is not None:
            temp_model = QueryIntentionPriceResponseBodyDataTmProducesThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        if m.get('FirstClassification') is not None:
            temp_model = QueryIntentionPriceResponseBodyDataTmProducesFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        return self


class QueryIntentionPriceResponseBodyData(TeaModel):
    def __init__(
        self,
        tm_produces: List[QueryIntentionPriceResponseBodyDataTmProduces] = None,
    ):
        self.tm_produces = tm_produces

    def validate(self):
        if self.tm_produces:
            for k in self.tm_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmProduces'] = []
        if self.tm_produces is not None:
            for k in self.tm_produces:
                result['TmProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tm_produces = []
        if m.get('TmProduces') is not None:
            for k in m.get('TmProduces'):
                temp_model = QueryIntentionPriceResponseBodyDataTmProduces()
                self.tm_produces.append(temp_model.from_map(k))
        return self


class QueryIntentionPriceResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        total_page_num: int = None,
        request_id: str = None,
        page_size: int = None,
        total_item_num: int = None,
        data: QueryIntentionPriceResponseBodyData = None,
    ):
        self.current_page_num = current_page_num
        self.total_page_num = total_page_num
        self.request_id = request_id
        self.page_size = page_size
        self.total_item_num = total_item_num
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryIntentionPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryIntentionPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryIntentionPriceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryIntentionPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOfficialFileCustomListRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_num: int = None,
    ):
        self.page_size = page_size
        self.page_num = page_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class QueryOfficialFileCustomListResponseBodyDataCustomList(TeaModel):
    def __init__(
        self,
        status: str = None,
        expire_time: int = None,
        remark: str = None,
        download_url: str = None,
        create_time: int = None,
        end_accept_time: int = None,
        start_accept_time: int = None,
    ):
        self.status = status
        self.expire_time = expire_time
        self.remark = remark
        self.download_url = download_url
        self.create_time = create_time
        self.end_accept_time = end_accept_time
        self.start_accept_time = start_accept_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_accept_time is not None:
            result['EndAcceptTime'] = self.end_accept_time
        if self.start_accept_time is not None:
            result['StartAcceptTime'] = self.start_accept_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndAcceptTime') is not None:
            self.end_accept_time = m.get('EndAcceptTime')
        if m.get('StartAcceptTime') is not None:
            self.start_accept_time = m.get('StartAcceptTime')
        return self


class QueryOfficialFileCustomListResponseBodyData(TeaModel):
    def __init__(
        self,
        custom_list: List[QueryOfficialFileCustomListResponseBodyDataCustomList] = None,
    ):
        self.custom_list = custom_list

    def validate(self):
        if self.custom_list:
            for k in self.custom_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomList'] = []
        if self.custom_list is not None:
            for k in self.custom_list:
                result['CustomList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_list = []
        if m.get('CustomList') is not None:
            for k in m.get('CustomList'):
                temp_model = QueryOfficialFileCustomListResponseBodyDataCustomList()
                self.custom_list.append(temp_model.from_map(k))
        return self


class QueryOfficialFileCustomListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        total_page_num: int = None,
        request_id: str = None,
        page_size: int = None,
        total_item_num: int = None,
        data: QueryOfficialFileCustomListResponseBodyData = None,
    ):
        self.current_page_num = current_page_num
        self.total_page_num = total_page_num
        self.request_id = request_id
        self.page_size = page_size
        self.total_item_num = total_item_num
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryOfficialFileCustomListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryOfficialFileCustomListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOfficialFileCustomListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryOfficialFileCustomListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckTrademarkIconRequest(TeaModel):
    def __init__(
        self,
        trademark_icon_oss_key: str = None,
        event_scene_type: int = None,
    ):
        self.trademark_icon_oss_key = trademark_icon_oss_key
        self.event_scene_type = event_scene_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trademark_icon_oss_key is not None:
            result['TrademarkIconOssKey'] = self.trademark_icon_oss_key
        if self.event_scene_type is not None:
            result['EventSceneType'] = self.event_scene_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrademarkIconOssKey') is not None:
            self.trademark_icon_oss_key = m.get('TrademarkIconOssKey')
        if m.get('EventSceneType') is not None:
            self.event_scene_type = m.get('EventSceneType')
        return self


class CheckTrademarkIconResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class CheckTrademarkIconResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckTrademarkIconResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckTrademarkIconResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySupplementDetailRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class QuerySupplementDetailResponseBodyFileTemplateUrls(TeaModel):
    def __init__(
        self,
        file_template_urls: List[str] = None,
    ):
        self.file_template_urls = file_template_urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_template_urls is not None:
            result['FileTemplateUrls'] = self.file_template_urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileTemplateUrls') is not None:
            self.file_template_urls = m.get('FileTemplateUrls')
        return self


class QuerySupplementDetailResponseBody(TeaModel):
    def __init__(
        self,
        operate_time: int = None,
        serial_number: str = None,
        status: int = None,
        type: int = None,
        sbj_dead_time: int = None,
        accept_dead_time: int = None,
        send_time: int = None,
        accept_time: int = None,
        request_id: str = None,
        tm_number: str = None,
        upload_file_template_url: str = None,
        content: str = None,
        id: int = None,
        file_template_urls: QuerySupplementDetailResponseBodyFileTemplateUrls = None,
    ):
        self.operate_time = operate_time
        self.serial_number = serial_number
        self.status = status
        self.type = type
        self.sbj_dead_time = sbj_dead_time
        self.accept_dead_time = accept_dead_time
        self.send_time = send_time
        self.accept_time = accept_time
        self.request_id = request_id
        self.tm_number = tm_number
        self.upload_file_template_url = upload_file_template_url
        self.content = content
        self.id = id
        self.file_template_urls = file_template_urls

    def validate(self):
        if self.file_template_urls:
            self.file_template_urls.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.sbj_dead_time is not None:
            result['SbjDeadTime'] = self.sbj_dead_time
        if self.accept_dead_time is not None:
            result['AcceptDeadTime'] = self.accept_dead_time
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.accept_time is not None:
            result['AcceptTime'] = self.accept_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.upload_file_template_url is not None:
            result['UploadFileTemplateUrl'] = self.upload_file_template_url
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.file_template_urls is not None:
            result['FileTemplateUrls'] = self.file_template_urls.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('SbjDeadTime') is not None:
            self.sbj_dead_time = m.get('SbjDeadTime')
        if m.get('AcceptDeadTime') is not None:
            self.accept_dead_time = m.get('AcceptDeadTime')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('AcceptTime') is not None:
            self.accept_time = m.get('AcceptTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('UploadFileTemplateUrl') is not None:
            self.upload_file_template_url = m.get('UploadFileTemplateUrl')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('FileTemplateUrls') is not None:
            temp_model = QuerySupplementDetailResponseBodyFileTemplateUrls()
            self.file_template_urls = temp_model.from_map(m['FileTemplateUrls'])
        return self


class QuerySupplementDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySupplementDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QuerySupplementDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadTrademarkOnSaleRequest(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        tm_name: str = None,
        tm_icon: str = None,
        original_price: float = None,
        tm_number: str = None,
        end_time: int = None,
        begin_time: int = None,
        description: str = None,
        label: str = None,
        reg_ann_date: int = None,
        owner_name: str = None,
        owner_en_name: str = None,
        secondary_classification: str = None,
        third_classification: str = None,
        type: str = None,
        reason: str = None,
        status: str = None,
    ):
        self.classification_code = classification_code
        self.tm_name = tm_name
        self.tm_icon = tm_icon
        self.original_price = original_price
        self.tm_number = tm_number
        self.end_time = end_time
        self.begin_time = begin_time
        self.description = description
        self.label = label
        self.reg_ann_date = reg_ann_date
        self.owner_name = owner_name
        self.owner_en_name = owner_en_name
        self.secondary_classification = secondary_classification
        self.third_classification = third_classification
        self.type = type
        self.reason = reason
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification
        if self.type is not None:
            result['Type'] = self.type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        if m.get('ThirdClassification') is not None:
            self.third_classification = m.get('ThirdClassification')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UploadTrademarkOnSaleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadTrademarkOnSaleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadTrademarkOnSaleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UploadTrademarkOnSaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyNotaryPostRequest(TeaModel):
    def __init__(
        self,
        notary_order_id: int = None,
        receiver_name: str = None,
        receiver_address: str = None,
        receiver_phone: str = None,
    ):
        self.notary_order_id = notary_order_id
        self.receiver_name = receiver_name
        self.receiver_address = receiver_address
        self.receiver_phone = receiver_phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        if self.receiver_name is not None:
            result['ReceiverName'] = self.receiver_name
        if self.receiver_address is not None:
            result['ReceiverAddress'] = self.receiver_address
        if self.receiver_phone is not None:
            result['ReceiverPhone'] = self.receiver_phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        if m.get('ReceiverName') is not None:
            self.receiver_name = m.get('ReceiverName')
        if m.get('ReceiverAddress') is not None:
            self.receiver_address = m.get('ReceiverAddress')
        if m.get('ReceiverPhone') is not None:
            self.receiver_phone = m.get('ReceiverPhone')
        return self


class ApplyNotaryPostResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class ApplyNotaryPostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApplyNotaryPostResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ApplyNotaryPostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeMarkApplicationsByIntentionRequest(TeaModel):
    def __init__(
        self,
        intention_biz_id: str = None,
        channel: str = None,
        page_num: int = None,
        page_size: int = None,
        tm_produce_status: str = None,
    ):
        self.intention_biz_id = intention_biz_id
        self.channel = channel
        self.page_num = page_num
        self.page_size = page_size
        self.tm_produce_status = tm_produce_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tm_produce_status is not None:
            result['TmProduceStatus'] = self.tm_produce_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TmProduceStatus') is not None:
            self.tm_produce_status = m.get('TmProduceStatus')
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassificationThirdClassifications(TeaModel):
    def __init__(
        self,
        classification_name: str = None,
        classification_code: str = None,
    ):
        self.classification_name = classification_name
        self.classification_code = classification_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassification(TeaModel):
    def __init__(
        self,
        third_classifications: List[QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassificationThirdClassifications] = None,
    ):
        self.third_classifications = third_classifications

    def validate(self):
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassificationThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesFirstClassification(TeaModel):
    def __init__(
        self,
        classification_name: str = None,
        classification_code: str = None,
    ):
        self.classification_name = classification_name
        self.classification_code = classification_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProduces(TeaModel):
    def __init__(
        self,
        principal_description: str = None,
        type: int = None,
        status: int = None,
        order_price: float = None,
        update_time: int = None,
        material_name: str = None,
        principal_value: int = None,
        create_time: int = None,
        biz_id: str = None,
        service_price: float = None,
        tm_icon: str = None,
        tm_name: str = None,
        material_id: str = None,
        supplement_id: int = None,
        loa_url: str = None,
        tm_number: str = None,
        note: str = None,
        supplement_status: int = None,
        total_price: float = None,
        third_classification: QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassification = None,
        first_classification: QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesFirstClassification = None,
    ):
        self.principal_description = principal_description
        self.type = type
        self.status = status
        self.order_price = order_price
        self.update_time = update_time
        self.material_name = material_name
        self.principal_value = principal_value
        self.create_time = create_time
        self.biz_id = biz_id
        self.service_price = service_price
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.material_id = material_id
        self.supplement_id = supplement_id
        self.loa_url = loa_url
        self.tm_number = tm_number
        self.note = note
        self.supplement_status = supplement_status
        self.total_price = total_price
        self.third_classification = third_classification
        self.first_classification = first_classification

    def validate(self):
        if self.third_classification:
            self.third_classification.validate()
        if self.first_classification:
            self.first_classification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.principal_value is not None:
            result['PrincipalValue'] = self.principal_value
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.note is not None:
            result['Note'] = self.note
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('PrincipalValue') is not None:
            self.principal_value = m.get('PrincipalValue')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('ThirdClassification') is not None:
            temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        if m.get('FirstClassification') is not None:
            temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProducesFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        return self


class QueryTradeMarkApplicationsByIntentionResponseBodyData(TeaModel):
    def __init__(
        self,
        tm_produces: List[QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProduces] = None,
    ):
        self.tm_produces = tm_produces

    def validate(self):
        if self.tm_produces:
            for k in self.tm_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmProduces'] = []
        if self.tm_produces is not None:
            for k in self.tm_produces:
                result['TmProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tm_produces = []
        if m.get('TmProduces') is not None:
            for k in m.get('TmProduces'):
                temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyDataTmProduces()
                self.tm_produces.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationsByIntentionResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        total_page_num: int = None,
        request_id: str = None,
        page_size: int = None,
        total_item_num: int = None,
        data: QueryTradeMarkApplicationsByIntentionResponseBodyData = None,
    ):
        self.current_page_num = current_page_num
        self.total_page_num = total_page_num
        self.request_id = request_id
        self.page_size = page_size
        self.total_item_num = total_item_num
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryTradeMarkApplicationsByIntentionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTradeMarkApplicationsByIntentionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTradeMarkApplicationsByIntentionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTradeMarkApplicationsByIntentionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveExtensionAttributeRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        attribute_key: str = None,
        attribute_value: str = None,
    ):
        self.biz_id = biz_id
        self.attribute_key = attribute_key
        self.attribute_value = attribute_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        return self


class SaveExtensionAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveExtensionAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveExtensionAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveExtensionAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AcceptPartnerNotificationRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        operation: str = None,
        material: str = None,
        remark: str = None,
    ):
        self.biz_id = biz_id
        self.operation = operation
        self.material = material
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.material is not None:
            result['Material'] = self.material
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Material') is not None:
            self.material = m.get('Material')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class AcceptPartnerNotificationResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class AcceptPartnerNotificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AcceptPartnerNotificationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AcceptPartnerNotificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSupplementRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        upload_oss_key_list: Dict[str, Any] = None,
        content: str = None,
    ):
        self.id = id
        self.upload_oss_key_list = upload_oss_key_list
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.upload_oss_key_list is not None:
            result['UploadOssKeyList'] = self.upload_oss_key_list
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('UploadOssKeyList') is not None:
            self.upload_oss_key_list = m.get('UploadOssKeyList')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class SubmitSupplementShrinkRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        upload_oss_key_list_shrink: str = None,
        content: str = None,
    ):
        self.id = id
        self.upload_oss_key_list_shrink = upload_oss_key_list_shrink
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.upload_oss_key_list_shrink is not None:
            result['UploadOssKeyList'] = self.upload_oss_key_list_shrink
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('UploadOssKeyList') is not None:
            self.upload_oss_key_list_shrink = m.get('UploadOssKeyList')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class SubmitSupplementResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class SubmitSupplementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitSupplementResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitSupplementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ForceUploadTrademarkOnsaleRequest(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        tm_name: str = None,
        tm_icon: str = None,
        original_price: float = None,
        tm_number: str = None,
        end_time: int = None,
        begin_time: int = None,
        description: str = None,
        label: str = None,
        reg_ann_date: int = None,
        owner_name: str = None,
        owner_en_name: str = None,
        secondary_classification: str = None,
        third_classification: str = None,
        type: str = None,
        reason: str = None,
    ):
        self.classification_code = classification_code
        self.tm_name = tm_name
        self.tm_icon = tm_icon
        self.original_price = original_price
        self.tm_number = tm_number
        self.end_time = end_time
        self.begin_time = begin_time
        self.description = description
        self.label = label
        self.reg_ann_date = reg_ann_date
        self.owner_name = owner_name
        self.owner_en_name = owner_en_name
        self.secondary_classification = secondary_classification
        self.third_classification = third_classification
        self.type = type
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification
        if self.type is not None:
            result['Type'] = self.type
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        if m.get('ThirdClassification') is not None:
            self.third_classification = m.get('ThirdClassification')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ForceUploadTrademarkOnsaleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ForceUploadTrademarkOnsaleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ForceUploadTrademarkOnsaleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ForceUploadTrademarkOnsaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindMaterialRequest(TeaModel):
    def __init__(
        self,
        material_id: str = None,
        biz_id: str = None,
        loa_oss_key: str = None,
        legal_notice_key: str = None,
    ):
        self.material_id = material_id
        self.biz_id = biz_id
        self.loa_oss_key = loa_oss_key
        self.legal_notice_key = legal_notice_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.legal_notice_key is not None:
            result['LegalNoticeKey'] = self.legal_notice_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('LegalNoticeKey') is not None:
            self.legal_notice_key = m.get('LegalNoticeKey')
        return self


class BindMaterialResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindMaterialResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BindMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultPrincipalResponseBody(TeaModel):
    def __init__(
        self,
        principal_description: str = None,
        principal_name: str = None,
        request_id: str = None,
        principal_value: int = None,
    ):
        self.principal_description = principal_description
        self.principal_name = principal_name
        self.request_id = request_id
        self.principal_value = principal_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.principal_value is not None:
            result['PrincipalValue'] = self.principal_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PrincipalValue') is not None:
            self.principal_value = m.get('PrincipalValue')
        return self


class GetDefaultPrincipalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDefaultPrincipalResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDefaultPrincipalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCommunicationLogsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        type: int = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.biz_id = biz_id
        self.type = type
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.type is not None:
            result['Type'] = self.type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryCommunicationLogsResponseBodyDataTaskList(TeaModel):
    def __init__(
        self,
        note: str = None,
        biz_id: str = None,
        update_time: int = None,
        partner_code: str = None,
        create_time: int = None,
    ):
        self.note = note
        self.biz_id = biz_id
        self.update_time = update_time
        self.partner_code = partner_code
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.note is not None:
            result['Note'] = self.note
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class QueryCommunicationLogsResponseBodyData(TeaModel):
    def __init__(
        self,
        task_list: List[QueryCommunicationLogsResponseBodyDataTaskList] = None,
    ):
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = QueryCommunicationLogsResponseBodyDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class QueryCommunicationLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryCommunicationLogsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryCommunicationLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryCommunicationLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCommunicationLogsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryCommunicationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateQrCodeRequest(TeaModel):
    def __init__(
        self,
        uuid: str = None,
        oss_key: str = None,
        field_key: str = None,
    ):
        self.uuid = uuid
        self.oss_key = oss_key
        self.field_key = field_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.field_key is not None:
            result['FieldKey'] = self.field_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')
        return self


class GenerateQrCodeResponseBody(TeaModel):
    def __init__(
        self,
        uuid: str = None,
        request_id: str = None,
        expire_time: int = None,
        success: bool = None,
        qrcode_url: str = None,
        field_key: str = None,
    ):
        self.uuid = uuid
        self.request_id = request_id
        self.expire_time = expire_time
        self.success = success
        self.qrcode_url = qrcode_url
        self.field_key = field_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.success is not None:
            result['Success'] = self.success
        if self.qrcode_url is not None:
            result['QrcodeUrl'] = self.qrcode_url
        if self.field_key is not None:
            result['FieldKey'] = self.field_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('QrcodeUrl') is not None:
            self.qrcode_url = m.get('QrcodeUrl')
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')
        return self


class GenerateQrCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateQrCodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateQrCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmDissentOriginalRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        contact_name: str = None,
        contact_address: str = None,
        contact_number: str = None,
        contact_province: str = None,
        contact_city: str = None,
        contact_district: str = None,
        contact_county: str = None,
    ):
        self.biz_id = biz_id
        self.contact_name = contact_name
        self.contact_address = contact_address
        self.contact_number = contact_number
        self.contact_province = contact_province
        self.contact_city = contact_city
        self.contact_district = contact_district
        self.contact_county = contact_county

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        return self


class ConfirmDissentOriginalResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfirmDissentOriginalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfirmDissentOriginalResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfirmDissentOriginalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertImageToGrayRequest(TeaModel):
    def __init__(
        self,
        oss_key: str = None,
    ):
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        return self


class ConvertImageToGrayResponseBody(TeaModel):
    def __init__(
        self,
        signature_url: str = None,
        request_id: str = None,
    ):
        self.signature_url = signature_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.signature_url is not None:
            result['SignatureUrl'] = self.signature_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SignatureUrl') is not None:
            self.signature_url = m.get('SignatureUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConvertImageToGrayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConvertImageToGrayResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConvertImageToGrayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIntentionListRequest(TeaModel):
    def __init__(
        self,
        type: int = None,
        status: int = None,
        page_size: int = None,
        page_num: int = None,
        sort_filed: str = None,
        sort_order: str = None,
    ):
        self.type = type
        self.status = status
        self.page_size = page_size
        self.page_num = page_num
        self.sort_filed = sort_filed
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class QueryIntentionListResponseBodyDataIntention(TeaModel):
    def __init__(
        self,
        type: int = None,
        status: int = None,
        update_time: int = None,
        description: str = None,
        register_number: str = None,
        create_time: int = None,
        user_id: str = None,
        biz_id: str = None,
        classification: str = None,
    ):
        self.type = type
        self.status = status
        self.update_time = update_time
        self.description = description
        self.register_number = register_number
        self.create_time = create_time
        self.user_id = user_id
        self.biz_id = biz_id
        self.classification = classification

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.description is not None:
            result['Description'] = self.description
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification is not None:
            result['Classification'] = self.classification
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        return self


class QueryIntentionListResponseBodyData(TeaModel):
    def __init__(
        self,
        intention: List[QueryIntentionListResponseBodyDataIntention] = None,
    ):
        self.intention = intention

    def validate(self):
        if self.intention:
            for k in self.intention:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Intention'] = []
        if self.intention is not None:
            for k in self.intention:
                result['Intention'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.intention = []
        if m.get('Intention') is not None:
            for k in m.get('Intention'):
                temp_model = QueryIntentionListResponseBodyDataIntention()
                self.intention.append(temp_model.from_map(k))
        return self


class QueryIntentionListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        total_page_num: int = None,
        request_id: str = None,
        page_size: int = None,
        total_item_num: int = None,
        data: QueryIntentionListResponseBodyData = None,
    ):
        self.current_page_num = current_page_num
        self.total_page_num = total_page_num
        self.request_id = request_id
        self.page_size = page_size
        self.total_item_num = total_item_num
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryIntentionListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryIntentionListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryIntentionListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryIntentionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthorizationLetterVersionRequest(TeaModel):
    def __init__(
        self,
        oss_key: str = None,
    ):
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        return self


class GetAuthorizationLetterVersionResponseBody(TeaModel):
    def __init__(
        self,
        version: str = None,
        request_id: str = None,
    ):
        self.version = version
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAuthorizationLetterVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAuthorizationLetterVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAuthorizationLetterVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkPriceRequest(TeaModel):
    def __init__(
        self,
        user_id: int = None,
        tm_name: str = None,
        tm_icon: str = None,
        type: int = None,
        order_data: Dict[str, Any] = None,
    ):
        self.user_id = user_id
        self.tm_name = tm_name
        self.tm_icon = tm_icon
        self.type = type
        self.order_data = order_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.type is not None:
            result['Type'] = self.type
        if self.order_data is not None:
            result['OrderData'] = self.order_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OrderData') is not None:
            self.order_data = m.get('OrderData')
        return self


class QueryTrademarkPriceShrinkRequest(TeaModel):
    def __init__(
        self,
        user_id: int = None,
        tm_name: str = None,
        tm_icon: str = None,
        type: int = None,
        order_data_shrink: str = None,
    ):
        self.user_id = user_id
        self.tm_name = tm_name
        self.tm_icon = tm_icon
        self.type = type
        self.order_data_shrink = order_data_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.type is not None:
            result['Type'] = self.type
        if self.order_data_shrink is not None:
            result['OrderData'] = self.order_data_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OrderData') is not None:
            self.order_data_shrink = m.get('OrderData')
        return self


class QueryTrademarkPriceResponseBodyPricesPrices(TeaModel):
    def __init__(
        self,
        original_price: float = None,
        discount_price: float = None,
        currency: str = None,
        trade_price: float = None,
        classification_code: str = None,
    ):
        self.original_price = original_price
        self.discount_price = discount_price
        self.currency = currency
        self.trade_price = trade_price
        self.classification_code = classification_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        return self


class QueryTrademarkPriceResponseBodyPrices(TeaModel):
    def __init__(
        self,
        prices: List[QueryTrademarkPriceResponseBodyPricesPrices] = None,
    ):
        self.prices = prices

    def validate(self):
        if self.prices:
            for k in self.prices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Prices'] = []
        if self.prices is not None:
            for k in self.prices:
                result['Prices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prices = []
        if m.get('Prices') is not None:
            for k in m.get('Prices'):
                temp_model = QueryTrademarkPriceResponseBodyPricesPrices()
                self.prices.append(temp_model.from_map(k))
        return self


class QueryTrademarkPriceResponseBody(TeaModel):
    def __init__(
        self,
        original_price: float = None,
        request_id: str = None,
        discount_price: float = None,
        currency: str = None,
        trade_price: float = None,
        prices: QueryTrademarkPriceResponseBodyPrices = None,
    ):
        self.original_price = original_price
        self.request_id = request_id
        self.discount_price = discount_price
        self.currency = currency
        self.trade_price = trade_price
        self.prices = prices

    def validate(self):
        if self.prices:
            self.prices.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        if self.prices is not None:
            result['Prices'] = self.prices.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        if m.get('Prices') is not None:
            temp_model = QueryTrademarkPriceResponseBodyPrices()
            self.prices = temp_model.from_map(m['Prices'])
        return self


class QueryTrademarkPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTrademarkPriceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTrademarkPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertTmMonitorRuleRequest(TeaModel):
    def __init__(
        self,
        rule_source: str = None,
        rule_name: str = None,
        rule_type: int = None,
        rule_keyword: str = None,
        start_apply_date: str = None,
        end_apply_date: str = None,
        classification: Dict[str, Any] = None,
        notify_status: Dict[str, Any] = None,
    ):
        self.rule_source = rule_source
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.rule_keyword = rule_keyword
        self.start_apply_date = start_apply_date
        self.end_apply_date = end_apply_date
        self.classification = classification
        self.notify_status = notify_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.rule_keyword is not None:
            result['RuleKeyword'] = self.rule_keyword
        if self.start_apply_date is not None:
            result['StartApplyDate'] = self.start_apply_date
        if self.end_apply_date is not None:
            result['EndApplyDate'] = self.end_apply_date
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.notify_status is not None:
            result['NotifyStatus'] = self.notify_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('RuleKeyword') is not None:
            self.rule_keyword = m.get('RuleKeyword')
        if m.get('StartApplyDate') is not None:
            self.start_apply_date = m.get('StartApplyDate')
        if m.get('EndApplyDate') is not None:
            self.end_apply_date = m.get('EndApplyDate')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('NotifyStatus') is not None:
            self.notify_status = m.get('NotifyStatus')
        return self


class InsertTmMonitorRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        rule_source: str = None,
        rule_name: str = None,
        rule_type: int = None,
        rule_keyword: str = None,
        start_apply_date: str = None,
        end_apply_date: str = None,
        classification_shrink: str = None,
        notify_status_shrink: str = None,
    ):
        self.rule_source = rule_source
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.rule_keyword = rule_keyword
        self.start_apply_date = start_apply_date
        self.end_apply_date = end_apply_date
        self.classification_shrink = classification_shrink
        self.notify_status_shrink = notify_status_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.rule_keyword is not None:
            result['RuleKeyword'] = self.rule_keyword
        if self.start_apply_date is not None:
            result['StartApplyDate'] = self.start_apply_date
        if self.end_apply_date is not None:
            result['EndApplyDate'] = self.end_apply_date
        if self.classification_shrink is not None:
            result['Classification'] = self.classification_shrink
        if self.notify_status_shrink is not None:
            result['NotifyStatus'] = self.notify_status_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('RuleKeyword') is not None:
            self.rule_keyword = m.get('RuleKeyword')
        if m.get('StartApplyDate') is not None:
            self.start_apply_date = m.get('StartApplyDate')
        if m.get('EndApplyDate') is not None:
            self.end_apply_date = m.get('EndApplyDate')
        if m.get('Classification') is not None:
            self.classification_shrink = m.get('Classification')
        if m.get('NotifyStatus') is not None:
            self.notify_status_shrink = m.get('NotifyStatus')
        return self


class InsertTmMonitorRuleResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class InsertTmMonitorRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InsertTmMonitorRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InsertTmMonitorRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTrademarkMonitorRulesRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        rule_name: str = None,
        notify_update: int = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.id = id
        self.rule_name = rule_name
        self.notify_update = notify_update
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.notify_update is not None:
            result['NotifyUpdate'] = self.notify_update
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('NotifyUpdate') is not None:
            self.notify_update = m.get('NotifyUpdate')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTrademarkMonitorRulesResponseBodyDataTmMonitorRule(TeaModel):
    def __init__(
        self,
        rule_status: str = None,
        last_finish_time: str = None,
        update_time: str = None,
        rule_type: int = None,
        create_time: str = None,
        user_id: str = None,
        rule_extend: str = None,
        rule_name: str = None,
        end_time: str = None,
        start_time: str = None,
        rule_keyword: str = None,
        last_run_time: str = None,
        version: int = None,
        rule_source: str = None,
        last_update_time: str = None,
        env: str = None,
        notify_update: int = None,
        rule_detail: str = None,
        id: str = None,
    ):
        self.rule_status = rule_status
        self.last_finish_time = last_finish_time
        self.update_time = update_time
        self.rule_type = rule_type
        self.create_time = create_time
        self.user_id = user_id
        self.rule_extend = rule_extend
        self.rule_name = rule_name
        self.end_time = end_time
        self.start_time = start_time
        self.rule_keyword = rule_keyword
        self.last_run_time = last_run_time
        self.version = version
        self.rule_source = rule_source
        self.last_update_time = last_update_time
        self.env = env
        self.notify_update = notify_update
        self.rule_detail = rule_detail
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status
        if self.last_finish_time is not None:
            result['LastFinishTime'] = self.last_finish_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.rule_extend is not None:
            result['RuleExtend'] = self.rule_extend
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.rule_keyword is not None:
            result['RuleKeyword'] = self.rule_keyword
        if self.last_run_time is not None:
            result['LastRunTime'] = self.last_run_time
        if self.version is not None:
            result['Version'] = self.version
        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.env is not None:
            result['Env'] = self.env
        if self.notify_update is not None:
            result['NotifyUpdate'] = self.notify_update
        if self.rule_detail is not None:
            result['RuleDetail'] = self.rule_detail
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')
        if m.get('LastFinishTime') is not None:
            self.last_finish_time = m.get('LastFinishTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RuleExtend') is not None:
            self.rule_extend = m.get('RuleExtend')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RuleKeyword') is not None:
            self.rule_keyword = m.get('RuleKeyword')
        if m.get('LastRunTime') is not None:
            self.last_run_time = m.get('LastRunTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('NotifyUpdate') is not None:
            self.notify_update = m.get('NotifyUpdate')
        if m.get('RuleDetail') is not None:
            self.rule_detail = m.get('RuleDetail')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class QueryTrademarkMonitorRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        tm_monitor_rule: List[QueryTrademarkMonitorRulesResponseBodyDataTmMonitorRule] = None,
    ):
        self.tm_monitor_rule = tm_monitor_rule

    def validate(self):
        if self.tm_monitor_rule:
            for k in self.tm_monitor_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmMonitorRule'] = []
        if self.tm_monitor_rule is not None:
            for k in self.tm_monitor_rule:
                result['TmMonitorRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tm_monitor_rule = []
        if m.get('TmMonitorRule') is not None:
            for k in m.get('TmMonitorRule'):
                temp_model = QueryTrademarkMonitorRulesResponseBodyDataTmMonitorRule()
                self.tm_monitor_rule.append(temp_model.from_map(k))
        return self


class QueryTrademarkMonitorRulesResponseBody(TeaModel):
    def __init__(
        self,
        next_page: bool = None,
        request_id: str = None,
        pre_page: bool = None,
        total_item_num: int = None,
        current_page_num: int = None,
        total_page_num: int = None,
        page_size: int = None,
        data: QueryTrademarkMonitorRulesResponseBodyData = None,
    ):
        self.next_page = next_page
        self.request_id = request_id
        self.pre_page = pre_page
        self.total_item_num = total_item_num
        self.current_page_num = current_page_num
        self.total_page_num = total_page_num
        self.page_size = page_size
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Data') is not None:
            temp_model = QueryTrademarkMonitorRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTrademarkMonitorRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTrademarkMonitorRulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTrademarkMonitorRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DenySupplementRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DenySupplementResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DenySupplementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DenySupplementResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DenySupplementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMaterialRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        query_unconfirmed_info: bool = None,
    ):
        self.id = id
        self.query_unconfirmed_info = query_unconfirmed_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.query_unconfirmed_info is not None:
            result['QueryUnconfirmedInfo'] = self.query_unconfirmed_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('QueryUnconfirmedInfo') is not None:
            self.query_unconfirmed_info = m.get('QueryUnconfirmedInfo')
        return self


class QueryMaterialResponseBodyReviewAdditionalFiles(TeaModel):
    def __init__(
        self,
        review_additional_file: List[str] = None,
    ):
        self.review_additional_file = review_additional_file

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_additional_file is not None:
            result['ReviewAdditionalFile'] = self.review_additional_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewAdditionalFile') is not None:
            self.review_additional_file = m.get('ReviewAdditionalFile')
        return self


class QueryMaterialResponseBody(TeaModel):
    def __init__(
        self,
        type: int = None,
        status: int = None,
        review_application_file: str = None,
        contact_district: str = None,
        business_licence_url: str = None,
        passport_url: str = None,
        contact_province: str = None,
        legal_notice_url: str = None,
        city: str = None,
        eaddress: str = None,
        contact_county: str = None,
        contact_email: str = None,
        request_id: str = None,
        contact_city: str = None,
        region: int = None,
        loa_url: str = None,
        address: str = None,
        note: str = None,
        principal_name: int = None,
        name: str = None,
        principal_description: str = None,
        contact_number: str = None,
        contact_address: str = None,
        contact_zipcode: str = None,
        contact_name: str = None,
        ename: str = None,
        valid_date: int = None,
        id_card_url: str = None,
        expiration_date: int = None,
        card_number: str = None,
        country: str = None,
        town: str = None,
        loa_status: int = None,
        reason: str = None,
        id: int = None,
        province: str = None,
        legal_notice_key: str = None,
        review_additional_files: QueryMaterialResponseBodyReviewAdditionalFiles = None,
    ):
        self.type = type
        self.status = status
        self.review_application_file = review_application_file
        self.contact_district = contact_district
        self.business_licence_url = business_licence_url
        self.passport_url = passport_url
        self.contact_province = contact_province
        self.legal_notice_url = legal_notice_url
        self.city = city
        self.eaddress = eaddress
        self.contact_county = contact_county
        self.contact_email = contact_email
        self.request_id = request_id
        self.contact_city = contact_city
        self.region = region
        self.loa_url = loa_url
        self.address = address
        self.note = note
        self.principal_name = principal_name
        self.name = name
        self.principal_description = principal_description
        self.contact_number = contact_number
        self.contact_address = contact_address
        self.contact_zipcode = contact_zipcode
        self.contact_name = contact_name
        self.ename = ename
        self.valid_date = valid_date
        self.id_card_url = id_card_url
        self.expiration_date = expiration_date
        self.card_number = card_number
        self.country = country
        self.town = town
        self.loa_status = loa_status
        self.reason = reason
        self.id = id
        self.province = province
        self.legal_notice_key = legal_notice_key
        self.review_additional_files = review_additional_files

    def validate(self):
        if self.review_additional_files:
            self.review_additional_files.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.review_application_file is not None:
            result['ReviewApplicationFile'] = self.review_application_file
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.legal_notice_url is not None:
            result['LegalNoticeUrl'] = self.legal_notice_url
        if self.city is not None:
            result['City'] = self.city
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.region is not None:
            result['Region'] = self.region
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.address is not None:
            result['Address'] = self.address
        if self.note is not None:
            result['Note'] = self.note
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.name is not None:
            result['Name'] = self.name
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.ename is not None:
            result['EName'] = self.ename
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.country is not None:
            result['Country'] = self.country
        if self.town is not None:
            result['Town'] = self.town
        if self.loa_status is not None:
            result['LoaStatus'] = self.loa_status
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.id is not None:
            result['Id'] = self.id
        if self.province is not None:
            result['Province'] = self.province
        if self.legal_notice_key is not None:
            result['LegalNoticeKey'] = self.legal_notice_key
        if self.review_additional_files is not None:
            result['ReviewAdditionalFiles'] = self.review_additional_files.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ReviewApplicationFile') is not None:
            self.review_application_file = m.get('ReviewApplicationFile')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('LegalNoticeUrl') is not None:
            self.legal_notice_url = m.get('LegalNoticeUrl')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('LoaStatus') is not None:
            self.loa_status = m.get('LoaStatus')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('LegalNoticeKey') is not None:
            self.legal_notice_key = m.get('LegalNoticeKey')
        if m.get('ReviewAdditionalFiles') is not None:
            temp_model = QueryMaterialResponseBodyReviewAdditionalFiles()
            self.review_additional_files = temp_model.from_map(m['ReviewAdditionalFiles'])
        return self


class QueryMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMaterialResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrademarkOrderRequest(TeaModel):
    def __init__(
        self,
        user_id: int = None,
        tm_name: str = None,
        tm_icon: str = None,
        type: int = None,
        order_data: str = None,
        material_id: str = None,
        loa_oss_key: str = None,
        is_black_icon: bool = None,
        renew_info_id: str = None,
        root_code: str = None,
        channel: str = None,
        register_number: str = None,
        tm_name_type: str = None,
        register_name: str = None,
        tm_comment: str = None,
        biz_id: str = None,
        uid: str = None,
        partner_code: str = None,
        real_user_name: str = None,
        phone_num: str = None,
        principal_name: int = None,
        big_dipper_source: str = None,
        ua: str = None,
        legal_notice_key: str = None,
    ):
        self.user_id = user_id
        self.tm_name = tm_name
        self.tm_icon = tm_icon
        self.type = type
        self.order_data = order_data
        self.material_id = material_id
        self.loa_oss_key = loa_oss_key
        self.is_black_icon = is_black_icon
        self.renew_info_id = renew_info_id
        self.root_code = root_code
        self.channel = channel
        self.register_number = register_number
        self.tm_name_type = tm_name_type
        self.register_name = register_name
        self.tm_comment = tm_comment
        self.biz_id = biz_id
        self.uid = uid
        self.partner_code = partner_code
        self.real_user_name = real_user_name
        self.phone_num = phone_num
        self.principal_name = principal_name
        self.big_dipper_source = big_dipper_source
        self.ua = ua
        self.legal_notice_key = legal_notice_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.type is not None:
            result['Type'] = self.type
        if self.order_data is not None:
            result['OrderData'] = self.order_data
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.is_black_icon is not None:
            result['IsBlackIcon'] = self.is_black_icon
        if self.renew_info_id is not None:
            result['RenewInfoId'] = self.renew_info_id
        if self.root_code is not None:
            result['RootCode'] = self.root_code
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.tm_name_type is not None:
            result['TmNameType'] = self.tm_name_type
        if self.register_name is not None:
            result['RegisterName'] = self.register_name
        if self.tm_comment is not None:
            result['TmComment'] = self.tm_comment
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.real_user_name is not None:
            result['RealUserName'] = self.real_user_name
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.big_dipper_source is not None:
            result['BigDipperSource'] = self.big_dipper_source
        if self.ua is not None:
            result['Ua'] = self.ua
        if self.legal_notice_key is not None:
            result['LegalNoticeKey'] = self.legal_notice_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OrderData') is not None:
            self.order_data = m.get('OrderData')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('IsBlackIcon') is not None:
            self.is_black_icon = m.get('IsBlackIcon')
        if m.get('RenewInfoId') is not None:
            self.renew_info_id = m.get('RenewInfoId')
        if m.get('RootCode') is not None:
            self.root_code = m.get('RootCode')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('TmNameType') is not None:
            self.tm_name_type = m.get('TmNameType')
        if m.get('RegisterName') is not None:
            self.register_name = m.get('RegisterName')
        if m.get('TmComment') is not None:
            self.tm_comment = m.get('TmComment')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('RealUserName') is not None:
            self.real_user_name = m.get('RealUserName')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('BigDipperSource') is not None:
            self.big_dipper_source = m.get('BigDipperSource')
        if m.get('Ua') is not None:
            self.ua = m.get('Ua')
        if m.get('LegalNoticeKey') is not None:
            self.legal_notice_key = m.get('LegalNoticeKey')
        return self


class CreateTrademarkOrderResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        order_id: int = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateTrademarkOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTrademarkOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateTrademarkOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMaterialListRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: int = None,
        region: int = None,
        status: int = None,
        page_num: int = None,
        page_size: int = None,
        card_number: str = None,
        principal_name: int = None,
        material_id: int = None,
    ):
        self.name = name
        self.type = type
        self.region = region
        self.status = status
        self.page_num = page_num
        self.page_size = page_size
        self.card_number = card_number
        self.principal_name = principal_name
        self.material_id = material_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        return self


class QueryMaterialListResponseBodyDataTrademark(TeaModel):
    def __init__(
        self,
        principal_description: str = None,
        status: int = None,
        type: int = None,
        contact_name: str = None,
        card_number: str = None,
        valid_date: int = None,
        region: int = None,
        principal_name: int = None,
        loa_status: int = None,
        name: str = None,
        loa_key: str = None,
        id: int = None,
        reason: str = None,
    ):
        self.principal_description = principal_description
        self.status = status
        self.type = type
        self.contact_name = contact_name
        self.card_number = card_number
        self.valid_date = valid_date
        self.region = region
        self.principal_name = principal_name
        self.loa_status = loa_status
        self.name = name
        self.loa_key = loa_key
        self.id = id
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        if self.region is not None:
            result['Region'] = self.region
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.loa_status is not None:
            result['LoaStatus'] = self.loa_status
        if self.name is not None:
            result['Name'] = self.name
        if self.loa_key is not None:
            result['LoaKey'] = self.loa_key
        if self.id is not None:
            result['Id'] = self.id
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('LoaStatus') is not None:
            self.loa_status = m.get('LoaStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('LoaKey') is not None:
            self.loa_key = m.get('LoaKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class QueryMaterialListResponseBodyData(TeaModel):
    def __init__(
        self,
        trademark: List[QueryMaterialListResponseBodyDataTrademark] = None,
    ):
        self.trademark = trademark

    def validate(self):
        if self.trademark:
            for k in self.trademark:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Trademark'] = []
        if self.trademark is not None:
            for k in self.trademark:
                result['Trademark'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trademark = []
        if m.get('Trademark') is not None:
            for k in m.get('Trademark'):
                temp_model = QueryMaterialListResponseBodyDataTrademark()
                self.trademark.append(temp_model.from_map(k))
        return self


class QueryMaterialListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        total_page_num: int = None,
        request_id: str = None,
        page_size: int = None,
        total_item_num: int = None,
        data: QueryMaterialListResponseBodyData = None,
    ):
        self.current_page_num = current_page_num
        self.total_page_num = total_page_num
        self.request_id = request_id
        self.page_size = page_size
        self.total_item_num = total_item_num
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryMaterialListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryMaterialListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMaterialListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryMaterialListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckTrademarkOrderRequest(TeaModel):
    def __init__(
        self,
        user_id: int = None,
        tm_name: str = None,
        tm_icon: str = None,
        type: int = None,
        order_data: str = None,
        material_id: str = None,
        loa_oss_key: str = None,
        is_black_icon: bool = None,
        renew_info_id: str = None,
        root_code: str = None,
        channel: str = None,
        register_number: str = None,
        tm_name_type: str = None,
        register_name: str = None,
        tm_comment: str = None,
        biz_id: str = None,
        uid: str = None,
        partner_code: str = None,
        real_user_name: str = None,
        phone_num: str = None,
        logo_goods_id: str = None,
    ):
        self.user_id = user_id
        self.tm_name = tm_name
        self.tm_icon = tm_icon
        self.type = type
        self.order_data = order_data
        self.material_id = material_id
        self.loa_oss_key = loa_oss_key
        self.is_black_icon = is_black_icon
        self.renew_info_id = renew_info_id
        self.root_code = root_code
        self.channel = channel
        self.register_number = register_number
        self.tm_name_type = tm_name_type
        self.register_name = register_name
        self.tm_comment = tm_comment
        self.biz_id = biz_id
        self.uid = uid
        self.partner_code = partner_code
        self.real_user_name = real_user_name
        self.phone_num = phone_num
        self.logo_goods_id = logo_goods_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.type is not None:
            result['Type'] = self.type
        if self.order_data is not None:
            result['OrderData'] = self.order_data
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.is_black_icon is not None:
            result['IsBlackIcon'] = self.is_black_icon
        if self.renew_info_id is not None:
            result['RenewInfoId'] = self.renew_info_id
        if self.root_code is not None:
            result['RootCode'] = self.root_code
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.tm_name_type is not None:
            result['TmNameType'] = self.tm_name_type
        if self.register_name is not None:
            result['RegisterName'] = self.register_name
        if self.tm_comment is not None:
            result['TmComment'] = self.tm_comment
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.real_user_name is not None:
            result['RealUserName'] = self.real_user_name
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.logo_goods_id is not None:
            result['LogoGoodsId'] = self.logo_goods_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OrderData') is not None:
            self.order_data = m.get('OrderData')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('IsBlackIcon') is not None:
            self.is_black_icon = m.get('IsBlackIcon')
        if m.get('RenewInfoId') is not None:
            self.renew_info_id = m.get('RenewInfoId')
        if m.get('RootCode') is not None:
            self.root_code = m.get('RootCode')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('TmNameType') is not None:
            self.tm_name_type = m.get('TmNameType')
        if m.get('RegisterName') is not None:
            self.register_name = m.get('RegisterName')
        if m.get('TmComment') is not None:
            self.tm_comment = m.get('TmComment')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('RealUserName') is not None:
            self.real_user_name = m.get('RealUserName')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('LogoGoodsId') is not None:
            self.logo_goods_id = m.get('LogoGoodsId')
        return self


class CheckTrademarkOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckTrademarkOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckTrademarkOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckTrademarkOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeMarkApplicationsRequest(TeaModel):
    def __init__(
        self,
        tm_name: str = None,
        page_num: int = None,
        page_size: int = None,
        material_name: str = None,
        tm_number: str = None,
        order_id: str = None,
        status: int = None,
        supplement_status: int = None,
        sort_order: str = None,
        type: str = None,
        biz_id: str = None,
        intention_biz_id: str = None,
        hidden: int = None,
        product_type: int = None,
        logistics_no: str = None,
        classification_code: str = None,
        sort_filed: str = None,
    ):
        self.tm_name = tm_name
        self.page_num = page_num
        self.page_size = page_size
        self.material_name = material_name
        self.tm_number = tm_number
        self.order_id = order_id
        self.status = status
        self.supplement_status = supplement_status
        self.sort_order = sort_order
        self.type = type
        self.biz_id = biz_id
        self.intention_biz_id = intention_biz_id
        self.hidden = hidden
        self.product_type = product_type
        self.logistics_no = logistics_no
        self.classification_code = classification_code
        self.sort_filed = sort_filed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.status is not None:
            result['Status'] = self.status
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.type is not None:
            result['Type'] = self.type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.hidden is not None:
            result['Hidden'] = self.hidden
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.sort_filed is not None:
            result['SortFiled'] = self.sort_filed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Hidden') is not None:
            self.hidden = m.get('Hidden')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('SortFiled') is not None:
            self.sort_filed = m.get('SortFiled')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassificationThirdClassifications(TeaModel):
    def __init__(
        self,
        classification_name: str = None,
        classification_code: str = None,
    ):
        self.classification_name = classification_name
        self.classification_code = classification_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassification(TeaModel):
    def __init__(
        self,
        third_classifications: List[QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassificationThirdClassifications] = None,
    ):
        self.third_classifications = third_classifications

    def validate(self):
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassificationThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesFlags(TeaModel):
    def __init__(
        self,
        flags: List[str] = None,
    ):
        self.flags = flags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flags is not None:
            result['Flags'] = self.flags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flags') is not None:
            self.flags = m.get('Flags')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesFirstClassification(TeaModel):
    def __init__(
        self,
        classification_name: str = None,
        classification_code: str = None,
    ):
        self.classification_name = classification_name
        self.classification_code = classification_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProducesRenewResponse(TeaModel):
    def __init__(
        self,
        eng_name: str = None,
        register_time: int = None,
        eng_address: str = None,
        address: str = None,
        name: str = None,
        submit_sbjtime: int = None,
    ):
        self.eng_name = eng_name
        self.register_time = register_time
        self.eng_address = eng_address
        self.address = address
        self.name = name
        self.submit_sbjtime = submit_sbjtime

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.address is not None:
            result['Address'] = self.address
        if self.name is not None:
            result['Name'] = self.name
        if self.submit_sbjtime is not None:
            result['SubmitSbjtime'] = self.submit_sbjtime
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SubmitSbjtime') is not None:
            self.submit_sbjtime = m.get('SubmitSbjtime')
        return self


class QueryTradeMarkApplicationsResponseBodyDataTmProduces(TeaModel):
    def __init__(
        self,
        type: int = None,
        status: int = None,
        order_price: float = None,
        submit_audit_time: int = None,
        update_time: int = None,
        material_name: str = None,
        remark: str = None,
        create_time: int = None,
        user_id: str = None,
        biz_id: str = None,
        service_price: float = None,
        tm_icon: str = None,
        tm_name: str = None,
        material_id: int = None,
        supplement_id: int = None,
        loa_url: str = None,
        tm_number: str = None,
        note: str = None,
        supplement_status: int = None,
        principal_name: int = None,
        total_price: float = None,
        submit_time: int = None,
        order_id: str = None,
        third_classification: QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassification = None,
        flags: QueryTradeMarkApplicationsResponseBodyDataTmProducesFlags = None,
        first_classification: QueryTradeMarkApplicationsResponseBodyDataTmProducesFirstClassification = None,
        renew_response: QueryTradeMarkApplicationsResponseBodyDataTmProducesRenewResponse = None,
    ):
        self.type = type
        self.status = status
        self.order_price = order_price
        self.submit_audit_time = submit_audit_time
        self.update_time = update_time
        self.material_name = material_name
        self.remark = remark
        self.create_time = create_time
        self.user_id = user_id
        self.biz_id = biz_id
        self.service_price = service_price
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.material_id = material_id
        self.supplement_id = supplement_id
        self.loa_url = loa_url
        self.tm_number = tm_number
        self.note = note
        self.supplement_status = supplement_status
        self.principal_name = principal_name
        self.total_price = total_price
        self.submit_time = submit_time
        self.order_id = order_id
        self.third_classification = third_classification
        self.flags = flags
        self.first_classification = first_classification
        self.renew_response = renew_response

    def validate(self):
        if self.third_classification:
            self.third_classification.validate()
        if self.flags:
            self.flags.validate()
        if self.first_classification:
            self.first_classification.validate()
        if self.renew_response:
            self.renew_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.submit_audit_time is not None:
            result['SubmitAuditTime'] = self.submit_audit_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.note is not None:
            result['Note'] = self.note
        if self.supplement_status is not None:
            result['SupplementStatus'] = self.supplement_status
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        if self.flags is not None:
            result['Flags'] = self.flags.to_map()
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.renew_response is not None:
            result['RenewResponse'] = self.renew_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('SubmitAuditTime') is not None:
            self.submit_audit_time = m.get('SubmitAuditTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('SupplementStatus') is not None:
            self.supplement_status = m.get('SupplementStatus')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ThirdClassification') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        if m.get('Flags') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesFlags()
            self.flags = temp_model.from_map(m['Flags'])
        if m.get('FirstClassification') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('RenewResponse') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProducesRenewResponse()
            self.renew_response = temp_model.from_map(m['RenewResponse'])
        return self


class QueryTradeMarkApplicationsResponseBodyData(TeaModel):
    def __init__(
        self,
        tm_produces: List[QueryTradeMarkApplicationsResponseBodyDataTmProduces] = None,
    ):
        self.tm_produces = tm_produces

    def validate(self):
        if self.tm_produces:
            for k in self.tm_produces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TmProduces'] = []
        if self.tm_produces is not None:
            for k in self.tm_produces:
                result['TmProduces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tm_produces = []
        if m.get('TmProduces') is not None:
            for k in m.get('TmProduces'):
                temp_model = QueryTradeMarkApplicationsResponseBodyDataTmProduces()
                self.tm_produces.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        total_page_num: int = None,
        request_id: str = None,
        page_size: int = None,
        total_item_num: int = None,
        data: QueryTradeMarkApplicationsResponseBodyData = None,
    ):
        self.current_page_num = current_page_num
        self.total_page_num = total_page_num
        self.request_id = request_id
        self.page_size = page_size
        self.total_item_num = total_item_num
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTradeMarkApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTradeMarkApplicationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTradeMarkApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicantContacterRequest(TeaModel):
    def __init__(
        self,
        contact_address: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_email: str = None,
        applicant_id: int = None,
        contact_zip_code: str = None,
        biz_id: str = None,
    ):
        self.contact_address = contact_address
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_email = contact_email
        self.applicant_id = applicant_id
        self.contact_zip_code = contact_zip_code
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.contact_zip_code is not None:
            result['ContactZipCode'] = self.contact_zip_code
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('ContactZipCode') is not None:
            self.contact_zip_code = m.get('ContactZipCode')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class UpdateApplicantContacterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateApplicantContacterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateApplicantContacterResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateApplicantContacterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskRequest(TeaModel):
    def __init__(
        self,
        request: str = None,
        biz_type: str = None,
    ):
        self.request = request
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request = m.get('Request')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class SaveTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTrademarkApplicationComplaintRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        files: Dict[str, Any] = None,
        content: str = None,
    ):
        self.biz_id = biz_id
        self.files = files
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.files is not None:
            result['Files'] = self.files
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Files') is not None:
            self.files = m.get('Files')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class SubmitTrademarkApplicationComplaintShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        files_shrink: str = None,
        content: str = None,
    ):
        self.biz_id = biz_id
        self.files_shrink = files_shrink
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.files_shrink is not None:
            result['Files'] = self.files_shrink
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class SubmitTrademarkApplicationComplaintResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitTrademarkApplicationComplaintResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitTrademarkApplicationComplaintResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitTrademarkApplicationComplaintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WriteIntentionCommunicationLogRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        note: str = None,
        reject: bool = None,
    ):
        self.biz_id = biz_id
        self.note = note
        self.reject = reject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        if self.reject is not None:
            result['Reject'] = self.reject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Reject') is not None:
            self.reject = m.get('Reject')
        return self


class WriteIntentionCommunicationLogResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class WriteIntentionCommunicationLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WriteIntentionCommunicationLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = WriteIntentionCommunicationLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTaskForOfficialFileCustomRequest(TeaModel):
    def __init__(
        self,
        end_accept_time: int = None,
        start_accept_time: int = None,
    ):
        self.end_accept_time = end_accept_time
        self.start_accept_time = start_accept_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_accept_time is not None:
            result['EndAcceptTime'] = self.end_accept_time
        if self.start_accept_time is not None:
            result['StartAcceptTime'] = self.start_accept_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndAcceptTime') is not None:
            self.end_accept_time = m.get('EndAcceptTime')
        if m.get('StartAcceptTime') is not None:
            self.start_accept_time = m.get('StartAcceptTime')
        return self


class SaveTaskForOfficialFileCustomResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
        request_id: str = None,
    ):
        self.success = success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveTaskForOfficialFileCustomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveTaskForOfficialFileCustomResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveTaskForOfficialFileCustomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescirbeCombineTrademarkRequest(TeaModel):
    def __init__(
        self,
        registration_number: str = None,
        name: str = None,
        owner_name: str = None,
        products: str = None,
        accurate_match: bool = None,
        page_number: int = None,
        page_size: int = None,
        classification: str = None,
        similar_groups: str = None,
    ):
        self.registration_number = registration_number
        self.name = name
        self.owner_name = owner_name
        self.products = products
        self.accurate_match = accurate_match
        self.page_number = page_number
        self.page_size = page_size
        self.classification = classification
        self.similar_groups = similar_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.products is not None:
            result['Products'] = self.products
        if self.accurate_match is not None:
            result['AccurateMatch'] = self.accurate_match
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.similar_groups is not None:
            result['SimilarGroups'] = self.similar_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Products') is not None:
            self.products = m.get('Products')
        if m.get('AccurateMatch') is not None:
            self.accurate_match = m.get('AccurateMatch')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('SimilarGroups') is not None:
            self.similar_groups = m.get('SimilarGroups')
        return self


class DescirbeCombineTrademarkResponseBodyDataAnnouncementList(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        ann_date: str = None,
        original_image_url: str = None,
        ann_type_name: str = None,
        ann_number: str = None,
        ann_type_code: str = None,
    ):
        self.image_url = image_url
        self.ann_date = ann_date
        self.original_image_url = original_image_url
        self.ann_type_name = ann_type_name
        self.ann_number = ann_number
        self.ann_type_code = ann_type_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.ann_date is not None:
            result['AnnDate'] = self.ann_date
        if self.original_image_url is not None:
            result['OriginalImageUrl'] = self.original_image_url
        if self.ann_type_name is not None:
            result['AnnTypeName'] = self.ann_type_name
        if self.ann_number is not None:
            result['AnnNumber'] = self.ann_number
        if self.ann_type_code is not None:
            result['AnnTypeCode'] = self.ann_type_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('AnnDate') is not None:
            self.ann_date = m.get('AnnDate')
        if m.get('OriginalImageUrl') is not None:
            self.original_image_url = m.get('OriginalImageUrl')
        if m.get('AnnTypeName') is not None:
            self.ann_type_name = m.get('AnnTypeName')
        if m.get('AnnNumber') is not None:
            self.ann_number = m.get('AnnNumber')
        if m.get('AnnTypeCode') is not None:
            self.ann_type_code = m.get('AnnTypeCode')
        return self


class DescirbeCombineTrademarkResponseBodyDataProcedures(TeaModel):
    def __init__(
        self,
        procedure_step: str = None,
        procedure_result: str = None,
        procedure_code: str = None,
        procedure_date: str = None,
        procedure_name: str = None,
    ):
        self.procedure_step = procedure_step
        self.procedure_result = procedure_result
        self.procedure_code = procedure_code
        self.procedure_date = procedure_date
        self.procedure_name = procedure_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.procedure_step is not None:
            result['ProcedureStep'] = self.procedure_step
        if self.procedure_result is not None:
            result['ProcedureResult'] = self.procedure_result
        if self.procedure_code is not None:
            result['ProcedureCode'] = self.procedure_code
        if self.procedure_date is not None:
            result['ProcedureDate'] = self.procedure_date
        if self.procedure_name is not None:
            result['ProcedureName'] = self.procedure_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcedureStep') is not None:
            self.procedure_step = m.get('ProcedureStep')
        if m.get('ProcedureResult') is not None:
            self.procedure_result = m.get('ProcedureResult')
        if m.get('ProcedureCode') is not None:
            self.procedure_code = m.get('ProcedureCode')
        if m.get('ProcedureDate') is not None:
            self.procedure_date = m.get('ProcedureDate')
        if m.get('ProcedureName') is not None:
            self.procedure_name = m.get('ProcedureName')
        return self


class DescirbeCombineTrademarkResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        owner_address: str = None,
        pre_ann_date: str = None,
        pre_ann_number: str = None,
        intl_reg_date: str = None,
        share: str = None,
        owner_en_name: str = None,
        subsequent_designation_date: str = None,
        index_id: str = None,
        reg_ann_number: str = None,
        registration_number: str = None,
        second_anno_type: str = None,
        agency: str = None,
        owner_en_address: str = None,
        classification: str = None,
        name: str = None,
        apply_date: str = None,
        priority_date: str = None,
        product_description: str = None,
        image: str = None,
        second_anno_number: str = None,
        registration_type: str = None,
        first_anno_number: str = None,
        owner_name: str = None,
        reg_ann_date: str = None,
        similar_group: str = None,
        on_sale: int = None,
        exclusive_date_limit: str = None,
        first_anno_type: str = None,
        last_procedure_status: str = None,
        law_final_status: str = None,
        announcement_list: List[DescirbeCombineTrademarkResponseBodyDataAnnouncementList] = None,
        procedures: List[DescirbeCombineTrademarkResponseBodyDataProcedures] = None,
    ):
        self.status = status
        self.owner_address = owner_address
        self.pre_ann_date = pre_ann_date
        self.pre_ann_number = pre_ann_number
        self.intl_reg_date = intl_reg_date
        self.share = share
        self.owner_en_name = owner_en_name
        self.subsequent_designation_date = subsequent_designation_date
        self.index_id = index_id
        self.reg_ann_number = reg_ann_number
        self.registration_number = registration_number
        self.second_anno_type = second_anno_type
        self.agency = agency
        self.owner_en_address = owner_en_address
        self.classification = classification
        self.name = name
        self.apply_date = apply_date
        self.priority_date = priority_date
        self.product_description = product_description
        self.image = image
        self.second_anno_number = second_anno_number
        self.registration_type = registration_type
        self.first_anno_number = first_anno_number
        self.owner_name = owner_name
        self.reg_ann_date = reg_ann_date
        self.similar_group = similar_group
        self.on_sale = on_sale
        self.exclusive_date_limit = exclusive_date_limit
        self.first_anno_type = first_anno_type
        self.last_procedure_status = last_procedure_status
        self.law_final_status = law_final_status
        self.announcement_list = announcement_list
        self.procedures = procedures

    def validate(self):
        if self.announcement_list:
            for k in self.announcement_list:
                if k:
                    k.validate()
        if self.procedures:
            for k in self.procedures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.owner_address is not None:
            result['OwnerAddress'] = self.owner_address
        if self.pre_ann_date is not None:
            result['PreAnnDate'] = self.pre_ann_date
        if self.pre_ann_number is not None:
            result['PreAnnNumber'] = self.pre_ann_number
        if self.intl_reg_date is not None:
            result['IntlRegDate'] = self.intl_reg_date
        if self.share is not None:
            result['Share'] = self.share
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.subsequent_designation_date is not None:
            result['SubsequentDesignationDate'] = self.subsequent_designation_date
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.reg_ann_number is not None:
            result['RegAnnNumber'] = self.reg_ann_number
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.second_anno_type is not None:
            result['SecondAnnoType'] = self.second_anno_type
        if self.agency is not None:
            result['Agency'] = self.agency
        if self.owner_en_address is not None:
            result['OwnerEnAddress'] = self.owner_en_address
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.name is not None:
            result['Name'] = self.name
        if self.apply_date is not None:
            result['ApplyDate'] = self.apply_date
        if self.priority_date is not None:
            result['PriorityDate'] = self.priority_date
        if self.product_description is not None:
            result['ProductDescription'] = self.product_description
        if self.image is not None:
            result['Image'] = self.image
        if self.second_anno_number is not None:
            result['SecondAnnoNumber'] = self.second_anno_number
        if self.registration_type is not None:
            result['RegistrationType'] = self.registration_type
        if self.first_anno_number is not None:
            result['FirstAnnoNumber'] = self.first_anno_number
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.similar_group is not None:
            result['SimilarGroup'] = self.similar_group
        if self.on_sale is not None:
            result['OnSale'] = self.on_sale
        if self.exclusive_date_limit is not None:
            result['ExclusiveDateLimit'] = self.exclusive_date_limit
        if self.first_anno_type is not None:
            result['FirstAnnoType'] = self.first_anno_type
        if self.last_procedure_status is not None:
            result['LastProcedureStatus'] = self.last_procedure_status
        if self.law_final_status is not None:
            result['LawFinalStatus'] = self.law_final_status
        result['AnnouncementList'] = []
        if self.announcement_list is not None:
            for k in self.announcement_list:
                result['AnnouncementList'].append(k.to_map() if k else None)
        result['Procedures'] = []
        if self.procedures is not None:
            for k in self.procedures:
                result['Procedures'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('OwnerAddress') is not None:
            self.owner_address = m.get('OwnerAddress')
        if m.get('PreAnnDate') is not None:
            self.pre_ann_date = m.get('PreAnnDate')
        if m.get('PreAnnNumber') is not None:
            self.pre_ann_number = m.get('PreAnnNumber')
        if m.get('IntlRegDate') is not None:
            self.intl_reg_date = m.get('IntlRegDate')
        if m.get('Share') is not None:
            self.share = m.get('Share')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('SubsequentDesignationDate') is not None:
            self.subsequent_designation_date = m.get('SubsequentDesignationDate')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('RegAnnNumber') is not None:
            self.reg_ann_number = m.get('RegAnnNumber')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('SecondAnnoType') is not None:
            self.second_anno_type = m.get('SecondAnnoType')
        if m.get('Agency') is not None:
            self.agency = m.get('Agency')
        if m.get('OwnerEnAddress') is not None:
            self.owner_en_address = m.get('OwnerEnAddress')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ApplyDate') is not None:
            self.apply_date = m.get('ApplyDate')
        if m.get('PriorityDate') is not None:
            self.priority_date = m.get('PriorityDate')
        if m.get('ProductDescription') is not None:
            self.product_description = m.get('ProductDescription')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('SecondAnnoNumber') is not None:
            self.second_anno_number = m.get('SecondAnnoNumber')
        if m.get('RegistrationType') is not None:
            self.registration_type = m.get('RegistrationType')
        if m.get('FirstAnnoNumber') is not None:
            self.first_anno_number = m.get('FirstAnnoNumber')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('SimilarGroup') is not None:
            self.similar_group = m.get('SimilarGroup')
        if m.get('OnSale') is not None:
            self.on_sale = m.get('OnSale')
        if m.get('ExclusiveDateLimit') is not None:
            self.exclusive_date_limit = m.get('ExclusiveDateLimit')
        if m.get('FirstAnnoType') is not None:
            self.first_anno_type = m.get('FirstAnnoType')
        if m.get('LastProcedureStatus') is not None:
            self.last_procedure_status = m.get('LastProcedureStatus')
        if m.get('LawFinalStatus') is not None:
            self.law_final_status = m.get('LawFinalStatus')
        self.announcement_list = []
        if m.get('AnnouncementList') is not None:
            for k in m.get('AnnouncementList'):
                temp_model = DescirbeCombineTrademarkResponseBodyDataAnnouncementList()
                self.announcement_list.append(temp_model.from_map(k))
        self.procedures = []
        if m.get('Procedures') is not None:
            for k in m.get('Procedures'):
                temp_model = DescirbeCombineTrademarkResponseBodyDataProcedures()
                self.procedures.append(temp_model.from_map(k))
        return self


class DescirbeCombineTrademarkResponseBody(TeaModel):
    def __init__(
        self,
        next_page: bool = None,
        request_id: str = None,
        total_page_number: int = None,
        pre_page: bool = None,
        current_page_number: int = None,
        total_item_number: int = None,
        page_size: int = None,
        data: List[DescirbeCombineTrademarkResponseBodyData] = None,
    ):
        self.next_page = next_page
        self.request_id = request_id
        self.total_page_number = total_page_number
        self.pre_page = pre_page
        self.current_page_number = current_page_number
        self.total_item_number = total_item_number
        self.page_size = page_size
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_page_number is not None:
            result['TotalPageNumber'] = self.total_page_number
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.current_page_number is not None:
            result['CurrentPageNumber'] = self.current_page_number
        if self.total_item_number is not None:
            result['TotalItemNumber'] = self.total_item_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalPageNumber') is not None:
            self.total_page_number = m.get('TotalPageNumber')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('CurrentPageNumber') is not None:
            self.current_page_number = m.get('CurrentPageNumber')
        if m.get('TotalItemNumber') is not None:
            self.total_item_number = m.get('TotalItemNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescirbeCombineTrademarkResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class DescirbeCombineTrademarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescirbeCombineTrademarkResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescirbeCombineTrademarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNotaryOrderRequest(TeaModel):
    def __init__(
        self,
        notary_order_id: int = None,
    ):
        self.notary_order_id = notary_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        return self


class GetNotaryOrderResponseBody(TeaModel):
    def __init__(
        self,
        type: str = None,
        order_price: float = None,
        legal_person_id_card: str = None,
        business_license_id: str = None,
        notary_post_receipt: str = None,
        company_contact_name: str = None,
        notary_status: int = None,
        seller_back_of_id_card: str = None,
        tm_register_change_certificate: str = None,
        request_id: str = None,
        legal_person_name: str = None,
        tm_image: str = None,
        notary_accept_date: int = None,
        error_code: str = None,
        aliyun_order_id: str = None,
        notary_succeed_date: int = None,
        apply_post_status: int = None,
        error_msg: str = None,
        name: str = None,
        business_license: str = None,
        receiver_name: str = None,
        order_date: int = None,
        company_contact_phone: str = None,
        notary_type: int = None,
        notary_failed_date: int = None,
        tm_classification: str = None,
        success: bool = None,
        biz_id: str = None,
        notary_order_id: int = None,
        phone: str = None,
        receiver_phone: str = None,
        tm_register_certificate: str = None,
        tm_name: str = None,
        tm_register_no: str = None,
        seller_company_name: str = None,
        tm_accept_certificate: str = None,
        receiver_postal_code: str = None,
        notary_certificate: str = None,
        legal_person_phone: str = None,
        notary_failed_reason: str = None,
        seller_front_of_id_card: str = None,
        receiver_address: str = None,
        notary_platform_name: str = None,
    ):
        self.type = type
        self.order_price = order_price
        self.legal_person_id_card = legal_person_id_card
        self.business_license_id = business_license_id
        self.notary_post_receipt = notary_post_receipt
        self.company_contact_name = company_contact_name
        self.notary_status = notary_status
        self.seller_back_of_id_card = seller_back_of_id_card
        self.tm_register_change_certificate = tm_register_change_certificate
        self.request_id = request_id
        self.legal_person_name = legal_person_name
        self.tm_image = tm_image
        self.notary_accept_date = notary_accept_date
        self.error_code = error_code
        self.aliyun_order_id = aliyun_order_id
        self.notary_succeed_date = notary_succeed_date
        self.apply_post_status = apply_post_status
        self.error_msg = error_msg
        self.name = name
        self.business_license = business_license
        self.receiver_name = receiver_name
        self.order_date = order_date
        self.company_contact_phone = company_contact_phone
        self.notary_type = notary_type
        self.notary_failed_date = notary_failed_date
        self.tm_classification = tm_classification
        self.success = success
        self.biz_id = biz_id
        self.notary_order_id = notary_order_id
        self.phone = phone
        self.receiver_phone = receiver_phone
        self.tm_register_certificate = tm_register_certificate
        self.tm_name = tm_name
        self.tm_register_no = tm_register_no
        self.seller_company_name = seller_company_name
        self.tm_accept_certificate = tm_accept_certificate
        self.receiver_postal_code = receiver_postal_code
        self.notary_certificate = notary_certificate
        self.legal_person_phone = legal_person_phone
        self.notary_failed_reason = notary_failed_reason
        self.seller_front_of_id_card = seller_front_of_id_card
        self.receiver_address = receiver_address
        self.notary_platform_name = notary_platform_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.legal_person_id_card is not None:
            result['LegalPersonIdCard'] = self.legal_person_id_card
        if self.business_license_id is not None:
            result['BusinessLicenseId'] = self.business_license_id
        if self.notary_post_receipt is not None:
            result['NotaryPostReceipt'] = self.notary_post_receipt
        if self.company_contact_name is not None:
            result['CompanyContactName'] = self.company_contact_name
        if self.notary_status is not None:
            result['NotaryStatus'] = self.notary_status
        if self.seller_back_of_id_card is not None:
            result['SellerBackOfIdCard'] = self.seller_back_of_id_card
        if self.tm_register_change_certificate is not None:
            result['TmRegisterChangeCertificate'] = self.tm_register_change_certificate
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name
        if self.tm_image is not None:
            result['TmImage'] = self.tm_image
        if self.notary_accept_date is not None:
            result['NotaryAcceptDate'] = self.notary_accept_date
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.notary_succeed_date is not None:
            result['NotarySucceedDate'] = self.notary_succeed_date
        if self.apply_post_status is not None:
            result['ApplyPostStatus'] = self.apply_post_status
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.name is not None:
            result['Name'] = self.name
        if self.business_license is not None:
            result['BusinessLicense'] = self.business_license
        if self.receiver_name is not None:
            result['ReceiverName'] = self.receiver_name
        if self.order_date is not None:
            result['OrderDate'] = self.order_date
        if self.company_contact_phone is not None:
            result['CompanyContactPhone'] = self.company_contact_phone
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.notary_failed_date is not None:
            result['NotaryFailedDate'] = self.notary_failed_date
        if self.tm_classification is not None:
            result['TmClassification'] = self.tm_classification
        if self.success is not None:
            result['Success'] = self.success
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.receiver_phone is not None:
            result['ReceiverPhone'] = self.receiver_phone
        if self.tm_register_certificate is not None:
            result['TmRegisterCertificate'] = self.tm_register_certificate
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_register_no is not None:
            result['TmRegisterNo'] = self.tm_register_no
        if self.seller_company_name is not None:
            result['SellerCompanyName'] = self.seller_company_name
        if self.tm_accept_certificate is not None:
            result['TmAcceptCertificate'] = self.tm_accept_certificate
        if self.receiver_postal_code is not None:
            result['ReceiverPostalCode'] = self.receiver_postal_code
        if self.notary_certificate is not None:
            result['NotaryCertificate'] = self.notary_certificate
        if self.legal_person_phone is not None:
            result['LegalPersonPhone'] = self.legal_person_phone
        if self.notary_failed_reason is not None:
            result['NotaryFailedReason'] = self.notary_failed_reason
        if self.seller_front_of_id_card is not None:
            result['SellerFrontOfIdCard'] = self.seller_front_of_id_card
        if self.receiver_address is not None:
            result['ReceiverAddress'] = self.receiver_address
        if self.notary_platform_name is not None:
            result['NotaryPlatformName'] = self.notary_platform_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('LegalPersonIdCard') is not None:
            self.legal_person_id_card = m.get('LegalPersonIdCard')
        if m.get('BusinessLicenseId') is not None:
            self.business_license_id = m.get('BusinessLicenseId')
        if m.get('NotaryPostReceipt') is not None:
            self.notary_post_receipt = m.get('NotaryPostReceipt')
        if m.get('CompanyContactName') is not None:
            self.company_contact_name = m.get('CompanyContactName')
        if m.get('NotaryStatus') is not None:
            self.notary_status = m.get('NotaryStatus')
        if m.get('SellerBackOfIdCard') is not None:
            self.seller_back_of_id_card = m.get('SellerBackOfIdCard')
        if m.get('TmRegisterChangeCertificate') is not None:
            self.tm_register_change_certificate = m.get('TmRegisterChangeCertificate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')
        if m.get('TmImage') is not None:
            self.tm_image = m.get('TmImage')
        if m.get('NotaryAcceptDate') is not None:
            self.notary_accept_date = m.get('NotaryAcceptDate')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('NotarySucceedDate') is not None:
            self.notary_succeed_date = m.get('NotarySucceedDate')
        if m.get('ApplyPostStatus') is not None:
            self.apply_post_status = m.get('ApplyPostStatus')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('BusinessLicense') is not None:
            self.business_license = m.get('BusinessLicense')
        if m.get('ReceiverName') is not None:
            self.receiver_name = m.get('ReceiverName')
        if m.get('OrderDate') is not None:
            self.order_date = m.get('OrderDate')
        if m.get('CompanyContactPhone') is not None:
            self.company_contact_phone = m.get('CompanyContactPhone')
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('NotaryFailedDate') is not None:
            self.notary_failed_date = m.get('NotaryFailedDate')
        if m.get('TmClassification') is not None:
            self.tm_classification = m.get('TmClassification')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ReceiverPhone') is not None:
            self.receiver_phone = m.get('ReceiverPhone')
        if m.get('TmRegisterCertificate') is not None:
            self.tm_register_certificate = m.get('TmRegisterCertificate')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmRegisterNo') is not None:
            self.tm_register_no = m.get('TmRegisterNo')
        if m.get('SellerCompanyName') is not None:
            self.seller_company_name = m.get('SellerCompanyName')
        if m.get('TmAcceptCertificate') is not None:
            self.tm_accept_certificate = m.get('TmAcceptCertificate')
        if m.get('ReceiverPostalCode') is not None:
            self.receiver_postal_code = m.get('ReceiverPostalCode')
        if m.get('NotaryCertificate') is not None:
            self.notary_certificate = m.get('NotaryCertificate')
        if m.get('LegalPersonPhone') is not None:
            self.legal_person_phone = m.get('LegalPersonPhone')
        if m.get('NotaryFailedReason') is not None:
            self.notary_failed_reason = m.get('NotaryFailedReason')
        if m.get('SellerFrontOfIdCard') is not None:
            self.seller_front_of_id_card = m.get('SellerFrontOfIdCard')
        if m.get('ReceiverAddress') is not None:
            self.receiver_address = m.get('ReceiverAddress')
        if m.get('NotaryPlatformName') is not None:
            self.notary_platform_name = m.get('NotaryPlatformName')
        return self


class GetNotaryOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetNotaryOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetNotaryOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmAdditionalMaterialRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        note: str = None,
    ):
        self.biz_id = biz_id
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class ConfirmAdditionalMaterialResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class ConfirmAdditionalMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfirmAdditionalMaterialResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfirmAdditionalMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertRenewInfoRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        eng_name: str = None,
        address: str = None,
        eng_address: str = None,
        register_time: int = None,
    ):
        self.name = name
        self.eng_name = eng_name
        self.address = address
        self.eng_address = eng_address
        self.register_time = register_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.address is not None:
            result['Address'] = self.address
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        return self


class InsertRenewInfoResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        id: int = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class InsertRenewInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InsertRenewInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InsertRenewInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCredentialsInfoRequest(TeaModel):
    def __init__(
        self,
        oss_key: str = None,
        material_type: str = None,
        company_name: str = None,
    ):
        self.oss_key = oss_key
        self.material_type = material_type
        self.company_name = company_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        return self


class QueryCredentialsInfoResponseBodyCredentialsInfo(TeaModel):
    def __init__(
        self,
        card_number: str = None,
        address: str = None,
        person_name: str = None,
        province: str = None,
        company_name: str = None,
    ):
        self.card_number = card_number
        self.address = address
        self.person_name = person_name
        self.province = province
        self.company_name = company_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.address is not None:
            result['Address'] = self.address
        if self.person_name is not None:
            result['PersonName'] = self.person_name
        if self.province is not None:
            result['Province'] = self.province
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('PersonName') is not None:
            self.person_name = m.get('PersonName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        return self


class QueryCredentialsInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        credentials_info: QueryCredentialsInfoResponseBodyCredentialsInfo = None,
    ):
        self.request_id = request_id
        self.credentials_info = credentials_info

    def validate(self):
        if self.credentials_info:
            self.credentials_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.credentials_info is not None:
            result['CredentialsInfo'] = self.credentials_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CredentialsInfo') is not None:
            temp_model = QueryCredentialsInfoResponseBodyCredentialsInfo()
            self.credentials_info = temp_model.from_map(m['CredentialsInfo'])
        return self


class QueryCredentialsInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCredentialsInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryCredentialsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTmOnsalesRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        classification: str = None,
        product_code: str = None,
        page_num: int = None,
        page_size: int = None,
        register_number: str = None,
        tm_name: str = None,
        top_search: str = None,
        tag: str = None,
        order_price_left: int = None,
        order_price_right: int = None,
        reg_left: int = None,
        reg_right: int = None,
        sort_name: str = None,
        sort_order: str = None,
        query_all: bool = None,
    ):
        self.keyword = keyword
        self.classification = classification
        self.product_code = product_code
        self.page_num = page_num
        self.page_size = page_size
        self.register_number = register_number
        self.tm_name = tm_name
        self.top_search = top_search
        self.tag = tag
        self.order_price_left = order_price_left
        self.order_price_right = order_price_right
        self.reg_left = reg_left
        self.reg_right = reg_right
        self.sort_name = sort_name
        self.sort_order = sort_order
        self.query_all = query_all

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.top_search is not None:
            result['TopSearch'] = self.top_search
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.order_price_left is not None:
            result['OrderPriceLeft'] = self.order_price_left
        if self.order_price_right is not None:
            result['OrderPriceRight'] = self.order_price_right
        if self.reg_left is not None:
            result['RegLeft'] = self.reg_left
        if self.reg_right is not None:
            result['RegRight'] = self.reg_right
        if self.sort_name is not None:
            result['SortName'] = self.sort_name
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.query_all is not None:
            result['QueryAll'] = self.query_all
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TopSearch') is not None:
            self.top_search = m.get('TopSearch')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('OrderPriceLeft') is not None:
            self.order_price_left = m.get('OrderPriceLeft')
        if m.get('OrderPriceRight') is not None:
            self.order_price_right = m.get('OrderPriceRight')
        if m.get('RegLeft') is not None:
            self.reg_left = m.get('RegLeft')
        if m.get('RegRight') is not None:
            self.reg_right = m.get('RegRight')
        if m.get('SortName') is not None:
            self.sort_name = m.get('SortName')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('QueryAll') is not None:
            self.query_all = m.get('QueryAll')
        return self


class SearchTmOnsalesResponseBodyTrademarks(TeaModel):
    def __init__(
        self,
        trademark_name: str = None,
        status: int = None,
        product_desc: str = None,
        registration_number: str = None,
        icon: str = None,
        partner_code: str = None,
        classification: str = None,
        uid: str = None,
        product_code: str = None,
        order_price: str = None,
    ):
        self.trademark_name = trademark_name
        self.status = status
        self.product_desc = product_desc
        self.registration_number = registration_number
        self.icon = icon
        self.partner_code = partner_code
        self.classification = classification
        self.uid = uid
        self.product_code = product_code
        self.order_price = order_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.status is not None:
            result['Status'] = self.status
        if self.product_desc is not None:
            result['ProductDesc'] = self.product_desc
        if self.registration_number is not None:
            result['RegistrationNumber'] = self.registration_number
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ProductDesc') is not None:
            self.product_desc = m.get('ProductDesc')
        if m.get('RegistrationNumber') is not None:
            self.registration_number = m.get('RegistrationNumber')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        return self


class SearchTmOnsalesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        total_page_number: int = None,
        total_count: int = None,
        trademarks: List[SearchTmOnsalesResponseBodyTrademarks] = None,
    ):
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.total_page_number = total_page_number
        self.total_count = total_count
        self.trademarks = trademarks

    def validate(self):
        if self.trademarks:
            for k in self.trademarks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_page_number is not None:
            result['TotalPageNumber'] = self.total_page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Trademarks'] = []
        if self.trademarks is not None:
            for k in self.trademarks:
                result['Trademarks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalPageNumber') is not None:
            self.total_page_number = m.get('TotalPageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.trademarks = []
        if m.get('Trademarks') is not None:
            for k in m.get('Trademarks'):
                temp_model = SearchTmOnsalesResponseBodyTrademarks()
                self.trademarks.append(temp_model.from_map(k))
        return self


class SearchTmOnsalesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchTmOnsalesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchTmOnsalesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUploadFilePolicyRequest(TeaModel):
    def __init__(
        self,
        file_type: str = None,
        biz_id: str = None,
    ):
        self.file_type = file_type
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class GenerateUploadFilePolicyResponseBody(TeaModel):
    def __init__(
        self,
        signature: str = None,
        host: str = None,
        request_id: str = None,
        expire_time: int = None,
        encoded_policy: str = None,
        file_dir: str = None,
        access_id: str = None,
    ):
        self.signature = signature
        self.host = host
        self.request_id = request_id
        self.expire_time = expire_time
        self.encoded_policy = encoded_policy
        self.file_dir = file_dir
        self.access_id = access_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.host is not None:
            result['Host'] = self.host
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.encoded_policy is not None:
            result['EncodedPolicy'] = self.encoded_policy
        if self.file_dir is not None:
            result['FileDir'] = self.file_dir
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('EncodedPolicy') is not None:
            self.encoded_policy = m.get('EncodedPolicy')
        if m.get('FileDir') is not None:
            self.file_dir = m.get('FileDir')
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        return self


class GenerateUploadFilePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateUploadFilePolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateUploadFilePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMaterialRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteMaterialResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DeleteMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMaterialResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WriteCommunicationLogRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        note: str = None,
        target_id: str = None,
    ):
        self.biz_id = biz_id
        self.note = note
        self.target_id = target_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        return self


class WriteCommunicationLogResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class WriteCommunicationLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WriteCommunicationLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = WriteCommunicationLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertTradeIntentionUserRequest(TeaModel):
    def __init__(
        self,
        register_number: str = None,
        classification: str = None,
        type: int = None,
        mobile: str = None,
        vcode: str = None,
        partner_code: str = None,
        user_name: str = None,
        description: str = None,
        channel: str = None,
        token: str = None,
        ua: str = None,
    ):
        self.register_number = register_number
        self.classification = classification
        self.type = type
        self.mobile = mobile
        self.vcode = vcode
        self.partner_code = partner_code
        self.user_name = user_name
        self.description = description
        self.channel = channel
        self.token = token
        self.ua = ua

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.type is not None:
            result['Type'] = self.type
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.vcode is not None:
            result['Vcode'] = self.vcode
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.description is not None:
            result['Description'] = self.description
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.token is not None:
            result['Token'] = self.token
        if self.ua is not None:
            result['Ua'] = self.ua
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Vcode') is not None:
            self.vcode = m.get('Vcode')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Ua') is not None:
            self.ua = m.get('Ua')
        return self


class InsertTradeIntentionUserResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertTradeIntentionUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InsertTradeIntentionUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InsertTradeIntentionUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryExtensionAttributeRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        attribute_key: str = None,
    ):
        self.biz_id = biz_id
        self.attribute_key = attribute_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')
        return self


class QueryExtensionAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        attribute_value: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.attribute_value = attribute_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        return self


class QueryExtensionAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryExtensionAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryExtensionAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrademarkOnsaleRequest(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        tm_name: str = None,
        tm_icon: str = None,
        original_price: float = None,
        tm_number: str = None,
        end_time: int = None,
        begin_time: int = None,
        description: str = None,
        label: str = None,
        reg_ann_date: int = None,
        owner_name: str = None,
        owner_en_name: str = None,
        secondary_classification: str = None,
        third_classification: str = None,
        type: str = None,
        reason: str = None,
    ):
        self.classification_code = classification_code
        self.tm_name = tm_name
        self.tm_icon = tm_icon
        self.original_price = original_price
        self.tm_number = tm_number
        self.end_time = end_time
        self.begin_time = begin_time
        self.description = description
        self.label = label
        self.reg_ann_date = reg_ann_date
        self.owner_name = owner_name
        self.owner_en_name = owner_en_name
        self.secondary_classification = secondary_classification
        self.third_classification = third_classification
        self.type = type
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification
        if self.type is not None:
            result['Type'] = self.type
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        if m.get('ThirdClassification') is not None:
            self.third_classification = m.get('ThirdClassification')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class UpdateTrademarkOnsaleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateTrademarkOnsaleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateTrademarkOnsaleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateTrademarkOnsaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeProduceDetailRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryTradeProduceDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        third_code: str = None,
        share: str = None,
        pre_amount: float = None,
        create_time: int = None,
        user_id: str = None,
        refund_amount: float = None,
        icon: str = None,
        biz_id: str = None,
        buyer_status: int = None,
        source: int = None,
        confiscate_amount: float = None,
        operate_note: str = None,
        pre_order_id: str = None,
        extend: Dict[str, Any] = None,
        tm_name: str = None,
        exclusive_date_limit: str = None,
        allow_cancel: bool = None,
        register_number: str = None,
        final_amount: float = None,
        classification: str = None,
        paid_amount: float = None,
    ):
        self.update_time = update_time
        self.third_code = third_code
        self.share = share
        self.pre_amount = pre_amount
        self.create_time = create_time
        self.user_id = user_id
        self.refund_amount = refund_amount
        self.icon = icon
        self.biz_id = biz_id
        self.buyer_status = buyer_status
        self.source = source
        self.confiscate_amount = confiscate_amount
        self.operate_note = operate_note
        self.pre_order_id = pre_order_id
        self.extend = extend
        self.tm_name = tm_name
        self.exclusive_date_limit = exclusive_date_limit
        self.allow_cancel = allow_cancel
        self.register_number = register_number
        self.final_amount = final_amount
        self.classification = classification
        self.paid_amount = paid_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.third_code is not None:
            result['ThirdCode'] = self.third_code
        if self.share is not None:
            result['Share'] = self.share
        if self.pre_amount is not None:
            result['PreAmount'] = self.pre_amount
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.refund_amount is not None:
            result['RefundAmount'] = self.refund_amount
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.buyer_status is not None:
            result['BuyerStatus'] = self.buyer_status
        if self.source is not None:
            result['Source'] = self.source
        if self.confiscate_amount is not None:
            result['ConfiscateAmount'] = self.confiscate_amount
        if self.operate_note is not None:
            result['OperateNote'] = self.operate_note
        if self.pre_order_id is not None:
            result['PreOrderId'] = self.pre_order_id
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.exclusive_date_limit is not None:
            result['ExclusiveDateLimit'] = self.exclusive_date_limit
        if self.allow_cancel is not None:
            result['AllowCancel'] = self.allow_cancel
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.final_amount is not None:
            result['FinalAmount'] = self.final_amount
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.paid_amount is not None:
            result['PaidAmount'] = self.paid_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ThirdCode') is not None:
            self.third_code = m.get('ThirdCode')
        if m.get('Share') is not None:
            self.share = m.get('Share')
        if m.get('PreAmount') is not None:
            self.pre_amount = m.get('PreAmount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RefundAmount') is not None:
            self.refund_amount = m.get('RefundAmount')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BuyerStatus') is not None:
            self.buyer_status = m.get('BuyerStatus')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('ConfiscateAmount') is not None:
            self.confiscate_amount = m.get('ConfiscateAmount')
        if m.get('OperateNote') is not None:
            self.operate_note = m.get('OperateNote')
        if m.get('PreOrderId') is not None:
            self.pre_order_id = m.get('PreOrderId')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('ExclusiveDateLimit') is not None:
            self.exclusive_date_limit = m.get('ExclusiveDateLimit')
        if m.get('AllowCancel') is not None:
            self.allow_cancel = m.get('AllowCancel')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('FinalAmount') is not None:
            self.final_amount = m.get('FinalAmount')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('PaidAmount') is not None:
            self.paid_amount = m.get('PaidAmount')
        return self


class QueryTradeProduceDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryTradeProduceDetailResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryTradeProduceDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTradeProduceDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTradeProduceDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTradeProduceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryQrCodeUploadStatusRequest(TeaModel):
    def __init__(
        self,
        oss_key: str = None,
        field_key: str = None,
        uuid: str = None,
    ):
        self.oss_key = oss_key
        self.field_key = field_key
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.field_key is not None:
            result['FieldKey'] = self.field_key
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryQrCodeUploadStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: int = None,
        request_id: str = None,
        oss_url: str = None,
        oss_key: str = None,
        success: bool = None,
    ):
        self.status = status
        self.request_id = request_id
        self.oss_url = oss_url
        self.oss_key = oss_key
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryQrCodeUploadStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryQrCodeUploadStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryQrCodeUploadStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectApplicantRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        note: str = None,
    ):
        self.instance_id = instance_id
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class RejectApplicantResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RejectApplicantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RejectApplicantResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RejectApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeIntentionUserListRequest(TeaModel):
    def __init__(
        self,
        begin: int = None,
        end: int = None,
        page_size: int = None,
        page_num: int = None,
        biz_id: str = None,
        status: int = None,
    ):
        self.begin = begin
        self.end = end
        self.page_size = page_size
        self.page_num = page_num
        self.biz_id = biz_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.end is not None:
            result['End'] = self.end
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryTradeIntentionUserListResponseBodyDataTrademark(TeaModel):
    def __init__(
        self,
        type: int = None,
        status: int = None,
        description: str = None,
        mobile: str = None,
        register_number: str = None,
        biz_id: str = None,
        classification: str = None,
        user_name: str = None,
    ):
        self.type = type
        self.status = status
        self.description = description
        self.mobile = mobile
        self.register_number = register_number
        self.biz_id = biz_id
        self.classification = classification
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.description is not None:
            result['Description'] = self.description
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.register_number is not None:
            result['RegisterNumber'] = self.register_number
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('RegisterNumber') is not None:
            self.register_number = m.get('RegisterNumber')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryTradeIntentionUserListResponseBodyData(TeaModel):
    def __init__(
        self,
        trademark: List[QueryTradeIntentionUserListResponseBodyDataTrademark] = None,
    ):
        self.trademark = trademark

    def validate(self):
        if self.trademark:
            for k in self.trademark:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Trademark'] = []
        if self.trademark is not None:
            for k in self.trademark:
                result['Trademark'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trademark = []
        if m.get('Trademark') is not None:
            for k in m.get('Trademark'):
                temp_model = QueryTradeIntentionUserListResponseBodyDataTrademark()
                self.trademark.append(temp_model.from_map(k))
        return self


class QueryTradeIntentionUserListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        total_page_num: int = None,
        request_id: str = None,
        page_size: int = None,
        total_item_num: int = None,
        data: QueryTradeIntentionUserListResponseBodyData = None,
    ):
        self.current_page_num = current_page_num
        self.total_page_num = total_page_num
        self.request_id = request_id
        self.page_size = page_size
        self.total_item_num = total_item_num
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryTradeIntentionUserListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTradeIntentionUserListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTradeIntentionUserListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTradeIntentionUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StoreMaterialTemporarilyRequest(TeaModel):
    def __init__(
        self,
        contact_zipcode: str = None,
        type: str = None,
        region: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_email: str = None,
        contact_address: str = None,
        loa_oss_key: str = None,
        name: str = None,
        card_number: str = None,
        province: str = None,
        city: str = None,
        town: str = None,
        address: str = None,
        ename: str = None,
        eaddress: str = None,
        country: str = None,
        id_card_oss_key: str = None,
        business_licence_oss_key: str = None,
        passport_oss_key: str = None,
        legal_notice_oss_key: str = None,
        principal_name: int = None,
        contact_province: str = None,
        contact_city: str = None,
        contact_district: str = None,
        contact_county: str = None,
    ):
        self.contact_zipcode = contact_zipcode
        self.type = type
        self.region = region
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_email = contact_email
        self.contact_address = contact_address
        self.loa_oss_key = loa_oss_key
        self.name = name
        self.card_number = card_number
        self.province = province
        self.city = city
        self.town = town
        self.address = address
        self.ename = ename
        self.eaddress = eaddress
        self.country = country
        self.id_card_oss_key = id_card_oss_key
        self.business_licence_oss_key = business_licence_oss_key
        self.passport_oss_key = passport_oss_key
        self.legal_notice_oss_key = legal_notice_oss_key
        self.principal_name = principal_name
        self.contact_province = contact_province
        self.contact_city = contact_city
        self.contact_district = contact_district
        self.contact_county = contact_county

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.type is not None:
            result['Type'] = self.type
        if self.region is not None:
            result['Region'] = self.region
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.town is not None:
            result['Town'] = self.town
        if self.address is not None:
            result['Address'] = self.address
        if self.ename is not None:
            result['EName'] = self.ename
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.country is not None:
            result['Country'] = self.country
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        return self


class StoreMaterialTemporarilyResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
        request_id: str = None,
    ):
        self.success = success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StoreMaterialTemporarilyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StoreMaterialTemporarilyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StoreMaterialTemporarilyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefuseAdditionalMaterialRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        note: str = None,
    ):
        self.biz_id = biz_id
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class RefuseAdditionalMaterialResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class RefuseAdditionalMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefuseAdditionalMaterialResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RefuseAdditionalMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNotaryInfosRequest(TeaModel):
    def __init__(
        self,
        notary_type: int = None,
        biz_order_no: str = None,
        token: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.notary_type = notary_type
        self.biz_order_no = biz_order_no
        self.token = token
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.biz_order_no is not None:
            result['BizOrderNo'] = self.biz_order_no
        if self.token is not None:
            result['Token'] = self.token
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('BizOrderNo') is not None:
            self.biz_order_no = m.get('BizOrderNo')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListNotaryInfosResponseBodyDataNotaryInfo(TeaModel):
    def __init__(
        self,
        token: str = None,
        tm_register_no: str = None,
        tm_classification: str = None,
        notary_failed_reason: str = None,
        gmt_modified: int = None,
        notary_status: int = None,
        biz_order_no: str = None,
    ):
        self.token = token
        self.tm_register_no = tm_register_no
        self.tm_classification = tm_classification
        self.notary_failed_reason = notary_failed_reason
        self.gmt_modified = gmt_modified
        self.notary_status = notary_status
        self.biz_order_no = biz_order_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        if self.tm_register_no is not None:
            result['TmRegisterNo'] = self.tm_register_no
        if self.tm_classification is not None:
            result['TmClassification'] = self.tm_classification
        if self.notary_failed_reason is not None:
            result['NotaryFailedReason'] = self.notary_failed_reason
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.notary_status is not None:
            result['NotaryStatus'] = self.notary_status
        if self.biz_order_no is not None:
            result['BizOrderNo'] = self.biz_order_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('TmRegisterNo') is not None:
            self.tm_register_no = m.get('TmRegisterNo')
        if m.get('TmClassification') is not None:
            self.tm_classification = m.get('TmClassification')
        if m.get('NotaryFailedReason') is not None:
            self.notary_failed_reason = m.get('NotaryFailedReason')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('NotaryStatus') is not None:
            self.notary_status = m.get('NotaryStatus')
        if m.get('BizOrderNo') is not None:
            self.biz_order_no = m.get('BizOrderNo')
        return self


class ListNotaryInfosResponseBodyData(TeaModel):
    def __init__(
        self,
        notary_info: List[ListNotaryInfosResponseBodyDataNotaryInfo] = None,
    ):
        self.notary_info = notary_info

    def validate(self):
        if self.notary_info:
            for k in self.notary_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NotaryInfo'] = []
        if self.notary_info is not None:
            for k in self.notary_info:
                result['NotaryInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.notary_info = []
        if m.get('NotaryInfo') is not None:
            for k in m.get('NotaryInfo'):
                temp_model = ListNotaryInfosResponseBodyDataNotaryInfo()
                self.notary_info.append(temp_model.from_map(k))
        return self


class ListNotaryInfosResponseBody(TeaModel):
    def __init__(
        self,
        next_page: bool = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        total_item_num: int = None,
        pre_page: bool = None,
        current_page_num: int = None,
        error_msg: str = None,
        total_page_num: int = None,
        page_size: int = None,
        data: ListNotaryInfosResponseBodyData = None,
    ):
        self.next_page = next_page
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.total_item_num = total_item_num
        self.pre_page = pre_page
        self.current_page_num = current_page_num
        self.error_msg = error_msg
        self.total_page_num = total_page_num
        self.page_size = page_size
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Data') is not None:
            temp_model = ListNotaryInfosResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListNotaryInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNotaryInfosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNotaryInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultPrincipalNameRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
    ):
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class GetDefaultPrincipalNameResponseBody(TeaModel):
    def __init__(
        self,
        principal_name: int = None,
        request_id: str = None,
    ):
        self.principal_name = principal_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDefaultPrincipalNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDefaultPrincipalNameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDefaultPrincipalNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeMarkApplicationDetailRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryTradeMarkApplicationDetailResponseBodyReceiptUrl(TeaModel):
    def __init__(
        self,
        receipt_url: List[str] = None,
    ):
        self.receipt_url = receipt_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        return self


class QueryTradeMarkApplicationDetailResponseBodyJudgeResultUrl(TeaModel):
    def __init__(
        self,
        judge_result_url: List[str] = None,
    ):
        self.judge_result_url = judge_result_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.judge_result_url is not None:
            result['JudgeResultUrl'] = self.judge_result_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JudgeResultUrl') is not None:
            self.judge_result_url = m.get('JudgeResultUrl')
        return self


class QueryTradeMarkApplicationDetailResponseBodyFlags(TeaModel):
    def __init__(
        self,
        flag: List[int] = None,
    ):
        self.flag = flag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flag is not None:
            result['Flag'] = self.flag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        return self


class QueryTradeMarkApplicationDetailResponseBodyAdminUploads(TeaModel):
    def __init__(
        self,
        loa_pic_url: str = None,
        license_pic_url: str = None,
    ):
        self.loa_pic_url = loa_pic_url
        self.license_pic_url = license_pic_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.loa_pic_url is not None:
            result['LoaPicUrl'] = self.loa_pic_url
        if self.license_pic_url is not None:
            result['LicensePicUrl'] = self.license_pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoaPicUrl') is not None:
            self.loa_pic_url = m.get('LoaPicUrl')
        if m.get('LicensePicUrl') is not None:
            self.license_pic_url = m.get('LicensePicUrl')
        return self


class QueryTradeMarkApplicationDetailResponseBodyFirstClassification(TeaModel):
    def __init__(
        self,
        name: str = None,
        code: str = None,
    ):
        self.name = name
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class QueryTradeMarkApplicationDetailResponseBodyMaterialDetailReviewAdditionalFiles(TeaModel):
    def __init__(
        self,
        review_additional_file: List[str] = None,
    ):
        self.review_additional_file = review_additional_file

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_additional_file is not None:
            result['ReviewAdditionalFile'] = self.review_additional_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewAdditionalFile') is not None:
            self.review_additional_file = m.get('ReviewAdditionalFile')
        return self


class QueryTradeMarkApplicationDetailResponseBodyMaterialDetail(TeaModel):
    def __init__(
        self,
        type: int = None,
        review_application_file: str = None,
        status: int = None,
        business_licence_url: str = None,
        passport_url: str = None,
        city: str = None,
        legal_notice_url: str = None,
        eaddress: str = None,
        contact_email: str = None,
        region: int = None,
        loa_url: str = None,
        address: str = None,
        principal_name: int = None,
        name: str = None,
        contact_number: str = None,
        contact_address: str = None,
        contact_zipcode: str = None,
        contact_name: str = None,
        ename: str = None,
        card_number: str = None,
        expiration_date: str = None,
        id_card_url: str = None,
        country: str = None,
        town: str = None,
        province: str = None,
        detailed_contact_address: str = None,
        review_additional_files: QueryTradeMarkApplicationDetailResponseBodyMaterialDetailReviewAdditionalFiles = None,
    ):
        self.type = type
        self.review_application_file = review_application_file
        self.status = status
        self.business_licence_url = business_licence_url
        self.passport_url = passport_url
        self.city = city
        self.legal_notice_url = legal_notice_url
        self.eaddress = eaddress
        self.contact_email = contact_email
        self.region = region
        self.loa_url = loa_url
        self.address = address
        self.principal_name = principal_name
        self.name = name
        self.contact_number = contact_number
        self.contact_address = contact_address
        self.contact_zipcode = contact_zipcode
        self.contact_name = contact_name
        self.ename = ename
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.id_card_url = id_card_url
        self.country = country
        self.town = town
        self.province = province
        # 详细收件地址
        self.detailed_contact_address = detailed_contact_address
        self.review_additional_files = review_additional_files

    def validate(self):
        if self.review_additional_files:
            self.review_additional_files.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.review_application_file is not None:
            result['ReviewApplicationFile'] = self.review_application_file
        if self.status is not None:
            result['Status'] = self.status
        if self.business_licence_url is not None:
            result['BusinessLicenceUrl'] = self.business_licence_url
        if self.passport_url is not None:
            result['PassportUrl'] = self.passport_url
        if self.city is not None:
            result['City'] = self.city
        if self.legal_notice_url is not None:
            result['LegalNoticeUrl'] = self.legal_notice_url
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.region is not None:
            result['Region'] = self.region
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.address is not None:
            result['Address'] = self.address
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.name is not None:
            result['Name'] = self.name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.ename is not None:
            result['EName'] = self.ename
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date
        if self.id_card_url is not None:
            result['IdCardUrl'] = self.id_card_url
        if self.country is not None:
            result['Country'] = self.country
        if self.town is not None:
            result['Town'] = self.town
        if self.province is not None:
            result['Province'] = self.province
        if self.detailed_contact_address is not None:
            result['DetailedContactAddress'] = self.detailed_contact_address
        if self.review_additional_files is not None:
            result['ReviewAdditionalFiles'] = self.review_additional_files.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ReviewApplicationFile') is not None:
            self.review_application_file = m.get('ReviewApplicationFile')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('BusinessLicenceUrl') is not None:
            self.business_licence_url = m.get('BusinessLicenceUrl')
        if m.get('PassportUrl') is not None:
            self.passport_url = m.get('PassportUrl')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('LegalNoticeUrl') is not None:
            self.legal_notice_url = m.get('LegalNoticeUrl')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')
        if m.get('IdCardUrl') is not None:
            self.id_card_url = m.get('IdCardUrl')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('DetailedContactAddress') is not None:
            self.detailed_contact_address = m.get('DetailedContactAddress')
        if m.get('ReviewAdditionalFiles') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyMaterialDetailReviewAdditionalFiles()
            self.review_additional_files = temp_model.from_map(m['ReviewAdditionalFiles'])
        return self


class QueryTradeMarkApplicationDetailResponseBodyRenewResponse(TeaModel):
    def __init__(
        self,
        eng_name: str = None,
        register_time: int = None,
        eng_address: str = None,
        address: str = None,
        name: str = None,
        submit_sbjtime: int = None,
    ):
        self.eng_name = eng_name
        self.register_time = register_time
        self.eng_address = eng_address
        self.address = address
        self.name = name
        self.submit_sbjtime = submit_sbjtime

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.address is not None:
            result['Address'] = self.address
        if self.name is not None:
            result['Name'] = self.name
        if self.submit_sbjtime is not None:
            result['SubmitSbjtime'] = self.submit_sbjtime
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SubmitSbjtime') is not None:
            self.submit_sbjtime = m.get('SubmitSbjtime')
        return self


class QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFilesReviewSupplements(TeaModel):
    def __init__(
        self,
        review_supplement: List[str] = None,
    ):
        self.review_supplement = review_supplement

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_supplement is not None:
            result['ReviewSupplement'] = self.review_supplement
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewSupplement') is not None:
            self.review_supplement = m.get('ReviewSupplement')
        return self


class QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFiles(TeaModel):
    def __init__(
        self,
        review_keep: str = None,
        review_audit: str = None,
        review_part: str = None,
        review_pass: str = None,
        review_supplements: QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFilesReviewSupplements = None,
    ):
        self.review_keep = review_keep
        self.review_audit = review_audit
        self.review_part = review_part
        self.review_pass = review_pass
        self.review_supplements = review_supplements

    def validate(self):
        if self.review_supplements:
            self.review_supplements.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.review_keep is not None:
            result['ReviewKeep'] = self.review_keep
        if self.review_audit is not None:
            result['ReviewAudit'] = self.review_audit
        if self.review_part is not None:
            result['ReviewPart'] = self.review_part
        if self.review_pass is not None:
            result['ReviewPass'] = self.review_pass
        if self.review_supplements is not None:
            result['ReviewSupplements'] = self.review_supplements.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewKeep') is not None:
            self.review_keep = m.get('ReviewKeep')
        if m.get('ReviewAudit') is not None:
            self.review_audit = m.get('ReviewAudit')
        if m.get('ReviewPart') is not None:
            self.review_part = m.get('ReviewPart')
        if m.get('ReviewPass') is not None:
            self.review_pass = m.get('ReviewPass')
        if m.get('ReviewSupplements') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFilesReviewSupplements()
            self.review_supplements = temp_model.from_map(m['ReviewSupplements'])
        return self


class QueryTradeMarkApplicationDetailResponseBodySupplementsSupplementsFileTemplateUrls(TeaModel):
    def __init__(
        self,
        file_template_urls: List[str] = None,
    ):
        self.file_template_urls = file_template_urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_template_urls is not None:
            result['FileTemplateUrls'] = self.file_template_urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileTemplateUrls') is not None:
            self.file_template_urls = m.get('FileTemplateUrls')
        return self


class QueryTradeMarkApplicationDetailResponseBodySupplementsSupplements(TeaModel):
    def __init__(
        self,
        type: int = None,
        operate_time: int = None,
        serial_number: str = None,
        status: int = None,
        sbj_dead_time: int = None,
        accept_dead_time: int = None,
        send_time: int = None,
        batch_num: str = None,
        accept_time: int = None,
        tm_number: str = None,
        upload_file_template_url: str = None,
        content: str = None,
        id: int = None,
        order_id: str = None,
        file_template_urls: QueryTradeMarkApplicationDetailResponseBodySupplementsSupplementsFileTemplateUrls = None,
    ):
        self.type = type
        self.operate_time = operate_time
        self.serial_number = serial_number
        self.status = status
        self.sbj_dead_time = sbj_dead_time
        self.accept_dead_time = accept_dead_time
        self.send_time = send_time
        self.batch_num = batch_num
        self.accept_time = accept_time
        self.tm_number = tm_number
        self.upload_file_template_url = upload_file_template_url
        self.content = content
        self.id = id
        self.order_id = order_id
        self.file_template_urls = file_template_urls

    def validate(self):
        if self.file_template_urls:
            self.file_template_urls.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        if self.sbj_dead_time is not None:
            result['SbjDeadTime'] = self.sbj_dead_time
        if self.accept_dead_time is not None:
            result['AcceptDeadTime'] = self.accept_dead_time
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.batch_num is not None:
            result['BatchNum'] = self.batch_num
        if self.accept_time is not None:
            result['AcceptTime'] = self.accept_time
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.upload_file_template_url is not None:
            result['UploadFileTemplateUrl'] = self.upload_file_template_url
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.file_template_urls is not None:
            result['FileTemplateUrls'] = self.file_template_urls.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SbjDeadTime') is not None:
            self.sbj_dead_time = m.get('SbjDeadTime')
        if m.get('AcceptDeadTime') is not None:
            self.accept_dead_time = m.get('AcceptDeadTime')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('BatchNum') is not None:
            self.batch_num = m.get('BatchNum')
        if m.get('AcceptTime') is not None:
            self.accept_time = m.get('AcceptTime')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('UploadFileTemplateUrl') is not None:
            self.upload_file_template_url = m.get('UploadFileTemplateUrl')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('FileTemplateUrls') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodySupplementsSupplementsFileTemplateUrls()
            self.file_template_urls = temp_model.from_map(m['FileTemplateUrls'])
        return self


class QueryTradeMarkApplicationDetailResponseBodySupplements(TeaModel):
    def __init__(
        self,
        supplements: List[QueryTradeMarkApplicationDetailResponseBodySupplementsSupplements] = None,
    ):
        self.supplements = supplements

    def validate(self):
        if self.supplements:
            for k in self.supplements:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Supplements'] = []
        if self.supplements is not None:
            for k in self.supplements:
                result['Supplements'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supplements = []
        if m.get('Supplements') is not None:
            for k in m.get('Supplements'):
                temp_model = QueryTradeMarkApplicationDetailResponseBodySupplementsSupplements()
                self.supplements.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationDetailResponseBodyThirdClassificationThirdClassifications(TeaModel):
    def __init__(
        self,
        name: str = None,
        code: str = None,
    ):
        self.name = name
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class QueryTradeMarkApplicationDetailResponseBodyThirdClassification(TeaModel):
    def __init__(
        self,
        third_classifications: List[QueryTradeMarkApplicationDetailResponseBodyThirdClassificationThirdClassifications] = None,
    ):
        self.third_classifications = third_classifications

    def validate(self):
        if self.third_classifications:
            for k in self.third_classifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThirdClassifications'] = []
        if self.third_classifications is not None:
            for k in self.third_classifications:
                result['ThirdClassifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.third_classifications = []
        if m.get('ThirdClassifications') is not None:
            for k in m.get('ThirdClassifications'):
                temp_model = QueryTradeMarkApplicationDetailResponseBodyThirdClassificationThirdClassifications()
                self.third_classifications.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationDetailResponseBody(TeaModel):
    def __init__(
        self,
        type: int = None,
        status: int = None,
        accept_url: str = None,
        order_price: float = None,
        submit_audit_time: int = None,
        update_time: int = None,
        create_time: int = None,
        not_accept_url: str = None,
        send_time: str = None,
        service_price: float = None,
        partner_mobile: str = None,
        recv_user_logistics: str = None,
        request_id: str = None,
        gray_icon_url: str = None,
        material_id: int = None,
        send_sbj_logistics: str = None,
        send_user_logistics: str = None,
        loa_url: str = None,
        tm_number: str = None,
        note: str = None,
        principal_name: int = None,
        partner_name: str = None,
        logistics_certificate_url: str = None,
        biz_id: str = None,
        partner_code: str = None,
        tm_name_type: int = None,
        extend_info: Dict[str, Any] = None,
        tm_icon: str = None,
        tm_name: str = None,
        logistics_no: str = None,
        total_price: float = None,
        submit_time: int = None,
        order_id: str = None,
        receipt_url: QueryTradeMarkApplicationDetailResponseBodyReceiptUrl = None,
        judge_result_url: QueryTradeMarkApplicationDetailResponseBodyJudgeResultUrl = None,
        flags: QueryTradeMarkApplicationDetailResponseBodyFlags = None,
        admin_uploads: QueryTradeMarkApplicationDetailResponseBodyAdminUploads = None,
        first_classification: QueryTradeMarkApplicationDetailResponseBodyFirstClassification = None,
        material_detail: QueryTradeMarkApplicationDetailResponseBodyMaterialDetail = None,
        renew_response: QueryTradeMarkApplicationDetailResponseBodyRenewResponse = None,
        review_official_files: QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFiles = None,
        supplements: QueryTradeMarkApplicationDetailResponseBodySupplements = None,
        third_classification: QueryTradeMarkApplicationDetailResponseBodyThirdClassification = None,
    ):
        self.type = type
        self.status = status
        self.accept_url = accept_url
        self.order_price = order_price
        self.submit_audit_time = submit_audit_time
        self.update_time = update_time
        self.create_time = create_time
        self.not_accept_url = not_accept_url
        self.send_time = send_time
        self.service_price = service_price
        self.partner_mobile = partner_mobile
        self.recv_user_logistics = recv_user_logistics
        self.request_id = request_id
        self.gray_icon_url = gray_icon_url
        self.material_id = material_id
        self.send_sbj_logistics = send_sbj_logistics
        self.send_user_logistics = send_user_logistics
        self.loa_url = loa_url
        self.tm_number = tm_number
        self.note = note
        self.principal_name = principal_name
        self.partner_name = partner_name
        self.logistics_certificate_url = logistics_certificate_url
        self.biz_id = biz_id
        self.partner_code = partner_code
        self.tm_name_type = tm_name_type
        self.extend_info = extend_info
        self.tm_icon = tm_icon
        self.tm_name = tm_name
        self.logistics_no = logistics_no
        self.total_price = total_price
        self.submit_time = submit_time
        self.order_id = order_id
        self.receipt_url = receipt_url
        self.judge_result_url = judge_result_url
        self.flags = flags
        self.admin_uploads = admin_uploads
        self.first_classification = first_classification
        self.material_detail = material_detail
        self.renew_response = renew_response
        self.review_official_files = review_official_files
        self.supplements = supplements
        self.third_classification = third_classification

    def validate(self):
        if self.receipt_url:
            self.receipt_url.validate()
        if self.judge_result_url:
            self.judge_result_url.validate()
        if self.flags:
            self.flags.validate()
        if self.admin_uploads:
            self.admin_uploads.validate()
        if self.first_classification:
            self.first_classification.validate()
        if self.material_detail:
            self.material_detail.validate()
        if self.renew_response:
            self.renew_response.validate()
        if self.review_official_files:
            self.review_official_files.validate()
        if self.supplements:
            self.supplements.validate()
        if self.third_classification:
            self.third_classification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.accept_url is not None:
            result['AcceptUrl'] = self.accept_url
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.submit_audit_time is not None:
            result['SubmitAuditTime'] = self.submit_audit_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.not_accept_url is not None:
            result['NotAcceptUrl'] = self.not_accept_url
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.service_price is not None:
            result['ServicePrice'] = self.service_price
        if self.partner_mobile is not None:
            result['PartnerMobile'] = self.partner_mobile
        if self.recv_user_logistics is not None:
            result['RecvUserLogistics'] = self.recv_user_logistics
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.gray_icon_url is not None:
            result['GrayIconUrl'] = self.gray_icon_url
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.send_sbj_logistics is not None:
            result['SendSbjLogistics'] = self.send_sbj_logistics
        if self.send_user_logistics is not None:
            result['SendUserLogistics'] = self.send_user_logistics
        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.note is not None:
            result['Note'] = self.note
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.partner_name is not None:
            result['PartnerName'] = self.partner_name
        if self.logistics_certificate_url is not None:
            result['LogisticsCertificateUrl'] = self.logistics_certificate_url
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code
        if self.tm_name_type is not None:
            result['TmNameType'] = self.tm_name_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url.to_map()
        if self.judge_result_url is not None:
            result['JudgeResultUrl'] = self.judge_result_url.to_map()
        if self.flags is not None:
            result['Flags'] = self.flags.to_map()
        if self.admin_uploads is not None:
            result['AdminUploads'] = self.admin_uploads.to_map()
        if self.first_classification is not None:
            result['FirstClassification'] = self.first_classification.to_map()
        if self.material_detail is not None:
            result['MaterialDetail'] = self.material_detail.to_map()
        if self.renew_response is not None:
            result['RenewResponse'] = self.renew_response.to_map()
        if self.review_official_files is not None:
            result['ReviewOfficialFiles'] = self.review_official_files.to_map()
        if self.supplements is not None:
            result['Supplements'] = self.supplements.to_map()
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AcceptUrl') is not None:
            self.accept_url = m.get('AcceptUrl')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('SubmitAuditTime') is not None:
            self.submit_audit_time = m.get('SubmitAuditTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NotAcceptUrl') is not None:
            self.not_accept_url = m.get('NotAcceptUrl')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('ServicePrice') is not None:
            self.service_price = m.get('ServicePrice')
        if m.get('PartnerMobile') is not None:
            self.partner_mobile = m.get('PartnerMobile')
        if m.get('RecvUserLogistics') is not None:
            self.recv_user_logistics = m.get('RecvUserLogistics')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GrayIconUrl') is not None:
            self.gray_icon_url = m.get('GrayIconUrl')
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('SendSbjLogistics') is not None:
            self.send_sbj_logistics = m.get('SendSbjLogistics')
        if m.get('SendUserLogistics') is not None:
            self.send_user_logistics = m.get('SendUserLogistics')
        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PartnerName') is not None:
            self.partner_name = m.get('PartnerName')
        if m.get('LogisticsCertificateUrl') is not None:
            self.logistics_certificate_url = m.get('LogisticsCertificateUrl')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')
        if m.get('TmNameType') is not None:
            self.tm_name_type = m.get('TmNameType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ReceiptUrl') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyReceiptUrl()
            self.receipt_url = temp_model.from_map(m['ReceiptUrl'])
        if m.get('JudgeResultUrl') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyJudgeResultUrl()
            self.judge_result_url = temp_model.from_map(m['JudgeResultUrl'])
        if m.get('Flags') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyFlags()
            self.flags = temp_model.from_map(m['Flags'])
        if m.get('AdminUploads') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyAdminUploads()
            self.admin_uploads = temp_model.from_map(m['AdminUploads'])
        if m.get('FirstClassification') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyFirstClassification()
            self.first_classification = temp_model.from_map(m['FirstClassification'])
        if m.get('MaterialDetail') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyMaterialDetail()
            self.material_detail = temp_model.from_map(m['MaterialDetail'])
        if m.get('RenewResponse') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyRenewResponse()
            self.renew_response = temp_model.from_map(m['RenewResponse'])
        if m.get('ReviewOfficialFiles') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyReviewOfficialFiles()
            self.review_official_files = temp_model.from_map(m['ReviewOfficialFiles'])
        if m.get('Supplements') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodySupplements()
            self.supplements = temp_model.from_map(m['Supplements'])
        if m.get('ThirdClassification') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBodyThirdClassification()
            self.third_classification = temp_model.from_map(m['ThirdClassification'])
        return self


class QueryTradeMarkApplicationDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTradeMarkApplicationDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTradeMarkApplicationDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveClassificationConditionsRequest(TeaModel):
    def __init__(
        self,
        type: int = None,
        biz_id: str = None,
        condition: str = None,
    ):
        self.type = type
        self.biz_id = biz_id
        self.condition = condition

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.condition is not None:
            result['Condition'] = self.condition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')
        return self


class SaveClassificationConditionsResponseBodyInvalidList(TeaModel):
    def __init__(
        self,
        parent_code: str = None,
        official_code: str = None,
        classification_name: str = None,
        classification_code: str = None,
    ):
        self.parent_code = parent_code
        self.official_code = official_code
        self.classification_name = classification_name
        self.classification_code = classification_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_code is not None:
            result['ParentCode'] = self.parent_code
        if self.official_code is not None:
            result['OfficialCode'] = self.official_code
        if self.classification_name is not None:
            result['ClassificationName'] = self.classification_name
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentCode') is not None:
            self.parent_code = m.get('ParentCode')
        if m.get('OfficialCode') is not None:
            self.official_code = m.get('OfficialCode')
        if m.get('ClassificationName') is not None:
            self.classification_name = m.get('ClassificationName')
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        return self


class SaveClassificationConditionsResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        tag_name: str = None,
        success: bool = None,
        invalid_list: List[SaveClassificationConditionsResponseBodyInvalidList] = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.tag_name = tag_name
        self.success = success
        self.invalid_list = invalid_list

    def validate(self):
        if self.invalid_list:
            for k in self.invalid_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.success is not None:
            result['Success'] = self.success
        result['InvalidList'] = []
        if self.invalid_list is not None:
            for k in self.invalid_list:
                result['InvalidList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.invalid_list = []
        if m.get('InvalidList') is not None:
            for k in m.get('InvalidList'):
                temp_model = SaveClassificationConditionsResponseBodyInvalidList()
                self.invalid_list.append(temp_model.from_map(k))
        return self


class SaveClassificationConditionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveClassificationConditionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveClassificationConditionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FillLogisticsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        logistics: str = None,
    ):
        self.biz_id = biz_id
        self.logistics = logistics

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.logistics is not None:
            result['Logistics'] = self.logistics
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Logistics') is not None:
            self.logistics = m.get('Logistics')
        return self


class FillLogisticsResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class FillLogisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FillLogisticsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FillLogisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMaterialRequest(TeaModel):
    def __init__(
        self,
        loa_id: int = None,
        contact_address: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_email: str = None,
        id: int = None,
        contact_zipcode: str = None,
        name: str = None,
        card_number: str = None,
        province: str = None,
        city: str = None,
        town: str = None,
        address: str = None,
        ename: str = None,
        eaddress: str = None,
        id_card_oss_key: str = None,
        business_licence_oss_key: str = None,
        passport_oss_key: str = None,
        loa_oss_key: str = None,
        legal_notice_oss_key: str = None,
        contact_province: str = None,
        contact_city: str = None,
        contact_district: str = None,
        contact_county: str = None,
    ):
        self.loa_id = loa_id
        self.contact_address = contact_address
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_email = contact_email
        self.id = id
        self.contact_zipcode = contact_zipcode
        self.name = name
        self.card_number = card_number
        self.province = province
        self.city = city
        self.town = town
        self.address = address
        self.ename = ename
        self.eaddress = eaddress
        self.id_card_oss_key = id_card_oss_key
        self.business_licence_oss_key = business_licence_oss_key
        self.passport_oss_key = passport_oss_key
        self.loa_oss_key = loa_oss_key
        self.legal_notice_oss_key = legal_notice_oss_key
        self.contact_province = contact_province
        self.contact_city = contact_city
        self.contact_district = contact_district
        self.contact_county = contact_county

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.loa_id is not None:
            result['LoaId'] = self.loa_id
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.id is not None:
            result['Id'] = self.id
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.name is not None:
            result['Name'] = self.name
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.town is not None:
            result['Town'] = self.town
        if self.address is not None:
            result['Address'] = self.address
        if self.ename is not None:
            result['EName'] = self.ename
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoaId') is not None:
            self.loa_id = m.get('LoaId')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        return self


class UpdateMaterialResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
        request_id: str = None,
    ):
        self.success = success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateMaterialResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTradeMarkApplicationLogsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryTradeMarkApplicationLogsResponseBodyDataData(TeaModel):
    def __init__(
        self,
        operate_time: int = None,
        operate_type: int = None,
        extend_content: str = None,
        biz_id: str = None,
        note: str = None,
        biz_status: int = None,
    ):
        self.operate_time = operate_time
        self.operate_type = operate_type
        self.extend_content = extend_content
        self.biz_id = biz_id
        self.note = note
        self.biz_status = biz_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.extend_content is not None:
            result['ExtendContent'] = self.extend_content
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('ExtendContent') is not None:
            self.extend_content = m.get('ExtendContent')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        return self


class QueryTradeMarkApplicationLogsResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[QueryTradeMarkApplicationLogsResponseBodyDataData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTradeMarkApplicationLogsResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryTradeMarkApplicationLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryTradeMarkApplicationLogsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryTradeMarkApplicationLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTradeMarkApplicationLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTradeMarkApplicationLogsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTradeMarkApplicationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundProduceRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class RefundProduceResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class RefundProduceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefundProduceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RefundProduceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncTrademarkRequest(TeaModel):
    def __init__(
        self,
        classification_code: str = None,
        tm_name: str = None,
        tm_icon: str = None,
        original_price: float = None,
        tm_number: str = None,
        status: str = None,
        end_time: int = None,
        begin_time: int = None,
        description: str = None,
        label: str = None,
        reg_ann_date: int = None,
        owner_name: str = None,
        owner_en_name: str = None,
        secondary_classification: str = None,
        third_classification: str = None,
        type: str = None,
        reason: str = None,
    ):
        self.classification_code = classification_code
        self.tm_name = tm_name
        self.tm_icon = tm_icon
        self.original_price = original_price
        self.tm_number = tm_number
        self.status = status
        self.end_time = end_time
        self.begin_time = begin_time
        self.description = description
        self.label = label
        self.reg_ann_date = reg_ann_date
        self.owner_name = owner_name
        self.owner_en_name = owner_en_name
        self.secondary_classification = secondary_classification
        self.third_classification = third_classification
        self.type = type
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification_code is not None:
            result['ClassificationCode'] = self.classification_code
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.tm_number is not None:
            result['TmNumber'] = self.tm_number
        if self.status is not None:
            result['Status'] = self.status
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.reg_ann_date is not None:
            result['RegAnnDate'] = self.reg_ann_date
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_en_name is not None:
            result['OwnerEnName'] = self.owner_en_name
        if self.secondary_classification is not None:
            result['SecondaryClassification'] = self.secondary_classification
        if self.third_classification is not None:
            result['ThirdClassification'] = self.third_classification
        if self.type is not None:
            result['Type'] = self.type
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassificationCode') is not None:
            self.classification_code = m.get('ClassificationCode')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TmNumber') is not None:
            self.tm_number = m.get('TmNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('RegAnnDate') is not None:
            self.reg_ann_date = m.get('RegAnnDate')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerEnName') is not None:
            self.owner_en_name = m.get('OwnerEnName')
        if m.get('SecondaryClassification') is not None:
            self.secondary_classification = m.get('SecondaryClassification')
        if m.get('ThirdClassification') is not None:
            self.third_classification = m.get('ThirdClassification')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class SyncTrademarkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SyncTrademarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SyncTrademarkResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SyncTrademarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CombineLoaRequest(TeaModel):
    def __init__(
        self,
        material_id: str = None,
        trademark_name: str = None,
        material_name: str = None,
        nationality: str = None,
        address: str = None,
        tm_produce_type: str = None,
        principal_name: int = None,
    ):
        self.material_id = material_id
        self.trademark_name = trademark_name
        self.material_name = material_name
        self.nationality = nationality
        self.address = address
        self.tm_produce_type = tm_produce_type
        self.principal_name = principal_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_id is not None:
            result['MaterialId'] = self.material_id
        if self.trademark_name is not None:
            result['TrademarkName'] = self.trademark_name
        if self.material_name is not None:
            result['MaterialName'] = self.material_name
        if self.nationality is not None:
            result['Nationality'] = self.nationality
        if self.address is not None:
            result['Address'] = self.address
        if self.tm_produce_type is not None:
            result['TmProduceType'] = self.tm_produce_type
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')
        if m.get('TrademarkName') is not None:
            self.trademark_name = m.get('TrademarkName')
        if m.get('MaterialName') is not None:
            self.material_name = m.get('MaterialName')
        if m.get('Nationality') is not None:
            self.nationality = m.get('Nationality')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('TmProduceType') is not None:
            self.tm_produce_type = m.get('TmProduceType')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        return self


class CombineLoaResponseBody(TeaModel):
    def __init__(
        self,
        template_combine_url: str = None,
        request_id: str = None,
    ):
        self.template_combine_url = template_combine_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_combine_url is not None:
            result['TemplateCombineUrl'] = self.template_combine_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCombineUrl') is not None:
            self.template_combine_url = m.get('TemplateCombineUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CombineLoaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CombineLoaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CombineLoaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FilterUnavailableCodesRequest(TeaModel):
    def __init__(
        self,
        codes: Dict[str, Any] = None,
    ):
        self.codes = codes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codes is not None:
            result['Codes'] = self.codes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes = m.get('Codes')
        return self


class FilterUnavailableCodesShrinkRequest(TeaModel):
    def __init__(
        self,
        codes_shrink: str = None,
    ):
        self.codes_shrink = codes_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codes_shrink is not None:
            result['Codes'] = self.codes_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes_shrink = m.get('Codes')
        return self


class FilterUnavailableCodesResponseBodyData(TeaModel):
    def __init__(
        self,
        codes: List[str] = None,
    ):
        self.codes = codes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codes is not None:
            result['Codes'] = self.codes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes = m.get('Codes')
        return self


class FilterUnavailableCodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: FilterUnavailableCodesResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = FilterUnavailableCodesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class FilterUnavailableCodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FilterUnavailableCodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FilterUnavailableCodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertMaterialRequest(TeaModel):
    def __init__(
        self,
        contact_zipcode: str = None,
        type: int = None,
        region: int = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_email: str = None,
        contact_address: str = None,
        loa_oss_key: str = None,
        name: str = None,
        card_number: str = None,
        province: str = None,
        city: str = None,
        town: str = None,
        address: str = None,
        ename: str = None,
        eaddress: str = None,
        country: str = None,
        id_card_oss_key: str = None,
        business_licence_oss_key: str = None,
        passport_oss_key: str = None,
        legal_notice_oss_key: str = None,
        principal_name: int = None,
        contact_province: str = None,
        contact_city: str = None,
        contact_district: str = None,
        contact_county: str = None,
    ):
        self.contact_zipcode = contact_zipcode
        self.type = type
        self.region = region
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_email = contact_email
        self.contact_address = contact_address
        self.loa_oss_key = loa_oss_key
        self.name = name
        self.card_number = card_number
        self.province = province
        self.city = city
        self.town = town
        self.address = address
        self.ename = ename
        self.eaddress = eaddress
        self.country = country
        self.id_card_oss_key = id_card_oss_key
        self.business_licence_oss_key = business_licence_oss_key
        self.passport_oss_key = passport_oss_key
        self.legal_notice_oss_key = legal_notice_oss_key
        self.principal_name = principal_name
        self.contact_province = contact_province
        self.contact_city = contact_city
        self.contact_district = contact_district
        self.contact_county = contact_county

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_zipcode is not None:
            result['ContactZipcode'] = self.contact_zipcode
        if self.type is not None:
            result['Type'] = self.type
        if self.region is not None:
            result['Region'] = self.region
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.town is not None:
            result['Town'] = self.town
        if self.address is not None:
            result['Address'] = self.address
        if self.ename is not None:
            result['EName'] = self.ename
        if self.eaddress is not None:
            result['EAddress'] = self.eaddress
        if self.country is not None:
            result['Country'] = self.country
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.contact_province is not None:
            result['ContactProvince'] = self.contact_province
        if self.contact_city is not None:
            result['ContactCity'] = self.contact_city
        if self.contact_district is not None:
            result['ContactDistrict'] = self.contact_district
        if self.contact_county is not None:
            result['ContactCounty'] = self.contact_county
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactZipcode') is not None:
            self.contact_zipcode = m.get('ContactZipcode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EName') is not None:
            self.ename = m.get('EName')
        if m.get('EAddress') is not None:
            self.eaddress = m.get('EAddress')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('ContactProvince') is not None:
            self.contact_province = m.get('ContactProvince')
        if m.get('ContactCity') is not None:
            self.contact_city = m.get('ContactCity')
        if m.get('ContactDistrict') is not None:
            self.contact_district = m.get('ContactDistrict')
        if m.get('ContactCounty') is not None:
            self.contact_county = m.get('ContactCounty')
        return self


class InsertMaterialResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
        request_id: str = None,
    ):
        self.success = success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InsertMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InsertMaterialResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InsertMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTradeMarkReviewMaterialDetailRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        type: int = None,
        region: int = None,
        country: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_email: str = None,
        contact_address: str = None,
        loa_oss_key: str = None,
        name: str = None,
        card_number: str = None,
        province: str = None,
        address: str = None,
        eng_name: str = None,
        eng_address: str = None,
        id_card_oss_key: str = None,
        business_licence_oss_key: str = None,
        passport_oss_key: str = None,
        legal_notice_oss_key: str = None,
        application_oss_key: str = None,
        additional_oss_key_list: Dict[str, Any] = None,
        submit_type: int = None,
    ):
        self.biz_id = biz_id
        self.type = type
        self.region = region
        self.country = country
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_email = contact_email
        self.contact_address = contact_address
        self.loa_oss_key = loa_oss_key
        self.name = name
        self.card_number = card_number
        self.province = province
        self.address = address
        self.eng_name = eng_name
        self.eng_address = eng_address
        self.id_card_oss_key = id_card_oss_key
        self.business_licence_oss_key = business_licence_oss_key
        self.passport_oss_key = passport_oss_key
        self.legal_notice_oss_key = legal_notice_oss_key
        self.application_oss_key = application_oss_key
        self.additional_oss_key_list = additional_oss_key_list
        self.submit_type = submit_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.type is not None:
            result['Type'] = self.type
        if self.region is not None:
            result['Region'] = self.region
        if self.country is not None:
            result['Country'] = self.country
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.province is not None:
            result['Province'] = self.province
        if self.address is not None:
            result['Address'] = self.address
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.application_oss_key is not None:
            result['ApplicationOssKey'] = self.application_oss_key
        if self.additional_oss_key_list is not None:
            result['AdditionalOssKeyList'] = self.additional_oss_key_list
        if self.submit_type is not None:
            result['SubmitType'] = self.submit_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('ApplicationOssKey') is not None:
            self.application_oss_key = m.get('ApplicationOssKey')
        if m.get('AdditionalOssKeyList') is not None:
            self.additional_oss_key_list = m.get('AdditionalOssKeyList')
        if m.get('SubmitType') is not None:
            self.submit_type = m.get('SubmitType')
        return self


class SaveTradeMarkReviewMaterialDetailShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        type: int = None,
        region: int = None,
        country: str = None,
        contact_name: str = None,
        contact_number: str = None,
        contact_email: str = None,
        contact_address: str = None,
        loa_oss_key: str = None,
        name: str = None,
        card_number: str = None,
        province: str = None,
        address: str = None,
        eng_name: str = None,
        eng_address: str = None,
        id_card_oss_key: str = None,
        business_licence_oss_key: str = None,
        passport_oss_key: str = None,
        legal_notice_oss_key: str = None,
        application_oss_key: str = None,
        additional_oss_key_list_shrink: str = None,
        submit_type: int = None,
    ):
        self.biz_id = biz_id
        self.type = type
        self.region = region
        self.country = country
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.contact_email = contact_email
        self.contact_address = contact_address
        self.loa_oss_key = loa_oss_key
        self.name = name
        self.card_number = card_number
        self.province = province
        self.address = address
        self.eng_name = eng_name
        self.eng_address = eng_address
        self.id_card_oss_key = id_card_oss_key
        self.business_licence_oss_key = business_licence_oss_key
        self.passport_oss_key = passport_oss_key
        self.legal_notice_oss_key = legal_notice_oss_key
        self.application_oss_key = application_oss_key
        self.additional_oss_key_list_shrink = additional_oss_key_list_shrink
        self.submit_type = submit_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.type is not None:
            result['Type'] = self.type
        if self.region is not None:
            result['Region'] = self.region
        if self.country is not None:
            result['Country'] = self.country
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_number is not None:
            result['ContactNumber'] = self.contact_number
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_address is not None:
            result['ContactAddress'] = self.contact_address
        if self.loa_oss_key is not None:
            result['LoaOssKey'] = self.loa_oss_key
        if self.name is not None:
            result['Name'] = self.name
        if self.card_number is not None:
            result['CardNumber'] = self.card_number
        if self.province is not None:
            result['Province'] = self.province
        if self.address is not None:
            result['Address'] = self.address
        if self.eng_name is not None:
            result['EngName'] = self.eng_name
        if self.eng_address is not None:
            result['EngAddress'] = self.eng_address
        if self.id_card_oss_key is not None:
            result['IdCardOssKey'] = self.id_card_oss_key
        if self.business_licence_oss_key is not None:
            result['BusinessLicenceOssKey'] = self.business_licence_oss_key
        if self.passport_oss_key is not None:
            result['PassportOssKey'] = self.passport_oss_key
        if self.legal_notice_oss_key is not None:
            result['LegalNoticeOssKey'] = self.legal_notice_oss_key
        if self.application_oss_key is not None:
            result['ApplicationOssKey'] = self.application_oss_key
        if self.additional_oss_key_list_shrink is not None:
            result['AdditionalOssKeyList'] = self.additional_oss_key_list_shrink
        if self.submit_type is not None:
            result['SubmitType'] = self.submit_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactNumber') is not None:
            self.contact_number = m.get('ContactNumber')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactAddress') is not None:
            self.contact_address = m.get('ContactAddress')
        if m.get('LoaOssKey') is not None:
            self.loa_oss_key = m.get('LoaOssKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CardNumber') is not None:
            self.card_number = m.get('CardNumber')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EngName') is not None:
            self.eng_name = m.get('EngName')
        if m.get('EngAddress') is not None:
            self.eng_address = m.get('EngAddress')
        if m.get('IdCardOssKey') is not None:
            self.id_card_oss_key = m.get('IdCardOssKey')
        if m.get('BusinessLicenceOssKey') is not None:
            self.business_licence_oss_key = m.get('BusinessLicenceOssKey')
        if m.get('PassportOssKey') is not None:
            self.passport_oss_key = m.get('PassportOssKey')
        if m.get('LegalNoticeOssKey') is not None:
            self.legal_notice_oss_key = m.get('LegalNoticeOssKey')
        if m.get('ApplicationOssKey') is not None:
            self.application_oss_key = m.get('ApplicationOssKey')
        if m.get('AdditionalOssKeyList') is not None:
            self.additional_oss_key_list_shrink = m.get('AdditionalOssKeyList')
        if m.get('SubmitType') is not None:
            self.submit_type = m.get('SubmitType')
        return self


class SaveTradeMarkReviewMaterialDetailResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveTradeMarkReviewMaterialDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveTradeMarkReviewMaterialDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveTradeMarkReviewMaterialDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonitorKeywordsRequest(TeaModel):
    def __init__(
        self,
        rule_type: int = None,
        keywords: List[str] = None,
    ):
        self.rule_type = rule_type
        self.keywords = keywords

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        return self


class QueryMonitorKeywordsResponseBodyData(TeaModel):
    def __init__(
        self,
        keywords: List[str] = None,
    ):
        self.keywords = keywords

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        return self


class QueryMonitorKeywordsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryMonitorKeywordsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryMonitorKeywordsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryMonitorKeywordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMonitorKeywordsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryMonitorKeywordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskListRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        page_size: int = None,
        page_num: int = None,
    ):
        self.biz_type = biz_type
        self.page_size = page_size
        self.page_num = page_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class QueryTaskListResponseBodyDataTaskList(TeaModel):
    def __init__(
        self,
        task_type: str = None,
        result: str = None,
        task_status: str = None,
        complete_time: int = None,
        create_time: int = None,
        err_msg: str = None,
        file_name: str = None,
    ):
        self.task_type = task_type
        self.result = result
        self.task_status = task_status
        self.complete_time = complete_time
        self.create_time = create_time
        self.err_msg = err_msg
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.result is not None:
            result['Result'] = self.result
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class QueryTaskListResponseBodyData(TeaModel):
    def __init__(
        self,
        task_list: List[QueryTaskListResponseBodyDataTaskList] = None,
    ):
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = QueryTaskListResponseBodyDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class QueryTaskListResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        total_page_num: int = None,
        request_id: str = None,
        page_size: int = None,
        total_item_num: int = None,
        data: QueryTaskListResponseBodyData = None,
    ):
        self.current_page_num = current_page_num
        self.total_page_num = total_page_num
        self.request_id = request_id
        self.page_size = page_size
        self.total_item_num = total_item_num
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('Data') is not None:
            temp_model = QueryTaskListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryTaskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTaskListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrademarkNameRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        biz_id: str = None,
        tm_name: str = None,
        tm_icon: str = None,
        tm_comment: str = None,
        type: int = None,
    ):
        # 幂等参数
        self.client_token = client_token
        # 业务id
        self.biz_id = biz_id
        # 商标名称
        self.tm_name = tm_name
        # 商标图片
        self.tm_icon = tm_icon
        self.tm_comment = tm_comment
        # 商标类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_icon is not None:
            result['TmIcon'] = self.tm_icon
        if self.tm_comment is not None:
            result['TmComment'] = self.tm_comment
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmIcon') is not None:
            self.tm_icon = m.get('TmIcon')
        if m.get('TmComment') is not None:
            self.tm_comment = m.get('TmComment')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateTrademarkNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_msg: str = None,
        success: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.error_code = error_code
        self.error_msg = error_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTrademarkNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateTrademarkNameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateTrademarkNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckLoaFillRequest(TeaModel):
    def __init__(
        self,
        oss_key: str = None,
        type: str = None,
    ):
        self.oss_key = oss_key
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CheckLoaFillResponseBodyDataErrorMsgs(TeaModel):
    def __init__(
        self,
        error_msg: List[str] = None,
    ):
        self.error_msg = error_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        return self


class CheckLoaFillResponseBodyData(TeaModel):
    def __init__(
        self,
        address_fill: bool = None,
        template_url: str = None,
        country_fill: bool = None,
        nationality_fill: bool = None,
        stamp_fill: bool = None,
        trade_mark_name_fill: bool = None,
        material_name_fill: bool = None,
        error_msgs: CheckLoaFillResponseBodyDataErrorMsgs = None,
    ):
        self.address_fill = address_fill
        self.template_url = template_url
        self.country_fill = country_fill
        self.nationality_fill = nationality_fill
        self.stamp_fill = stamp_fill
        self.trade_mark_name_fill = trade_mark_name_fill
        self.material_name_fill = material_name_fill
        self.error_msgs = error_msgs

    def validate(self):
        if self.error_msgs:
            self.error_msgs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_fill is not None:
            result['AddressFill'] = self.address_fill
        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url
        if self.country_fill is not None:
            result['CountryFill'] = self.country_fill
        if self.nationality_fill is not None:
            result['NationalityFill'] = self.nationality_fill
        if self.stamp_fill is not None:
            result['StampFill'] = self.stamp_fill
        if self.trade_mark_name_fill is not None:
            result['TradeMarkNameFill'] = self.trade_mark_name_fill
        if self.material_name_fill is not None:
            result['MaterialNameFill'] = self.material_name_fill
        if self.error_msgs is not None:
            result['ErrorMsgs'] = self.error_msgs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressFill') is not None:
            self.address_fill = m.get('AddressFill')
        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')
        if m.get('CountryFill') is not None:
            self.country_fill = m.get('CountryFill')
        if m.get('NationalityFill') is not None:
            self.nationality_fill = m.get('NationalityFill')
        if m.get('StampFill') is not None:
            self.stamp_fill = m.get('StampFill')
        if m.get('TradeMarkNameFill') is not None:
            self.trade_mark_name_fill = m.get('TradeMarkNameFill')
        if m.get('MaterialNameFill') is not None:
            self.material_name_fill = m.get('MaterialNameFill')
        if m.get('ErrorMsgs') is not None:
            temp_model = CheckLoaFillResponseBodyDataErrorMsgs()
            self.error_msgs = temp_model.from_map(m['ErrorMsgs'])
        return self


class CheckLoaFillResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: CheckLoaFillResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CheckLoaFillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CheckLoaFillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckLoaFillResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckLoaFillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmApplicantRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        note: str = None,
    ):
        self.biz_id = biz_id
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class ConfirmApplicantResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class ConfirmApplicantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfirmApplicantResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfirmApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntentionOrderRequest(TeaModel):
    def __init__(
        self,
        intention_biz_id: str = None,
        channel: str = None,
    ):
        self.intention_biz_id = intention_biz_id
        self.channel = channel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.channel is not None:
            result['Channel'] = self.channel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        return self


class CreateIntentionOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        order_ids: List[str] = None,
    ):
        self.order_ids = order_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class CreateIntentionOrderResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        data: CreateIntentionOrderResponseBodyData = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = CreateIntentionOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CreateIntentionOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateIntentionOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateIntentionOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOssResourcesRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryOssResourcesResponseBodyDataTaskList(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        update_time: int = None,
        oss_url: str = None,
        name: str = None,
        create_time: int = None,
    ):
        self.biz_id = biz_id
        self.update_time = update_time
        self.oss_url = oss_url
        self.name = name
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.name is not None:
            result['Name'] = self.name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class QueryOssResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        task_list: List[QueryOssResourcesResponseBodyDataTaskList] = None,
    ):
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = QueryOssResourcesResponseBodyDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class QueryOssResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: QueryOssResourcesResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryOssResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryOssResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOssResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryOssResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefuseApplicantRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        note: str = None,
    ):
        self.biz_id = biz_id
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.note is not None:
            result['Note'] = self.note
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        return self


class RefuseApplicantResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class RefuseApplicantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefuseApplicantResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RefuseApplicantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntentionOrderGeneratingPayRequest(TeaModel):
    def __init__(
        self,
        intention_biz_id: str = None,
        payment_callback: str = None,
        channel: str = None,
    ):
        self.intention_biz_id = intention_biz_id
        self.payment_callback = payment_callback
        self.channel = channel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id
        if self.payment_callback is not None:
            result['PaymentCallback'] = self.payment_callback
        if self.channel is not None:
            result['Channel'] = self.channel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')
        if m.get('PaymentCallback') is not None:
            self.payment_callback = m.get('PaymentCallback')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        return self


class CreateIntentionOrderGeneratingPayResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        pay_url: str = None,
        success: bool = None,
        order_ids: List[int] = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.pay_url = pay_url
        self.success = success
        self.order_ids = order_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pay_url is not None:
            result['PayUrl'] = self.pay_url
        if self.success is not None:
            result['Success'] = self.success
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PayUrl') is not None:
            self.pay_url = m.get('PayUrl')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class CreateIntentionOrderGeneratingPayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateIntentionOrderGeneratingPayResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateIntentionOrderGeneratingPayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNotaryOrdersRequest(TeaModel):
    def __init__(
        self,
        start_order_date: int = None,
        end_order_date: int = None,
        notary_status: int = None,
        aliyun_order_id: str = None,
        sort_by_type: str = None,
        sort_key_type: int = None,
        page_num: int = None,
        page_size: int = None,
        biz_id: str = None,
        notary_type: int = None,
    ):
        self.start_order_date = start_order_date
        self.end_order_date = end_order_date
        self.notary_status = notary_status
        self.aliyun_order_id = aliyun_order_id
        self.sort_by_type = sort_by_type
        self.sort_key_type = sort_key_type
        self.page_num = page_num
        self.page_size = page_size
        self.biz_id = biz_id
        self.notary_type = notary_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_order_date is not None:
            result['StartOrderDate'] = self.start_order_date
        if self.end_order_date is not None:
            result['EndOrderDate'] = self.end_order_date
        if self.notary_status is not None:
            result['NotaryStatus'] = self.notary_status
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.sort_by_type is not None:
            result['SortByType'] = self.sort_by_type
        if self.sort_key_type is not None:
            result['SortKeyType'] = self.sort_key_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartOrderDate') is not None:
            self.start_order_date = m.get('StartOrderDate')
        if m.get('EndOrderDate') is not None:
            self.end_order_date = m.get('EndOrderDate')
        if m.get('NotaryStatus') is not None:
            self.notary_status = m.get('NotaryStatus')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('SortByType') is not None:
            self.sort_by_type = m.get('SortByType')
        if m.get('SortKeyType') is not None:
            self.sort_key_type = m.get('SortKeyType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        return self


class ListNotaryOrdersResponseBodyDataNotaryOrder(TeaModel):
    def __init__(
        self,
        order_date: int = None,
        order_price: float = None,
        notary_type: int = None,
        tm_classification: str = None,
        biz_id: str = None,
        gmt_modified: int = None,
        notary_status: int = None,
        notary_order_id: int = None,
        tm_name: str = None,
        tm_register_no: str = None,
        tm_image: str = None,
        aliyun_order_id: str = None,
        apply_post_status: str = None,
        notary_certificate: str = None,
        notary_platform_name: str = None,
    ):
        self.order_date = order_date
        self.order_price = order_price
        self.notary_type = notary_type
        self.tm_classification = tm_classification
        self.biz_id = biz_id
        self.gmt_modified = gmt_modified
        self.notary_status = notary_status
        self.notary_order_id = notary_order_id
        self.tm_name = tm_name
        self.tm_register_no = tm_register_no
        self.tm_image = tm_image
        self.aliyun_order_id = aliyun_order_id
        self.apply_post_status = apply_post_status
        self.notary_certificate = notary_certificate
        self.notary_platform_name = notary_platform_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_date is not None:
            result['OrderDate'] = self.order_date
        if self.order_price is not None:
            result['OrderPrice'] = self.order_price
        if self.notary_type is not None:
            result['NotaryType'] = self.notary_type
        if self.tm_classification is not None:
            result['TmClassification'] = self.tm_classification
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.notary_status is not None:
            result['NotaryStatus'] = self.notary_status
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        if self.tm_name is not None:
            result['TmName'] = self.tm_name
        if self.tm_register_no is not None:
            result['TmRegisterNo'] = self.tm_register_no
        if self.tm_image is not None:
            result['TmImage'] = self.tm_image
        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id
        if self.apply_post_status is not None:
            result['ApplyPostStatus'] = self.apply_post_status
        if self.notary_certificate is not None:
            result['NotaryCertificate'] = self.notary_certificate
        if self.notary_platform_name is not None:
            result['NotaryPlatformName'] = self.notary_platform_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderDate') is not None:
            self.order_date = m.get('OrderDate')
        if m.get('OrderPrice') is not None:
            self.order_price = m.get('OrderPrice')
        if m.get('NotaryType') is not None:
            self.notary_type = m.get('NotaryType')
        if m.get('TmClassification') is not None:
            self.tm_classification = m.get('TmClassification')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('NotaryStatus') is not None:
            self.notary_status = m.get('NotaryStatus')
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        if m.get('TmName') is not None:
            self.tm_name = m.get('TmName')
        if m.get('TmRegisterNo') is not None:
            self.tm_register_no = m.get('TmRegisterNo')
        if m.get('TmImage') is not None:
            self.tm_image = m.get('TmImage')
        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')
        if m.get('ApplyPostStatus') is not None:
            self.apply_post_status = m.get('ApplyPostStatus')
        if m.get('NotaryCertificate') is not None:
            self.notary_certificate = m.get('NotaryCertificate')
        if m.get('NotaryPlatformName') is not None:
            self.notary_platform_name = m.get('NotaryPlatformName')
        return self


class ListNotaryOrdersResponseBodyData(TeaModel):
    def __init__(
        self,
        notary_order: List[ListNotaryOrdersResponseBodyDataNotaryOrder] = None,
    ):
        self.notary_order = notary_order

    def validate(self):
        if self.notary_order:
            for k in self.notary_order:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NotaryOrder'] = []
        if self.notary_order is not None:
            for k in self.notary_order:
                result['NotaryOrder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.notary_order = []
        if m.get('NotaryOrder') is not None:
            for k in m.get('NotaryOrder'):
                temp_model = ListNotaryOrdersResponseBodyDataNotaryOrder()
                self.notary_order.append(temp_model.from_map(k))
        return self


class ListNotaryOrdersResponseBody(TeaModel):
    def __init__(
        self,
        next_page: bool = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
        total_item_num: int = None,
        pre_page: bool = None,
        current_page_num: int = None,
        error_msg: str = None,
        total_page_num: int = None,
        page_size: int = None,
        data: ListNotaryOrdersResponseBodyData = None,
    ):
        self.next_page = next_page
        self.request_id = request_id
        self.success = success
        self.error_code = error_code
        self.total_item_num = total_item_num
        self.pre_page = pre_page
        self.current_page_num = current_page_num
        self.error_msg = error_msg
        self.total_page_num = total_page_num
        self.page_size = page_size
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Data') is not None:
            temp_model = ListNotaryOrdersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListNotaryOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNotaryOrdersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNotaryOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSupportPrincipalNameResponseBodyPrincipals(TeaModel):
    def __init__(
        self,
        principal_description: str = None,
        default_principal: bool = None,
        principal_value: int = None,
    ):
        self.principal_description = principal_description
        self.default_principal = default_principal
        self.principal_value = principal_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_description is not None:
            result['PrincipalDescription'] = self.principal_description
        if self.default_principal is not None:
            result['DefaultPrincipal'] = self.default_principal
        if self.principal_value is not None:
            result['PrincipalValue'] = self.principal_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalDescription') is not None:
            self.principal_description = m.get('PrincipalDescription')
        if m.get('DefaultPrincipal') is not None:
            self.default_principal = m.get('DefaultPrincipal')
        if m.get('PrincipalValue') is not None:
            self.principal_value = m.get('PrincipalValue')
        return self


class GetSupportPrincipalNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        principals: List[GetSupportPrincipalNameResponseBodyPrincipals] = None,
    ):
        self.request_id = request_id
        self.principals = principals

    def validate(self):
        if self.principals:
            for k in self.principals:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Principals'] = []
        if self.principals is not None:
            for k in self.principals:
                result['Principals'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.principals = []
        if m.get('Principals') is not None:
            for k in m.get('Principals'):
                temp_model = GetSupportPrincipalNameResponseBodyPrincipals()
                self.principals.append(temp_model.from_map(k))
        return self


class GetSupportPrincipalNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSupportPrincipalNameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSupportPrincipalNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartNotaryRequest(TeaModel):
    def __init__(
        self,
        notary_order_id: int = None,
    ):
        self.notary_order_id = notary_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notary_order_id is not None:
            result['NotaryOrderId'] = self.notary_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotaryOrderId') is not None:
            self.notary_order_id = m.get('NotaryOrderId')
        return self


class StartNotaryResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        notary_url: str = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.notary_url = notary_url
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.notary_url is not None:
            result['NotaryUrl'] = self.notary_url
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('NotaryUrl') is not None:
            self.notary_url = m.get('NotaryUrl')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class StartNotaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartNotaryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartNotaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSendMaterialNumRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        num: str = None,
        operate_type: int = None,
    ):
        self.biz_id = biz_id
        self.num = num
        self.operate_type = operate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.num is not None:
            result['Num'] = self.num
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class UpdateSendMaterialNumResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        error_code: str = None,
    ):
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class UpdateSendMaterialNumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSendMaterialNumResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSendMaterialNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrademarkApplicationRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DeleteTrademarkApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTrademarkApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTrademarkApplicationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteTrademarkApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


