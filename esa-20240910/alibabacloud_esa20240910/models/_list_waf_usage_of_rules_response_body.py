# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListWafUsageOfRulesResponseBody(DaraModel):
    def __init__(
        self,
        batch_config_usage: int = None,
        instance_usage: int = None,
        request_id: str = None,
        sites: List[main_models.ListWafUsageOfRulesResponseBodySites] = None,
    ):
        self.batch_config_usage = batch_config_usage
        self.instance_usage = instance_usage
        # Request ID.
        self.request_id = request_id
        # List of site usage.
        self.sites = sites

    def validate(self):
        if self.sites:
            for v1 in self.sites:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_config_usage is not None:
            result['BatchConfigUsage'] = self.batch_config_usage

        if self.instance_usage is not None:
            result['InstanceUsage'] = self.instance_usage

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Sites'] = []
        if self.sites is not None:
            for k1 in self.sites:
                result['Sites'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchConfigUsage') is not None:
            self.batch_config_usage = m.get('BatchConfigUsage')

        if m.get('InstanceUsage') is not None:
            self.instance_usage = m.get('InstanceUsage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sites = []
        if m.get('Sites') is not None:
            for k1 in m.get('Sites'):
                temp_model = main_models.ListWafUsageOfRulesResponseBodySites()
                self.sites.append(temp_model.from_map(k1))

        return self

class ListWafUsageOfRulesResponseBodySites(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        usage: int = None,
    ):
        # Site ID.
        self.id = id
        # Site name.
        self.name = name
        # Usage of WAF rules/WAF rule sets.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

