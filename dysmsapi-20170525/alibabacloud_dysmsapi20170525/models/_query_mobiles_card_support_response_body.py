# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QueryMobilesCardSupportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryMobilesCardSupportResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 请求状态码。
        # 
        # - 返回OK代表请求成功。
        # - 其他错误码，请参见[错误码列表](https://help.aliyun.com/document_detail/101346.html)。
        self.code = code
        # 返回数据。
        self.data = data
        # 阿里云为该请求生成的唯一标识符。
        self.request_id = request_id
        # 调用接口是否成功。取值：
        # 
        # - **true**：调用成功。
        # 
        # - **false**：调用失败。
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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
            temp_model = main_models.QueryMobilesCardSupportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryMobilesCardSupportResponseBodyData(DaraModel):
    def __init__(
        self,
        query_result: List[main_models.QueryMobilesCardSupportResponseBodyDataQueryResult] = None,
    ):
        # 查询值。
        self.query_result = query_result

    def validate(self):
        if self.query_result:
            for v1 in self.query_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['QueryResult'] = []
        if self.query_result is not None:
            for k1 in self.query_result:
                result['QueryResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.query_result = []
        if m.get('QueryResult') is not None:
            for k1 in m.get('QueryResult'):
                temp_model = main_models.QueryMobilesCardSupportResponseBodyDataQueryResult()
                self.query_result.append(temp_model.from_map(k1))

        return self

class QueryMobilesCardSupportResponseBodyDataQueryResult(DaraModel):
    def __init__(
        self,
        mobile: str = None,
        support: bool = None,
    ):
        # 查询的手机号码。
        self.mobile = mobile
        # 是否支持卡片短信。取值：
        # 
        # - **true**：支持。
        # - **false**：不支持。
        self.support = support

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.support is not None:
            result['Support'] = self.support

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Support') is not None:
            self.support = m.get('Support')

        return self

