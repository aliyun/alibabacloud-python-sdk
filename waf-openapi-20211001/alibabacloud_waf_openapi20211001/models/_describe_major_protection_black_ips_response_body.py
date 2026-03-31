# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeMajorProtectionBlackIpsResponseBody(DaraModel):
    def __init__(
        self,
        ip_list: List[main_models.DescribeMajorProtectionBlackIpsResponseBodyIpList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array of IP addresses in the IP address blacklist.
        self.ip_list = ip_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of IP addresses in the blacklist.
        self.total_count = total_count

    def validate(self):
        if self.ip_list:
            for v1 in self.ip_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpList'] = []
        if self.ip_list is not None:
            for k1 in self.ip_list:
                result['IpList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_list = []
        if m.get('IpList') is not None:
            for k1 in m.get('IpList'):
                temp_model = main_models.DescribeMajorProtectionBlackIpsResponseBodyIpList()
                self.ip_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeMajorProtectionBlackIpsResponseBodyIpList(DaraModel):
    def __init__(
        self,
        description: str = None,
        expired_time: int = None,
        gmt_modified: int = None,
        ip: str = None,
        rule_id: int = None,
        template_id: int = None,
    ):
        # The description of the IP address in the blacklist.
        self.description = description
        # The time after which the IP address blacklist becomes invalid. Unit: seconds.
        # 
        # >  If the value of this parameter is **0**, the blacklist is permanently valid.
        self.expired_time = expired_time
        # The most recent time when the IP address blacklist was modified.
        self.gmt_modified = gmt_modified
        # The IP address in the IP address blacklist.
        self.ip = ip
        # The ID of the IP address blacklist rule for major event protection.
        self.rule_id = rule_id
        # The ID of the rule template for major event protection.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

