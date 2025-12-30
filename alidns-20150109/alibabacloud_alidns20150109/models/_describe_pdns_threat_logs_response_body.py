# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribePdnsThreatLogsResponseBody(DaraModel):
    def __init__(
        self,
        logs: List[main_models.DescribePdnsThreatLogsResponseBodyLogs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.logs = logs
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

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
        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.DescribePdnsThreatLogsResponseBodyLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePdnsThreatLogsResponseBodyLogs(DaraModel):
    def __init__(
        self,
        source_ip: str = None,
        sub_domain: str = None,
        threat_level: str = None,
        threat_time: str = None,
        threat_type: str = None,
    ):
        self.source_ip = source_ip
        self.sub_domain = sub_domain
        self.threat_level = threat_level
        self.threat_time = threat_time
        self.threat_type = threat_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain

        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        if self.threat_time is not None:
            result['ThreatTime'] = self.threat_time

        if self.threat_type is not None:
            result['ThreatType'] = self.threat_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        if m.get('ThreatTime') is not None:
            self.threat_time = m.get('ThreatTime')

        if m.get('ThreatType') is not None:
            self.threat_type = m.get('ThreatType')

        return self

