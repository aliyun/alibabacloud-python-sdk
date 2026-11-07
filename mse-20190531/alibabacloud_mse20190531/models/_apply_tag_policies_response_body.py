# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ApplyTagPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ApplyTagPoliciesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data overview.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The request result.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ApplyTagPoliciesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ApplyTagPoliciesResponseBodyData(DaraModel):
    def __init__(
        self,
        carry_data: bool = None,
        enable: bool = None,
        id: int = None,
        instance_num: int = None,
        name: str = None,
        rate: int = None,
        remove: bool = None,
        rules: str = None,
        status: int = None,
        tag: str = None,
    ):
        # Indicates whether it is a primary key.
        self.carry_data = carry_data
        # Indicates whether the feature is enabled. Valid values:
        # 
        # - `true`: Enabled.
        # - `false`: Disabled.
        self.enable = enable
        # The primary key ID.
        self.id = id
        # The number of instances.
        self.instance_num = instance_num
        # The policy name.
        self.name = name
        # The ratio.
        self.rate = rate
        # Indicates whether the deletion is successful.
        self.remove = remove
        # The tag rules.
        self.rules = rules
        # The effective status.
        self.status = status
        # The tag.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carry_data is not None:
            result['CarryData'] = self.carry_data

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_num is not None:
            result['InstanceNum'] = self.instance_num

        if self.name is not None:
            result['Name'] = self.name

        if self.rate is not None:
            result['Rate'] = self.rate

        if self.remove is not None:
            result['Remove'] = self.remove

        if self.rules is not None:
            result['Rules'] = self.rules

        if self.status is not None:
            result['Status'] = self.status

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CarryData') is not None:
            self.carry_data = m.get('CarryData')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceNum') is not None:
            self.instance_num = m.get('InstanceNum')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('Remove') is not None:
            self.remove = m.get('Remove')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

