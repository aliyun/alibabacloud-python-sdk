# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDatabaseInstanceParameterRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        database_instance_id: str = None,
        force_restart: bool = None,
        parameters: str = None,
        region_id: str = None,
    ):
        # A client-generated token to ensure request idempotence. You must ensure that the token is unique for each request. It can contain only ASCII characters and cannot be longer than 64 characters. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The ID of the database instance.
        # 
        # This parameter is required.
        self.database_instance_id = database_instance_id
        # Specifies whether to restart the database for the parameter changes to take effect. Valid values:
        # 
        # - true: Forces a restart. Set this to true if any modified parameter requires a restart to take effect. Otherwise, the change will not take effect.
        # 
        # - false: Do not force a restart.
        # 
        # Default value: false.
        self.force_restart = force_restart
        # A JSON string that specifies the database parameters and their values. The value for each parameter must be a string. Format: `{"ParameterName1":"Value1","ParameterName2":"Value2",...}`.
        # 
        # This parameter is required.
        self.parameters = parameters
        # The region ID of the database instance. Call [ListRegions](https://help.aliyun.com/document_detail/189315.html) to view the supported Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id

        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')

        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

