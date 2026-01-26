# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class SearchAlertHistoriesResponseBody(DaraModel):
    def __init__(
        self,
        page_bean: main_models.SearchAlertHistoriesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # The returned struct.
        self.page_bean = page_bean
        # The ID of the request.
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
            temp_model = main_models.SearchAlertHistoriesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m.get('PageBean'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SearchAlertHistoriesResponseBodyPageBean(DaraModel):
    def __init__(
        self,
        alarm_histories: List[main_models.SearchAlertHistoriesResponseBodyPageBeanAlarmHistories] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The information about alert records.
        self.alarm_histories = alarm_histories
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.alarm_histories:
            for v1 in self.alarm_histories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlarmHistories'] = []
        if self.alarm_histories is not None:
            for k1 in self.alarm_histories:
                result['AlarmHistories'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_histories = []
        if m.get('AlarmHistories') is not None:
            for k1 in m.get('AlarmHistories'):
                temp_model = main_models.SearchAlertHistoriesResponseBodyPageBeanAlarmHistories()
                self.alarm_histories.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SearchAlertHistoriesResponseBodyPageBeanAlarmHistories(DaraModel):
    def __init__(
        self,
        alarm_content: str = None,
        alarm_response_code: int = None,
        alarm_sources: str = None,
        alarm_time: int = None,
        alarm_type: int = None,
        emails: str = None,
        id: int = None,
        phones: str = None,
        strategy_id: str = None,
        target: str = None,
        user_id: str = None,
    ):
        # The content of the alert notification.
        self.alarm_content = alarm_content
        # The response code returned after the alert notification was sent.
        self.alarm_response_code = alarm_response_code
        # The webhook URL, such as the webhook URL of a DingTalk chatbot.
        self.alarm_sources = alarm_sources
        # The time when the alert notification was sent.
        self.alarm_time = alarm_time
        # The type of the alert rule. Default value: 4. Valid values:
        # 
        # *   `1`: a custom alert rule that is used to monitor drill-down data sets
        # *   `3`: a custom alert rule that is used to monitor tiled data sets
        # *   `4`: an alert rule that is used to monitor web pages, including the default alert rule for browser monitoring
        # *   `5`: an alert rule that is used to monitor applications, including the default alert rule for application monitoring
        # *   `6`: the default alert rule for browser monitoring
        # *   `7`: the default alert rule for application monitoring
        # *   `8`: a Tracing Analysis alert rule
        # *   `101`: a Prometheus alert rule
        self.alarm_type = alarm_type
        # The email address of the alert contact.
        self.emails = emails
        # The ID of the alert notification.
        self.id = id
        # The mobile phone number of the alert contact.
        self.phones = phones
        # The internal fields.
        self.strategy_id = strategy_id
        # The internal fields.
        self.target = target
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_content is not None:
            result['AlarmContent'] = self.alarm_content

        if self.alarm_response_code is not None:
            result['AlarmResponseCode'] = self.alarm_response_code

        if self.alarm_sources is not None:
            result['AlarmSources'] = self.alarm_sources

        if self.alarm_time is not None:
            result['AlarmTime'] = self.alarm_time

        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type

        if self.emails is not None:
            result['Emails'] = self.emails

        if self.id is not None:
            result['Id'] = self.id

        if self.phones is not None:
            result['Phones'] = self.phones

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.target is not None:
            result['Target'] = self.target

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmContent') is not None:
            self.alarm_content = m.get('AlarmContent')

        if m.get('AlarmResponseCode') is not None:
            self.alarm_response_code = m.get('AlarmResponseCode')

        if m.get('AlarmSources') is not None:
            self.alarm_sources = m.get('AlarmSources')

        if m.get('AlarmTime') is not None:
            self.alarm_time = m.get('AlarmTime')

        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')

        if m.get('Emails') is not None:
            self.emails = m.get('Emails')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Phones') is not None:
            self.phones = m.get('Phones')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

