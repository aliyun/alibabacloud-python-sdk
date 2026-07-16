# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appflow20230904 import models as main_models
from darabonba.model import DaraModel

class ListFlowsResponseBody(DaraModel):
    def __init__(
        self,
        flows: List[main_models.ListFlowsResponseBodyFlows] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of connector flows.
        self.flows = flows
        # The page size.
        self.max_results = max_results
        # The token for the next query.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.flows:
            for v1 in self.flows:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Flows'] = []
        if self.flows is not None:
            for k1 in self.flows:
                result['Flows'].append(k1.to_map() if k1 else None)

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
        self.flows = []
        if m.get('Flows') is not None:
            for k1 in m.get('Flows'):
                temp_model = main_models.ListFlowsResponseBodyFlows()
                self.flows.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFlowsResponseBodyFlows(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        flow_desc: str = None,
        flow_id: str = None,
        flow_name: str = None,
        flow_template: str = None,
        flow_version: str = None,
        flow_version_status: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        released_version: int = None,
        tags: List[main_models.ListFlowsResponseBodyFlowsTags] = None,
        webhook_url: str = None,
    ):
        # Indicates whether the connector flow is enabled.
        self.enabled = enabled
        # The connector flow description.
        self.flow_desc = flow_desc
        # The connector flow ID.
        self.flow_id = flow_id
        # The connector flow name.
        self.flow_name = flow_name
        # The connector flow template content.
        self.flow_template = flow_template
        # The connector flow version.
        self.flow_version = flow_version
        # The connector flow version status.
        self.flow_version_status = flow_version_status
        # The time when the connector flow was created.
        self.gmt_create = gmt_create
        # The time when the connector flow was last modified.
        self.gmt_modified = gmt_modified
        # The released version number.
        self.released_version = released_version
        # The tag values.
        self.tags = tags
        # The webhook URL.
        self.webhook_url = webhook_url

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.flow_desc is not None:
            result['FlowDesc'] = self.flow_desc

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.flow_template is not None:
            result['FlowTemplate'] = self.flow_template

        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version

        if self.flow_version_status is not None:
            result['FlowVersionStatus'] = self.flow_version_status

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.released_version is not None:
            result['ReleasedVersion'] = self.released_version

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.webhook_url is not None:
            result['WebhookUrl'] = self.webhook_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('FlowDesc') is not None:
            self.flow_desc = m.get('FlowDesc')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('FlowTemplate') is not None:
            self.flow_template = m.get('FlowTemplate')

        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')

        if m.get('FlowVersionStatus') is not None:
            self.flow_version_status = m.get('FlowVersionStatus')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ReleasedVersion') is not None:
            self.released_version = m.get('ReleasedVersion')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListFlowsResponseBodyFlowsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('WebhookUrl') is not None:
            self.webhook_url = m.get('WebhookUrl')

        return self

class ListFlowsResponseBodyFlowsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key can be up to 64 characters in length.
        self.key = key
        # The tag values.
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

