# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeMaskingRulesResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        data: main_models.DescribeMaskingRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # The result data that is returned.
        self.data = data
        # The message that is returned for the request.
        # 
        # > If the request is successful, Successful is returned. If the request fails, an error message such as an error code is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid value:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeMaskingRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeMaskingRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        rule_list: List[str] = None,
        rule_version: str = None,
    ):
        # Details about the masking rules.
        self.rule_list = rule_list
        # The version of the masking rule. Valid values: v1 and v2. Default value: v1
        self.rule_version = rule_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_list is not None:
            result['RuleList'] = self.rule_list

        if self.rule_version is not None:
            result['RuleVersion'] = self.rule_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleList') is not None:
            self.rule_list = m.get('RuleList')

        if m.get('RuleVersion') is not None:
            self.rule_version = m.get('RuleVersion')

        return self

