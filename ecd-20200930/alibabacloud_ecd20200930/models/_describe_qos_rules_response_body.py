# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeQosRulesResponseBody(DaraModel):
    def __init__(
        self,
        qos_rules: List[main_models.DescribeQosRulesResponseBodyQosRules] = None,
        request_id: str = None,
    ):
        self.qos_rules = qos_rules
        self.request_id = request_id

    def validate(self):
        if self.qos_rules:
            for v1 in self.qos_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['QosRules'] = []
        if self.qos_rules is not None:
            for k1 in self.qos_rules:
                result['QosRules'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.qos_rules = []
        if m.get('QosRules') is not None:
            for k1 in m.get('QosRules'):
                temp_model = main_models.DescribeQosRulesResponseBodyQosRules()
                self.qos_rules.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeQosRulesResponseBodyQosRules(DaraModel):
    def __init__(
        self,
        desktop_count: str = None,
        download: str = None,
        network_package_id: str = None,
        qos_rule_id: str = None,
        qos_rule_name: str = None,
        upload: str = None,
    ):
        self.desktop_count = desktop_count
        self.download = download
        self.network_package_id = network_package_id
        self.qos_rule_id = qos_rule_id
        self.qos_rule_name = qos_rule_name
        self.upload = upload

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_count is not None:
            result['DesktopCount'] = self.desktop_count

        if self.download is not None:
            result['Download'] = self.download

        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id

        if self.qos_rule_id is not None:
            result['QosRuleId'] = self.qos_rule_id

        if self.qos_rule_name is not None:
            result['QosRuleName'] = self.qos_rule_name

        if self.upload is not None:
            result['Upload'] = self.upload

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopCount') is not None:
            self.desktop_count = m.get('DesktopCount')

        if m.get('Download') is not None:
            self.download = m.get('Download')

        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')

        if m.get('QosRuleId') is not None:
            self.qos_rule_id = m.get('QosRuleId')

        if m.get('QosRuleName') is not None:
            self.qos_rule_name = m.get('QosRuleName')

        if m.get('Upload') is not None:
            self.upload = m.get('Upload')

        return self

