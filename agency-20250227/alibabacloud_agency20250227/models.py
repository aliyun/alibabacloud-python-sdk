# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class GetBillDetailFileListRequest(TeaModel):
    def __init__(
        self,
        bill_month: str = None,
        oss_access_key_id: str = None,
        oss_access_key_secret: str = None,
        oss_bucket_name: str = None,
        oss_endpoint: str = None,
        oss_region: str = None,
        oss_security_token: str = None,
    ):
        # This parameter is required.
        self.bill_month = bill_month
        self.oss_access_key_id = oss_access_key_id
        self.oss_access_key_secret = oss_access_key_secret
        self.oss_bucket_name = oss_bucket_name
        self.oss_endpoint = oss_endpoint
        self.oss_region = oss_region
        self.oss_security_token = oss_security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_month is not None:
            result['BillMonth'] = self.bill_month
        if self.oss_access_key_id is not None:
            result['OssAccessKeyId'] = self.oss_access_key_id
        if self.oss_access_key_secret is not None:
            result['OssAccessKeySecret'] = self.oss_access_key_secret
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_region is not None:
            result['OssRegion'] = self.oss_region
        if self.oss_security_token is not None:
            result['OssSecurityToken'] = self.oss_security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillMonth') is not None:
            self.bill_month = m.get('BillMonth')
        if m.get('OssAccessKeyId') is not None:
            self.oss_access_key_id = m.get('OssAccessKeyId')
        if m.get('OssAccessKeySecret') is not None:
            self.oss_access_key_secret = m.get('OssAccessKeySecret')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssRegion') is not None:
            self.oss_region = m.get('OssRegion')
        if m.get('OssSecurityToken') is not None:
            self.oss_security_token = m.get('OssSecurityToken')
        return self


class GetBillDetailFileListResponseBodyData(TeaModel):
    def __init__(
        self,
        bill_month: str = None,
        file_name: str = None,
        file_url: str = None,
        status: str = None,
        type: str = None,
    ):
        self.bill_month = bill_month
        self.file_name = file_name
        self.file_url = file_url
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_month is not None:
            result['BillMonth'] = self.bill_month
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillMonth') is not None:
            self.bill_month = m.get('BillMonth')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetBillDetailFileListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetBillDetailFileListResponseBodyData] = None,
        message: str = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.msg = msg
        # Id of the request
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetBillDetailFileListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetBillDetailFileListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBillDetailFileListResponseBody = None,
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
            temp_model = GetBillDetailFileListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCommissionDetailFileListRequest(TeaModel):
    def __init__(
        self,
        bill_month: str = None,
        oss_access_key_id: str = None,
        oss_access_key_secret: str = None,
        oss_bucket_name: str = None,
        oss_endpoint: str = None,
        oss_region: str = None,
        oss_security_token: str = None,
    ):
        self.bill_month = bill_month
        self.oss_access_key_id = oss_access_key_id
        self.oss_access_key_secret = oss_access_key_secret
        self.oss_bucket_name = oss_bucket_name
        self.oss_endpoint = oss_endpoint
        self.oss_region = oss_region
        self.oss_security_token = oss_security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_month is not None:
            result['BillMonth'] = self.bill_month
        if self.oss_access_key_id is not None:
            result['OssAccessKeyId'] = self.oss_access_key_id
        if self.oss_access_key_secret is not None:
            result['OssAccessKeySecret'] = self.oss_access_key_secret
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_region is not None:
            result['OssRegion'] = self.oss_region
        if self.oss_security_token is not None:
            result['OssSecurityToken'] = self.oss_security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillMonth') is not None:
            self.bill_month = m.get('BillMonth')
        if m.get('OssAccessKeyId') is not None:
            self.oss_access_key_id = m.get('OssAccessKeyId')
        if m.get('OssAccessKeySecret') is not None:
            self.oss_access_key_secret = m.get('OssAccessKeySecret')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssRegion') is not None:
            self.oss_region = m.get('OssRegion')
        if m.get('OssSecurityToken') is not None:
            self.oss_security_token = m.get('OssSecurityToken')
        return self


class GetCommissionDetailFileListResponseBodyDataFileList(TeaModel):
    def __init__(
        self,
        bucket_sync_status: str = None,
        commission_policy_name: str = None,
        file_name: str = None,
        file_type: str = None,
        file_url: str = None,
    ):
        self.bucket_sync_status = bucket_sync_status
        self.commission_policy_name = commission_policy_name
        self.file_name = file_name
        self.file_type = file_type
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_sync_status is not None:
            result['BucketSyncStatus'] = self.bucket_sync_status
        if self.commission_policy_name is not None:
            result['CommissionPolicyName'] = self.commission_policy_name
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketSyncStatus') is not None:
            self.bucket_sync_status = m.get('BucketSyncStatus')
        if m.get('CommissionPolicyName') is not None:
            self.commission_policy_name = m.get('CommissionPolicyName')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class GetCommissionDetailFileListResponseBodyData(TeaModel):
    def __init__(
        self,
        bill_month: str = None,
        file_list: List[GetCommissionDetailFileListResponseBodyDataFileList] = None,
        partner_uid: str = None,
    ):
        self.bill_month = bill_month
        self.file_list = file_list
        self.partner_uid = partner_uid

    def validate(self):
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_month is not None:
            result['BillMonth'] = self.bill_month
        result['FileList'] = []
        if self.file_list is not None:
            for k in self.file_list:
                result['FileList'].append(k.to_map() if k else None)
        if self.partner_uid is not None:
            result['PartnerUid'] = self.partner_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillMonth') is not None:
            self.bill_month = m.get('BillMonth')
        self.file_list = []
        if m.get('FileList') is not None:
            for k in m.get('FileList'):
                temp_model = GetCommissionDetailFileListResponseBodyDataFileList()
                self.file_list.append(temp_model.from_map(k))
        if m.get('PartnerUid') is not None:
            self.partner_uid = m.get('PartnerUid')
        return self


class GetCommissionDetailFileListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetCommissionDetailFileListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetCommissionDetailFileListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCommissionDetailFileListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCommissionDetailFileListResponseBody = None,
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
            temp_model = GetCommissionDetailFileListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomerOrderListRequest(TeaModel):
    def __init__(
        self,
        customer_account: str = None,
        customer_uid: int = None,
        order_create_after: int = None,
        order_create_before: int = None,
        order_id: int = None,
        order_pay_after: int = None,
        order_pay_before: int = None,
        order_status: int = None,
        order_type_list: List[str] = None,
        page_no: int = None,
        page_size: int = None,
        pay_amount_after: float = None,
        pay_amount_before: float = None,
        pay_type: int = None,
        product_code: str = None,
        product_name: str = None,
        project_id: int = None,
        ram_account_for_customer_manager: str = None,
    ):
        self.customer_account = customer_account
        self.customer_uid = customer_uid
        self.order_create_after = order_create_after
        self.order_create_before = order_create_before
        self.order_id = order_id
        self.order_pay_after = order_pay_after
        self.order_pay_before = order_pay_before
        self.order_status = order_status
        self.order_type_list = order_type_list
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.pay_amount_after = pay_amount_after
        self.pay_amount_before = pay_amount_before
        self.pay_type = pay_type
        self.product_code = product_code
        self.product_name = product_name
        self.project_id = project_id
        self.ram_account_for_customer_manager = ram_account_for_customer_manager

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_account is not None:
            result['CustomerAccount'] = self.customer_account
        if self.customer_uid is not None:
            result['CustomerUid'] = self.customer_uid
        if self.order_create_after is not None:
            result['OrderCreateAfter'] = self.order_create_after
        if self.order_create_before is not None:
            result['OrderCreateBefore'] = self.order_create_before
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_pay_after is not None:
            result['OrderPayAfter'] = self.order_pay_after
        if self.order_pay_before is not None:
            result['OrderPayBefore'] = self.order_pay_before
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.order_type_list is not None:
            result['OrderTypeList'] = self.order_type_list
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pay_amount_after is not None:
            result['PayAmountAfter'] = self.pay_amount_after
        if self.pay_amount_before is not None:
            result['PayAmountBefore'] = self.pay_amount_before
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.ram_account_for_customer_manager is not None:
            result['RamAccountForCustomerManager'] = self.ram_account_for_customer_manager
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerAccount') is not None:
            self.customer_account = m.get('CustomerAccount')
        if m.get('CustomerUid') is not None:
            self.customer_uid = m.get('CustomerUid')
        if m.get('OrderCreateAfter') is not None:
            self.order_create_after = m.get('OrderCreateAfter')
        if m.get('OrderCreateBefore') is not None:
            self.order_create_before = m.get('OrderCreateBefore')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPayAfter') is not None:
            self.order_pay_after = m.get('OrderPayAfter')
        if m.get('OrderPayBefore') is not None:
            self.order_pay_before = m.get('OrderPayBefore')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('OrderTypeList') is not None:
            self.order_type_list = m.get('OrderTypeList')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PayAmountAfter') is not None:
            self.pay_amount_after = m.get('PayAmountAfter')
        if m.get('PayAmountBefore') is not None:
            self.pay_amount_before = m.get('PayAmountBefore')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RamAccountForCustomerManager') is not None:
            self.ram_account_for_customer_manager = m.get('RamAccountForCustomerManager')
        return self


class GetCustomerOrderListShrinkRequest(TeaModel):
    def __init__(
        self,
        customer_account: str = None,
        customer_uid: int = None,
        order_create_after: int = None,
        order_create_before: int = None,
        order_id: int = None,
        order_pay_after: int = None,
        order_pay_before: int = None,
        order_status: int = None,
        order_type_list_shrink: str = None,
        page_no: int = None,
        page_size: int = None,
        pay_amount_after: float = None,
        pay_amount_before: float = None,
        pay_type: int = None,
        product_code: str = None,
        product_name: str = None,
        project_id: int = None,
        ram_account_for_customer_manager: str = None,
    ):
        self.customer_account = customer_account
        self.customer_uid = customer_uid
        self.order_create_after = order_create_after
        self.order_create_before = order_create_before
        self.order_id = order_id
        self.order_pay_after = order_pay_after
        self.order_pay_before = order_pay_before
        self.order_status = order_status
        self.order_type_list_shrink = order_type_list_shrink
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.pay_amount_after = pay_amount_after
        self.pay_amount_before = pay_amount_before
        self.pay_type = pay_type
        self.product_code = product_code
        self.product_name = product_name
        self.project_id = project_id
        self.ram_account_for_customer_manager = ram_account_for_customer_manager

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_account is not None:
            result['CustomerAccount'] = self.customer_account
        if self.customer_uid is not None:
            result['CustomerUid'] = self.customer_uid
        if self.order_create_after is not None:
            result['OrderCreateAfter'] = self.order_create_after
        if self.order_create_before is not None:
            result['OrderCreateBefore'] = self.order_create_before
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_pay_after is not None:
            result['OrderPayAfter'] = self.order_pay_after
        if self.order_pay_before is not None:
            result['OrderPayBefore'] = self.order_pay_before
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.order_type_list_shrink is not None:
            result['OrderTypeList'] = self.order_type_list_shrink
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pay_amount_after is not None:
            result['PayAmountAfter'] = self.pay_amount_after
        if self.pay_amount_before is not None:
            result['PayAmountBefore'] = self.pay_amount_before
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.ram_account_for_customer_manager is not None:
            result['RamAccountForCustomerManager'] = self.ram_account_for_customer_manager
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerAccount') is not None:
            self.customer_account = m.get('CustomerAccount')
        if m.get('CustomerUid') is not None:
            self.customer_uid = m.get('CustomerUid')
        if m.get('OrderCreateAfter') is not None:
            self.order_create_after = m.get('OrderCreateAfter')
        if m.get('OrderCreateBefore') is not None:
            self.order_create_before = m.get('OrderCreateBefore')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPayAfter') is not None:
            self.order_pay_after = m.get('OrderPayAfter')
        if m.get('OrderPayBefore') is not None:
            self.order_pay_before = m.get('OrderPayBefore')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('OrderTypeList') is not None:
            self.order_type_list_shrink = m.get('OrderTypeList')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PayAmountAfter') is not None:
            self.pay_amount_after = m.get('PayAmountAfter')
        if m.get('PayAmountBefore') is not None:
            self.pay_amount_before = m.get('PayAmountBefore')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RamAccountForCustomerManager') is not None:
            self.ram_account_for_customer_manager = m.get('RamAccountForCustomerManager')
        return self


class GetCustomerOrderListResponseBodyData(TeaModel):
    def __init__(
        self,
        amount_discount: float = None,
        amount_due: float = None,
        created_at: str = None,
        customer_account: str = None,
        customer_classification: str = None,
        customer_uid: int = None,
        deducted_amount_by_coupons: float = None,
        discounted_price: float = None,
        order_id: int = None,
        order_status: int = None,
        order_type: str = None,
        paid_at: str = None,
        pay_type: int = None,
        price: float = None,
        product_code: str = None,
        product_name: str = None,
        project_id: int = None,
        ram_account_for_customer_managers: List[str] = None,
    ):
        self.amount_discount = amount_discount
        self.amount_due = amount_due
        self.created_at = created_at
        self.customer_account = customer_account
        self.customer_classification = customer_classification
        self.customer_uid = customer_uid
        self.deducted_amount_by_coupons = deducted_amount_by_coupons
        self.discounted_price = discounted_price
        self.order_id = order_id
        self.order_status = order_status
        self.order_type = order_type
        self.paid_at = paid_at
        self.pay_type = pay_type
        self.price = price
        self.product_code = product_code
        self.product_name = product_name
        self.project_id = project_id
        self.ram_account_for_customer_managers = ram_account_for_customer_managers

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount_discount is not None:
            result['AmountDiscount'] = self.amount_discount
        if self.amount_due is not None:
            result['AmountDue'] = self.amount_due
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.customer_account is not None:
            result['CustomerAccount'] = self.customer_account
        if self.customer_classification is not None:
            result['CustomerClassification'] = self.customer_classification
        if self.customer_uid is not None:
            result['CustomerUid'] = self.customer_uid
        if self.deducted_amount_by_coupons is not None:
            result['DeductedAmountByCoupons'] = self.deducted_amount_by_coupons
        if self.discounted_price is not None:
            result['DiscountedPrice'] = self.discounted_price
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.paid_at is not None:
            result['PaidAt'] = self.paid_at
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.price is not None:
            result['Price'] = self.price
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.ram_account_for_customer_managers is not None:
            result['RamAccountForCustomerManagers'] = self.ram_account_for_customer_managers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AmountDiscount') is not None:
            self.amount_discount = m.get('AmountDiscount')
        if m.get('AmountDue') is not None:
            self.amount_due = m.get('AmountDue')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('CustomerAccount') is not None:
            self.customer_account = m.get('CustomerAccount')
        if m.get('CustomerClassification') is not None:
            self.customer_classification = m.get('CustomerClassification')
        if m.get('CustomerUid') is not None:
            self.customer_uid = m.get('CustomerUid')
        if m.get('DeductedAmountByCoupons') is not None:
            self.deducted_amount_by_coupons = m.get('DeductedAmountByCoupons')
        if m.get('DiscountedPrice') is not None:
            self.discounted_price = m.get('DiscountedPrice')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PaidAt') is not None:
            self.paid_at = m.get('PaidAt')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RamAccountForCustomerManagers') is not None:
            self.ram_account_for_customer_managers = m.get('RamAccountForCustomerManagers')
        return self


class GetCustomerOrderListResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[GetCustomerOrderListResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total = total

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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetCustomerOrderListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetCustomerOrderListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCustomerOrderListResponseBody = None,
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
            temp_model = GetCustomerOrderListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRenewalRateListRequest(TeaModel):
    def __init__(
        self,
        fiscal_year_and_quarter: str = None,
    ):
        # This parameter is required.
        self.fiscal_year_and_quarter = fiscal_year_and_quarter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fiscal_year_and_quarter is not None:
            result['FiscalYearAndQuarter'] = self.fiscal_year_and_quarter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FiscalYearAndQuarter') is not None:
            self.fiscal_year_and_quarter = m.get('FiscalYearAndQuarter')
        return self


class GetRenewalRateListResponseBodyData(TeaModel):
    def __init__(
        self,
        customer_adjusted_renewal_amount_due: float = None,
        customer_other_bill_amount: float = None,
        final_customer_renewal_amount_due: float = None,
        final_customer_renewal_rate: float = None,
        final_customer_renewed_amount: float = None,
        final_other_bill_amount: float = None,
        final_renewal_amount_due: float = None,
        final_renewal_rate: float = None,
        final_renewed_amount: float = None,
        final_sub_partner_renewal_amount_due: float = None,
        final_sub_partner_renewal_rate: float = None,
        final_sub_partner_renewed_amount: float = None,
        fiscal_year_and_quarter: str = None,
        master_pid: str = None,
        master_pid_name: str = None,
        special_customer_renew_ratio: float = None,
        special_customer_renewal_amount_due: float = None,
        special_customer_renewed_amount: float = None,
        special_final_renew_ratio: float = None,
        special_final_renewal_amount_due: float = None,
        special_final_renewed_amount: float = None,
        special_sub_partner_renew_ratio: float = None,
        special_sub_partner_renewal_amount_due: float = None,
        special_sub_partner_renewed_amount: float = None,
        sub_partner_adjusted_renewal_amount_due: float = None,
        sub_partner_other_bill_amount: float = None,
    ):
        self.customer_adjusted_renewal_amount_due = customer_adjusted_renewal_amount_due
        self.customer_other_bill_amount = customer_other_bill_amount
        self.final_customer_renewal_amount_due = final_customer_renewal_amount_due
        self.final_customer_renewal_rate = final_customer_renewal_rate
        self.final_customer_renewed_amount = final_customer_renewed_amount
        self.final_other_bill_amount = final_other_bill_amount
        self.final_renewal_amount_due = final_renewal_amount_due
        self.final_renewal_rate = final_renewal_rate
        self.final_renewed_amount = final_renewed_amount
        self.final_sub_partner_renewal_amount_due = final_sub_partner_renewal_amount_due
        self.final_sub_partner_renewal_rate = final_sub_partner_renewal_rate
        self.final_sub_partner_renewed_amount = final_sub_partner_renewed_amount
        self.fiscal_year_and_quarter = fiscal_year_and_quarter
        self.master_pid = master_pid
        self.master_pid_name = master_pid_name
        self.special_customer_renew_ratio = special_customer_renew_ratio
        self.special_customer_renewal_amount_due = special_customer_renewal_amount_due
        self.special_customer_renewed_amount = special_customer_renewed_amount
        self.special_final_renew_ratio = special_final_renew_ratio
        self.special_final_renewal_amount_due = special_final_renewal_amount_due
        self.special_final_renewed_amount = special_final_renewed_amount
        self.special_sub_partner_renew_ratio = special_sub_partner_renew_ratio
        self.special_sub_partner_renewal_amount_due = special_sub_partner_renewal_amount_due
        self.special_sub_partner_renewed_amount = special_sub_partner_renewed_amount
        self.sub_partner_adjusted_renewal_amount_due = sub_partner_adjusted_renewal_amount_due
        self.sub_partner_other_bill_amount = sub_partner_other_bill_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_adjusted_renewal_amount_due is not None:
            result['CustomerAdjustedRenewalAmountDue'] = self.customer_adjusted_renewal_amount_due
        if self.customer_other_bill_amount is not None:
            result['CustomerOtherBillAmount'] = self.customer_other_bill_amount
        if self.final_customer_renewal_amount_due is not None:
            result['FinalCustomerRenewalAmountDue'] = self.final_customer_renewal_amount_due
        if self.final_customer_renewal_rate is not None:
            result['FinalCustomerRenewalRate'] = self.final_customer_renewal_rate
        if self.final_customer_renewed_amount is not None:
            result['FinalCustomerRenewedAmount'] = self.final_customer_renewed_amount
        if self.final_other_bill_amount is not None:
            result['FinalOtherBillAmount'] = self.final_other_bill_amount
        if self.final_renewal_amount_due is not None:
            result['FinalRenewalAmountDue'] = self.final_renewal_amount_due
        if self.final_renewal_rate is not None:
            result['FinalRenewalRate'] = self.final_renewal_rate
        if self.final_renewed_amount is not None:
            result['FinalRenewedAmount'] = self.final_renewed_amount
        if self.final_sub_partner_renewal_amount_due is not None:
            result['FinalSubPartnerRenewalAmountDue'] = self.final_sub_partner_renewal_amount_due
        if self.final_sub_partner_renewal_rate is not None:
            result['FinalSubPartnerRenewalRate'] = self.final_sub_partner_renewal_rate
        if self.final_sub_partner_renewed_amount is not None:
            result['FinalSubPartnerRenewedAmount'] = self.final_sub_partner_renewed_amount
        if self.fiscal_year_and_quarter is not None:
            result['FiscalYearAndQuarter'] = self.fiscal_year_and_quarter
        if self.master_pid is not None:
            result['MasterPid'] = self.master_pid
        if self.master_pid_name is not None:
            result['MasterPidName'] = self.master_pid_name
        if self.special_customer_renew_ratio is not None:
            result['SpecialCustomerRenewRatio'] = self.special_customer_renew_ratio
        if self.special_customer_renewal_amount_due is not None:
            result['SpecialCustomerRenewalAmountDue'] = self.special_customer_renewal_amount_due
        if self.special_customer_renewed_amount is not None:
            result['SpecialCustomerRenewedAmount'] = self.special_customer_renewed_amount
        if self.special_final_renew_ratio is not None:
            result['SpecialFinalRenewRatio'] = self.special_final_renew_ratio
        if self.special_final_renewal_amount_due is not None:
            result['SpecialFinalRenewalAmountDue'] = self.special_final_renewal_amount_due
        if self.special_final_renewed_amount is not None:
            result['SpecialFinalRenewedAmount'] = self.special_final_renewed_amount
        if self.special_sub_partner_renew_ratio is not None:
            result['SpecialSubPartnerRenewRatio'] = self.special_sub_partner_renew_ratio
        if self.special_sub_partner_renewal_amount_due is not None:
            result['SpecialSubPartnerRenewalAmountDue'] = self.special_sub_partner_renewal_amount_due
        if self.special_sub_partner_renewed_amount is not None:
            result['SpecialSubPartnerRenewedAmount'] = self.special_sub_partner_renewed_amount
        if self.sub_partner_adjusted_renewal_amount_due is not None:
            result['SubPartnerAdjustedRenewalAmountDue'] = self.sub_partner_adjusted_renewal_amount_due
        if self.sub_partner_other_bill_amount is not None:
            result['SubPartnerOtherBillAmount'] = self.sub_partner_other_bill_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerAdjustedRenewalAmountDue') is not None:
            self.customer_adjusted_renewal_amount_due = m.get('CustomerAdjustedRenewalAmountDue')
        if m.get('CustomerOtherBillAmount') is not None:
            self.customer_other_bill_amount = m.get('CustomerOtherBillAmount')
        if m.get('FinalCustomerRenewalAmountDue') is not None:
            self.final_customer_renewal_amount_due = m.get('FinalCustomerRenewalAmountDue')
        if m.get('FinalCustomerRenewalRate') is not None:
            self.final_customer_renewal_rate = m.get('FinalCustomerRenewalRate')
        if m.get('FinalCustomerRenewedAmount') is not None:
            self.final_customer_renewed_amount = m.get('FinalCustomerRenewedAmount')
        if m.get('FinalOtherBillAmount') is not None:
            self.final_other_bill_amount = m.get('FinalOtherBillAmount')
        if m.get('FinalRenewalAmountDue') is not None:
            self.final_renewal_amount_due = m.get('FinalRenewalAmountDue')
        if m.get('FinalRenewalRate') is not None:
            self.final_renewal_rate = m.get('FinalRenewalRate')
        if m.get('FinalRenewedAmount') is not None:
            self.final_renewed_amount = m.get('FinalRenewedAmount')
        if m.get('FinalSubPartnerRenewalAmountDue') is not None:
            self.final_sub_partner_renewal_amount_due = m.get('FinalSubPartnerRenewalAmountDue')
        if m.get('FinalSubPartnerRenewalRate') is not None:
            self.final_sub_partner_renewal_rate = m.get('FinalSubPartnerRenewalRate')
        if m.get('FinalSubPartnerRenewedAmount') is not None:
            self.final_sub_partner_renewed_amount = m.get('FinalSubPartnerRenewedAmount')
        if m.get('FiscalYearAndQuarter') is not None:
            self.fiscal_year_and_quarter = m.get('FiscalYearAndQuarter')
        if m.get('MasterPid') is not None:
            self.master_pid = m.get('MasterPid')
        if m.get('MasterPidName') is not None:
            self.master_pid_name = m.get('MasterPidName')
        if m.get('SpecialCustomerRenewRatio') is not None:
            self.special_customer_renew_ratio = m.get('SpecialCustomerRenewRatio')
        if m.get('SpecialCustomerRenewalAmountDue') is not None:
            self.special_customer_renewal_amount_due = m.get('SpecialCustomerRenewalAmountDue')
        if m.get('SpecialCustomerRenewedAmount') is not None:
            self.special_customer_renewed_amount = m.get('SpecialCustomerRenewedAmount')
        if m.get('SpecialFinalRenewRatio') is not None:
            self.special_final_renew_ratio = m.get('SpecialFinalRenewRatio')
        if m.get('SpecialFinalRenewalAmountDue') is not None:
            self.special_final_renewal_amount_due = m.get('SpecialFinalRenewalAmountDue')
        if m.get('SpecialFinalRenewedAmount') is not None:
            self.special_final_renewed_amount = m.get('SpecialFinalRenewedAmount')
        if m.get('SpecialSubPartnerRenewRatio') is not None:
            self.special_sub_partner_renew_ratio = m.get('SpecialSubPartnerRenewRatio')
        if m.get('SpecialSubPartnerRenewalAmountDue') is not None:
            self.special_sub_partner_renewal_amount_due = m.get('SpecialSubPartnerRenewalAmountDue')
        if m.get('SpecialSubPartnerRenewedAmount') is not None:
            self.special_sub_partner_renewed_amount = m.get('SpecialSubPartnerRenewedAmount')
        if m.get('SubPartnerAdjustedRenewalAmountDue') is not None:
            self.sub_partner_adjusted_renewal_amount_due = m.get('SubPartnerAdjustedRenewalAmountDue')
        if m.get('SubPartnerOtherBillAmount') is not None:
            self.sub_partner_other_bill_amount = m.get('SubPartnerOtherBillAmount')
        return self


class GetRenewalRateListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetRenewalRateListResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetRenewalRateListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRenewalRateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRenewalRateListResponseBody = None,
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
            temp_model = GetRenewalRateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubPartnerListRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        sub_partner_company_name: str = None,
        sub_partner_pid: str = None,
    ):
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.sub_partner_company_name = sub_partner_company_name
        self.sub_partner_pid = sub_partner_pid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sub_partner_company_name is not None:
            result['SubPartnerCompanyName'] = self.sub_partner_company_name
        if self.sub_partner_pid is not None:
            result['SubPartnerPid'] = self.sub_partner_pid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SubPartnerCompanyName') is not None:
            self.sub_partner_company_name = m.get('SubPartnerCompanyName')
        if m.get('SubPartnerPid') is not None:
            self.sub_partner_pid = m.get('SubPartnerPid')
        return self


class GetSubPartnerListResponseBodySubPartnerList(TeaModel):
    def __init__(
        self,
        address: str = None,
        agreement_status: str = None,
        agreement_status_desc: str = None,
        city: str = None,
        company_name: str = None,
        contact: str = None,
        district: str = None,
        join_time: str = None,
        master_account: str = None,
        master_uid: str = None,
        pid: str = None,
        province: str = None,
    ):
        self.address = address
        self.agreement_status = agreement_status
        self.agreement_status_desc = agreement_status_desc
        self.city = city
        self.company_name = company_name
        self.contact = contact
        self.district = district
        self.join_time = join_time
        self.master_account = master_account
        self.master_uid = master_uid
        self.pid = pid
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.agreement_status is not None:
            result['AgreementStatus'] = self.agreement_status
        if self.agreement_status_desc is not None:
            result['AgreementStatusDesc'] = self.agreement_status_desc
        if self.city is not None:
            result['City'] = self.city
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.contact is not None:
            result['Contact'] = self.contact
        if self.district is not None:
            result['District'] = self.district
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.master_account is not None:
            result['MasterAccount'] = self.master_account
        if self.master_uid is not None:
            result['MasterUid'] = self.master_uid
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AgreementStatus') is not None:
            self.agreement_status = m.get('AgreementStatus')
        if m.get('AgreementStatusDesc') is not None:
            self.agreement_status_desc = m.get('AgreementStatusDesc')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('Contact') is not None:
            self.contact = m.get('Contact')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('MasterAccount') is not None:
            self.master_account = m.get('MasterAccount')
        if m.get('MasterUid') is not None:
            self.master_uid = m.get('MasterUid')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class GetSubPartnerListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        page_no: str = None,
        page_size: str = None,
        request_id: str = None,
        sub_partner_list: List[GetSubPartnerListResponseBodySubPartnerList] = None,
        success: bool = None,
        total: int = None,
    ):
        self.message = message
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.request_id = request_id
        self.sub_partner_list = sub_partner_list
        self.success = success
        self.total = total

    def validate(self):
        if self.sub_partner_list:
            for k in self.sub_partner_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SubPartnerList'] = []
        if self.sub_partner_list is not None:
            for k in self.sub_partner_list:
                result['SubPartnerList'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sub_partner_list = []
        if m.get('SubPartnerList') is not None:
            for k in m.get('SubPartnerList'):
                temp_model = GetSubPartnerListResponseBodySubPartnerList()
                self.sub_partner_list.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetSubPartnerListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSubPartnerListResponseBody = None,
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
            temp_model = GetSubPartnerListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubPartnerOrderListRequest(TeaModel):
    def __init__(
        self,
        order_create_after: int = None,
        order_create_before: int = None,
        order_id: int = None,
        order_pay_after: int = None,
        order_pay_before: int = None,
        order_status: int = None,
        order_type_list: List[str] = None,
        page_no: int = None,
        page_size: int = None,
        pay_amount_after: int = None,
        pay_amount_before: int = None,
        pay_type: int = None,
        product_code: str = None,
        product_name: str = None,
        project_id: int = None,
        sub_partner_name: str = None,
        sub_partner_uid: int = None,
    ):
        self.order_create_after = order_create_after
        self.order_create_before = order_create_before
        self.order_id = order_id
        self.order_pay_after = order_pay_after
        self.order_pay_before = order_pay_before
        self.order_status = order_status
        self.order_type_list = order_type_list
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.pay_amount_after = pay_amount_after
        self.pay_amount_before = pay_amount_before
        self.pay_type = pay_type
        self.product_code = product_code
        self.product_name = product_name
        self.project_id = project_id
        self.sub_partner_name = sub_partner_name
        self.sub_partner_uid = sub_partner_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_create_after is not None:
            result['OrderCreateAfter'] = self.order_create_after
        if self.order_create_before is not None:
            result['OrderCreateBefore'] = self.order_create_before
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_pay_after is not None:
            result['OrderPayAfter'] = self.order_pay_after
        if self.order_pay_before is not None:
            result['OrderPayBefore'] = self.order_pay_before
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.order_type_list is not None:
            result['OrderTypeList'] = self.order_type_list
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pay_amount_after is not None:
            result['PayAmountAfter'] = self.pay_amount_after
        if self.pay_amount_before is not None:
            result['PayAmountBefore'] = self.pay_amount_before
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sub_partner_name is not None:
            result['SubPartnerName'] = self.sub_partner_name
        if self.sub_partner_uid is not None:
            result['SubPartnerUid'] = self.sub_partner_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderCreateAfter') is not None:
            self.order_create_after = m.get('OrderCreateAfter')
        if m.get('OrderCreateBefore') is not None:
            self.order_create_before = m.get('OrderCreateBefore')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPayAfter') is not None:
            self.order_pay_after = m.get('OrderPayAfter')
        if m.get('OrderPayBefore') is not None:
            self.order_pay_before = m.get('OrderPayBefore')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('OrderTypeList') is not None:
            self.order_type_list = m.get('OrderTypeList')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PayAmountAfter') is not None:
            self.pay_amount_after = m.get('PayAmountAfter')
        if m.get('PayAmountBefore') is not None:
            self.pay_amount_before = m.get('PayAmountBefore')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SubPartnerName') is not None:
            self.sub_partner_name = m.get('SubPartnerName')
        if m.get('SubPartnerUid') is not None:
            self.sub_partner_uid = m.get('SubPartnerUid')
        return self


class GetSubPartnerOrderListShrinkRequest(TeaModel):
    def __init__(
        self,
        order_create_after: int = None,
        order_create_before: int = None,
        order_id: int = None,
        order_pay_after: int = None,
        order_pay_before: int = None,
        order_status: int = None,
        order_type_list_shrink: str = None,
        page_no: int = None,
        page_size: int = None,
        pay_amount_after: int = None,
        pay_amount_before: int = None,
        pay_type: int = None,
        product_code: str = None,
        product_name: str = None,
        project_id: int = None,
        sub_partner_name: str = None,
        sub_partner_uid: int = None,
    ):
        self.order_create_after = order_create_after
        self.order_create_before = order_create_before
        self.order_id = order_id
        self.order_pay_after = order_pay_after
        self.order_pay_before = order_pay_before
        self.order_status = order_status
        self.order_type_list_shrink = order_type_list_shrink
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.pay_amount_after = pay_amount_after
        self.pay_amount_before = pay_amount_before
        self.pay_type = pay_type
        self.product_code = product_code
        self.product_name = product_name
        self.project_id = project_id
        self.sub_partner_name = sub_partner_name
        self.sub_partner_uid = sub_partner_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_create_after is not None:
            result['OrderCreateAfter'] = self.order_create_after
        if self.order_create_before is not None:
            result['OrderCreateBefore'] = self.order_create_before
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_pay_after is not None:
            result['OrderPayAfter'] = self.order_pay_after
        if self.order_pay_before is not None:
            result['OrderPayBefore'] = self.order_pay_before
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.order_type_list_shrink is not None:
            result['OrderTypeList'] = self.order_type_list_shrink
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pay_amount_after is not None:
            result['PayAmountAfter'] = self.pay_amount_after
        if self.pay_amount_before is not None:
            result['PayAmountBefore'] = self.pay_amount_before
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sub_partner_name is not None:
            result['SubPartnerName'] = self.sub_partner_name
        if self.sub_partner_uid is not None:
            result['SubPartnerUid'] = self.sub_partner_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderCreateAfter') is not None:
            self.order_create_after = m.get('OrderCreateAfter')
        if m.get('OrderCreateBefore') is not None:
            self.order_create_before = m.get('OrderCreateBefore')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderPayAfter') is not None:
            self.order_pay_after = m.get('OrderPayAfter')
        if m.get('OrderPayBefore') is not None:
            self.order_pay_before = m.get('OrderPayBefore')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('OrderTypeList') is not None:
            self.order_type_list_shrink = m.get('OrderTypeList')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PayAmountAfter') is not None:
            self.pay_amount_after = m.get('PayAmountAfter')
        if m.get('PayAmountBefore') is not None:
            self.pay_amount_before = m.get('PayAmountBefore')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SubPartnerName') is not None:
            self.sub_partner_name = m.get('SubPartnerName')
        if m.get('SubPartnerUid') is not None:
            self.sub_partner_uid = m.get('SubPartnerUid')
        return self


class GetSubPartnerOrderListResponseBodyData(TeaModel):
    def __init__(
        self,
        amount_discount: float = None,
        amount_due: float = None,
        created_at: str = None,
        customer_classification: str = None,
        deducted_amount_by_coupons: float = None,
        discounted_price: float = None,
        order_id: int = None,
        order_status: int = None,
        order_type: str = None,
        paid_at: str = None,
        pay_type: int = None,
        price: float = None,
        product_code: str = None,
        product_name: str = None,
        project_id: int = None,
        sub_partner_name: str = None,
        sub_partner_uid: int = None,
    ):
        self.amount_discount = amount_discount
        self.amount_due = amount_due
        self.created_at = created_at
        self.customer_classification = customer_classification
        self.deducted_amount_by_coupons = deducted_amount_by_coupons
        self.discounted_price = discounted_price
        self.order_id = order_id
        self.order_status = order_status
        self.order_type = order_type
        self.paid_at = paid_at
        self.pay_type = pay_type
        self.price = price
        self.product_code = product_code
        self.product_name = product_name
        self.project_id = project_id
        self.sub_partner_name = sub_partner_name
        self.sub_partner_uid = sub_partner_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount_discount is not None:
            result['AmountDiscount'] = self.amount_discount
        if self.amount_due is not None:
            result['AmountDue'] = self.amount_due
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.customer_classification is not None:
            result['CustomerClassification'] = self.customer_classification
        if self.deducted_amount_by_coupons is not None:
            result['DeductedAmountByCoupons'] = self.deducted_amount_by_coupons
        if self.discounted_price is not None:
            result['DiscountedPrice'] = self.discounted_price
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.paid_at is not None:
            result['PaidAt'] = self.paid_at
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.price is not None:
            result['Price'] = self.price
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sub_partner_name is not None:
            result['SubPartnerName'] = self.sub_partner_name
        if self.sub_partner_uid is not None:
            result['SubPartnerUid'] = self.sub_partner_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AmountDiscount') is not None:
            self.amount_discount = m.get('AmountDiscount')
        if m.get('AmountDue') is not None:
            self.amount_due = m.get('AmountDue')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('CustomerClassification') is not None:
            self.customer_classification = m.get('CustomerClassification')
        if m.get('DeductedAmountByCoupons') is not None:
            self.deducted_amount_by_coupons = m.get('DeductedAmountByCoupons')
        if m.get('DiscountedPrice') is not None:
            self.discounted_price = m.get('DiscountedPrice')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PaidAt') is not None:
            self.paid_at = m.get('PaidAt')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SubPartnerName') is not None:
            self.sub_partner_name = m.get('SubPartnerName')
        if m.get('SubPartnerUid') is not None:
            self.sub_partner_uid = m.get('SubPartnerUid')
        return self


class GetSubPartnerOrderListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetSubPartnerOrderListResponseBodyData] = None,
        message: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_no = page_no
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total = total

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetSubPartnerOrderListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetSubPartnerOrderListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSubPartnerOrderListResponseBody = None,
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
            temp_model = GetSubPartnerOrderListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


