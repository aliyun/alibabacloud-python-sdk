# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AcceptDemandRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        message: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AcceptDemandResponseBody(TeaModel):
    def __init__(
        self,
        bind_url: str = None,
        request_id: str = None,
    ):
        self.bind_url = bind_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_url is not None:
            result['BindUrl'] = self.bind_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindUrl') is not None:
            self.bind_url = m.get('BindUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AcceptDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AcceptDemandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AcceptDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchIntrudeDomainsRequest(TeaModel):
    def __init__(
        self,
        domain_names: List[str] = None,
    ):
        self.domain_names = domain_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        return self


class BatchIntrudeDomainsShrinkRequest(TeaModel):
    def __init__(
        self,
        domain_names_shrink: str = None,
    ):
        self.domain_names_shrink = domain_names_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names_shrink is not None:
            result['DomainNames'] = self.domain_names_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names_shrink = m.get('DomainNames')
        return self


class BatchIntrudeDomainsResponseBodyDataFailureList(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        error_code: str = None,
        error_msg: str = None,
        success: bool = None,
    ):
        self.domain_name = domain_name
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
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchIntrudeDomainsResponseBodyDataSuccessList(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        error_code: str = None,
        error_msg: str = None,
        success: bool = None,
    ):
        self.domain_name = domain_name
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
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchIntrudeDomainsResponseBodyData(TeaModel):
    def __init__(
        self,
        failure_count: int = None,
        failure_list: List[BatchIntrudeDomainsResponseBodyDataFailureList] = None,
        success_count: int = None,
        success_list: List[BatchIntrudeDomainsResponseBodyDataSuccessList] = None,
    ):
        self.failure_count = failure_count
        self.failure_list = failure_list
        self.success_count = success_count
        self.success_list = success_list

    def validate(self):
        if self.failure_list:
            for k in self.failure_list:
                if k:
                    k.validate()
        if self.success_list:
            for k in self.success_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failure_count is not None:
            result['FailureCount'] = self.failure_count
        result['FailureList'] = []
        if self.failure_list is not None:
            for k in self.failure_list:
                result['FailureList'].append(k.to_map() if k else None)
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        result['SuccessList'] = []
        if self.success_list is not None:
            for k in self.success_list:
                result['SuccessList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailureCount') is not None:
            self.failure_count = m.get('FailureCount')
        self.failure_list = []
        if m.get('FailureList') is not None:
            for k in m.get('FailureList'):
                temp_model = BatchIntrudeDomainsResponseBodyDataFailureList()
                self.failure_list.append(temp_model.from_map(k))
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        self.success_list = []
        if m.get('SuccessList') is not None:
            for k in m.get('SuccessList'):
                temp_model = BatchIntrudeDomainsResponseBodyDataSuccessList()
                self.success_list.append(temp_model.from_map(k))
        return self


class BatchIntrudeDomainsResponseBody(TeaModel):
    def __init__(
        self,
        data: BatchIntrudeDomainsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = BatchIntrudeDomainsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchIntrudeDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchIntrudeDomainsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = BatchIntrudeDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BidDomainRequest(TeaModel):
    def __init__(
        self,
        auction_id: str = None,
        currency: str = None,
        max_bid: float = None,
    ):
        # This parameter is required.
        self.auction_id = auction_id
        # This parameter is required.
        self.currency = currency
        # This parameter is required.
        self.max_bid = max_bid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.max_bid is not None:
            result['MaxBid'] = self.max_bid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('MaxBid') is not None:
            self.max_bid = m.get('MaxBid')
        return self


class BidDomainResponseBody(TeaModel):
    def __init__(
        self,
        auction_id: str = None,
        request_id: str = None,
    ):
        self.auction_id = auction_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BidDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BidDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = BidDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeAuctionRequestAuctionListBidRecords(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        price: float = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.create_time = create_time
        # This parameter is required.
        self.price = price
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.price is not None:
            result['Price'] = self.price
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ChangeAuctionRequestAuctionList(TeaModel):
    def __init__(
        self,
        bid_records: List[ChangeAuctionRequestAuctionListBidRecords] = None,
        domain_name: str = None,
        end_time: str = None,
        is_reserve: int = None,
        reserve_price: float = None,
        reserve_range: str = None,
        status: str = None,
        time_left: int = None,
        winner: str = None,
        winner_price: float = None,
    ):
        self.bid_records = bid_records
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.end_time = end_time
        self.is_reserve = is_reserve
        self.reserve_price = reserve_price
        self.reserve_range = reserve_range
        self.status = status
        self.time_left = time_left
        # This parameter is required.
        self.winner = winner
        # This parameter is required.
        self.winner_price = winner_price

    def validate(self):
        if self.bid_records:
            for k in self.bid_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BidRecords'] = []
        if self.bid_records is not None:
            for k in self.bid_records:
                result['BidRecords'].append(k.to_map() if k else None)
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_reserve is not None:
            result['IsReserve'] = self.is_reserve
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.reserve_range is not None:
            result['ReserveRange'] = self.reserve_range
        if self.status is not None:
            result['Status'] = self.status
        if self.time_left is not None:
            result['TimeLeft'] = self.time_left
        if self.winner is not None:
            result['Winner'] = self.winner
        if self.winner_price is not None:
            result['WinnerPrice'] = self.winner_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bid_records = []
        if m.get('BidRecords') is not None:
            for k in m.get('BidRecords'):
                temp_model = ChangeAuctionRequestAuctionListBidRecords()
                self.bid_records.append(temp_model.from_map(k))
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsReserve') is not None:
            self.is_reserve = m.get('IsReserve')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('ReserveRange') is not None:
            self.reserve_range = m.get('ReserveRange')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeLeft') is not None:
            self.time_left = m.get('TimeLeft')
        if m.get('Winner') is not None:
            self.winner = m.get('Winner')
        if m.get('WinnerPrice') is not None:
            self.winner_price = m.get('WinnerPrice')
        return self


class ChangeAuctionRequest(TeaModel):
    def __init__(
        self,
        auction_list: List[ChangeAuctionRequestAuctionList] = None,
    ):
        self.auction_list = auction_list

    def validate(self):
        if self.auction_list:
            for k in self.auction_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuctionList'] = []
        if self.auction_list is not None:
            for k in self.auction_list:
                result['AuctionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auction_list = []
        if m.get('AuctionList') is not None:
            for k in m.get('AuctionList'):
                temp_model = ChangeAuctionRequestAuctionList()
                self.auction_list.append(temp_model.from_map(k))
        return self


class ChangeAuctionResponseBody(TeaModel):
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


class ChangeAuctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeAuctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ChangeAuctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDomainStatusRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        # This parameter is required.
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class CheckDomainStatusResponseBodyModule(TeaModel):
    def __init__(
        self,
        dead_date: int = None,
        domain: str = None,
        end_time: int = None,
        price: float = None,
        reg_date: int = None,
    ):
        self.dead_date = dead_date
        self.domain = domain
        self.end_time = end_time
        self.price = price
        self.reg_date = reg_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_date is not None:
            result['DeadDate'] = self.dead_date
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.price is not None:
            result['Price'] = self.price
        if self.reg_date is not None:
            result['RegDate'] = self.reg_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadDate') is not None:
            self.dead_date = m.get('DeadDate')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RegDate') is not None:
            self.reg_date = m.get('RegDate')
        return self


class CheckDomainStatusResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        http_status_code: int = None,
        module: CheckDomainStatusResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.module = module
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            temp_model = CheckDomainStatusResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckDomainStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDomainStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CheckDomainStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckSelectedDomainStatusRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        # This parameter is required.
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class CheckSelectedDomainStatusResponseBodyModule(TeaModel):
    def __init__(
        self,
        dead_date: int = None,
        domain: str = None,
        end_time: int = None,
        premium: bool = None,
        price: float = None,
        reg_date: int = None,
    ):
        self.dead_date = dead_date
        self.domain = domain
        self.end_time = end_time
        self.premium = premium
        self.price = price
        self.reg_date = reg_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_date is not None:
            result['DeadDate'] = self.dead_date
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.premium is not None:
            result['Premium'] = self.premium
        if self.price is not None:
            result['Price'] = self.price
        if self.reg_date is not None:
            result['RegDate'] = self.reg_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadDate') is not None:
            self.dead_date = m.get('DeadDate')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Premium') is not None:
            self.premium = m.get('Premium')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RegDate') is not None:
            self.reg_date = m.get('RegDate')
        return self


class CheckSelectedDomainStatusResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        http_status_code: int = None,
        module: CheckSelectedDomainStatusResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.module = module
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            temp_model = CheckSelectedDomainStatusResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckSelectedDomainStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckSelectedDomainStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CheckSelectedDomainStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFixedPriceDemandOrderRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        contact_id: str = None,
        domain: str = None,
        source: str = None,
    ):
        self.code = code
        self.contact_id = contact_id
        self.domain = domain
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateFixedPriceDemandOrderResponseBodyModule(TeaModel):
    def __init__(
        self,
        domain: str = None,
        order_no: str = None,
        price: int = None,
    ):
        self.domain = domain
        self.order_no = order_no
        self.price = price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.order_no is not None:
            result['OrderNo'] = self.order_no
        if self.price is not None:
            result['Price'] = self.price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        return self


class CreateFixedPriceDemandOrderResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        http_status_code: int = None,
        module: CreateFixedPriceDemandOrderResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.module = module
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            temp_model = CreateFixedPriceDemandOrderResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFixedPriceDemandOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFixedPriceDemandOrderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateFixedPriceDemandOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFixedPriceSelectedOrderRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        contact_id: str = None,
        domain_name: str = None,
        expected_price: float = None,
        source: str = None,
    ):
        self.code = code
        # This parameter is required.
        self.contact_id = contact_id
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.expected_price = expected_price
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.expected_price is not None:
            result['ExpectedPrice'] = self.expected_price
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ExpectedPrice') is not None:
            self.expected_price = m.get('ExpectedPrice')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateFixedPriceSelectedOrderResponseBodyModule(TeaModel):
    def __init__(
        self,
        domain: str = None,
        domain_block_trade: List[str] = None,
        order_no: str = None,
        price: int = None,
    ):
        self.domain = domain
        self.domain_block_trade = domain_block_trade
        self.order_no = order_no
        self.price = price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_block_trade is not None:
            result['DomainBlockTrade'] = self.domain_block_trade
        if self.order_no is not None:
            result['OrderNo'] = self.order_no
        if self.price is not None:
            result['Price'] = self.price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainBlockTrade') is not None:
            self.domain_block_trade = m.get('DomainBlockTrade')
        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        return self


class CreateFixedPriceSelectedOrderResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        http_status_code: int = None,
        module: CreateFixedPriceSelectedOrderResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.module = module
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            temp_model = CreateFixedPriceSelectedOrderResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFixedPriceSelectedOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFixedPriceSelectedOrderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateFixedPriceSelectedOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FailDemandRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        message: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class FailDemandResponseBody(TeaModel):
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


class FailDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FailDemandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = FailDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FinishDemandRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        message: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class FinishDemandResponseBody(TeaModel):
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


class FinishDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FinishDemandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = FinishDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIntlDomainDownloadUrlResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        url: str = None,
    ):
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetIntlDomainDownloadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIntlDomainDownloadUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetIntlDomainDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReserveDomainUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        url: str = None,
    ):
        self.request_id = request_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetReserveDomainUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetReserveDomainUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetReserveDomainUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PurchaseIntlDomainRequest(TeaModel):
    def __init__(
        self,
        auction_id: str = None,
        currency: str = None,
        price: float = None,
    ):
        # This parameter is required.
        self.auction_id = auction_id
        # This parameter is required.
        self.currency = currency
        # This parameter is required.
        self.price = price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.price is not None:
            result['Price'] = self.price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        return self


class PurchaseIntlDomainResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        auction_id: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.auction_id = auction_id
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PurchaseIntlDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PurchaseIntlDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = PurchaseIntlDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAuctionDetailRequest(TeaModel):
    def __init__(
        self,
        auction_id: str = None,
    ):
        # This parameter is required.
        self.auction_id = auction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        return self


class QueryAuctionDetailResponseBody(TeaModel):
    def __init__(
        self,
        auction_end_time: int = None,
        auction_id: str = None,
        book_end_time: int = None,
        booked_partner: str = None,
        currency: str = None,
        delivery_time: int = None,
        domain_name: str = None,
        domain_type: str = None,
        fail_code: str = None,
        high_bid: float = None,
        high_bidder: str = None,
        next_valid_bid: float = None,
        partner_type: str = None,
        pay_end_time: int = None,
        pay_price: float = None,
        pay_status: str = None,
        produce_status: str = None,
        request_id: str = None,
        reserve_met: bool = None,
        reserve_price: float = None,
        status: str = None,
        transfer_in_price: float = None,
        your_current_bid: float = None,
        your_max_bid: float = None,
    ):
        self.auction_end_time = auction_end_time
        self.auction_id = auction_id
        self.book_end_time = book_end_time
        self.booked_partner = booked_partner
        self.currency = currency
        self.delivery_time = delivery_time
        self.domain_name = domain_name
        self.domain_type = domain_type
        self.fail_code = fail_code
        self.high_bid = high_bid
        self.high_bidder = high_bidder
        self.next_valid_bid = next_valid_bid
        self.partner_type = partner_type
        self.pay_end_time = pay_end_time
        self.pay_price = pay_price
        self.pay_status = pay_status
        self.produce_status = produce_status
        self.request_id = request_id
        self.reserve_met = reserve_met
        self.reserve_price = reserve_price
        self.status = status
        self.transfer_in_price = transfer_in_price
        self.your_current_bid = your_current_bid
        self.your_max_bid = your_max_bid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_end_time is not None:
            result['AuctionEndTime'] = self.auction_end_time
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.book_end_time is not None:
            result['BookEndTime'] = self.book_end_time
        if self.booked_partner is not None:
            result['BookedPartner'] = self.booked_partner
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.fail_code is not None:
            result['FailCode'] = self.fail_code
        if self.high_bid is not None:
            result['HighBid'] = self.high_bid
        if self.high_bidder is not None:
            result['HighBidder'] = self.high_bidder
        if self.next_valid_bid is not None:
            result['NextValidBid'] = self.next_valid_bid
        if self.partner_type is not None:
            result['PartnerType'] = self.partner_type
        if self.pay_end_time is not None:
            result['PayEndTime'] = self.pay_end_time
        if self.pay_price is not None:
            result['PayPrice'] = self.pay_price
        if self.pay_status is not None:
            result['PayStatus'] = self.pay_status
        if self.produce_status is not None:
            result['ProduceStatus'] = self.produce_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.reserve_met is not None:
            result['ReserveMet'] = self.reserve_met
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.status is not None:
            result['Status'] = self.status
        if self.transfer_in_price is not None:
            result['TransferInPrice'] = self.transfer_in_price
        if self.your_current_bid is not None:
            result['YourCurrentBid'] = self.your_current_bid
        if self.your_max_bid is not None:
            result['YourMaxBid'] = self.your_max_bid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionEndTime') is not None:
            self.auction_end_time = m.get('AuctionEndTime')
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('BookEndTime') is not None:
            self.book_end_time = m.get('BookEndTime')
        if m.get('BookedPartner') is not None:
            self.booked_partner = m.get('BookedPartner')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('FailCode') is not None:
            self.fail_code = m.get('FailCode')
        if m.get('HighBid') is not None:
            self.high_bid = m.get('HighBid')
        if m.get('HighBidder') is not None:
            self.high_bidder = m.get('HighBidder')
        if m.get('NextValidBid') is not None:
            self.next_valid_bid = m.get('NextValidBid')
        if m.get('PartnerType') is not None:
            self.partner_type = m.get('PartnerType')
        if m.get('PayEndTime') is not None:
            self.pay_end_time = m.get('PayEndTime')
        if m.get('PayPrice') is not None:
            self.pay_price = m.get('PayPrice')
        if m.get('PayStatus') is not None:
            self.pay_status = m.get('PayStatus')
        if m.get('ProduceStatus') is not None:
            self.produce_status = m.get('ProduceStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReserveMet') is not None:
            self.reserve_met = m.get('ReserveMet')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransferInPrice') is not None:
            self.transfer_in_price = m.get('TransferInPrice')
        if m.get('YourCurrentBid') is not None:
            self.your_current_bid = m.get('YourCurrentBid')
        if m.get('YourMaxBid') is not None:
            self.your_max_bid = m.get('YourMaxBid')
        return self


class QueryAuctionDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAuctionDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryAuctionDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAuctionsRequest(TeaModel):
    def __init__(
        self,
        auction_end_time_order: str = None,
        current_page: int = None,
        page_size: int = None,
        status: str = None,
        statuses: str = None,
    ):
        self.auction_end_time_order = auction_end_time_order
        self.current_page = current_page
        self.page_size = page_size
        self.status = status
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_end_time_order is not None:
            result['AuctionEndTimeOrder'] = self.auction_end_time_order
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.statuses is not None:
            result['Statuses'] = self.statuses
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionEndTimeOrder') is not None:
            self.auction_end_time_order = m.get('AuctionEndTimeOrder')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')
        return self


class QueryAuctionsResponseBodyData(TeaModel):
    def __init__(
        self,
        auction_end_time: int = None,
        auction_id: str = None,
        book_end_time: int = None,
        booked_partner: str = None,
        currency: str = None,
        delivery_time: int = None,
        domain_name: str = None,
        domain_type: str = None,
        fail_code: str = None,
        high_bid: float = None,
        high_bidder: str = None,
        next_valid_bid: float = None,
        partner_type: str = None,
        pay_end_time: int = None,
        pay_price: float = None,
        pay_status: str = None,
        produce_status: str = None,
        reserve_max: int = None,
        reserve_met: bool = None,
        reserve_min: int = None,
        reserve_price: int = None,
        status: str = None,
        transfer_in_price: float = None,
        your_current_bid: float = None,
        your_max_bid: float = None,
    ):
        self.auction_end_time = auction_end_time
        self.auction_id = auction_id
        self.book_end_time = book_end_time
        self.booked_partner = booked_partner
        self.currency = currency
        self.delivery_time = delivery_time
        self.domain_name = domain_name
        self.domain_type = domain_type
        self.fail_code = fail_code
        self.high_bid = high_bid
        self.high_bidder = high_bidder
        self.next_valid_bid = next_valid_bid
        self.partner_type = partner_type
        self.pay_end_time = pay_end_time
        self.pay_price = pay_price
        self.pay_status = pay_status
        self.produce_status = produce_status
        self.reserve_max = reserve_max
        self.reserve_met = reserve_met
        self.reserve_min = reserve_min
        self.reserve_price = reserve_price
        self.status = status
        self.transfer_in_price = transfer_in_price
        self.your_current_bid = your_current_bid
        self.your_max_bid = your_max_bid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_end_time is not None:
            result['AuctionEndTime'] = self.auction_end_time
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.book_end_time is not None:
            result['BookEndTime'] = self.book_end_time
        if self.booked_partner is not None:
            result['BookedPartner'] = self.booked_partner
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.fail_code is not None:
            result['FailCode'] = self.fail_code
        if self.high_bid is not None:
            result['HighBid'] = self.high_bid
        if self.high_bidder is not None:
            result['HighBidder'] = self.high_bidder
        if self.next_valid_bid is not None:
            result['NextValidBid'] = self.next_valid_bid
        if self.partner_type is not None:
            result['PartnerType'] = self.partner_type
        if self.pay_end_time is not None:
            result['PayEndTime'] = self.pay_end_time
        if self.pay_price is not None:
            result['PayPrice'] = self.pay_price
        if self.pay_status is not None:
            result['PayStatus'] = self.pay_status
        if self.produce_status is not None:
            result['ProduceStatus'] = self.produce_status
        if self.reserve_max is not None:
            result['ReserveMax'] = self.reserve_max
        if self.reserve_met is not None:
            result['ReserveMet'] = self.reserve_met
        if self.reserve_min is not None:
            result['ReserveMin'] = self.reserve_min
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.status is not None:
            result['Status'] = self.status
        if self.transfer_in_price is not None:
            result['TransferInPrice'] = self.transfer_in_price
        if self.your_current_bid is not None:
            result['YourCurrentBid'] = self.your_current_bid
        if self.your_max_bid is not None:
            result['YourMaxBid'] = self.your_max_bid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionEndTime') is not None:
            self.auction_end_time = m.get('AuctionEndTime')
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('BookEndTime') is not None:
            self.book_end_time = m.get('BookEndTime')
        if m.get('BookedPartner') is not None:
            self.booked_partner = m.get('BookedPartner')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('FailCode') is not None:
            self.fail_code = m.get('FailCode')
        if m.get('HighBid') is not None:
            self.high_bid = m.get('HighBid')
        if m.get('HighBidder') is not None:
            self.high_bidder = m.get('HighBidder')
        if m.get('NextValidBid') is not None:
            self.next_valid_bid = m.get('NextValidBid')
        if m.get('PartnerType') is not None:
            self.partner_type = m.get('PartnerType')
        if m.get('PayEndTime') is not None:
            self.pay_end_time = m.get('PayEndTime')
        if m.get('PayPrice') is not None:
            self.pay_price = m.get('PayPrice')
        if m.get('PayStatus') is not None:
            self.pay_status = m.get('PayStatus')
        if m.get('ProduceStatus') is not None:
            self.produce_status = m.get('ProduceStatus')
        if m.get('ReserveMax') is not None:
            self.reserve_max = m.get('ReserveMax')
        if m.get('ReserveMet') is not None:
            self.reserve_met = m.get('ReserveMet')
        if m.get('ReserveMin') is not None:
            self.reserve_min = m.get('ReserveMin')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransferInPrice') is not None:
            self.transfer_in_price = m.get('TransferInPrice')
        if m.get('YourCurrentBid') is not None:
            self.your_current_bid = m.get('YourCurrentBid')
        if m.get('YourMaxBid') is not None:
            self.your_max_bid = m.get('YourMaxBid')
        return self


class QueryAuctionsResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[QueryAuctionsResponseBodyData] = None,
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
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = QueryAuctionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryAuctionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAuctionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryAuctionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBidRecordsRequest(TeaModel):
    def __init__(
        self,
        auction_id: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.auction_id = auction_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryBidRecordsResponseBodyData(TeaModel):
    def __init__(
        self,
        bid: float = None,
        bid_time: int = None,
        bidder: str = None,
        currency: str = None,
        domain_name: str = None,
    ):
        self.bid = bid
        self.bid_time = bid_time
        self.bidder = bidder
        self.currency = currency
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.bid_time is not None:
            result['BidTime'] = self.bid_time
        if self.bidder is not None:
            result['Bidder'] = self.bidder
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('BidTime') is not None:
            self.bid_time = m.get('BidTime')
        if m.get('Bidder') is not None:
            self.bidder = m.get('Bidder')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class QueryBidRecordsResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[QueryBidRecordsResponseBodyData] = None,
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
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = QueryBidRecordsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryBidRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBidRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryBidRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBookingDomainInfoRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class QueryBookingDomainInfoResponseBody(TeaModel):
    def __init__(
        self,
        auction_id: int = None,
        book_end_time: int = None,
        currency: str = None,
        max_bid: float = None,
        partner_type: str = None,
        request_id: str = None,
        snatch_no: str = None,
        transfer_in_price: float = None,
    ):
        self.auction_id = auction_id
        self.book_end_time = book_end_time
        self.currency = currency
        self.max_bid = max_bid
        self.partner_type = partner_type
        self.request_id = request_id
        self.snatch_no = snatch_no
        self.transfer_in_price = transfer_in_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.book_end_time is not None:
            result['BookEndTime'] = self.book_end_time
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.max_bid is not None:
            result['MaxBid'] = self.max_bid
        if self.partner_type is not None:
            result['PartnerType'] = self.partner_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snatch_no is not None:
            result['SnatchNo'] = self.snatch_no
        if self.transfer_in_price is not None:
            result['TransferInPrice'] = self.transfer_in_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('BookEndTime') is not None:
            self.book_end_time = m.get('BookEndTime')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('MaxBid') is not None:
            self.max_bid = m.get('MaxBid')
        if m.get('PartnerType') is not None:
            self.partner_type = m.get('PartnerType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnatchNo') is not None:
            self.snatch_no = m.get('SnatchNo')
        if m.get('TransferInPrice') is not None:
            self.transfer_in_price = m.get('TransferInPrice')
        return self


class QueryBookingDomainInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBookingDomainInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryBookingDomainInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBrokerDemandRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        current_page: int = None,
        page_size: int = None,
        status: str = None,
    ):
        self.biz_id = biz_id
        self.current_page = current_page
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryBrokerDemandResponseBodyData(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class QueryBrokerDemandResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[QueryBrokerDemandResponseBodyData] = None,
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
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = QueryBrokerDemandResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryBrokerDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBrokerDemandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryBrokerDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBrokerDemandRecordRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        self.current_page = current_page
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryBrokerDemandRecordResponseBodyDataBrokerDemandRecord(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        create_time: int = None,
        description: str = None,
    ):
        self.biz_id = biz_id
        self.create_time = create_time
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class QueryBrokerDemandRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        broker_demand_record: List[QueryBrokerDemandRecordResponseBodyDataBrokerDemandRecord] = None,
    ):
        self.broker_demand_record = broker_demand_record

    def validate(self):
        if self.broker_demand_record:
            for k in self.broker_demand_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BrokerDemandRecord'] = []
        if self.broker_demand_record is not None:
            for k in self.broker_demand_record:
                result['BrokerDemandRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.broker_demand_record = []
        if m.get('BrokerDemandRecord') is not None:
            for k in m.get('BrokerDemandRecord'):
                temp_model = QueryBrokerDemandRecordResponseBodyDataBrokerDemandRecord()
                self.broker_demand_record.append(temp_model.from_map(k))
        return self


class QueryBrokerDemandRecordResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: QueryBrokerDemandRecordResponseBodyData = None,
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
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = QueryBrokerDemandRecordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryBrokerDemandRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBrokerDemandRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryBrokerDemandRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDomainTransferStatusRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class QueryDomainTransferStatusResponseBodyDomainTransferStatus(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_status_description: str = None,
    ):
        self.domain_name = domain_name
        self.domain_status_description = domain_status_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status_description is not None:
            result['DomainStatusDescription'] = self.domain_status_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatusDescription') is not None:
            self.domain_status_description = m.get('DomainStatusDescription')
        return self


class QueryDomainTransferStatusResponseBody(TeaModel):
    def __init__(
        self,
        domain_transfer_status: List[QueryDomainTransferStatusResponseBodyDomainTransferStatus] = None,
        request_id: str = None,
    ):
        self.domain_transfer_status = domain_transfer_status
        self.request_id = request_id

    def validate(self):
        if self.domain_transfer_status:
            for k in self.domain_transfer_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainTransferStatus'] = []
        if self.domain_transfer_status is not None:
            for k in self.domain_transfer_status:
                result['DomainTransferStatus'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_transfer_status = []
        if m.get('DomainTransferStatus') is not None:
            for k in m.get('DomainTransferStatus'):
                temp_model = QueryDomainTransferStatusResponseBodyDomainTransferStatus()
                self.domain_transfer_status.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDomainTransferStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDomainTransferStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryDomainTransferStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryExchangeRateRequest(TeaModel):
    def __init__(
        self,
        from_currency: str = None,
        to_currency: str = None,
    ):
        # This parameter is required.
        self.from_currency = from_currency
        # This parameter is required.
        self.to_currency = to_currency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_currency is not None:
            result['FromCurrency'] = self.from_currency
        if self.to_currency is not None:
            result['ToCurrency'] = self.to_currency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromCurrency') is not None:
            self.from_currency = m.get('FromCurrency')
        if m.get('ToCurrency') is not None:
            self.to_currency = m.get('ToCurrency')
        return self


class QueryExchangeRateResponseBody(TeaModel):
    def __init__(
        self,
        exchange_rate: float = None,
        request_id: str = None,
    ):
        self.exchange_rate = exchange_rate
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exchange_rate is not None:
            result['ExchangeRate'] = self.exchange_rate
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExchangeRate') is not None:
            self.exchange_rate = m.get('ExchangeRate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryExchangeRateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryExchangeRateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryExchangeRateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryExportAuctionDetailRequest(TeaModel):
    def __init__(
        self,
        auction_id: str = None,
    ):
        self.auction_id = auction_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        return self


class QueryExportAuctionDetailResponseBody(TeaModel):
    def __init__(
        self,
        auction_end_time: str = None,
        auction_id: str = None,
        auction_status: str = None,
        book_end_time: str = None,
        buyer_status: str = None,
        current_price: float = None,
        increase_price: float = None,
        my_price: float = None,
        my_proxy_price: float = None,
        others_max_proxy_price: float = None,
        proxy_price: float = None,
        request_id: str = None,
    ):
        self.auction_end_time = auction_end_time
        self.auction_id = auction_id
        self.auction_status = auction_status
        self.book_end_time = book_end_time
        self.buyer_status = buyer_status
        self.current_price = current_price
        self.increase_price = increase_price
        self.my_price = my_price
        self.my_proxy_price = my_proxy_price
        self.others_max_proxy_price = others_max_proxy_price
        self.proxy_price = proxy_price
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_end_time is not None:
            result['AuctionEndTime'] = self.auction_end_time
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.auction_status is not None:
            result['AuctionStatus'] = self.auction_status
        if self.book_end_time is not None:
            result['BookEndTime'] = self.book_end_time
        if self.buyer_status is not None:
            result['BuyerStatus'] = self.buyer_status
        if self.current_price is not None:
            result['CurrentPrice'] = self.current_price
        if self.increase_price is not None:
            result['IncreasePrice'] = self.increase_price
        if self.my_price is not None:
            result['MyPrice'] = self.my_price
        if self.my_proxy_price is not None:
            result['MyProxyPrice'] = self.my_proxy_price
        if self.others_max_proxy_price is not None:
            result['OthersMaxProxyPrice'] = self.others_max_proxy_price
        if self.proxy_price is not None:
            result['ProxyPrice'] = self.proxy_price
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionEndTime') is not None:
            self.auction_end_time = m.get('AuctionEndTime')
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('AuctionStatus') is not None:
            self.auction_status = m.get('AuctionStatus')
        if m.get('BookEndTime') is not None:
            self.book_end_time = m.get('BookEndTime')
        if m.get('BuyerStatus') is not None:
            self.buyer_status = m.get('BuyerStatus')
        if m.get('CurrentPrice') is not None:
            self.current_price = m.get('CurrentPrice')
        if m.get('IncreasePrice') is not None:
            self.increase_price = m.get('IncreasePrice')
        if m.get('MyPrice') is not None:
            self.my_price = m.get('MyPrice')
        if m.get('MyProxyPrice') is not None:
            self.my_proxy_price = m.get('MyProxyPrice')
        if m.get('OthersMaxProxyPrice') is not None:
            self.others_max_proxy_price = m.get('OthersMaxProxyPrice')
        if m.get('ProxyPrice') is not None:
            self.proxy_price = m.get('ProxyPrice')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryExportAuctionDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryExportAuctionDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryExportAuctionDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryExportDomainExpireSnatchsRequest(TeaModel):
    def __init__(
        self,
        current_id: int = None,
        max_results: int = None,
        next_token: str = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.current_id = current_id
        self.max_results = max_results
        # This parameter is required.
        self.next_token = next_token
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_id is not None:
            result['CurrentId'] = self.current_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentId') is not None:
            self.current_id = m.get('CurrentId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryExportDomainExpireSnatchsResponseBodyData(TeaModel):
    def __init__(
        self,
        auction_end_time: str = None,
        auction_remaining_seconds: int = None,
        baidu_anti_link: int = None,
        baidu_ex_link: int = None,
        baidu_index: int = None,
        baidu_weight: int = None,
        book_end_time: str = None,
        book_remaining_seconds: int = None,
        booked_num: int = None,
        booked_partners: str = None,
        constitute: str = None,
        currency_type: str = None,
        delivery_time: str = None,
        domain_id: str = None,
        domain_len: int = None,
        domain_name: str = None,
        domain_type: str = None,
        end_date: str = None,
        expire_date: str = None,
        extend: str = None,
        freeze_amount: float = None,
        introduction: str = None,
        is_premium: bool = None,
        partner_types: str = None,
        price: float = None,
        product_id: str = None,
        publish_time: str = None,
        reg_date: str = None,
        renew_price: float = None,
        reserved: bool = None,
        rmb_price: float = None,
        s_360weight: int = None,
        seo_attributes: str = None,
        short_name: str = None,
        snatch_no: str = None,
        snatch_type_desc: str = None,
        sougou_anti_link: int = None,
        sougou_index: int = None,
        sougou_weight: int = None,
        suffix: str = None,
        weight: int = None,
    ):
        self.auction_end_time = auction_end_time
        self.auction_remaining_seconds = auction_remaining_seconds
        self.baidu_anti_link = baidu_anti_link
        self.baidu_ex_link = baidu_ex_link
        self.baidu_index = baidu_index
        self.baidu_weight = baidu_weight
        self.book_end_time = book_end_time
        self.book_remaining_seconds = book_remaining_seconds
        self.booked_num = booked_num
        self.booked_partners = booked_partners
        self.constitute = constitute
        self.currency_type = currency_type
        self.delivery_time = delivery_time
        self.domain_id = domain_id
        self.domain_len = domain_len
        self.domain_name = domain_name
        self.domain_type = domain_type
        self.end_date = end_date
        self.expire_date = expire_date
        self.extend = extend
        self.freeze_amount = freeze_amount
        self.introduction = introduction
        self.is_premium = is_premium
        self.partner_types = partner_types
        self.price = price
        self.product_id = product_id
        self.publish_time = publish_time
        self.reg_date = reg_date
        self.renew_price = renew_price
        self.reserved = reserved
        self.rmb_price = rmb_price
        self.s_360weight = s_360weight
        self.seo_attributes = seo_attributes
        self.short_name = short_name
        self.snatch_no = snatch_no
        self.snatch_type_desc = snatch_type_desc
        self.sougou_anti_link = sougou_anti_link
        self.sougou_index = sougou_index
        self.sougou_weight = sougou_weight
        self.suffix = suffix
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_end_time is not None:
            result['AuctionEndTime'] = self.auction_end_time
        if self.auction_remaining_seconds is not None:
            result['AuctionRemainingSeconds'] = self.auction_remaining_seconds
        if self.baidu_anti_link is not None:
            result['BaiduAntiLink'] = self.baidu_anti_link
        if self.baidu_ex_link is not None:
            result['BaiduExLink'] = self.baidu_ex_link
        if self.baidu_index is not None:
            result['BaiduIndex'] = self.baidu_index
        if self.baidu_weight is not None:
            result['BaiduWeight'] = self.baidu_weight
        if self.book_end_time is not None:
            result['BookEndTime'] = self.book_end_time
        if self.book_remaining_seconds is not None:
            result['BookRemainingSeconds'] = self.book_remaining_seconds
        if self.booked_num is not None:
            result['BookedNum'] = self.booked_num
        if self.booked_partners is not None:
            result['BookedPartners'] = self.booked_partners
        if self.constitute is not None:
            result['Constitute'] = self.constitute
        if self.currency_type is not None:
            result['CurrencyType'] = self.currency_type
        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.domain_len is not None:
            result['DomainLen'] = self.domain_len
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.freeze_amount is not None:
            result['FreezeAmount'] = self.freeze_amount
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.is_premium is not None:
            result['IsPremium'] = self.is_premium
        if self.partner_types is not None:
            result['PartnerTypes'] = self.partner_types
        if self.price is not None:
            result['Price'] = self.price
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.reg_date is not None:
            result['RegDate'] = self.reg_date
        if self.renew_price is not None:
            result['RenewPrice'] = self.renew_price
        if self.reserved is not None:
            result['Reserved'] = self.reserved
        if self.rmb_price is not None:
            result['RmbPrice'] = self.rmb_price
        if self.s_360weight is not None:
            result['S360Weight'] = self.s_360weight
        if self.seo_attributes is not None:
            result['SeoAttributes'] = self.seo_attributes
        if self.short_name is not None:
            result['ShortName'] = self.short_name
        if self.snatch_no is not None:
            result['SnatchNo'] = self.snatch_no
        if self.snatch_type_desc is not None:
            result['SnatchTypeDesc'] = self.snatch_type_desc
        if self.sougou_anti_link is not None:
            result['SougouAntiLink'] = self.sougou_anti_link
        if self.sougou_index is not None:
            result['SougouIndex'] = self.sougou_index
        if self.sougou_weight is not None:
            result['SougouWeight'] = self.sougou_weight
        if self.suffix is not None:
            result['Suffix'] = self.suffix
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionEndTime') is not None:
            self.auction_end_time = m.get('AuctionEndTime')
        if m.get('AuctionRemainingSeconds') is not None:
            self.auction_remaining_seconds = m.get('AuctionRemainingSeconds')
        if m.get('BaiduAntiLink') is not None:
            self.baidu_anti_link = m.get('BaiduAntiLink')
        if m.get('BaiduExLink') is not None:
            self.baidu_ex_link = m.get('BaiduExLink')
        if m.get('BaiduIndex') is not None:
            self.baidu_index = m.get('BaiduIndex')
        if m.get('BaiduWeight') is not None:
            self.baidu_weight = m.get('BaiduWeight')
        if m.get('BookEndTime') is not None:
            self.book_end_time = m.get('BookEndTime')
        if m.get('BookRemainingSeconds') is not None:
            self.book_remaining_seconds = m.get('BookRemainingSeconds')
        if m.get('BookedNum') is not None:
            self.booked_num = m.get('BookedNum')
        if m.get('BookedPartners') is not None:
            self.booked_partners = m.get('BookedPartners')
        if m.get('Constitute') is not None:
            self.constitute = m.get('Constitute')
        if m.get('CurrencyType') is not None:
            self.currency_type = m.get('CurrencyType')
        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DomainLen') is not None:
            self.domain_len = m.get('DomainLen')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('FreezeAmount') is not None:
            self.freeze_amount = m.get('FreezeAmount')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('IsPremium') is not None:
            self.is_premium = m.get('IsPremium')
        if m.get('PartnerTypes') is not None:
            self.partner_types = m.get('PartnerTypes')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('RegDate') is not None:
            self.reg_date = m.get('RegDate')
        if m.get('RenewPrice') is not None:
            self.renew_price = m.get('RenewPrice')
        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')
        if m.get('RmbPrice') is not None:
            self.rmb_price = m.get('RmbPrice')
        if m.get('S360Weight') is not None:
            self.s_360weight = m.get('S360Weight')
        if m.get('SeoAttributes') is not None:
            self.seo_attributes = m.get('SeoAttributes')
        if m.get('ShortName') is not None:
            self.short_name = m.get('ShortName')
        if m.get('SnatchNo') is not None:
            self.snatch_no = m.get('SnatchNo')
        if m.get('SnatchTypeDesc') is not None:
            self.snatch_type_desc = m.get('SnatchTypeDesc')
        if m.get('SougouAntiLink') is not None:
            self.sougou_anti_link = m.get('SougouAntiLink')
        if m.get('SougouIndex') is not None:
            self.sougou_index = m.get('SougouIndex')
        if m.get('SougouWeight') is not None:
            self.sougou_weight = m.get('SougouWeight')
        if m.get('Suffix') is not None:
            self.suffix = m.get('Suffix')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class QueryExportDomainExpireSnatchsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[QueryExportDomainExpireSnatchsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryExportDomainExpireSnatchsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryExportDomainExpireSnatchsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryExportDomainExpireSnatchsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryExportDomainExpireSnatchsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPurchasedDomainsRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        domain_name: str = None,
        end_operation_time: str = None,
        op_time_order: bool = None,
        operation_status: int = None,
        page_size: int = None,
        product_type: int = None,
        start_operation_time: str = None,
        update_time_order: bool = None,
    ):
        self.current_page = current_page
        self.domain_name = domain_name
        self.end_operation_time = end_operation_time
        self.op_time_order = op_time_order
        self.operation_status = operation_status
        self.page_size = page_size
        self.product_type = product_type
        self.start_operation_time = start_operation_time
        self.update_time_order = update_time_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_operation_time is not None:
            result['EndOperationTime'] = self.end_operation_time
        if self.op_time_order is not None:
            result['OpTimeOrder'] = self.op_time_order
        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.start_operation_time is not None:
            result['StartOperationTime'] = self.start_operation_time
        if self.update_time_order is not None:
            result['UpdateTimeOrder'] = self.update_time_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndOperationTime') is not None:
            self.end_operation_time = m.get('EndOperationTime')
        if m.get('OpTimeOrder') is not None:
            self.op_time_order = m.get('OpTimeOrder')
        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('StartOperationTime') is not None:
            self.start_operation_time = m.get('StartOperationTime')
        if m.get('UpdateTimeOrder') is not None:
            self.update_time_order = m.get('UpdateTimeOrder')
        return self


class QueryPurchasedDomainsResponseBodyData(TeaModel):
    def __init__(
        self,
        delivery_time: str = None,
        domain_name: str = None,
        operation_status: str = None,
        operation_time: str = None,
        product_type: str = None,
        trade_money: float = None,
    ):
        self.delivery_time = delivery_time
        self.domain_name = domain_name
        self.operation_status = operation_status
        self.operation_time = operation_time
        self.product_type = product_type
        self.trade_money = trade_money

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status
        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.trade_money is not None:
            result['TradeMoney'] = self.trade_money
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')
        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('TradeMoney') is not None:
            self.trade_money = m.get('TradeMoney')
        return self


class QueryPurchasedDomainsResponseBody(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[QueryPurchasedDomainsResponseBodyData] = None,
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
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = QueryPurchasedDomainsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class QueryPurchasedDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPurchasedDomainsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryPurchasedDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecordDemandRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        message: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecordDemandResponseBody(TeaModel):
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


class RecordDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecordDemandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RecordDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefuseDemandRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        message: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RefuseDemandResponseBody(TeaModel):
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


class RefuseDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefuseDemandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RefuseDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestPayDemandRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        domain_name: str = None,
        message: str = None,
        price: float = None,
        produce_type: int = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.domain_name = domain_name
        self.message = message
        # This parameter is required.
        self.price = price
        self.produce_type = produce_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.message is not None:
            result['Message'] = self.message
        if self.price is not None:
            result['Price'] = self.price
        if self.produce_type is not None:
            result['ProduceType'] = self.produce_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('ProduceType') is not None:
            self.produce_type = m.get('ProduceType')
        return self


class RequestPayDemandResponseBody(TeaModel):
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


class RequestPayDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RequestPayDemandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RequestPayDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReserveDomainRequest(TeaModel):
    def __init__(
        self,
        channels: List[str] = None,
        domain_name: str = None,
    ):
        self.channels = channels
        # This parameter is required.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class ReserveDomainResponseBody(TeaModel):
    def __init__(
        self,
        auction_id: str = None,
        request_id: str = None,
    ):
        self.auction_id = auction_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReserveDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReserveDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ReserveDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReserveIntlDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class ReserveIntlDomainResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        auction_id: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.auction_id = auction_id
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auction_id is not None:
            result['AuctionId'] = self.auction_id
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuctionId') is not None:
            self.auction_id = m.get('AuctionId')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReserveIntlDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReserveIntlDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ReserveIntlDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SelectedDomainListRequest(TeaModel):
    def __init__(
        self,
        list_date: str = None,
    ):
        # This parameter is required.
        self.list_date = list_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_date is not None:
            result['ListDate'] = self.list_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListDate') is not None:
            self.list_date = m.get('ListDate')
        return self


class SelectedDomainListResponseBodyModule(TeaModel):
    def __init__(
        self,
        download_url: str = None,
    ):
        self.download_url = download_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        return self


class SelectedDomainListResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        module: SelectedDomainListResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.module = module
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Module') is not None:
            temp_model = SelectedDomainListResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SelectedDomainListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SelectedDomainListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SelectedDomainListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitPurchaseInfoRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        purchase_currency: str = None,
        purchase_price: float = None,
        purchase_proofs: List[str] = None,
    ):
        self.biz_id = biz_id
        self.purchase_currency = purchase_currency
        self.purchase_price = purchase_price
        self.purchase_proofs = purchase_proofs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.purchase_currency is not None:
            result['PurchaseCurrency'] = self.purchase_currency
        if self.purchase_price is not None:
            result['PurchasePrice'] = self.purchase_price
        if self.purchase_proofs is not None:
            result['PurchaseProofs'] = self.purchase_proofs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('PurchaseCurrency') is not None:
            self.purchase_currency = m.get('PurchaseCurrency')
        if m.get('PurchasePrice') is not None:
            self.purchase_price = m.get('PurchasePrice')
        if m.get('PurchaseProofs') is not None:
            self.purchase_proofs = m.get('PurchaseProofs')
        return self


class SubmitPurchaseInfoResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: Any = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_status_code = http_status_code
        self.module = module
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitPurchaseInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitPurchaseInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SubmitPurchaseInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePartnerReservePriceRequest(TeaModel):
    def __init__(
        self,
        bidding_id: int = None,
        domain_name: str = None,
        partner_type: str = None,
        reserve_price: float = None,
    ):
        # This parameter is required.
        self.bidding_id = bidding_id
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.partner_type = partner_type
        # This parameter is required.
        self.reserve_price = reserve_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bidding_id is not None:
            result['BiddingId'] = self.bidding_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.partner_type is not None:
            result['PartnerType'] = self.partner_type
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BiddingId') is not None:
            self.bidding_id = m.get('BiddingId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PartnerType') is not None:
            self.partner_type = m.get('PartnerType')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        return self


class UpdatePartnerReservePriceResponseBody(TeaModel):
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


class UpdatePartnerReservePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePartnerReservePriceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdatePartnerReservePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


