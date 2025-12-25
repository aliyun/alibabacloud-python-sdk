# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetTableDesignProjectFlowResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        project_flow: main_models.GetTableDesignProjectFlowResponseBodyProjectFlow = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The information about the schema design process.
        self.project_flow = project_flow
        # The request ID. You can use the request ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.project_flow:
            self.project_flow.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.project_flow is not None:
            result['ProjectFlow'] = self.project_flow.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ProjectFlow') is not None:
            temp_model = main_models.GetTableDesignProjectFlowResponseBodyProjectFlow()
            self.project_flow = temp_model.from_map(m.get('ProjectFlow'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTableDesignProjectFlowResponseBodyProjectFlow(DaraModel):
    def __init__(
        self,
        current_position: int = None,
        flow_node_array: List[main_models.GetTableDesignProjectFlowResponseBodyProjectFlowFlowNodeArray] = None,
        rule_comment: str = None,
        rule_name: str = None,
    ):
        # The position of the current node in the process.
        self.current_position = current_position
        # The nodes in the process.
        self.flow_node_array = flow_node_array
        # The description of the security rule set that is applied to the schema design ticket.
        self.rule_comment = rule_comment
        # The name of the security rule set that is applied to the schema design ticket.
        self.rule_name = rule_name

    def validate(self):
        if self.flow_node_array:
            for v1 in self.flow_node_array:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_position is not None:
            result['CurrentPosition'] = self.current_position

        result['FlowNodeArray'] = []
        if self.flow_node_array is not None:
            for k1 in self.flow_node_array:
                result['FlowNodeArray'].append(k1.to_map() if k1 else None)

        if self.rule_comment is not None:
            result['RuleComment'] = self.rule_comment

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPosition') is not None:
            self.current_position = m.get('CurrentPosition')

        self.flow_node_array = []
        if m.get('FlowNodeArray') is not None:
            for k1 in m.get('FlowNodeArray'):
                temp_model = main_models.GetTableDesignProjectFlowResponseBodyProjectFlowFlowNodeArray()
                self.flow_node_array.append(temp_model.from_map(k1))

        if m.get('RuleComment') is not None:
            self.rule_comment = m.get('RuleComment')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class GetTableDesignProjectFlowResponseBodyProjectFlowFlowNodeArray(DaraModel):
    def __init__(
        self,
        back_to_design: bool = None,
        can_skip: bool = None,
        node_role: str = None,
        node_title: str = None,
        position: int = None,
        publish_anchor: bool = None,
        publish_strategies: List[str] = None,
    ):
        # Indicates whether the ticket can be returned to the schema design node. Valid values:
        # 
        # *   **1**: The ticket can be returned to the schema design node.
        # *   **0**: The ticket cannot be returned to the schema design node. This value can be returned only for the PUBLISH node.
        self.back_to_design = back_to_design
        # Indicates whether the current node can be skipped. Valid values:
        # 
        # *   **1**: The current node can be skipped.
        # *   **0**: The current node cannot be skipped. This value can be returned only for the PUBLISH node.
        self.can_skip = can_skip
        # The role of the node in the process.
        # 
        # *   START: The ticket was created.
        # *   DESIGN: The schema is being created.
        # *   PUBLISH: The schema is published.
        # *   END: The ticket is complete.
        self.node_role = node_role
        # The title of the node.
        self.node_title = node_title
        # The position of the node in the process. The value starts from 1.
        self.position = position
        # Indicates whether the node is the anchor node. A schema design process has only one anchor node, on which the schema is published. After the schema is published on the anchor node, a post-publish image is generated and the DDL metadata lock is released.
        self.publish_anchor = publish_anchor
        # The available publishing strategies.
        self.publish_strategies = publish_strategies

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.back_to_design is not None:
            result['BackToDesign'] = self.back_to_design

        if self.can_skip is not None:
            result['CanSkip'] = self.can_skip

        if self.node_role is not None:
            result['NodeRole'] = self.node_role

        if self.node_title is not None:
            result['NodeTitle'] = self.node_title

        if self.position is not None:
            result['Position'] = self.position

        if self.publish_anchor is not None:
            result['PublishAnchor'] = self.publish_anchor

        if self.publish_strategies is not None:
            result['PublishStrategies'] = self.publish_strategies

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackToDesign') is not None:
            self.back_to_design = m.get('BackToDesign')

        if m.get('CanSkip') is not None:
            self.can_skip = m.get('CanSkip')

        if m.get('NodeRole') is not None:
            self.node_role = m.get('NodeRole')

        if m.get('NodeTitle') is not None:
            self.node_title = m.get('NodeTitle')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('PublishAnchor') is not None:
            self.publish_anchor = m.get('PublishAnchor')

        if m.get('PublishStrategies') is not None:
            self.publish_strategies = m.get('PublishStrategies')

        return self

