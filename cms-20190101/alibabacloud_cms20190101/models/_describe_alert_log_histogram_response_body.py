# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeAlertLogHistogramResponseBody(DaraModel):
    def __init__(
        self,
        alert_log_histogram_list: List[main_models.DescribeAlertLogHistogramResponseBodyAlertLogHistogramList] = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The number of alert logs that were generated during each interval of a time period.
        self.alert_log_histogram_list = alert_log_histogram_list
        # The response code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.alert_log_histogram_list:
            for v1 in self.alert_log_histogram_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertLogHistogramList'] = []
        if self.alert_log_histogram_list is not None:
            for k1 in self.alert_log_histogram_list:
                result['AlertLogHistogramList'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_log_histogram_list = []
        if m.get('AlertLogHistogramList') is not None:
            for k1 in m.get('AlertLogHistogramList'):
                temp_model = main_models.DescribeAlertLogHistogramResponseBodyAlertLogHistogramList()
                self.alert_log_histogram_list.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeAlertLogHistogramResponseBodyAlertLogHistogramList(DaraModel):
    def __init__(
        self,
        count: int = None,
        from_: int = None,
        to: int = None,
    ):
        # The number of alert logs.
        self.count = count
        # The start timestamp of the queried alert logs.
        # 
        # Unit: seconds.
        self.from_ = from_
        # The end timestamp of the queried alert logs.
        # 
        # Unit: seconds.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.from_ is not None:
            result['From'] = self.from_

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

