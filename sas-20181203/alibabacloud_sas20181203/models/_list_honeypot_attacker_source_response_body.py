# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListHoneypotAttackerSourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        list: List[main_models.ListHoneypotAttackerSourceResponseBodyList] = None,
        message: str = None,
        page_info: main_models.ListHoneypotAttackerSourceResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The HTTP status code that is returned.
        self.http_status_code = http_status_code
        # The source IP addresses of the attack.
        self.list = list
        # The returned message.
        self.message = message
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListHoneypotAttackerSourceResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListHoneypotAttackerSourceResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListHoneypotAttackerSourceResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListHoneypotAttackerSourceResponseBodyList(DaraModel):
    def __init__(
        self,
        event_count: int = None,
        last_target_honeypot: str = None,
        last_target_ip: str = None,
        last_time: int = None,
        risk_level: str = None,
        src_ip: str = None,
    ):
        # The total number of attack events.
        self.event_count = event_count
        # The most recent honeypot that was attacked.
        self.last_target_honeypot = last_target_honeypot
        # The most recent IP address that was attacked.
        self.last_target_ip = last_target_ip
        # The last time when the attack event occurred.
        self.last_time = last_time
        # The risk level. Valid values:
        # 
        # *   **2**: low
        # *   **3**: medium
        # *   **4**: high
        self.risk_level = risk_level
        # The source IP address of the attack.
        self.src_ip = src_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_count is not None:
            result['EventCount'] = self.event_count

        if self.last_target_honeypot is not None:
            result['LastTargetHoneypot'] = self.last_target_honeypot

        if self.last_target_ip is not None:
            result['LastTargetIp'] = self.last_target_ip

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')

        if m.get('LastTargetHoneypot') is not None:
            self.last_target_honeypot = m.get('LastTargetHoneypot')

        if m.get('LastTargetIp') is not None:
            self.last_target_ip = m.get('LastTargetIp')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        return self

