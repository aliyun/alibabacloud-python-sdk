# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyParametersRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        force_restart_instance: bool = None,
        parameters: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Specifies whether to forcibly restart the instance. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.force_restart_instance = force_restart_instance
        # The name and value of the parameter to be modified. Specify the parameter in the `<Parameter name>:<Parameter value>` format.
        # 
        # You can call the [DescribeParameters](https://help.aliyun.com/document_detail/208310.html) operation to query the parameters that can be modified.
        # 
        # This parameter is required.
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.force_restart_instance is not None:
            result['ForceRestartInstance'] = self.force_restart_instance

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ForceRestartInstance') is not None:
            self.force_restart_instance = m.get('ForceRestartInstance')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        return self

