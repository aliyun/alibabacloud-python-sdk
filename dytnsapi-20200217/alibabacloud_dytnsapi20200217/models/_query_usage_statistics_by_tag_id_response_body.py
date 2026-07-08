# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class QueryUsageStatisticsByTagIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.QueryUsageStatisticsByTagIdResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 请求状态码。 **OK**为成功。
        self.code = code
        # 返回的数据内容。
        self.data = data
        # 返回状态码描述。
        self.message = message
        # 请求ID。
        self.request_id = request_id
        # 表示是否调用成功。
        # - true：调用成功。             
        #  - false：调用失败。
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('Data'):
                temp_model = main_models.QueryUsageStatisticsByTagIdResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryUsageStatisticsByTagIdResponseBodyData(DaraModel):
    def __init__(
        self,
        authorization_code: str = None,
        fail_total: int = None,
        gmt_date_str: str = None,
        id: int = None,
        industry_name: str = None,
        partner_id: int = None,
        scene_name: str = None,
        success_total: int = None,
        tag_id: int = None,
        tag_name: str = None,
        total: int = None,
    ):
        # 授权码。
        self.authorization_code = authorization_code
        # 查询失败号码数。
        self.fail_total = fail_total
        # 创建时间。
        self.gmt_date_str = gmt_date_str
        # 授权码使用记录ID。
        self.id = id
        # 行业名称。
        self.industry_name = industry_name
        # 客户pid。
        self.partner_id = partner_id
        # 场景名称。
        self.scene_name = scene_name
        # 查询成功号码数。
        self.success_total = success_total
        # 标签名称。
        self.tag_id = tag_id
        # 标签名称。
        self.tag_name = tag_name
        # 查询总号码数。
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_code is not None:
            result['AuthorizationCode'] = self.authorization_code

        if self.fail_total is not None:
            result['FailTotal'] = self.fail_total

        if self.gmt_date_str is not None:
            result['GmtDateStr'] = self.gmt_date_str

        if self.id is not None:
            result['Id'] = self.id

        if self.industry_name is not None:
            result['IndustryName'] = self.industry_name

        if self.partner_id is not None:
            result['PartnerId'] = self.partner_id

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.success_total is not None:
            result['SuccessTotal'] = self.success_total

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationCode') is not None:
            self.authorization_code = m.get('AuthorizationCode')

        if m.get('FailTotal') is not None:
            self.fail_total = m.get('FailTotal')

        if m.get('GmtDateStr') is not None:
            self.gmt_date_str = m.get('GmtDateStr')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IndustryName') is not None:
            self.industry_name = m.get('IndustryName')

        if m.get('PartnerId') is not None:
            self.partner_id = m.get('PartnerId')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('SuccessTotal') is not None:
            self.success_total = m.get('SuccessTotal')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

