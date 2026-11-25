# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_market20151101 import models as main_models
from darabonba.model import DaraModel

class DescribeCurrentNodeInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DescribeCurrentNodeInfoResponseBodyResult = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The process node information returned upon success.
        self.result = result
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.DescribeCurrentNodeInfoResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCurrentNodeInfoResponseBodyResult(DaraModel):
    def __init__(
        self,
        allow_rollback_node: bool = None,
        auto_finish_node: bool = None,
        final_step_no: int = None,
        gmt_expired: int = None,
        gmt_finished: int = None,
        gmt_start: int = None,
        need_attachment: bool = None,
        next_node_id: int = None,
        node_id: int = None,
        node_name: str = None,
        node_status: str = None,
        operator_role: str = None,
        parent_node_id: int = None,
        previous_node_id: int = None,
        step_no: int = None,
        template_form: str = None,
    ):
        # Indicates whether rollback to the previous process node is allowed.
        self.allow_rollback_node = allow_rollback_node
        # Indicates whether the node is automatically completed.
        self.auto_finish_node = auto_finish_node
        # The sequence number of the last node.
        self.final_step_no = final_step_no
        # The timeout of the process node. The value is a UNIX timestamp.
        self.gmt_expired = gmt_expired
        # The completion time of the process node. The value is a UNIX timestamp.
        self.gmt_finished = gmt_finished
        # The start time of the process node. The value is a UNIX timestamp.
        self.gmt_start = gmt_start
        # Indicates whether uploading an attachment is mandatory.
        self.need_attachment = need_attachment
        # The ID of the next process node.
        self.next_node_id = next_node_id
        # The ID of the process node.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The execution status of the node. Valid values:
        # - NotStart: not started.
        # - Starting: in progress.
        # - Cancel: canceled.
        # - Finish: completed.
        self.node_status = node_status
        # The role of the operator for the process node. Valid values:
        # - system: system.
        # - custom: user.
        self.operator_role = operator_role
        # The ID of the parent process node.
        self.parent_node_id = parent_node_id
        # The ID of the previous process node.
        self.previous_node_id = previous_node_id
        # The sequence number of the process node.
        self.step_no = step_no
        # The form content of the process node in JSON format.
        # Sample code:
        # `[ { "fieldKey": "TFD0", //form key "isRequired": true, //whether the field is required "maxLength": 50, //maximum length "placeHolder": "Name", //form value description "stepNum": 0, //sort value (ascending) "title": "Consignee name", //form title "type": "text" //form type }, { "fieldKey": "TFD1", "isRequired": true, "maxLength": 50, "placeHolder": "Phone number", "stepNum": 1, "title": "Consignee phone number", "type": "text" }, { "fieldKey": "TFD2", "isRequired": true, "maxLength": 50, "placeHolder": "Province, city, district, street, and house number", "stepNum": 2, "title": "Detailed shipping address", "type": "textarea" } ]`.
        self.template_form = template_form

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_rollback_node is not None:
            result['AllowRollbackNode'] = self.allow_rollback_node

        if self.auto_finish_node is not None:
            result['AutoFinishNode'] = self.auto_finish_node

        if self.final_step_no is not None:
            result['FinalStepNo'] = self.final_step_no

        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired

        if self.gmt_finished is not None:
            result['GmtFinished'] = self.gmt_finished

        if self.gmt_start is not None:
            result['GmtStart'] = self.gmt_start

        if self.need_attachment is not None:
            result['NeedAttachment'] = self.need_attachment

        if self.next_node_id is not None:
            result['NextNodeId'] = self.next_node_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_status is not None:
            result['NodeStatus'] = self.node_status

        if self.operator_role is not None:
            result['OperatorRole'] = self.operator_role

        if self.parent_node_id is not None:
            result['ParentNodeId'] = self.parent_node_id

        if self.previous_node_id is not None:
            result['PreviousNodeId'] = self.previous_node_id

        if self.step_no is not None:
            result['StepNo'] = self.step_no

        if self.template_form is not None:
            result['TemplateForm'] = self.template_form

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRollbackNode') is not None:
            self.allow_rollback_node = m.get('AllowRollbackNode')

        if m.get('AutoFinishNode') is not None:
            self.auto_finish_node = m.get('AutoFinishNode')

        if m.get('FinalStepNo') is not None:
            self.final_step_no = m.get('FinalStepNo')

        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')

        if m.get('GmtFinished') is not None:
            self.gmt_finished = m.get('GmtFinished')

        if m.get('GmtStart') is not None:
            self.gmt_start = m.get('GmtStart')

        if m.get('NeedAttachment') is not None:
            self.need_attachment = m.get('NeedAttachment')

        if m.get('NextNodeId') is not None:
            self.next_node_id = m.get('NextNodeId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')

        if m.get('OperatorRole') is not None:
            self.operator_role = m.get('OperatorRole')

        if m.get('ParentNodeId') is not None:
            self.parent_node_id = m.get('ParentNodeId')

        if m.get('PreviousNodeId') is not None:
            self.previous_node_id = m.get('PreviousNodeId')

        if m.get('StepNo') is not None:
            self.step_no = m.get('StepNo')

        if m.get('TemplateForm') is not None:
            self.template_form = m.get('TemplateForm')

        return self

