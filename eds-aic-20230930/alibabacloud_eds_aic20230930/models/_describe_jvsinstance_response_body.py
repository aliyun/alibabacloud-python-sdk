# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeJVSInstanceResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeJVSInstanceResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        # 当前页实际返回条数
        self.max_results = max_results
        # 下一页游标，末页不返回
        self.next_token = next_token
        self.request_id = request_id
        # 符合条件的总记录数
        self.total_count = total_count

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeJVSInstanceResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeJVSInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        credit_config: List[main_models.DescribeJVSInstanceResponseBodyDataCreditConfig] = None,
        expire_time: str = None,
        instance_id: str = None,
        jvs_package_id: str = None,
        modify_time: str = None,
        status: str = None,
        used_credit: List[main_models.DescribeJVSInstanceResponseBodyDataUsedCredit] = None,
    ):
        self.create_time = create_time
        self.credit_config = credit_config
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.jvs_package_id = jvs_package_id
        self.modify_time = modify_time
        self.status = status
        self.used_credit = used_credit

    def validate(self):
        if self.credit_config:
            for v1 in self.credit_config:
                 if v1:
                    v1.validate()
        if self.used_credit:
            for v1 in self.used_credit:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['CreditConfig'] = []
        if self.credit_config is not None:
            for k1 in self.credit_config:
                result['CreditConfig'].append(k1.to_map() if k1 else None)

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.jvs_package_id is not None:
            result['JvsPackageId'] = self.jvs_package_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.status is not None:
            result['Status'] = self.status

        result['UsedCredit'] = []
        if self.used_credit is not None:
            for k1 in self.used_credit:
                result['UsedCredit'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.credit_config = []
        if m.get('CreditConfig') is not None:
            for k1 in m.get('CreditConfig'):
                temp_model = main_models.DescribeJVSInstanceResponseBodyDataCreditConfig()
                self.credit_config.append(temp_model.from_map(k1))

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JvsPackageId') is not None:
            self.jvs_package_id = m.get('JvsPackageId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.used_credit = []
        if m.get('UsedCredit') is not None:
            for k1 in m.get('UsedCredit'):
                temp_model = main_models.DescribeJVSInstanceResponseBodyDataUsedCredit()
                self.used_credit.append(temp_model.from_map(k1))

        return self

class DescribeJVSInstanceResponseBodyDataUsedCredit(DaraModel):
    def __init__(
        self,
        credit: int = None,
        limit_period: str = None,
    ):
        self.credit = credit
        self.limit_period = limit_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit is not None:
            result['Credit'] = self.credit

        if self.limit_period is not None:
            result['LimitPeriod'] = self.limit_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Credit') is not None:
            self.credit = m.get('Credit')

        if m.get('LimitPeriod') is not None:
            self.limit_period = m.get('LimitPeriod')

        return self

class DescribeJVSInstanceResponseBodyDataCreditConfig(DaraModel):
    def __init__(
        self,
        credit_limit: int = None,
        limit_period: str = None,
    ):
        self.credit_limit = credit_limit
        self.limit_period = limit_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit_limit is not None:
            result['CreditLimit'] = self.credit_limit

        if self.limit_period is not None:
            result['LimitPeriod'] = self.limit_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditLimit') is not None:
            self.credit_limit = m.get('CreditLimit')

        if m.get('LimitPeriod') is not None:
            self.limit_period = m.get('LimitPeriod')

        return self

