# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class DescribeModelOperatorResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeModelOperatorResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('Data') is not None:
            temp_model = main_models.DescribeModelOperatorResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeModelOperatorResponseBodyData(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        auto_renew: bool = None,
        base_url: str = None,
        charge_type: str = None,
        daily_usage: List[main_models.DescribeModelOperatorResponseBodyDataDailyUsage] = None,
        end_time: int = None,
        instance_class: str = None,
        instance_id: str = None,
        key_usage_list: List[main_models.DescribeModelOperatorResponseBodyDataKeyUsageList] = None,
        start_time: int = None,
        status: str = None,
        total_quota: int = None,
        used_quota: int = None,
    ):
        self.api_key = api_key
        self.auto_renew = auto_renew
        self.base_url = base_url
        self.charge_type = charge_type
        self.daily_usage = daily_usage
        self.end_time = end_time
        self.instance_class = instance_class
        self.instance_id = instance_id
        self.key_usage_list = key_usage_list
        self.start_time = start_time
        self.status = status
        self.total_quota = total_quota
        self.used_quota = used_quota

    def validate(self):
        if self.daily_usage:
            for v1 in self.daily_usage:
                 if v1:
                    v1.validate()
        if self.key_usage_list:
            for v1 in self.key_usage_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        result['DailyUsage'] = []
        if self.daily_usage is not None:
            for k1 in self.daily_usage:
                result['DailyUsage'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['KeyUsageList'] = []
        if self.key_usage_list is not None:
            for k1 in self.key_usage_list:
                result['KeyUsageList'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota

        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        self.daily_usage = []
        if m.get('DailyUsage') is not None:
            for k1 in m.get('DailyUsage'):
                temp_model = main_models.DescribeModelOperatorResponseBodyDataDailyUsage()
                self.daily_usage.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.key_usage_list = []
        if m.get('KeyUsageList') is not None:
            for k1 in m.get('KeyUsageList'):
                temp_model = main_models.DescribeModelOperatorResponseBodyDataKeyUsageList()
                self.key_usage_list.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')

        if m.get('UsedQuota') is not None:
            self.used_quota = m.get('UsedQuota')

        return self

class DescribeModelOperatorResponseBodyDataKeyUsageList(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        daily_usage: List[main_models.DescribeModelOperatorResponseBodyDataKeyUsageListDailyUsage] = None,
        deleted: bool = None,
        key_name: str = None,
        key_type: str = None,
        key_used: str = None,
        used_quota: str = None,
    ):
        # API Key
        self.api_key = api_key
        self.daily_usage = daily_usage
        self.deleted = deleted
        self.key_name = key_name
        self.key_type = key_type
        self.key_used = key_used
        self.used_quota = used_quota

    def validate(self):
        if self.daily_usage:
            for v1 in self.daily_usage:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        result['DailyUsage'] = []
        if self.daily_usage is not None:
            for k1 in self.daily_usage:
                result['DailyUsage'].append(k1.to_map() if k1 else None)

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        if self.key_used is not None:
            result['KeyUsed'] = self.key_used

        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        self.daily_usage = []
        if m.get('DailyUsage') is not None:
            for k1 in m.get('DailyUsage'):
                temp_model = main_models.DescribeModelOperatorResponseBodyDataKeyUsageListDailyUsage()
                self.daily_usage.append(temp_model.from_map(k1))

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        if m.get('KeyUsed') is not None:
            self.key_used = m.get('KeyUsed')

        if m.get('UsedQuota') is not None:
            self.used_quota = m.get('UsedQuota')

        return self

class DescribeModelOperatorResponseBodyDataKeyUsageListDailyUsage(DaraModel):
    def __init__(
        self,
        date: str = None,
        usage: str = None,
    ):
        self.date = date
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

class DescribeModelOperatorResponseBodyDataDailyUsage(DaraModel):
    def __init__(
        self,
        date: str = None,
        usage: int = None,
    ):
        self.date = date
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

