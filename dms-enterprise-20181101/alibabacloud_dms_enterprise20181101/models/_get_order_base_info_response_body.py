# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetOrderBaseInfoResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        order_base_info: main_models.GetOrderBaseInfoResponseBodyOrderBaseInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The basic information about the ticket.
        self.order_base_info = order_base_info
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.order_base_info:
            self.order_base_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.order_base_info is not None:
            result['OrderBaseInfo'] = self.order_base_info.to_map()

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

        if m.get('OrderBaseInfo') is not None:
            temp_model = main_models.GetOrderBaseInfoResponseBodyOrderBaseInfo()
            self.order_base_info = temp_model.from_map(m.get('OrderBaseInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetOrderBaseInfoResponseBodyOrderBaseInfo(DaraModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        committer: str = None,
        committer_id: int = None,
        create_time: str = None,
        last_modify_time: str = None,
        order_id: int = None,
        origin_attachment_name: str = None,
        plugin_type: str = None,
        related_user_list: main_models.GetOrderBaseInfoResponseBodyOrderBaseInfoRelatedUserList = None,
        related_user_nick_list: main_models.GetOrderBaseInfoResponseBodyOrderBaseInfoRelatedUserNickList = None,
        status_code: str = None,
        status_desc: str = None,
        workflow_instance_id: int = None,
        workflow_status_desc: str = None,
    ):
        # The Key of the ticket attachment. This information is returned only when an attachment is uploaded when a ticket is created.
        self.attachment_key = attachment_key
        # The remarks of the ticket.
        self.comment = comment
        # The applicant.
        self.committer = committer
        # The ID of the applicant. Note: The ID is different from the Alibaba Cloud account ID of the applicant.
        self.committer_id = committer_id
        # The time when the ticket was created.
        self.create_time = create_time
        # The time when the ticket was last modified.
        self.last_modify_time = last_modify_time
        # The ID of the ticket.
        self.order_id = order_id
        # The original file name of the ticket attachment. This information is returned only when an attachment is uploaded when a ticket is created.
        self.origin_attachment_name = origin_attachment_name
        # The type of the ticket. For more information about the value of this parameter, see the request parameters of the [CreateOrder](https://help.aliyun.com/document_detail/465865.html) operation.
        self.plugin_type = plugin_type
        # The IDs of the operators that are related to the ticket.
        self.related_user_list = related_user_list
        # The nicknames of the operators that are related to the ticket.
        self.related_user_nick_list = related_user_nick_list
        # The status code of the ticket. Valid values:
        # 
        # *   **new**: The ticket is created.
        # *   **toaudit**: The ticket is being reviewed.
        # *   **Approved**: The ticket is approved.
        # *   **reject**: The ticket is rejected.
        # *   **processing**: The ticket is being executed.
        # *   **success**: The ticket is executed.
        # *   **closed**: The ticket is closed.
        self.status_code = status_code
        # The description of the status.
        self.status_desc = status_desc
        # The ID of the approval process.
        self.workflow_instance_id = workflow_instance_id
        # The description of the approval process.
        self.workflow_status_desc = workflow_status_desc

    def validate(self):
        if self.related_user_list:
            self.related_user_list.validate()
        if self.related_user_nick_list:
            self.related_user_nick_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.committer is not None:
            result['Committer'] = self.committer

        if self.committer_id is not None:
            result['CommitterId'] = self.committer_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.origin_attachment_name is not None:
            result['OriginAttachmentName'] = self.origin_attachment_name

        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type

        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list.to_map()

        if self.related_user_nick_list is not None:
            result['RelatedUserNickList'] = self.related_user_nick_list.to_map()

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id

        if self.workflow_status_desc is not None:
            result['WorkflowStatusDesc'] = self.workflow_status_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Committer') is not None:
            self.committer = m.get('Committer')

        if m.get('CommitterId') is not None:
            self.committer_id = m.get('CommitterId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OriginAttachmentName') is not None:
            self.origin_attachment_name = m.get('OriginAttachmentName')

        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')

        if m.get('RelatedUserList') is not None:
            temp_model = main_models.GetOrderBaseInfoResponseBodyOrderBaseInfoRelatedUserList()
            self.related_user_list = temp_model.from_map(m.get('RelatedUserList'))

        if m.get('RelatedUserNickList') is not None:
            temp_model = main_models.GetOrderBaseInfoResponseBodyOrderBaseInfoRelatedUserNickList()
            self.related_user_nick_list = temp_model.from_map(m.get('RelatedUserNickList'))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')

        if m.get('WorkflowStatusDesc') is not None:
            self.workflow_status_desc = m.get('WorkflowStatusDesc')

        return self

class GetOrderBaseInfoResponseBodyOrderBaseInfoRelatedUserNickList(DaraModel):
    def __init__(
        self,
        user_nicks: List[str] = None,
    ):
        self.user_nicks = user_nicks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_nicks is not None:
            result['UserNicks'] = self.user_nicks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserNicks') is not None:
            self.user_nicks = m.get('UserNicks')

        return self

class GetOrderBaseInfoResponseBodyOrderBaseInfoRelatedUserList(DaraModel):
    def __init__(
        self,
        user_ids: List[str] = None,
    ):
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

