# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        deployed_revision_id: str = None,
        name: str = None,
        new_name: str = None,
        operation_name: str = None,
        parameters_shrink: str = None,
        region_id: str = None,
    ):
        # The application name.
        # 
        # This parameter is required.
        self.application_name = application_name
        self.deployed_revision_id = deployed_revision_id
        # The name of the application group.
        # 
        # This parameter is required.
        self.name = name
        # The new name of the application group.
        self.new_name = new_name
        # The name of the configuration update operation.
        self.operation_name = operation_name
        # The JSON string that consists of a set of parameters. Default value: {}.
        self.parameters_shrink = parameters_shrink
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.deployed_revision_id is not None:
            result['DeployedRevisionId'] = self.deployed_revision_id

        if self.name is not None:
            result['Name'] = self.name

        if self.new_name is not None:
            result['NewName'] = self.new_name

        if self.operation_name is not None:
            result['OperationName'] = self.operation_name

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('DeployedRevisionId') is not None:
            self.deployed_revision_id = m.get('DeployedRevisionId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NewName') is not None:
            self.new_name = m.get('NewName')

        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')

        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

