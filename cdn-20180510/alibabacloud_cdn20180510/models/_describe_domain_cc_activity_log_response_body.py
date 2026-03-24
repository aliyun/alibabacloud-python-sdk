# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainCcActivityLogResponseBody(DaraModel):
    def __init__(
        self,
        activity_log: List[main_models.DescribeDomainCcActivityLogResponseBodyActivityLog] = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The list of rate limiting logs.
        self.activity_log = activity_log
        # The page number of the returned page.
        self.page_index = page_index
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.activity_log:
            for v1 in self.activity_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ActivityLog'] = []
        if self.activity_log is not None:
            for k1 in self.activity_log:
                result['ActivityLog'].append(k1.to_map() if k1 else None)

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.activity_log = []
        if m.get('ActivityLog') is not None:
            for k1 in m.get('ActivityLog'):
                temp_model = main_models.DescribeDomainCcActivityLogResponseBodyActivityLog()
                self.activity_log.append(temp_model.from_map(k1))

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeDomainCcActivityLogResponseBodyActivityLog(DaraModel):
    def __init__(
        self,
        action: str = None,
        domain_name: str = None,
        rule_name: str = None,
        time_stamp: str = None,
        trigger_object: str = None,
        ttl: int = None,
        value: str = None,
    ):
        # The action that was triggered.
        self.action = action
        # The accelerated domain name.
        self.domain_name = domain_name
        # The name of the rule based on which rate limiting was triggered.
        self.rule_name = rule_name
        # The timestamp of the data returned.
        self.time_stamp = time_stamp
        # The trigger of rate limiting.
        self.trigger_object = trigger_object
        # The period of time during which rate limiting remains effective.
        self.ttl = ttl
        # The value of the trigger for rate limiting.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.trigger_object is not None:
            result['TriggerObject'] = self.trigger_object

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('TriggerObject') is not None:
            self.trigger_object = m.get('TriggerObject')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

