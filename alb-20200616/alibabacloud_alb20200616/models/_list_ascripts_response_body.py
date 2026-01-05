# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class ListAScriptsResponseBody(DaraModel):
    def __init__(
        self,
        ascripts: List[main_models.ListAScriptsResponseBodyAScripts] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The AScript rules.
        self.ascripts = ascripts
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value is the token that determines the start point of the next query.
        # 
        # This parameter is required.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        # 
        # > This parameter is optional. By default, this parameter is not returned.
        self.total_count = total_count

    def validate(self):
        if self.ascripts:
            for v1 in self.ascripts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AScripts'] = []
        if self.ascripts is not None:
            for k1 in self.ascripts:
                result['AScripts'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ascripts = []
        if m.get('AScripts') is not None:
            for k1 in m.get('AScripts'):
                temp_model = main_models.ListAScriptsResponseBodyAScripts()
                self.ascripts.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAScriptsResponseBodyAScripts(DaraModel):
    def __init__(
        self,
        ascript_id: str = None,
        ascript_name: str = None,
        ascript_status: str = None,
        enabled: bool = None,
        listener_id: str = None,
        load_balancer_id: str = None,
        script_content: str = None,
    ):
        # The AScript rule ID.
        self.ascript_id = ascript_id
        # The name of the AScript rule.
        self.ascript_name = ascript_name
        # The status of the AScript rule. Valid values:
        # 
        # *   **Creating**
        # *   **Available**
        # *   **Configuring**
        # *   **Deleting**
        self.ascript_status = ascript_status
        # Indicates whether the AScript rule is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enabled = enabled
        # The listener ID.
        self.listener_id = listener_id
        # The Application Load Balancer (ALB) instance ID.
        self.load_balancer_id = load_balancer_id
        # The content of the AScript rule.
        self.script_content = script_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ascript_id is not None:
            result['AScriptId'] = self.ascript_id

        if self.ascript_name is not None:
            result['AScriptName'] = self.ascript_name

        if self.ascript_status is not None:
            result['AScriptStatus'] = self.ascript_status

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.script_content is not None:
            result['ScriptContent'] = self.script_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AScriptId') is not None:
            self.ascript_id = m.get('AScriptId')

        if m.get('AScriptName') is not None:
            self.ascript_name = m.get('AScriptName')

        if m.get('AScriptStatus') is not None:
            self.ascript_status = m.get('AScriptStatus')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')

        return self

