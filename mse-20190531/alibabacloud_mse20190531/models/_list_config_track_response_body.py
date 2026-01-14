# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListConfigTrackResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        traces: List[main_models.ListConfigTrackResponseBodyTraces] = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code returned.
        self.http_code = http_code
        # The message returned.
        self.message = message
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count
        # The track data.
        self.traces = traces

    def validate(self):
        if self.traces:
            for v1 in self.traces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Traces'] = []
        if self.traces is not None:
            for k1 in self.traces:
                result['Traces'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.traces = []
        if m.get('Traces') is not None:
            for k1 in m.get('Traces'):
                temp_model = main_models.ListConfigTrackResponseBodyTraces()
                self.traces.append(temp_model.from_map(k1))

        return self

class ListConfigTrackResponseBodyTraces(DaraModel):
    def __init__(
        self,
        client: bool = None,
        data_id: str = None,
        delay: str = None,
        event: str = None,
        group: str = None,
        log_date: str = None,
        md_5: str = None,
        push: bool = None,
        request_ip: str = None,
        response_ip: str = None,
        result: str = None,
        ts: str = None,
        type: str = None,
    ):
        # Indicates whether the request is sent from the client. Valid values:
        # 
        # *   true
        # *   false
        self.client = client
        # The ID of the configuration.
        self.data_id = data_id
        # The response latency. Unit: milliseconds.
        self.delay = delay
        # The event. Valid values:
        # 
        # *   pull: configuration acquisition events
        # *   persist: persistence events
        self.event = event
        # The name of the configuration group.
        self.group = group
        # The logging time.
        self.log_date = log_date
        # The MD5 value.
        self.md_5 = md_5
        # Indicates whether messages are pushed by a server. Valid values:
        # 
        # *   true
        # *   false
        self.push = push
        # The source IP address of the request.
        self.request_ip = request_ip
        # The response node.
        self.response_ip = response_ip
        # The result.
        self.result = result
        # The timestamp that indicates the time when the metric value is collected.
        # 
        # Unit: seconds.
        self.ts = ts
        # The release type. Valid values:
        # 
        # *   beta: beta release
        # *   tag: canary release
        # *   batch: batch release
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client is not None:
            result['Client'] = self.client

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.delay is not None:
            result['Delay'] = self.delay

        if self.event is not None:
            result['Event'] = self.event

        if self.group is not None:
            result['Group'] = self.group

        if self.log_date is not None:
            result['LogDate'] = self.log_date

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.push is not None:
            result['Push'] = self.push

        if self.request_ip is not None:
            result['RequestIp'] = self.request_ip

        if self.response_ip is not None:
            result['ResponseIp'] = self.response_ip

        if self.result is not None:
            result['Result'] = self.result

        if self.ts is not None:
            result['Ts'] = self.ts

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Client') is not None:
            self.client = m.get('Client')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('LogDate') is not None:
            self.log_date = m.get('LogDate')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('Push') is not None:
            self.push = m.get('Push')

        if m.get('RequestIp') is not None:
            self.request_ip = m.get('RequestIp')

        if m.get('ResponseIp') is not None:
            self.response_ip = m.get('ResponseIp')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Ts') is not None:
            self.ts = m.get('Ts')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

