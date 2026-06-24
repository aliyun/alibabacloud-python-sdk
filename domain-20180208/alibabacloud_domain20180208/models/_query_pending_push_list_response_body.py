# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class QueryPendingPushListResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        http_status_code: int = None,
        max_results: int = None,
        module: main_models.QueryPendingPushListResponseBodyModule = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # RAM鉴权失败时的标准化错误详情，JSON字符串，包含NoPermissionType、PolicyType、AuthPrincipalType、EncodedDiagnosticMessage等字段
        self.access_denied_detail = access_denied_detail
        # 是否允许重试
        self.allow_retry = allow_retry
        # HTTP状态码
        self.http_status_code = http_status_code
        # 本次返回的最大记录条数
        self.max_results = max_results
        # 业务数据模块
        self.module = module
        # 获取下一页需用到的凭证
        self.next_token = next_token
        # 唯一请求识别码
        self.request_id = request_id
        # 是否调用成功
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Module') is not None:
            temp_model = main_models.QueryPendingPushListResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryPendingPushListResponseBodyModule(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        push_list: List[main_models.QueryPendingPushListResponseBodyModulePushList] = None,
        total_count: int = None,
    ):
        # 当前页码
        self.page_num = page_num
        # 每页大小
        self.page_size = page_size
        # 待接收Push列表
        self.push_list = push_list
        # 满足条件的总记录数
        self.total_count = total_count

    def validate(self):
        if self.push_list:
            for v1 in self.push_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PushList'] = []
        if self.push_list is not None:
            for k1 in self.push_list:
                result['PushList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.push_list = []
        if m.get('PushList') is not None:
            for k1 in m.get('PushList'):
                temp_model = main_models.QueryPendingPushListResponseBodyModulePushList()
                self.push_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryPendingPushListResponseBodyModulePushList(DaraModel):
    def __init__(
        self,
        domain_count: int = None,
        domain_list: str = None,
        expire_time: str = None,
        out_biz_id: str = None,
        push_no: str = None,
        push_time: str = None,
        seller_remark: str = None,
        trade_money: str = None,
    ):
        # 本次Push包含的域名数量
        self.domain_count = domain_count
        # 域名列表，逗号分隔摘要
        self.domain_list = domain_list
        # 超过该时间未操作将自动关闭
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.expire_time = expire_time
        # 卖家发起时指定，用于双方业务关联
        self.out_biz_id = out_biz_id
        # Push编号
        self.push_no = push_no
        # Push发起时间
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.push_time = push_time
        # 卖家发起Push时填写的备注信息
        self.seller_remark = seller_remark
        # 交易金额，0表示免费Push
        self.trade_money = trade_money

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count

        if self.domain_list is not None:
            result['DomainList'] = self.domain_list

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id

        if self.push_no is not None:
            result['PushNo'] = self.push_no

        if self.push_time is not None:
            result['PushTime'] = self.push_time

        if self.seller_remark is not None:
            result['SellerRemark'] = self.seller_remark

        if self.trade_money is not None:
            result['TradeMoney'] = self.trade_money

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')

        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')

        if m.get('PushNo') is not None:
            self.push_no = m.get('PushNo')

        if m.get('PushTime') is not None:
            self.push_time = m.get('PushTime')

        if m.get('SellerRemark') is not None:
            self.seller_remark = m.get('SellerRemark')

        if m.get('TradeMoney') is not None:
            self.trade_money = m.get('TradeMoney')

        return self

