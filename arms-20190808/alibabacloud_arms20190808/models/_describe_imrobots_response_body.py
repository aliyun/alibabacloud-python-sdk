# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class DescribeIMRobotsResponseBody(DaraModel):
    def __init__(
        self,
        page_bean: main_models.DescribeIMRobotsResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # The returned objects.
        self.page_bean = page_bean
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = main_models.DescribeIMRobotsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m.get('PageBean'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeIMRobotsResponseBodyPageBean(DaraModel):
    def __init__(
        self,
        alert_imrobots: List[main_models.DescribeIMRobotsResponseBodyPageBeanAlertIMRobots] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        # The queried IM chatbots.
        self.alert_imrobots = alert_imrobots
        # The page number of the returned page.
        self.page = page
        # The number of IM chatbots returned per page.
        self.size = size
        # The total number of queried IM chatbots.
        self.total = total

    def validate(self):
        if self.alert_imrobots:
            for v1 in self.alert_imrobots:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertIMRobots'] = []
        if self.alert_imrobots is not None:
            for k1 in self.alert_imrobots:
                result['AlertIMRobots'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_imrobots = []
        if m.get('AlertIMRobots') is not None:
            for k1 in m.get('AlertIMRobots'):
                temp_model = main_models.DescribeIMRobotsResponseBodyPageBeanAlertIMRobots()
                self.alert_imrobots.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeIMRobotsResponseBodyPageBeanAlertIMRobots(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        daily_noc: bool = None,
        daily_noc_time: str = None,
        ding_sign_key: str = None,
        dispatch_rules: List[main_models.DescribeIMRobotsResponseBodyPageBeanAlertIMRobotsDispatchRules] = None,
        robot_addr: str = None,
        robot_id: float = None,
        robot_name: str = None,
        type: str = None,
    ):
        # The time when the IM chatbot was created.
        self.create_time = create_time
        # Indicates whether daily statistics are sent. Valid values:
        # 
        # *   `false` (default): Daily statistics are not sent.
        # *   `true`: Daily statistics are sent.
        self.daily_noc = daily_noc
        # The point in time at which the daily statistics are sent. The information that ARMS sends at the specified points in time includes the total number of alerts generated on the current day, the number of cleared alerts, and the number of alerts to be cleared.
        self.daily_noc_time = daily_noc_time
        # The signature key of DingTalk. If you specify a signature key, DingTalk authentication is performed by using the signature key. If you do not specify a signature key, a whitelist is used for authentication by default. The keyword of the whitelist is **Alert**.
        self.ding_sign_key = ding_sign_key
        # The notification policies.
        self.dispatch_rules = dispatch_rules
        # The webhook URL of the IM chatbot.
        self.robot_addr = robot_addr
        # The ID of the IM chatbot.
        self.robot_id = robot_id
        # The name of the IM chatbot.
        self.robot_name = robot_name
        # The type of the IM chatbot. Valid values:
        # 
        # *   `dingding`: DingTalk chatbot
        # *   `wechat`: WeCom chatbot
        self.type = type

    def validate(self):
        if self.dispatch_rules:
            for v1 in self.dispatch_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.daily_noc is not None:
            result['DailyNoc'] = self.daily_noc

        if self.daily_noc_time is not None:
            result['DailyNocTime'] = self.daily_noc_time

        if self.ding_sign_key is not None:
            result['DingSignKey'] = self.ding_sign_key

        result['DispatchRules'] = []
        if self.dispatch_rules is not None:
            for k1 in self.dispatch_rules:
                result['DispatchRules'].append(k1.to_map() if k1 else None)

        if self.robot_addr is not None:
            result['RobotAddr'] = self.robot_addr

        if self.robot_id is not None:
            result['RobotId'] = self.robot_id

        if self.robot_name is not None:
            result['RobotName'] = self.robot_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DailyNoc') is not None:
            self.daily_noc = m.get('DailyNoc')

        if m.get('DailyNocTime') is not None:
            self.daily_noc_time = m.get('DailyNocTime')

        if m.get('DingSignKey') is not None:
            self.ding_sign_key = m.get('DingSignKey')

        self.dispatch_rules = []
        if m.get('DispatchRules') is not None:
            for k1 in m.get('DispatchRules'):
                temp_model = main_models.DescribeIMRobotsResponseBodyPageBeanAlertIMRobotsDispatchRules()
                self.dispatch_rules.append(temp_model.from_map(k1))

        if m.get('RobotAddr') is not None:
            self.robot_addr = m.get('RobotAddr')

        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')

        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeIMRobotsResponseBodyPageBeanAlertIMRobotsDispatchRules(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The ID of the notification policy.
        self.id = id
        # The name of the notification policy.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

