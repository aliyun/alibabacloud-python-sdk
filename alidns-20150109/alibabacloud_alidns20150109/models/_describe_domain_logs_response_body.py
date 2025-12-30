# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainLogsResponseBody(DaraModel):
    def __init__(
        self,
        domain_logs: main_models.DescribeDomainLogsResponseBodyDomainLogs = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The operation logs.
        self.domain_logs = domain_logs
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.domain_logs:
            self.domain_logs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_logs is not None:
            result['DomainLogs'] = self.domain_logs.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainLogs') is not None:
            temp_model = main_models.DescribeDomainLogsResponseBodyDomainLogs()
            self.domain_logs = temp_model.from_map(m.get('DomainLogs'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDomainLogsResponseBodyDomainLogs(DaraModel):
    def __init__(
        self,
        domain_log: List[main_models.DescribeDomainLogsResponseBodyDomainLogsDomainLog] = None,
    ):
        self.domain_log = domain_log

    def validate(self):
        if self.domain_log:
            for v1 in self.domain_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainLog'] = []
        if self.domain_log is not None:
            for k1 in self.domain_log:
                result['DomainLog'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_log = []
        if m.get('DomainLog') is not None:
            for k1 in m.get('DomainLog'):
                temp_model = main_models.DescribeDomainLogsResponseBodyDomainLogsDomainLog()
                self.domain_log.append(temp_model.from_map(k1))

        return self

class DescribeDomainLogsResponseBodyDomainLogsDomainLog(DaraModel):
    def __init__(
        self,
        action: str = None,
        action_time: str = None,
        action_timestamp: int = None,
        client_ip: str = None,
        domain_name: str = None,
        message: str = None,
        zone_id: str = None,
    ):
        # The operation.
        self.action = action
        # The time when the operation is performed. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.action_time = action_time
        # The time when the operation was performed. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.action_timestamp = action_timestamp
        # The IP address of the operator.
        self.client_ip = client_ip
        # The domain name.
        self.domain_name = domain_name
        # The message for the operation.
        self.message = message
        # The ID of the private zone.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.action_time is not None:
            result['ActionTime'] = self.action_time

        if self.action_timestamp is not None:
            result['ActionTimestamp'] = self.action_timestamp

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.message is not None:
            result['Message'] = self.message

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ActionTime') is not None:
            self.action_time = m.get('ActionTime')

        if m.get('ActionTimestamp') is not None:
            self.action_timestamp = m.get('ActionTimestamp')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

