# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListHoneypotAttackerPortraitResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        list: List[main_models.ListHoneypotAttackerPortraitResponseBodyList] = None,
        message: str = None,
        page_info: main_models.ListHoneypotAttackerPortraitResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code that is returned. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the attacker profile.
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
                temp_model = main_models.ListHoneypotAttackerPortraitResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListHoneypotAttackerPortraitResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListHoneypotAttackerPortraitResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
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

class ListHoneypotAttackerPortraitResponseBodyList(DaraModel):
    def __init__(
        self,
        attack_count: int = None,
        browser: List[str] = None,
        host: List[str] = None,
        last_time: int = None,
        network: main_models.ListHoneypotAttackerPortraitResponseBodyListNetwork = None,
        portrait_id: str = None,
        social: List[str] = None,
    ):
        # The number of attacks.
        self.attack_count = attack_count
        # The information about the browsers of the attack source.
        self.browser = browser
        # The information about the hosts of the attack source.
        self.host = host
        # The timestamp at which the attack was last detected. Unit: milliseconds.
        self.last_time = last_time
        # The network information about the attack source.
        self.network = network
        # The attacker profile ID.
        self.portrait_id = portrait_id
        # The social information about the attack source.
        self.social = social

    def validate(self):
        if self.network:
            self.network.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_count is not None:
            result['AttackCount'] = self.attack_count

        if self.browser is not None:
            result['Browser'] = self.browser

        if self.host is not None:
            result['Host'] = self.host

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.network is not None:
            result['Network'] = self.network.to_map()

        if self.portrait_id is not None:
            result['PortraitId'] = self.portrait_id

        if self.social is not None:
            result['Social'] = self.social

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackCount') is not None:
            self.attack_count = m.get('AttackCount')

        if m.get('Browser') is not None:
            self.browser = m.get('Browser')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('Network') is not None:
            temp_model = main_models.ListHoneypotAttackerPortraitResponseBodyListNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('PortraitId') is not None:
            self.portrait_id = m.get('PortraitId')

        if m.get('Social') is not None:
            self.social = m.get('Social')

        return self

class ListHoneypotAttackerPortraitResponseBodyListNetwork(DaraModel):
    def __init__(
        self,
        external_ip: List[str] = None,
        internal_ip: List[str] = None,
        real_ip: List[str] = None,
    ):
        # The public IP addresses.
        self.external_ip = external_ip
        # The private IP addresses.
        self.internal_ip = internal_ip
        # The originating IP addresses.
        self.real_ip = real_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip

        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip

        if self.real_ip is not None:
            result['RealIp'] = self.real_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')

        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')

        if m.get('RealIp') is not None:
            self.real_ip = m.get('RealIp')

        return self

