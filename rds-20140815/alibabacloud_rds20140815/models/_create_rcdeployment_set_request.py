# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class CreateRCDeploymentSetRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        deployment_set_name: str = None,
        description: str = None,
        group_count: int = None,
        on_unable_to_redeploy_failed_instance: str = None,
        region_id: str = None,
        strategy: str = None,
        tag: List[main_models.CreateRCDeploymentSetRequestTag] = None,
    ):
        self.client_token = client_token
        self.deployment_set_name = deployment_set_name
        self.description = description
        self.group_count = group_count
        self.on_unable_to_redeploy_failed_instance = on_unable_to_redeploy_failed_instance
        # This parameter is required.
        self.region_id = region_id
        self.strategy = strategy
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.deployment_set_name is not None:
            result['DeploymentSetName'] = self.deployment_set_name

        if self.description is not None:
            result['Description'] = self.description

        if self.group_count is not None:
            result['GroupCount'] = self.group_count

        if self.on_unable_to_redeploy_failed_instance is not None:
            result['OnUnableToRedeployFailedInstance'] = self.on_unable_to_redeploy_failed_instance

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeploymentSetName') is not None:
            self.deployment_set_name = m.get('DeploymentSetName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupCount') is not None:
            self.group_count = m.get('GroupCount')

        if m.get('OnUnableToRedeployFailedInstance') is not None:
            self.on_unable_to_redeploy_failed_instance = m.get('OnUnableToRedeployFailedInstance')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateRCDeploymentSetRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateRCDeploymentSetRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

