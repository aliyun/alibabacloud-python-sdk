# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetRunningSqlConcurrencyControlRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetRunningSqlConcurrencyControlRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The detailed information, including the error codes and the number of entries that are returned.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, Successful is returned. If the request failed, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.GetRunningSqlConcurrencyControlRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetRunningSqlConcurrencyControlRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        list: main_models.GetRunningSqlConcurrencyControlRulesResponseBodyDataList = None,
        total: int = None,
    ):
        # The returned data.
        self.list = list
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list is not None:
            result['List'] = self.list.to_map()

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('List') is not None:
            temp_model = main_models.GetRunningSqlConcurrencyControlRulesResponseBodyDataList()
            self.list = temp_model.from_map(m.get('List'))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetRunningSqlConcurrencyControlRulesResponseBodyDataList(DaraModel):
    def __init__(
        self,
        running_rules: List[main_models.GetRunningSqlConcurrencyControlRulesResponseBodyDataListRunningRules] = None,
    ):
        self.running_rules = running_rules

    def validate(self):
        if self.running_rules:
            for v1 in self.running_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['runningRules'] = []
        if self.running_rules is not None:
            for k1 in self.running_rules:
                result['runningRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.running_rules = []
        if m.get('runningRules') is not None:
            for k1 in m.get('runningRules'):
                temp_model = main_models.GetRunningSqlConcurrencyControlRulesResponseBodyDataListRunningRules()
                self.running_rules.append(temp_model.from_map(k1))

        return self

class GetRunningSqlConcurrencyControlRulesResponseBodyDataListRunningRules(DaraModel):
    def __init__(
        self,
        concurrency_control_time: int = None,
        instance_id: str = None,
        item_id: int = None,
        keywords_hash: str = None,
        max_concurrency: str = None,
        sql_keywords: str = None,
        sql_type: str = None,
        start_time: int = None,
        status: str = None,
        user_id: str = None,
    ):
        # The duration within which the SQL throttling rule takes effect. Unit: seconds.
        # 
        # > The throttling rule takes effect only within this duration.
        self.concurrency_control_time = concurrency_control_time
        # The instance ID.
        self.instance_id = instance_id
        # The ID of the throttling rule that is applied to the instance.
        self.item_id = item_id
        # The hash value of the SQL keywords. The hash value is calculated based on the SQL keywords that are contained in the SQL statements to which the throttling rule is applied.
        self.keywords_hash = keywords_hash
        # The maximum number of concurrent SQL statements. The value is a positive integer.
        # 
        # > If the number of concurrent SQL statements that contain the specified keywords reaches this upper limit, the throttling rule is triggered.
        self.max_concurrency = max_concurrency
        # The keywords contained in the SQL statements to which the throttling rule was applied.
        # 
        # > SQL keywords are separated by tildes (~). If the number of concurrent SQL statements that contain all the specified SQL keywords reaches the specified upper limit, the throttling rule is triggered.
        self.sql_keywords = sql_keywords
        # The type of the SQL statements. Valid values:
        # 
        # * **SELECT**
        # * **UPDATE**
        # * **DELETE**
        self.sql_type = sql_type
        # The time when the throttling rule started to take effect. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The status of the throttling rule. The value of **Open** indicates that the throttling rule is in effect.
        self.status = status
        # The Alibaba Cloud account ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrency_control_time is not None:
            result['ConcurrencyControlTime'] = self.concurrency_control_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.keywords_hash is not None:
            result['KeywordsHash'] = self.keywords_hash

        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        if self.sql_keywords is not None:
            result['SqlKeywords'] = self.sql_keywords

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrencyControlTime') is not None:
            self.concurrency_control_time = m.get('ConcurrencyControlTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('KeywordsHash') is not None:
            self.keywords_hash = m.get('KeywordsHash')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('SqlKeywords') is not None:
            self.sql_keywords = m.get('SqlKeywords')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

