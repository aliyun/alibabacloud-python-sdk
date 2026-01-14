# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListListenersByConfigResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        http_code: str = None,
        listeners: List[main_models.ListListenersByConfigResponseBodyListeners] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code returned.
        self.http_code = http_code
        # The information about listeners.
        self.listeners = listeners
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

    def validate(self):
        if self.listeners:
            for v1 in self.listeners:
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

        result['Listeners'] = []
        if self.listeners is not None:
            for k1 in self.listeners:
                result['Listeners'].append(k1.to_map() if k1 else None)

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        self.listeners = []
        if m.get('Listeners') is not None:
            for k1 in m.get('Listeners'):
                temp_model = main_models.ListListenersByConfigResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k1))

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

        return self

class ListListenersByConfigResponseBodyListeners(DaraModel):
    def __init__(
        self,
        ip: str = None,
        labels: Dict[str, str] = None,
        match_rule_name: str = None,
        match_rule_type: str = None,
        md_5: str = None,
        status: str = None,
        version: str = None,
    ):
        # The IP address.
        self.ip = ip
        # The label of the listener.
        self.labels = labels
        self.match_rule_name = match_rule_name
        self.match_rule_type = match_rule_type
        # The verification string.
        self.md_5 = md_5
        # The status.
        self.status = status
        # The current version of the listener. Valid values: gray and normal.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.match_rule_name is not None:
            result['MatchRuleName'] = self.match_rule_name

        if self.match_rule_type is not None:
            result['MatchRuleType'] = self.match_rule_type

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('MatchRuleName') is not None:
            self.match_rule_name = m.get('MatchRuleName')

        if m.get('MatchRuleType') is not None:
            self.match_rule_type = m.get('MatchRuleType')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

