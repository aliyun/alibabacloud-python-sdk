# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConnectorProperties(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        dry_run_request_body: str = None,
        max_retries: str = None,
        model_list: str = None,
        network: str = None,
        protocol: str = None,
        qps_limit: str = None,
        region: str = None,
        response_body_path: str = None,
        security_group_id: str = None,
        timeout_ms: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The channel type: custom or apig. This parameter is optional for model_service and defaults to custom.
        self.channel_type = channel_type
        # The sample request body provided by the user for verifying endpoint connectivity. This parameter is required when dryRun is set to All and type is set to agent_app. The value is not persisted.
        self.dry_run_request_body = dry_run_request_body
        # The number of retries after a failed invocation of the dial-test registration service. Valid values: 0 to 10. Default value: 3.
        self.max_retries = max_retries
        # The list of supported models in comma-separated format. This parameter is required for model_service.
        self.model_list = model_list
        # The network type: internet or aliyun-vpc.
        self.network = network
        # The protocol type: openai, openai-compatible, or anthropic. This parameter is required for model_service.
        self.protocol = protocol
        # The QPS limit for the dial-test registration service. A value of 0 indicates no throttling. Otherwise, valid values: 0.1 to 1000. Default value: 20 for agent_app, 100 for model_service.
        self.qps_limit = qps_limit
        # The region. This parameter is required when the network type is aliyun-vpc.
        self.region = region
        # The JSON Path extraction path for the response body. This parameter is optional for agent_app.
        self.response_body_path = response_body_path
        # The security group ID. This parameter is optional for agent_app.
        self.security_group_id = security_group_id
        # The timeout for a single call, in milliseconds. Valid values: 1000 to 1800000. Default value: 300000.
        self.timeout_ms = timeout_ms
        # The vSwitch ID. This parameter is optional for agent_app.
        self.v_switch_id = v_switch_id
        # The VPC ID. This parameter is optional for agent_app.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['channelType'] = self.channel_type

        if self.dry_run_request_body is not None:
            result['dryRunRequestBody'] = self.dry_run_request_body

        if self.max_retries is not None:
            result['maxRetries'] = self.max_retries

        if self.model_list is not None:
            result['modelList'] = self.model_list

        if self.network is not None:
            result['network'] = self.network

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.qps_limit is not None:
            result['qpsLimit'] = self.qps_limit

        if self.region is not None:
            result['region'] = self.region

        if self.response_body_path is not None:
            result['responseBodyPath'] = self.response_body_path

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.timeout_ms is not None:
            result['timeoutMs'] = self.timeout_ms

        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')

        if m.get('dryRunRequestBody') is not None:
            self.dry_run_request_body = m.get('dryRunRequestBody')

        if m.get('maxRetries') is not None:
            self.max_retries = m.get('maxRetries')

        if m.get('modelList') is not None:
            self.model_list = m.get('modelList')

        if m.get('network') is not None:
            self.network = m.get('network')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('qpsLimit') is not None:
            self.qps_limit = m.get('qpsLimit')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('responseBodyPath') is not None:
            self.response_body_path = m.get('responseBodyPath')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('timeoutMs') is not None:
            self.timeout_ms = m.get('timeoutMs')

        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

