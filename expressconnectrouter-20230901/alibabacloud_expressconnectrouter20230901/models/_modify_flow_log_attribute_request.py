# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyFlowLogAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        flow_log_id: str = None,
        flow_log_name: str = None,
        interval: int = None,
        sampling_rate: str = None,
        version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the token on your client. Make sure that the token is unique across different requests. The client token supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is unique.
        self.client_token = client_token
        # The description of the flow log. The description can be empty or 0 to 256 characters in length.
        self.description = description
        # Specifies whether to perform a dry run on the request. Valid values:
        # 
        # - **true**: sends a dry run request. No EPS resource is modified.
        # 
        # - **false**: sends a normal request. This is the default value.
        self.dry_run = dry_run
        # The instance ID of the Express Connect Router (ECR).
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The instance ID of the flow log instance.
        # 
        # This parameter is required.
        self.flow_log_id = flow_log_id
        # The new name of the flow log. The name must be 0 to 128 characters in length.
        self.flow_log_name = flow_log_name
        # The duration of the capture window for the flow log to capture traffic. Unit: seconds. Valid values:
        # 
        # - **60** 
        # - **600**
        # 
        # Default value: **600**.
        self.interval = interval
        # The sampling rate. Valid values:
        # 
        # - **1:4096**
        # - **1:2048**
        # - **1:1024**
        # 
        # Default value: **1:4096**.
        self.sampling_rate = sampling_rate
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id

        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')

        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

