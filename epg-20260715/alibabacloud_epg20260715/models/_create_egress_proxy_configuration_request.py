# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class CreateEgressProxyConfigurationRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        default_rule_phase_actions: main_models.CreateEgressProxyConfigurationRequestDefaultRulePhaseActions = None,
        description: str = None,
        dry_run: bool = None,
        egress_proxy_configuration_name: str = None,
        resource_group_id: str = None,
        tag: List[main_models.CreateEgressProxyConfigurationRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > Note If you do not specify this parameter, the system automatically uses the RequestId of the API request as the client token. The RequestId of each API request is different.
        self.client_token = client_token
        # The default actions to be performed in each effective phase (PreDns, PreRequest, and PostResponse) when traffic does not match any rules.
        self.default_rule_phase_actions = default_rule_phase_actions
        # The description of the egress proxy configuration. The description must be 2 to 256 characters in length, and can contain Chinese characters, letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (_).
        self.description = description
        # Specifies whether to perform a dry run of the request. Valid values:
        # 
        # - **true**: performs a dry run and does not create the egress proxy configuration. The system checks whether the required parameters are specified, the request format is valid, and the service limits are met. If the request fails the dry run, the corresponding error code is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # 
        # - **false** (default): sends a normal request. If the request passes the check, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The name of the egress proxy configuration. The name must be 2 to 128 characters in length, and must start with a letter or a Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.egress_proxy_configuration_name = egress_proxy_configuration_name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The list of tags.
        self.tag = tag

    def validate(self):
        if self.default_rule_phase_actions:
            self.default_rule_phase_actions.validate()
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

        if self.default_rule_phase_actions is not None:
            result['DefaultRulePhaseActions'] = self.default_rule_phase_actions.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.egress_proxy_configuration_name is not None:
            result['EgressProxyConfigurationName'] = self.egress_proxy_configuration_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DefaultRulePhaseActions') is not None:
            temp_model = main_models.CreateEgressProxyConfigurationRequestDefaultRulePhaseActions()
            self.default_rule_phase_actions = temp_model.from_map(m.get('DefaultRulePhaseActions'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EgressProxyConfigurationName') is not None:
            self.egress_proxy_configuration_name = m.get('EgressProxyConfigurationName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateEgressProxyConfigurationRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateEgressProxyConfigurationRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The key can be up to 128 characters in length, and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. The value can be up to 256 characters in length, and cannot contain `http://` or `https://`.
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

class CreateEgressProxyConfigurationRequestDefaultRulePhaseActions(DaraModel):
    def __init__(
        self,
        post_response: str = None,
        pre_dns: str = None,
        pre_request: str = None,
    ):
        # The default action to be performed in the PostResponse phase (after the response is returned) when traffic does not match any rules. This phase supports only the **Allow** value (default), which allows the traffic to pass through.
        self.post_response = post_response
        # The default action to be performed in the PreDns phase (before DNS resolution) when traffic does not match any rules. Valid values:
        # 
        # - **Allow** (default): allows the traffic to pass through.
        # 
        # - **Deny**: denies the traffic.
        self.pre_dns = pre_dns
        # The default action to be performed in the PreRequest phase (before the request is forwarded) when traffic does not match any rules. Valid values:
        # 
        # - **Allow** (default): allows the traffic to pass through.
        # 
        # - **Deny**: denies the traffic.
        self.pre_request = pre_request

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.post_response is not None:
            result['PostResponse'] = self.post_response

        if self.pre_dns is not None:
            result['PreDns'] = self.pre_dns

        if self.pre_request is not None:
            result['PreRequest'] = self.pre_request

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PostResponse') is not None:
            self.post_response = m.get('PostResponse')

        if m.get('PreDns') is not None:
            self.pre_dns = m.get('PreDns')

        if m.get('PreRequest') is not None:
            self.pre_request = m.get('PreRequest')

        return self

