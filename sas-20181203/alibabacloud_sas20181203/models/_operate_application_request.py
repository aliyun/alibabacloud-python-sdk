# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class OperateApplicationRequest(DaraModel):
    def __init__(
        self,
        container_web_defense_application_dtos: List[main_models.OperateApplicationRequestContainerWebDefenseApplicationDTOS] = None,
        rule_id: int = None,
    ):
        # The container application that is protected from being tampered with.
        # 
        # This parameter is required.
        self.container_web_defense_application_dtos = container_web_defense_application_dtos
        # The ID of the rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        if self.container_web_defense_application_dtos:
            for v1 in self.container_web_defense_application_dtos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContainerWebDefenseApplicationDTOS'] = []
        if self.container_web_defense_application_dtos is not None:
            for k1 in self.container_web_defense_application_dtos:
                result['ContainerWebDefenseApplicationDTOS'].append(k1.to_map() if k1 else None)

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.container_web_defense_application_dtos = []
        if m.get('ContainerWebDefenseApplicationDTOS') is not None:
            for k1 in m.get('ContainerWebDefenseApplicationDTOS'):
                temp_model = main_models.OperateApplicationRequestContainerWebDefenseApplicationDTOS()
                self.container_web_defense_application_dtos.append(temp_model.from_map(k1))

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

class OperateApplicationRequestContainerWebDefenseApplicationDTOS(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        flag: str = None,
        id: int = None,
        tag: str = None,
    ):
        # The ID of the cluster to which the container belongs.
        # 
        # >  You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Specifies whether to apply the configuration to the asset. Valid values:
        # 
        # *   **add**: applied
        # *   **del**: not applied
        # 
        # This parameter is required.
        self.flag = flag
        # The application ID. If the application is newly added, you do not need to specify this parameter.
        self.id = id
        # The value of the application tag.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.flag is not None:
            result['Flag'] = self.flag

        if self.id is not None:
            result['Id'] = self.id

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Flag') is not None:
            self.flag = m.get('Flag')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

