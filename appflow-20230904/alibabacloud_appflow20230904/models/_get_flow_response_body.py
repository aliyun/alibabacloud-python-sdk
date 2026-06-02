# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appflow20230904 import models as main_models
from darabonba.model import DaraModel

class GetFlowResponseBody(DaraModel):
    def __init__(
        self,
        flow: main_models.GetFlowResponseBodyFlow = None,
        request_id: str = None,
    ):
        self.flow = flow
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.flow:
            self.flow.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow is not None:
            result['Flow'] = self.flow.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            temp_model = main_models.GetFlowResponseBodyFlow()
            self.flow = temp_model.from_map(m.get('Flow'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetFlowResponseBodyFlow(DaraModel):
    def __init__(
        self,
        enabled: str = None,
        flow_desc: str = None,
        flow_id: str = None,
        flow_name: str = None,
        flow_nodes: List[main_models.GetFlowResponseBodyFlowFlowNodes] = None,
        flow_template: str = None,
        flow_version: str = None,
        flow_version_status: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        tags: List[main_models.GetFlowResponseBodyFlowTags] = None,
    ):
        self.enabled = enabled
        self.flow_desc = flow_desc
        self.flow_id = flow_id
        self.flow_name = flow_name
        self.flow_nodes = flow_nodes
        self.flow_template = flow_template
        self.flow_version = flow_version
        self.flow_version_status = flow_version_status
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.tags = tags

    def validate(self):
        if self.flow_nodes:
            for v1 in self.flow_nodes:
                 if v1:
                    v1.validate()
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

        result['FlowNodes'] = []
        if self.flow_nodes is not None:
            for k1 in self.flow_nodes:
                result['FlowNodes'].append(k1.to_map() if k1 else None)

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

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

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

        self.flow_nodes = []
        if m.get('FlowNodes') is not None:
            for k1 in m.get('FlowNodes'):
                temp_model = main_models.GetFlowResponseBodyFlowFlowNodes()
                self.flow_nodes.append(temp_model.from_map(k1))

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

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetFlowResponseBodyFlowTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class GetFlowResponseBodyFlowTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

class GetFlowResponseBodyFlowFlowNodes(DaraModel):
    def __init__(
        self,
        auth_metadata: str = None,
        connector_id: str = None,
        connector_version: str = None,
        flow_id: str = None,
        flow_version: str = None,
        input_schema: str = None,
        node_id: str = None,
        node_key: str = None,
        node_name: str = None,
        node_type: str = None,
        prev_node_id: str = None,
        ref_id: str = None,
        ref_version: str = None,
        webhook_url: str = None,
    ):
        self.auth_metadata = auth_metadata
        self.connector_id = connector_id
        self.connector_version = connector_version
        self.flow_id = flow_id
        self.flow_version = flow_version
        self.input_schema = input_schema
        self.node_id = node_id
        self.node_key = node_key
        self.node_name = node_name
        self.node_type = node_type
        self.prev_node_id = prev_node_id
        self.ref_id = ref_id
        self.ref_version = ref_version
        self.webhook_url = webhook_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_metadata is not None:
            result['AuthMetadata'] = self.auth_metadata

        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.connector_version is not None:
            result['ConnectorVersion'] = self.connector_version

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version

        if self.input_schema is not None:
            result['InputSchema'] = self.input_schema

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_key is not None:
            result['NodeKey'] = self.node_key

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.prev_node_id is not None:
            result['PrevNodeId'] = self.prev_node_id

        if self.ref_id is not None:
            result['RefId'] = self.ref_id

        if self.ref_version is not None:
            result['RefVersion'] = self.ref_version

        if self.webhook_url is not None:
            result['WebhookUrl'] = self.webhook_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthMetadata') is not None:
            self.auth_metadata = m.get('AuthMetadata')

        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('ConnectorVersion') is not None:
            self.connector_version = m.get('ConnectorVersion')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')

        if m.get('InputSchema') is not None:
            self.input_schema = m.get('InputSchema')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeKey') is not None:
            self.node_key = m.get('NodeKey')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('PrevNodeId') is not None:
            self.prev_node_id = m.get('PrevNodeId')

        if m.get('RefId') is not None:
            self.ref_id = m.get('RefId')

        if m.get('RefVersion') is not None:
            self.ref_version = m.get('RefVersion')

        if m.get('WebhookUrl') is not None:
            self.webhook_url = m.get('WebhookUrl')

        return self

