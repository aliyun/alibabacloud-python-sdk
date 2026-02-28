# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LaunchAuthenticationRequest(DaraModel):
    def __init__(
        self,
        contact_flow_id: str = None,
        contact_flow_variables: str = None,
        device_id: str = None,
        instance_id: str = None,
        job_id: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.contact_flow_id = contact_flow_id
        self.contact_flow_variables = contact_flow_variables
        self.device_id = device_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.job_id = job_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_flow_id is not None:
            result['ContactFlowId'] = self.contact_flow_id

        if self.contact_flow_variables is not None:
            result['ContactFlowVariables'] = self.contact_flow_variables

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactFlowId') is not None:
            self.contact_flow_id = m.get('ContactFlowId')

        if m.get('ContactFlowVariables') is not None:
            self.contact_flow_variables = m.get('ContactFlowVariables')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

