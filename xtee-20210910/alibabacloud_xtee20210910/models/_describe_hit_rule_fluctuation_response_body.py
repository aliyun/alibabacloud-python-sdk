# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeHitRuleFluctuationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: List[main_models.DescribeHitRuleFluctuationResponseBodyResultObject] = None,
        success: bool = None,
    ):
        # Status code.
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Return object
        self.result_object = result_object
        # Whether the request was successful.
        self.success = success

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeHitRuleFluctuationResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class DescribeHitRuleFluctuationResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        rule_id: str = None,
        rule_name: str = None,
        today_num: int = None,
        within_seven_day_num: str = None,
        within_thirty_day_num: str = None,
        within_three_day_num: str = None,
        yesterday_num: int = None,
    ):
        # Policy ID
        self.rule_id = rule_id
        # Policy name
        self.rule_name = rule_name
        # Today\\"s count
        self.today_num = today_num
        # Count within seven days
        self.within_seven_day_num = within_seven_day_num
        # Count within thirty days
        self.within_thirty_day_num = within_thirty_day_num
        # Count within three days
        self.within_three_day_num = within_three_day_num
        # Yesterday\\"s count
        self.yesterday_num = yesterday_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        if self.today_num is not None:
            result['todayNum'] = self.today_num

        if self.within_seven_day_num is not None:
            result['withinSevenDayNum'] = self.within_seven_day_num

        if self.within_thirty_day_num is not None:
            result['withinThirtyDayNum'] = self.within_thirty_day_num

        if self.within_three_day_num is not None:
            result['withinThreeDayNum'] = self.within_three_day_num

        if self.yesterday_num is not None:
            result['yesterdayNum'] = self.yesterday_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        if m.get('todayNum') is not None:
            self.today_num = m.get('todayNum')

        if m.get('withinSevenDayNum') is not None:
            self.within_seven_day_num = m.get('withinSevenDayNum')

        if m.get('withinThirtyDayNum') is not None:
            self.within_thirty_day_num = m.get('withinThirtyDayNum')

        if m.get('withinThreeDayNum') is not None:
            self.within_three_day_num = m.get('withinThreeDayNum')

        if m.get('yesterdayNum') is not None:
            self.yesterday_num = m.get('yesterdayNum')

        return self

