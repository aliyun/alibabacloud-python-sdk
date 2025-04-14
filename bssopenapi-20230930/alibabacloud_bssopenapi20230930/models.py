# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class AddCouponDeductTagRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class AddCouponDeductTagRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class AddCouponDeductTagRequest(TeaModel):
    def __init__(
        self,
        coupon_id: str = None,
        ec_id_account_ids: List[AddCouponDeductTagRequestEcIdAccountIds] = None,
        nbid: str = None,
        tags: List[AddCouponDeductTagRequestTags] = None,
    ):
        self.coupon_id = coupon_id
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid
        self.tags = tags

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = AddCouponDeductTagRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = AddCouponDeductTagRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class AddCouponDeductTagShrinkRequest(TeaModel):
    def __init__(
        self,
        coupon_id: str = None,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
        tags_shrink: str = None,
    ):
        self.coupon_id = coupon_id
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class AddCouponDeductTagResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddCouponDeductTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddCouponDeductTagResponseBody = None,
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
            temp_model = AddCouponDeductTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelFundAccountLowAvailableAmountAlarmRequest(TeaModel):
    def __init__(
        self,
        fund_account_id: int = None,
    ):
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        return self


class CancelFundAccountLowAvailableAmountAlarmResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.data = data
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelFundAccountLowAvailableAmountAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelFundAccountLowAvailableAmountAlarmResponseBody = None,
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
            temp_model = CancelFundAccountLowAvailableAmountAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFundAccountTransferRequest(TeaModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        finance_type: str = None,
        from_fund_account_id: int = None,
        remark: str = None,
        to_fund_account_id: int = None,
        transfer_type: str = None,
    ):
        # This parameter is required.
        self.amount = amount
        # This parameter is required.
        self.currency = currency
        # This parameter is required.
        self.finance_type = finance_type
        # This parameter is required.
        self.from_fund_account_id = from_fund_account_id
        # This parameter is required.
        self.remark = remark
        # This parameter is required.
        self.to_fund_account_id = to_fund_account_id
        # This parameter is required.
        self.transfer_type = transfer_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.finance_type is not None:
            result['FinanceType'] = self.finance_type
        if self.from_fund_account_id is not None:
            result['FromFundAccountId'] = self.from_fund_account_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.to_fund_account_id is not None:
            result['ToFundAccountId'] = self.to_fund_account_id
        if self.transfer_type is not None:
            result['TransferType'] = self.transfer_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('FinanceType') is not None:
            self.finance_type = m.get('FinanceType')
        if m.get('FromFundAccountId') is not None:
            self.from_fund_account_id = m.get('FromFundAccountId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ToFundAccountId') is not None:
            self.to_fund_account_id = m.get('ToFundAccountId')
        if m.get('TransferType') is not None:
            self.transfer_type = m.get('TransferType')
        return self


class CreateFundAccountTransferResponseBody(TeaModel):
    def __init__(
        self,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFundAccountTransferResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFundAccountTransferResponseBody = None,
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
            temp_model = CreateFundAccountTransferResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCouponDeductTagRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class DeleteCouponDeductTagRequest(TeaModel):
    def __init__(
        self,
        coupon_id: str = None,
        ec_id_account_ids: List[DeleteCouponDeductTagRequestEcIdAccountIds] = None,
        nbid: str = None,
        tag_keys: List[str] = None,
    ):
        self.coupon_id = coupon_id
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid
        self.tag_keys = tag_keys

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = DeleteCouponDeductTagRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class DeleteCouponDeductTagShrinkRequest(TeaModel):
    def __init__(
        self,
        coupon_id: str = None,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
        tag_keys_shrink: str = None,
    ):
        self.coupon_id = coupon_id
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid
        self.tag_keys_shrink = tag_keys_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.tag_keys_shrink is not None:
            result['TagKeys'] = self.tag_keys_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('TagKeys') is not None:
            self.tag_keys_shrink = m.get('TagKeys')
        return self


class DeleteCouponDeductTagResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCouponDeductTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCouponDeductTagResponseBody = None,
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
            temp_model = DeleteCouponDeductTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCouponRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class DescribeCouponRequest(TeaModel):
    def __init__(
        self,
        coupon_id: int = None,
        coupon_no: str = None,
        coupon_type: str = None,
        current_page: int = None,
        ec_id_account_ids: List[DescribeCouponRequestEcIdAccountIds] = None,
        effective_end_time: int = None,
        effective_start_time: int = None,
        expire_end_date: int = None,
        expire_start_date: int = None,
        nbid: str = None,
        page_size: int = None,
        status: str = None,
    ):
        self.coupon_id = coupon_id
        self.coupon_no = coupon_no
        self.coupon_type = coupon_type
        # This parameter is required.
        self.current_page = current_page
        self.ec_id_account_ids = ec_id_account_ids
        self.effective_end_time = effective_end_time
        self.effective_start_time = effective_start_time
        self.expire_end_date = expire_end_date
        self.expire_start_date = expire_start_date
        self.nbid = nbid
        # This parameter is required.
        self.page_size = page_size
        self.status = status

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.coupon_type is not None:
            result['CouponType'] = self.coupon_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        if self.expire_end_date is not None:
            result['ExpireEndDate'] = self.expire_end_date
        if self.expire_start_date is not None:
            result['ExpireStartDate'] = self.expire_start_date
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('CouponType') is not None:
            self.coupon_type = m.get('CouponType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = DescribeCouponRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        if m.get('ExpireEndDate') is not None:
            self.expire_end_date = m.get('ExpireEndDate')
        if m.get('ExpireStartDate') is not None:
            self.expire_start_date = m.get('ExpireStartDate')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCouponShrinkRequest(TeaModel):
    def __init__(
        self,
        coupon_id: int = None,
        coupon_no: str = None,
        coupon_type: str = None,
        current_page: int = None,
        ec_id_account_ids_shrink: str = None,
        effective_end_time: int = None,
        effective_start_time: int = None,
        expire_end_date: int = None,
        expire_start_date: int = None,
        nbid: str = None,
        page_size: int = None,
        status: str = None,
    ):
        self.coupon_id = coupon_id
        self.coupon_no = coupon_no
        self.coupon_type = coupon_type
        # This parameter is required.
        self.current_page = current_page
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.effective_end_time = effective_end_time
        self.effective_start_time = effective_start_time
        self.expire_end_date = expire_end_date
        self.expire_start_date = expire_start_date
        self.nbid = nbid
        # This parameter is required.
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.coupon_type is not None:
            result['CouponType'] = self.coupon_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        if self.expire_end_date is not None:
            result['ExpireEndDate'] = self.expire_end_date
        if self.expire_start_date is not None:
            result['ExpireStartDate'] = self.expire_start_date
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('CouponType') is not None:
            self.coupon_type = m.get('CouponType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        if m.get('ExpireEndDate') is not None:
            self.expire_end_date = m.get('ExpireEndDate')
        if m.get('ExpireStartDate') is not None:
            self.expire_start_date = m.get('ExpireStartDate')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCouponResponseBodyDataShareUidList(TeaModel):
    def __init__(
        self,
        uid: str = None,
        user_nick: str = None,
    ):
        self.uid = uid
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        return self


class DescribeCouponResponseBodyData(TeaModel):
    def __init__(
        self,
        amount: str = None,
        coupon_id: int = None,
        coupon_no: str = None,
        coupon_type: str = None,
        coupon_type_name: str = None,
        currency: str = None,
        end_time: str = None,
        gmt_create: str = None,
        item_names: List[str] = None,
        money_limit: str = None,
        order_time_rule: str = None,
        remain_amount: str = None,
        remark: str = None,
        share_uid_list: List[DescribeCouponResponseBodyDataShareUidList] = None,
        show_set_deduct_tag_button: bool = None,
        site: str = None,
        site_name: str = None,
        start_time: str = None,
        status: str = None,
        suit_account: str = None,
        suit_item_type: str = None,
        universal_type: str = None,
        yh_order_types: List[str] = None,
    ):
        self.amount = amount
        self.coupon_id = coupon_id
        self.coupon_no = coupon_no
        self.coupon_type = coupon_type
        self.coupon_type_name = coupon_type_name
        self.currency = currency
        self.end_time = end_time
        self.gmt_create = gmt_create
        self.item_names = item_names
        self.money_limit = money_limit
        self.order_time_rule = order_time_rule
        self.remain_amount = remain_amount
        self.remark = remark
        self.share_uid_list = share_uid_list
        self.show_set_deduct_tag_button = show_set_deduct_tag_button
        self.site = site
        self.site_name = site_name
        self.start_time = start_time
        self.status = status
        self.suit_account = suit_account
        self.suit_item_type = suit_item_type
        self.universal_type = universal_type
        self.yh_order_types = yh_order_types

    def validate(self):
        if self.share_uid_list:
            for k in self.share_uid_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.coupon_type is not None:
            result['CouponType'] = self.coupon_type
        if self.coupon_type_name is not None:
            result['CouponTypeName'] = self.coupon_type_name
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.item_names is not None:
            result['ItemNames'] = self.item_names
        if self.money_limit is not None:
            result['MoneyLimit'] = self.money_limit
        if self.order_time_rule is not None:
            result['OrderTimeRule'] = self.order_time_rule
        if self.remain_amount is not None:
            result['RemainAmount'] = self.remain_amount
        if self.remark is not None:
            result['Remark'] = self.remark
        result['ShareUidList'] = []
        if self.share_uid_list is not None:
            for k in self.share_uid_list:
                result['ShareUidList'].append(k.to_map() if k else None)
        if self.show_set_deduct_tag_button is not None:
            result['ShowSetDeductTagButton'] = self.show_set_deduct_tag_button
        if self.site is not None:
            result['Site'] = self.site
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.suit_account is not None:
            result['SuitAccount'] = self.suit_account
        if self.suit_item_type is not None:
            result['SuitItemType'] = self.suit_item_type
        if self.universal_type is not None:
            result['UniversalType'] = self.universal_type
        if self.yh_order_types is not None:
            result['YhOrderTypes'] = self.yh_order_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('CouponType') is not None:
            self.coupon_type = m.get('CouponType')
        if m.get('CouponTypeName') is not None:
            self.coupon_type_name = m.get('CouponTypeName')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ItemNames') is not None:
            self.item_names = m.get('ItemNames')
        if m.get('MoneyLimit') is not None:
            self.money_limit = m.get('MoneyLimit')
        if m.get('OrderTimeRule') is not None:
            self.order_time_rule = m.get('OrderTimeRule')
        if m.get('RemainAmount') is not None:
            self.remain_amount = m.get('RemainAmount')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        self.share_uid_list = []
        if m.get('ShareUidList') is not None:
            for k in m.get('ShareUidList'):
                temp_model = DescribeCouponResponseBodyDataShareUidList()
                self.share_uid_list.append(temp_model.from_map(k))
        if m.get('ShowSetDeductTagButton') is not None:
            self.show_set_deduct_tag_button = m.get('ShowSetDeductTagButton')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SuitAccount') is not None:
            self.suit_account = m.get('SuitAccount')
        if m.get('SuitItemType') is not None:
            self.suit_item_type = m.get('SuitItemType')
        if m.get('UniversalType') is not None:
            self.universal_type = m.get('UniversalType')
        if m.get('YhOrderTypes') is not None:
            self.yh_order_types = m.get('YhOrderTypes')
        return self


class DescribeCouponResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[DescribeCouponResponseBodyData] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeCouponResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCouponResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCouponResponseBody = None,
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
            temp_model = DescribeCouponResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCouponItemListRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class DescribeCouponItemListRequest(TeaModel):
    def __init__(
        self,
        coupon_id: int = None,
        current_page: int = None,
        ec_id_account_ids: List[DescribeCouponItemListRequestEcIdAccountIds] = None,
        name: str = None,
        nbid: str = None,
        page_size: int = None,
    ):
        self.coupon_id = coupon_id
        self.current_page = current_page
        self.ec_id_account_ids = ec_id_account_ids
        self.name = name
        self.nbid = nbid
        self.page_size = page_size

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = DescribeCouponItemListRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeCouponItemListShrinkRequest(TeaModel):
    def __init__(
        self,
        coupon_id: int = None,
        current_page: int = None,
        ec_id_account_ids_shrink: str = None,
        name: str = None,
        nbid: str = None,
        page_size: int = None,
    ):
        self.coupon_id = coupon_id
        self.current_page = current_page
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.name = name
        self.nbid = nbid
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeCouponItemListResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeCouponItemListResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[DescribeCouponItemListResponseBodyData] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeCouponItemListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCouponItemListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCouponItemListResponseBody = None,
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
            temp_model = DescribeCouponItemListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFundAccountAvailableAmountRequest(TeaModel):
    def __init__(
        self,
        fund_account_id: str = None,
    ):
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        return self


class GetFundAccountAvailableAmountResponseBodyExtendLedgerList(TeaModel):
    def __init__(
        self,
        currency: str = None,
        ledger_name: str = None,
        original_amount: str = None,
    ):
        self.currency = currency
        self.ledger_name = ledger_name
        self.original_amount = original_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.ledger_name is not None:
            result['LedgerName'] = self.ledger_name
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('LedgerName') is not None:
            self.ledger_name = m.get('LedgerName')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        return self


class GetFundAccountAvailableAmountResponseBodyOriginalCashAmountList(TeaModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
    ):
        self.amount = amount
        self.currency = currency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.currency is not None:
            result['Currency'] = self.currency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        return self


class GetFundAccountAvailableAmountResponseBody(TeaModel):
    def __init__(
        self,
        available_amount: str = None,
        available_credit_amount: str = None,
        bank_acceptance_amount: str = None,
        cash_amount: str = None,
        credit_amount: str = None,
        credit_refund_amount: str = None,
        credit_user: bool = None,
        currency: str = None,
        current_month_uncleared_amount: str = None,
        extend_ledger_list: List[GetFundAccountAvailableAmountResponseBodyExtendLedgerList] = None,
        fund_account_id: str = None,
        fund_account_owner_account_id: str = None,
        fund_account_status: str = None,
        fund_account_type: str = None,
        history_month_uncleared_amount: str = None,
        metadata: Any = None,
        negative_bill_amount: str = None,
        original_cash_amount_list: List[GetFundAccountAvailableAmountResponseBodyOriginalCashAmountList] = None,
        quota_amount: str = None,
        quota_consumed_amount: str = None,
        request_id: str = None,
        uncleared_amount: str = None,
    ):
        self.available_amount = available_amount
        self.available_credit_amount = available_credit_amount
        self.bank_acceptance_amount = bank_acceptance_amount
        self.cash_amount = cash_amount
        self.credit_amount = credit_amount
        self.credit_refund_amount = credit_refund_amount
        self.credit_user = credit_user
        self.currency = currency
        self.current_month_uncleared_amount = current_month_uncleared_amount
        self.extend_ledger_list = extend_ledger_list
        self.fund_account_id = fund_account_id
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.fund_account_status = fund_account_status
        self.fund_account_type = fund_account_type
        self.history_month_uncleared_amount = history_month_uncleared_amount
        self.metadata = metadata
        self.negative_bill_amount = negative_bill_amount
        self.original_cash_amount_list = original_cash_amount_list
        self.quota_amount = quota_amount
        self.quota_consumed_amount = quota_consumed_amount
        self.request_id = request_id
        self.uncleared_amount = uncleared_amount

    def validate(self):
        if self.extend_ledger_list:
            for k in self.extend_ledger_list:
                if k:
                    k.validate()
        if self.original_cash_amount_list:
            for k in self.original_cash_amount_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_amount is not None:
            result['AvailableAmount'] = self.available_amount
        if self.available_credit_amount is not None:
            result['AvailableCreditAmount'] = self.available_credit_amount
        if self.bank_acceptance_amount is not None:
            result['BankAcceptanceAmount'] = self.bank_acceptance_amount
        if self.cash_amount is not None:
            result['CashAmount'] = self.cash_amount
        if self.credit_amount is not None:
            result['CreditAmount'] = self.credit_amount
        if self.credit_refund_amount is not None:
            result['CreditRefundAmount'] = self.credit_refund_amount
        if self.credit_user is not None:
            result['CreditUser'] = self.credit_user
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.current_month_uncleared_amount is not None:
            result['CurrentMonthUnclearedAmount'] = self.current_month_uncleared_amount
        result['ExtendLedgerList'] = []
        if self.extend_ledger_list is not None:
            for k in self.extend_ledger_list:
                result['ExtendLedgerList'].append(k.to_map() if k else None)
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id
        if self.fund_account_status is not None:
            result['FundAccountStatus'] = self.fund_account_status
        if self.fund_account_type is not None:
            result['FundAccountType'] = self.fund_account_type
        if self.history_month_uncleared_amount is not None:
            result['HistoryMonthUnclearedAmount'] = self.history_month_uncleared_amount
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.negative_bill_amount is not None:
            result['NegativeBillAmount'] = self.negative_bill_amount
        result['OriginalCashAmountList'] = []
        if self.original_cash_amount_list is not None:
            for k in self.original_cash_amount_list:
                result['OriginalCashAmountList'].append(k.to_map() if k else None)
        if self.quota_amount is not None:
            result['QuotaAmount'] = self.quota_amount
        if self.quota_consumed_amount is not None:
            result['QuotaConsumedAmount'] = self.quota_consumed_amount
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uncleared_amount is not None:
            result['UnclearedAmount'] = self.uncleared_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAmount') is not None:
            self.available_amount = m.get('AvailableAmount')
        if m.get('AvailableCreditAmount') is not None:
            self.available_credit_amount = m.get('AvailableCreditAmount')
        if m.get('BankAcceptanceAmount') is not None:
            self.bank_acceptance_amount = m.get('BankAcceptanceAmount')
        if m.get('CashAmount') is not None:
            self.cash_amount = m.get('CashAmount')
        if m.get('CreditAmount') is not None:
            self.credit_amount = m.get('CreditAmount')
        if m.get('CreditRefundAmount') is not None:
            self.credit_refund_amount = m.get('CreditRefundAmount')
        if m.get('CreditUser') is not None:
            self.credit_user = m.get('CreditUser')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('CurrentMonthUnclearedAmount') is not None:
            self.current_month_uncleared_amount = m.get('CurrentMonthUnclearedAmount')
        self.extend_ledger_list = []
        if m.get('ExtendLedgerList') is not None:
            for k in m.get('ExtendLedgerList'):
                temp_model = GetFundAccountAvailableAmountResponseBodyExtendLedgerList()
                self.extend_ledger_list.append(temp_model.from_map(k))
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')
        if m.get('FundAccountStatus') is not None:
            self.fund_account_status = m.get('FundAccountStatus')
        if m.get('FundAccountType') is not None:
            self.fund_account_type = m.get('FundAccountType')
        if m.get('HistoryMonthUnclearedAmount') is not None:
            self.history_month_uncleared_amount = m.get('HistoryMonthUnclearedAmount')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('NegativeBillAmount') is not None:
            self.negative_bill_amount = m.get('NegativeBillAmount')
        self.original_cash_amount_list = []
        if m.get('OriginalCashAmountList') is not None:
            for k in m.get('OriginalCashAmountList'):
                temp_model = GetFundAccountAvailableAmountResponseBodyOriginalCashAmountList()
                self.original_cash_amount_list.append(temp_model.from_map(k))
        if m.get('QuotaAmount') is not None:
            self.quota_amount = m.get('QuotaAmount')
        if m.get('QuotaConsumedAmount') is not None:
            self.quota_consumed_amount = m.get('QuotaConsumedAmount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UnclearedAmount') is not None:
            self.uncleared_amount = m.get('UnclearedAmount')
        return self


class GetFundAccountAvailableAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFundAccountAvailableAmountResponseBody = None,
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
            temp_model = GetFundAccountAvailableAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFundAccountCanAllocateCreditAmountRequest(TeaModel):
    def __init__(
        self,
        fund_account_id: int = None,
    ):
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        return self


class GetFundAccountCanAllocateCreditAmountResponseBody(TeaModel):
    def __init__(
        self,
        ecid: str = None,
        ecid_allocated_credit_amount: str = None,
        ecid_credit_amount: str = None,
        fund_account_ecid: str = None,
        fund_account_id: int = None,
        fund_account_name: str = None,
        fund_account_owner_account_id: int = None,
        max_can_allocate_credit_amount: str = None,
        metadata: Any = None,
        min_can_allocate_credit_amount: str = None,
        nbid: str = None,
        request_id: str = None,
        site: str = None,
    ):
        self.ecid = ecid
        self.ecid_allocated_credit_amount = ecid_allocated_credit_amount
        self.ecid_credit_amount = ecid_credit_amount
        self.fund_account_ecid = fund_account_ecid
        self.fund_account_id = fund_account_id
        self.fund_account_name = fund_account_name
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.max_can_allocate_credit_amount = max_can_allocate_credit_amount
        self.metadata = metadata
        self.min_can_allocate_credit_amount = min_can_allocate_credit_amount
        self.nbid = nbid
        self.request_id = request_id
        self.site = site

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecid is not None:
            result['Ecid'] = self.ecid
        if self.ecid_allocated_credit_amount is not None:
            result['EcidAllocatedCreditAmount'] = self.ecid_allocated_credit_amount
        if self.ecid_credit_amount is not None:
            result['EcidCreditAmount'] = self.ecid_credit_amount
        if self.fund_account_ecid is not None:
            result['FundAccountEcid'] = self.fund_account_ecid
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.fund_account_name is not None:
            result['FundAccountName'] = self.fund_account_name
        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id
        if self.max_can_allocate_credit_amount is not None:
            result['MaxCanAllocateCreditAmount'] = self.max_can_allocate_credit_amount
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.min_can_allocate_credit_amount is not None:
            result['MinCanAllocateCreditAmount'] = self.min_can_allocate_credit_amount
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site is not None:
            result['Site'] = self.site
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ecid') is not None:
            self.ecid = m.get('Ecid')
        if m.get('EcidAllocatedCreditAmount') is not None:
            self.ecid_allocated_credit_amount = m.get('EcidAllocatedCreditAmount')
        if m.get('EcidCreditAmount') is not None:
            self.ecid_credit_amount = m.get('EcidCreditAmount')
        if m.get('FundAccountEcid') is not None:
            self.fund_account_ecid = m.get('FundAccountEcid')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('FundAccountName') is not None:
            self.fund_account_name = m.get('FundAccountName')
        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')
        if m.get('MaxCanAllocateCreditAmount') is not None:
            self.max_can_allocate_credit_amount = m.get('MaxCanAllocateCreditAmount')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('MinCanAllocateCreditAmount') is not None:
            self.min_can_allocate_credit_amount = m.get('MinCanAllocateCreditAmount')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        return self


class GetFundAccountCanAllocateCreditAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFundAccountCanAllocateCreditAmountResponseBody = None,
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
            temp_model = GetFundAccountCanAllocateCreditAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFundAccountCanRecycleAmountRequest(TeaModel):
    def __init__(
        self,
        currency: str = None,
        recycle_from_fund_account_id: str = None,
    ):
        # This parameter is required.
        self.currency = currency
        self.recycle_from_fund_account_id = recycle_from_fund_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.recycle_from_fund_account_id is not None:
            result['RecycleFromFundAccountId'] = self.recycle_from_fund_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('RecycleFromFundAccountId') is not None:
            self.recycle_from_fund_account_id = m.get('RecycleFromFundAccountId')
        return self


class GetFundAccountCanRecycleAmountResponseBodyRecycleToFundAccountList(TeaModel):
    def __init__(
        self,
        fund_account_id: str = None,
        fund_account_name: str = None,
        fund_account_owner_account_id: str = None,
        max_recyclable_amount: str = None,
        original_transfer_remain_amount: str = None,
    ):
        self.fund_account_id = fund_account_id
        self.fund_account_name = fund_account_name
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.max_recyclable_amount = max_recyclable_amount
        self.original_transfer_remain_amount = original_transfer_remain_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.fund_account_name is not None:
            result['FundAccountName'] = self.fund_account_name
        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id
        if self.max_recyclable_amount is not None:
            result['MaxRecyclableAmount'] = self.max_recyclable_amount
        if self.original_transfer_remain_amount is not None:
            result['OriginalTransferRemainAmount'] = self.original_transfer_remain_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('FundAccountName') is not None:
            self.fund_account_name = m.get('FundAccountName')
        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')
        if m.get('MaxRecyclableAmount') is not None:
            self.max_recyclable_amount = m.get('MaxRecyclableAmount')
        if m.get('OriginalTransferRemainAmount') is not None:
            self.original_transfer_remain_amount = m.get('OriginalTransferRemainAmount')
        return self


class GetFundAccountCanRecycleAmountResponseBody(TeaModel):
    def __init__(
        self,
        available_amount: str = None,
        currency: str = None,
        metadata: Any = None,
        recycle_from_fund_account_id: str = None,
        recycle_to_fund_account_list: List[GetFundAccountCanRecycleAmountResponseBodyRecycleToFundAccountList] = None,
        request_id: str = None,
        transfer_amount: str = None,
    ):
        self.available_amount = available_amount
        self.currency = currency
        self.metadata = metadata
        self.recycle_from_fund_account_id = recycle_from_fund_account_id
        self.recycle_to_fund_account_list = recycle_to_fund_account_list
        self.request_id = request_id
        self.transfer_amount = transfer_amount

    def validate(self):
        if self.recycle_to_fund_account_list:
            for k in self.recycle_to_fund_account_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_amount is not None:
            result['AvailableAmount'] = self.available_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.recycle_from_fund_account_id is not None:
            result['RecycleFromFundAccountId'] = self.recycle_from_fund_account_id
        result['RecycleToFundAccountList'] = []
        if self.recycle_to_fund_account_list is not None:
            for k in self.recycle_to_fund_account_list:
                result['RecycleToFundAccountList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transfer_amount is not None:
            result['TransferAmount'] = self.transfer_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAmount') is not None:
            self.available_amount = m.get('AvailableAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RecycleFromFundAccountId') is not None:
            self.recycle_from_fund_account_id = m.get('RecycleFromFundAccountId')
        self.recycle_to_fund_account_list = []
        if m.get('RecycleToFundAccountList') is not None:
            for k in m.get('RecycleToFundAccountList'):
                temp_model = GetFundAccountCanRecycleAmountResponseBodyRecycleToFundAccountList()
                self.recycle_to_fund_account_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransferAmount') is not None:
            self.transfer_amount = m.get('TransferAmount')
        return self


class GetFundAccountCanRecycleAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFundAccountCanRecycleAmountResponseBody = None,
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
            temp_model = GetFundAccountCanRecycleAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFundAccountCanTransferAmountRequest(TeaModel):
    def __init__(
        self,
        currency: str = None,
        fund_account_id: str = None,
    ):
        # This parameter is required.
        self.currency = currency
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        return self


class GetFundAccountCanTransferAmountResponseBody(TeaModel):
    def __init__(
        self,
        available_amount: str = None,
        cash_amount: str = None,
        currency: str = None,
        fund_account_ecid: str = None,
        fund_account_id: int = None,
        fund_account_name: str = None,
        fund_account_owner_account_id: int = None,
        max_transferable_amount: str = None,
        metadata: Any = None,
        nbid: str = None,
        request_id: str = None,
        site: str = None,
        transfer_amount: str = None,
    ):
        self.available_amount = available_amount
        self.cash_amount = cash_amount
        self.currency = currency
        self.fund_account_ecid = fund_account_ecid
        self.fund_account_id = fund_account_id
        self.fund_account_name = fund_account_name
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.max_transferable_amount = max_transferable_amount
        self.metadata = metadata
        self.nbid = nbid
        self.request_id = request_id
        self.site = site
        self.transfer_amount = transfer_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_amount is not None:
            result['AvailableAmount'] = self.available_amount
        if self.cash_amount is not None:
            result['CashAmount'] = self.cash_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.fund_account_ecid is not None:
            result['FundAccountEcid'] = self.fund_account_ecid
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.fund_account_name is not None:
            result['FundAccountName'] = self.fund_account_name
        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id
        if self.max_transferable_amount is not None:
            result['MaxTransferableAmount'] = self.max_transferable_amount
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site is not None:
            result['Site'] = self.site
        if self.transfer_amount is not None:
            result['TransferAmount'] = self.transfer_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAmount') is not None:
            self.available_amount = m.get('AvailableAmount')
        if m.get('CashAmount') is not None:
            self.cash_amount = m.get('CashAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('FundAccountEcid') is not None:
            self.fund_account_ecid = m.get('FundAccountEcid')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('FundAccountName') is not None:
            self.fund_account_name = m.get('FundAccountName')
        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')
        if m.get('MaxTransferableAmount') is not None:
            self.max_transferable_amount = m.get('MaxTransferableAmount')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('TransferAmount') is not None:
            self.transfer_amount = m.get('TransferAmount')
        return self


class GetFundAccountCanTransferAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFundAccountCanTransferAmountResponseBody = None,
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
            temp_model = GetFundAccountCanTransferAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFundAccountCanWithdrawAmountRequest(TeaModel):
    def __init__(
        self,
        fund_account_id: int = None,
    ):
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        return self


class GetFundAccountCanWithdrawAmountResponseBody(TeaModel):
    def __init__(
        self,
        can_original_withdraw_amount: str = None,
        can_withdraw_amount: str = None,
        cannot_original_withdraw_amount: str = None,
        cash_amount: str = None,
        credit_memo_amount: str = None,
        current_month_uncleared_amount: str = None,
        history_month_uncleared_amount: str = None,
        metadata: Any = None,
        pay_as_you_go_reversed_amount: str = None,
        request_id: str = None,
        transfer_amount: str = None,
    ):
        self.can_original_withdraw_amount = can_original_withdraw_amount
        self.can_withdraw_amount = can_withdraw_amount
        self.cannot_original_withdraw_amount = cannot_original_withdraw_amount
        self.cash_amount = cash_amount
        self.credit_memo_amount = credit_memo_amount
        self.current_month_uncleared_amount = current_month_uncleared_amount
        self.history_month_uncleared_amount = history_month_uncleared_amount
        self.metadata = metadata
        self.pay_as_you_go_reversed_amount = pay_as_you_go_reversed_amount
        self.request_id = request_id
        self.transfer_amount = transfer_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_original_withdraw_amount is not None:
            result['CanOriginalWithdrawAmount'] = self.can_original_withdraw_amount
        if self.can_withdraw_amount is not None:
            result['CanWithdrawAmount'] = self.can_withdraw_amount
        if self.cannot_original_withdraw_amount is not None:
            result['CannotOriginalWithdrawAmount'] = self.cannot_original_withdraw_amount
        if self.cash_amount is not None:
            result['CashAmount'] = self.cash_amount
        if self.credit_memo_amount is not None:
            result['CreditMemoAmount'] = self.credit_memo_amount
        if self.current_month_uncleared_amount is not None:
            result['CurrentMonthUnclearedAmount'] = self.current_month_uncleared_amount
        if self.history_month_uncleared_amount is not None:
            result['HistoryMonthUnclearedAmount'] = self.history_month_uncleared_amount
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.pay_as_you_go_reversed_amount is not None:
            result['PayAsYouGoReversedAmount'] = self.pay_as_you_go_reversed_amount
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transfer_amount is not None:
            result['TransferAmount'] = self.transfer_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanOriginalWithdrawAmount') is not None:
            self.can_original_withdraw_amount = m.get('CanOriginalWithdrawAmount')
        if m.get('CanWithdrawAmount') is not None:
            self.can_withdraw_amount = m.get('CanWithdrawAmount')
        if m.get('CannotOriginalWithdrawAmount') is not None:
            self.cannot_original_withdraw_amount = m.get('CannotOriginalWithdrawAmount')
        if m.get('CashAmount') is not None:
            self.cash_amount = m.get('CashAmount')
        if m.get('CreditMemoAmount') is not None:
            self.credit_memo_amount = m.get('CreditMemoAmount')
        if m.get('CurrentMonthUnclearedAmount') is not None:
            self.current_month_uncleared_amount = m.get('CurrentMonthUnclearedAmount')
        if m.get('HistoryMonthUnclearedAmount') is not None:
            self.history_month_uncleared_amount = m.get('HistoryMonthUnclearedAmount')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('PayAsYouGoReversedAmount') is not None:
            self.pay_as_you_go_reversed_amount = m.get('PayAsYouGoReversedAmount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransferAmount') is not None:
            self.transfer_amount = m.get('TransferAmount')
        return self


class GetFundAccountCanWithdrawAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFundAccountCanWithdrawAmountResponseBody = None,
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
            temp_model = GetFundAccountCanWithdrawAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFundAccountLowAvailableAmountAlarmRequest(TeaModel):
    def __init__(
        self,
        fund_account_id: int = None,
    ):
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        return self


class GetFundAccountLowAvailableAmountAlarmResponseBody(TeaModel):
    def __init__(
        self,
        alarm_enabled: bool = None,
        metadata: Any = None,
        request_id: str = None,
        threshold_amount: str = None,
    ):
        self.alarm_enabled = alarm_enabled
        self.metadata = metadata
        self.request_id = request_id
        self.threshold_amount = threshold_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_enabled is not None:
            result['AlarmEnabled'] = self.alarm_enabled
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.threshold_amount is not None:
            result['ThresholdAmount'] = self.threshold_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmEnabled') is not None:
            self.alarm_enabled = m.get('AlarmEnabled')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ThresholdAmount') is not None:
            self.threshold_amount = m.get('ThresholdAmount')
        return self


class GetFundAccountLowAvailableAmountAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFundAccountLowAvailableAmountAlarmResponseBody = None,
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
            temp_model = GetFundAccountLowAvailableAmountAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFundAccountTransactionDetailsRequest(TeaModel):
    def __init__(
        self,
        bill_number: str = None,
        channel_transaction_number: str = None,
        current_page: int = None,
        end_time: int = None,
        fund_account_id: int = None,
        page_size: int = None,
        start_time: int = None,
        transaction_channel_list: List[str] = None,
        transaction_direction: str = None,
        transaction_number: int = None,
        transaction_type: str = None,
        transaction_type_list: List[str] = None,
    ):
        self.bill_number = bill_number
        self.channel_transaction_number = channel_transaction_number
        self.current_page = current_page
        self.end_time = end_time
        self.fund_account_id = fund_account_id
        self.page_size = page_size
        self.start_time = start_time
        self.transaction_channel_list = transaction_channel_list
        self.transaction_direction = transaction_direction
        self.transaction_number = transaction_number
        self.transaction_type = transaction_type
        self.transaction_type_list = transaction_type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_number is not None:
            result['BillNumber'] = self.bill_number
        if self.channel_transaction_number is not None:
            result['ChannelTransactionNumber'] = self.channel_transaction_number
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.transaction_channel_list is not None:
            result['TransactionChannelList'] = self.transaction_channel_list
        if self.transaction_direction is not None:
            result['TransactionDirection'] = self.transaction_direction
        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number
        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type
        if self.transaction_type_list is not None:
            result['TransactionTypeList'] = self.transaction_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillNumber') is not None:
            self.bill_number = m.get('BillNumber')
        if m.get('ChannelTransactionNumber') is not None:
            self.channel_transaction_number = m.get('ChannelTransactionNumber')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TransactionChannelList') is not None:
            self.transaction_channel_list = m.get('TransactionChannelList')
        if m.get('TransactionDirection') is not None:
            self.transaction_direction = m.get('TransactionDirection')
        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')
        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')
        if m.get('TransactionTypeList') is not None:
            self.transaction_type_list = m.get('TransactionTypeList')
        return self


class GetFundAccountTransactionDetailsShrinkRequest(TeaModel):
    def __init__(
        self,
        bill_number: str = None,
        channel_transaction_number: str = None,
        current_page: int = None,
        end_time: int = None,
        fund_account_id: int = None,
        page_size: int = None,
        start_time: int = None,
        transaction_channel_list_shrink: str = None,
        transaction_direction: str = None,
        transaction_number: int = None,
        transaction_type: str = None,
        transaction_type_list_shrink: str = None,
    ):
        self.bill_number = bill_number
        self.channel_transaction_number = channel_transaction_number
        self.current_page = current_page
        self.end_time = end_time
        self.fund_account_id = fund_account_id
        self.page_size = page_size
        self.start_time = start_time
        self.transaction_channel_list_shrink = transaction_channel_list_shrink
        self.transaction_direction = transaction_direction
        self.transaction_number = transaction_number
        self.transaction_type = transaction_type
        self.transaction_type_list_shrink = transaction_type_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_number is not None:
            result['BillNumber'] = self.bill_number
        if self.channel_transaction_number is not None:
            result['ChannelTransactionNumber'] = self.channel_transaction_number
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.transaction_channel_list_shrink is not None:
            result['TransactionChannelList'] = self.transaction_channel_list_shrink
        if self.transaction_direction is not None:
            result['TransactionDirection'] = self.transaction_direction
        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number
        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type
        if self.transaction_type_list_shrink is not None:
            result['TransactionTypeList'] = self.transaction_type_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillNumber') is not None:
            self.bill_number = m.get('BillNumber')
        if m.get('ChannelTransactionNumber') is not None:
            self.channel_transaction_number = m.get('ChannelTransactionNumber')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TransactionChannelList') is not None:
            self.transaction_channel_list_shrink = m.get('TransactionChannelList')
        if m.get('TransactionDirection') is not None:
            self.transaction_direction = m.get('TransactionDirection')
        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')
        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')
        if m.get('TransactionTypeList') is not None:
            self.transaction_type_list_shrink = m.get('TransactionTypeList')
        return self


class GetFundAccountTransactionDetailsResponseBodyData(TeaModel):
    def __init__(
        self,
        balance: str = None,
        bill_number: str = None,
        channel_transaction_number: str = None,
        currency: str = None,
        fund_account_ecid: str = None,
        fund_account_id: int = None,
        fund_account_name: str = None,
        fund_account_owner_account_id: int = None,
        fund_type: str = None,
        nbid: str = None,
        remark: str = None,
        site: str = None,
        transaction_account: str = None,
        transaction_amount: str = None,
        transaction_channel: str = None,
        transaction_direction: str = None,
        transaction_number: int = None,
        transaction_time: str = None,
        transaction_type: str = None,
    ):
        self.balance = balance
        self.bill_number = bill_number
        self.channel_transaction_number = channel_transaction_number
        self.currency = currency
        self.fund_account_ecid = fund_account_ecid
        self.fund_account_id = fund_account_id
        self.fund_account_name = fund_account_name
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.fund_type = fund_type
        self.nbid = nbid
        self.remark = remark
        self.site = site
        self.transaction_account = transaction_account
        self.transaction_amount = transaction_amount
        self.transaction_channel = transaction_channel
        self.transaction_direction = transaction_direction
        self.transaction_number = transaction_number
        self.transaction_time = transaction_time
        self.transaction_type = transaction_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.bill_number is not None:
            result['BillNumber'] = self.bill_number
        if self.channel_transaction_number is not None:
            result['ChannelTransactionNumber'] = self.channel_transaction_number
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.fund_account_ecid is not None:
            result['FundAccountEcid'] = self.fund_account_ecid
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.fund_account_name is not None:
            result['FundAccountName'] = self.fund_account_name
        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.site is not None:
            result['Site'] = self.site
        if self.transaction_account is not None:
            result['TransactionAccount'] = self.transaction_account
        if self.transaction_amount is not None:
            result['TransactionAmount'] = self.transaction_amount
        if self.transaction_channel is not None:
            result['TransactionChannel'] = self.transaction_channel
        if self.transaction_direction is not None:
            result['TransactionDirection'] = self.transaction_direction
        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number
        if self.transaction_time is not None:
            result['TransactionTime'] = self.transaction_time
        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('BillNumber') is not None:
            self.bill_number = m.get('BillNumber')
        if m.get('ChannelTransactionNumber') is not None:
            self.channel_transaction_number = m.get('ChannelTransactionNumber')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('FundAccountEcid') is not None:
            self.fund_account_ecid = m.get('FundAccountEcid')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('FundAccountName') is not None:
            self.fund_account_name = m.get('FundAccountName')
        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('TransactionAccount') is not None:
            self.transaction_account = m.get('TransactionAccount')
        if m.get('TransactionAmount') is not None:
            self.transaction_amount = m.get('TransactionAmount')
        if m.get('TransactionChannel') is not None:
            self.transaction_channel = m.get('TransactionChannel')
        if m.get('TransactionDirection') is not None:
            self.transaction_direction = m.get('TransactionDirection')
        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')
        if m.get('TransactionTime') is not None:
            self.transaction_time = m.get('TransactionTime')
        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')
        return self


class GetFundAccountTransactionDetailsResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[GetFundAccountTransactionDetailsResponseBodyData] = None,
        metadata: Any = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.metadata = metadata
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetFundAccountTransactionDetailsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetFundAccountTransactionDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFundAccountTransactionDetailsResponseBody = None,
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
            temp_model = GetFundAccountTransactionDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCouponDeductTagRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class ListCouponDeductTagRequest(TeaModel):
    def __init__(
        self,
        coupon_id: str = None,
        ec_id_account_ids: List[ListCouponDeductTagRequestEcIdAccountIds] = None,
        nbid: str = None,
    ):
        self.coupon_id = coupon_id
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = ListCouponDeductTagRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class ListCouponDeductTagShrinkRequest(TeaModel):
    def __init__(
        self,
        coupon_id: str = None,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
    ):
        self.coupon_id = coupon_id
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class ListCouponDeductTagResponseBodyData(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListCouponDeductTagResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListCouponDeductTagResponseBodyData] = None,
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
                temp_model = ListCouponDeductTagResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCouponDeductTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCouponDeductTagResponseBody = None,
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
            temp_model = ListCouponDeductTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFundAccountRequest(TeaModel):
    def __init__(
        self,
        nbid: str = None,
        query_only_in_use: bool = None,
        query_only_manage: bool = None,
    ):
        self.nbid = nbid
        self.query_only_in_use = query_only_in_use
        self.query_only_manage = query_only_manage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.query_only_in_use is not None:
            result['QueryOnlyInUse'] = self.query_only_in_use
        if self.query_only_manage is not None:
            result['QueryOnlyManage'] = self.query_only_manage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('QueryOnlyInUse') is not None:
            self.query_only_in_use = m.get('QueryOnlyInUse')
        if m.get('QueryOnlyManage') is not None:
            self.query_only_manage = m.get('QueryOnlyManage')
        return self


class ListFundAccountResponseBodyData(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        fund_account_admin_account_id: str = None,
        fund_account_admin_account_name: str = None,
        fund_account_id: str = None,
        fund_account_name: str = None,
        fund_account_owner_account_id: str = None,
        fund_account_status: str = None,
        fund_account_type: str = None,
        nbid: str = None,
        permissions: List[str] = None,
        site: str = None,
    ):
        self.create_date = create_date
        self.fund_account_admin_account_id = fund_account_admin_account_id
        self.fund_account_admin_account_name = fund_account_admin_account_name
        self.fund_account_id = fund_account_id
        self.fund_account_name = fund_account_name
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.fund_account_status = fund_account_status
        self.fund_account_type = fund_account_type
        self.nbid = nbid
        self.permissions = permissions
        self.site = site

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.fund_account_admin_account_id is not None:
            result['FundAccountAdminAccountId'] = self.fund_account_admin_account_id
        if self.fund_account_admin_account_name is not None:
            result['FundAccountAdminAccountName'] = self.fund_account_admin_account_name
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.fund_account_name is not None:
            result['FundAccountName'] = self.fund_account_name
        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id
        if self.fund_account_status is not None:
            result['FundAccountStatus'] = self.fund_account_status
        if self.fund_account_type is not None:
            result['FundAccountType'] = self.fund_account_type
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.permissions is not None:
            result['Permissions'] = self.permissions
        if self.site is not None:
            result['Site'] = self.site
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('FundAccountAdminAccountId') is not None:
            self.fund_account_admin_account_id = m.get('FundAccountAdminAccountId')
        if m.get('FundAccountAdminAccountName') is not None:
            self.fund_account_admin_account_name = m.get('FundAccountAdminAccountName')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('FundAccountName') is not None:
            self.fund_account_name = m.get('FundAccountName')
        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')
        if m.get('FundAccountStatus') is not None:
            self.fund_account_status = m.get('FundAccountStatus')
        if m.get('FundAccountType') is not None:
            self.fund_account_type = m.get('FundAccountType')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        return self


class ListFundAccountResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListFundAccountResponseBodyData] = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.data = data
        self.metadata = metadata
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
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListFundAccountResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFundAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFundAccountResponseBody = None,
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
            temp_model = ListFundAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFundAccountPayRelationRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        fund_account_id: str = None,
        nbid: str = None,
        page_size: int = None,
        status: str = None,
    ):
        self.current_page = current_page
        # This parameter is required.
        self.fund_account_id = fund_account_id
        self.nbid = nbid
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFundAccountPayRelationResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        ecid: str = None,
        effective_time: str = None,
        fund_account_id: str = None,
        fund_account_owner_account_id: str = None,
        ineffective_time: str = None,
        nbid: str = None,
        operator_name: str = None,
        operator_no: str = None,
        operator_type: str = None,
        relation_type: str = None,
        site: str = None,
        status: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.ecid = ecid
        self.effective_time = effective_time
        self.fund_account_id = fund_account_id
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.ineffective_time = ineffective_time
        self.nbid = nbid
        self.operator_name = operator_name
        self.operator_no = operator_no
        self.operator_type = operator_type
        self.relation_type = relation_type
        self.site = site
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.ecid is not None:
            result['Ecid'] = self.ecid
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id
        if self.ineffective_time is not None:
            result['IneffectiveTime'] = self.ineffective_time
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.operator_no is not None:
            result['OperatorNo'] = self.operator_no
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.relation_type is not None:
            result['RelationType'] = self.relation_type
        if self.site is not None:
            result['Site'] = self.site
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Ecid') is not None:
            self.ecid = m.get('Ecid')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')
        if m.get('IneffectiveTime') is not None:
            self.ineffective_time = m.get('IneffectiveTime')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('OperatorNo') is not None:
            self.operator_no = m.get('OperatorNo')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFundAccountPayRelationResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[ListFundAccountPayRelationResponseBodyData] = None,
        metadata: Any = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.metadata = metadata
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListFundAccountPayRelationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFundAccountPayRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFundAccountPayRelationResponseBody = None,
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
            temp_model = ListFundAccountPayRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetFundAccountCreditAmountRequest(TeaModel):
    def __init__(
        self,
        credit_amount: str = None,
        currency: str = None,
        fund_account_id: int = None,
    ):
        # This parameter is required.
        self.credit_amount = credit_amount
        # This parameter is required.
        self.currency = currency
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credit_amount is not None:
            result['CreditAmount'] = self.credit_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditAmount') is not None:
            self.credit_amount = m.get('CreditAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        return self


class SetFundAccountCreditAmountResponseBody(TeaModel):
    def __init__(
        self,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetFundAccountCreditAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetFundAccountCreditAmountResponseBody = None,
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
            temp_model = SetFundAccountCreditAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetFundAccountLowAvailableAmountAlarmRequest(TeaModel):
    def __init__(
        self,
        fund_account_id: int = None,
        threshold_amount: str = None,
    ):
        self.fund_account_id = fund_account_id
        self.threshold_amount = threshold_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.threshold_amount is not None:
            result['ThresholdAmount'] = self.threshold_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('ThresholdAmount') is not None:
            self.threshold_amount = m.get('ThresholdAmount')
        return self


class SetFundAccountLowAvailableAmountAlarmResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.data = data
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetFundAccountLowAvailableAmountAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetFundAccountLowAvailableAmountAlarmResponseBody = None,
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
            temp_model = SetFundAccountLowAvailableAmountAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSavingPlanUserDeductRuleRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class SetSavingPlanUserDeductRuleRequestUserDeductRules(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        module_code: str = None,
        skip_deduct: bool = None,
    ):
        self.commodity_code = commodity_code
        self.module_code = module_code
        self.skip_deduct = skip_deduct

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.skip_deduct is not None:
            result['SkipDeduct'] = self.skip_deduct
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('SkipDeduct') is not None:
            self.skip_deduct = m.get('SkipDeduct')
        return self


class SetSavingPlanUserDeductRuleRequest(TeaModel):
    def __init__(
        self,
        ec_id_account_ids: List[SetSavingPlanUserDeductRuleRequestEcIdAccountIds] = None,
        nbid: str = None,
        spn_instance_code: str = None,
        user_deduct_rules: List[SetSavingPlanUserDeductRuleRequestUserDeductRules] = None,
    ):
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid
        self.spn_instance_code = spn_instance_code
        self.user_deduct_rules = user_deduct_rules

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()
        if self.user_deduct_rules:
            for k in self.user_deduct_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.spn_instance_code is not None:
            result['SpnInstanceCode'] = self.spn_instance_code
        result['UserDeductRules'] = []
        if self.user_deduct_rules is not None:
            for k in self.user_deduct_rules:
                result['UserDeductRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = SetSavingPlanUserDeductRuleRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('SpnInstanceCode') is not None:
            self.spn_instance_code = m.get('SpnInstanceCode')
        self.user_deduct_rules = []
        if m.get('UserDeductRules') is not None:
            for k in m.get('UserDeductRules'):
                temp_model = SetSavingPlanUserDeductRuleRequestUserDeductRules()
                self.user_deduct_rules.append(temp_model.from_map(k))
        return self


class SetSavingPlanUserDeductRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
        spn_instance_code: str = None,
        user_deduct_rules_shrink: str = None,
    ):
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid
        self.spn_instance_code = spn_instance_code
        self.user_deduct_rules_shrink = user_deduct_rules_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.spn_instance_code is not None:
            result['SpnInstanceCode'] = self.spn_instance_code
        if self.user_deduct_rules_shrink is not None:
            result['UserDeductRules'] = self.user_deduct_rules_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('SpnInstanceCode') is not None:
            self.spn_instance_code = m.get('SpnInstanceCode')
        if m.get('UserDeductRules') is not None:
            self.user_deduct_rules_shrink = m.get('UserDeductRules')
        return self


class SetSavingPlanUserDeductRuleResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetSavingPlanUserDeductRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetSavingPlanUserDeductRuleResponseBody = None,
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
            temp_model = SetSavingPlanUserDeductRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


