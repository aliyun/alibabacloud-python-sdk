# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class EnDisableScalingRulesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.EnDisableScalingRulesResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.EnDisableScalingRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class EnDisableScalingRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        db_instance_id: str = None,
        scaling_rules_enable: bool = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The instance ID.
        self.db_instance_id = db_instance_id
        # Indicates whether the scheduled scaling policy is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.scaling_rules_enable = scaling_rules_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.scaling_rules_enable is not None:
            result['ScalingRulesEnable'] = self.scaling_rules_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('ScalingRulesEnable') is not None:
            self.scaling_rules_enable = m.get('ScalingRulesEnable')

        return self

