# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class DescribeInnerIpWhitelistGroupsResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        data: List[main_models.DescribeInnerIpWhitelistGroupsResponseBodyData] = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.data = data

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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.DescribeInnerIpWhitelistGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        return self

class DescribeInnerIpWhitelistGroupsResponseBodyData(DaraModel):
    def __init__(
        self,
        cidr_ip_list: List[str] = None,
        inner_ip_whitelist_group_id: str = None,
    ):
        self.cidr_ip_list = cidr_ip_list
        self.inner_ip_whitelist_group_id = inner_ip_whitelist_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_ip_list is not None:
            result['CidrIpList'] = self.cidr_ip_list

        if self.inner_ip_whitelist_group_id is not None:
            result['InnerIpWhitelistGroupId'] = self.inner_ip_whitelist_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrIpList') is not None:
            self.cidr_ip_list = m.get('CidrIpList')

        if m.get('InnerIpWhitelistGroupId') is not None:
            self.inner_ip_whitelist_group_id = m.get('InnerIpWhitelistGroupId')

        return self

