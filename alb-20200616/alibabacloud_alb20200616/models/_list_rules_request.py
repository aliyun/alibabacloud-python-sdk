# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class ListRulesRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        listener_ids: List[str] = None,
        load_balancer_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        rule_ids: List[str] = None,
        tag: List[main_models.ListRulesRequestTag] = None,
    ):
        # The direction to which the forwarding rule is applied. Valid values:
        # 
        # *   **Request** (default): The forwarding rule is applied to the client requests received by ALB.
        # *   **Response**: The forwarding rule is applied to the responses returned by backend servers.
        # 
        # > You cannot set this parameter to Response if you use basic ALB instances.
        self.direction = direction
        # The listener IDs.
        self.listener_ids = listener_ids
        # The Application Load Balancer (ALB) instance IDs.
        self.load_balancer_ids = load_balancer_ids
        # The maximum number of entries to return.
        # 
        # Valid values: **1 to 100**.
        # 
        # Default value: **20**. If you do not specify this parameter, the default value is used.
        # 
        # > This parameter is optional.
        self.max_results = max_results
        # The starting point of the current query. If you do not specify this parameter, the query starts from the beginning.
        self.next_token = next_token
        # The forwarding rules.
        self.rule_ids = rule_ids
        # The tag.
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
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.listener_ids is not None:
            result['ListenerIds'] = self.listener_ids

        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('ListenerIds') is not None:
            self.listener_ids = m.get('ListenerIds')

        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListRulesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListRulesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://.
        self.key = key
        # The tag value. The tag value can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://.
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

