# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class ModifyCfwInstanceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        update_list: List[main_models.ModifyCfwInstanceRequestUpdateList] = None,
    ):
        # The ID of the Cloud Firewall instance.
        self.instance_id = instance_id
        # A list of instance properties to update.
        self.update_list = update_list

    def validate(self):
        if self.update_list:
            for v1 in self.update_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['UpdateList'] = []
        if self.update_list is not None:
            for k1 in self.update_list:
                result['UpdateList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.update_list = []
        if m.get('UpdateList') is not None:
            for k1 in m.get('UpdateList'):
                temp_model = main_models.ModifyCfwInstanceRequestUpdateList()
                self.update_list.append(temp_model.from_map(k1))

        return self

class ModifyCfwInstanceRequestUpdateList(DaraModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        # The code of the instance property to update.
        # The following codes are supported:
        # 
        # - \\`Code\\`: \\`MajorVersion\\`. Set \\`Value\\` to \\`2\\`. This is available only for pay-as-you-go 1.0 users to upgrade their instances to pay-as-you-go 2.0.
        # 
        #   >Warning: 
        # 
        #   Make sure you understand the billing methods and pricing of pay-as-you-go 2.0.
        # 
        #   
        # 
        #   >Warning: 
        # 
        #   Note that if log delivery is enabled before the upgrade, it will remain enabled after the upgrade, and logs will be delivered to a new Logstore.
        # 
        #   
        # 
        # - \\`Code\\`: \\`ThreatIntelligence\\`. This is available only for pay-as-you-go 2.0 users to enable or disable the threat intelligence feature. Set \\`Value\\` to \\`1\\` to enable the feature or \\`0\\` to disable it.
        # 
        # - \\`Code\\`: \\`Sdl\\`. This is available only for pay-as-you-go 2.0 users to enable or disable the sensitive data leak detection feature. Set \\`Value\\` to \\`1\\` to enable the feature or \\`0\\` to disable it.
        self.code = code
        # The value for the specified \\`Code\\`. For valid values, see the description of the \\`Code\\` parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

