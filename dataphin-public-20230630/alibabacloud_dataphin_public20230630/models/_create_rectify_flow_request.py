# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateRectifyFlowRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateRectifyFlowRequestCreateCommand = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The business request parameters.
        # 
        # This parameter is required.
        self.create_command = create_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator.
        self.op_user_id = op_user_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateRectifyFlowRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class CreateRectifyFlowRequestCreateCommand(DaraModel):
    def __init__(
        self,
        bind_to_rectify: bool = None,
        bind_to_rectify_id: int = None,
        comment: str = None,
        govern_item_type: str = None,
        govern_object_ids: List[int] = None,
        rectify_name: str = None,
        rectify_priority: str = None,
        rectify_scope: str = None,
        rectify_user: str = None,
        verify_user: str = None,
    ):
        # Specifies whether to associate with an existing process. Default value: false.
        self.bind_to_rectify = bind_to_rectify
        # This parameter is required when you associate with an existing process.
        self.bind_to_rectify_id = bind_to_rectify_id
        # The operation description. This parameter is optional. Maximum length: 128 characters.
        self.comment = comment
        # The governance object type. Valid values: TABLE, DATASOURCE_TABLE, DATASOURCE, INDEX, REALTIME_LOGICAL_TABLE, and QD_FEATURE.
        # 
        # This parameter is required.
        self.govern_item_type = govern_item_type
        # The list of issue IDs. Issues that cannot be rectified are skipped. If all issues are skipped, the original business error is returned.
        # 
        # This parameter is required.
        self.govern_object_ids = govern_object_ids
        # The rectification name. This parameter is required when you create a process and can contain up to 128 characters. It is ignored when you associate with an existing process.
        self.rectify_name = rectify_name
        # The rectification priority. Valid values: HIGH, MIDDLE, and LOW. Default value: MIDDLE. This parameter is ignored and not verified when you associate with an existing process.
        self.rectify_priority = rectify_priority
        # The rectification scope. Valid values: QUALITY_RULE_SCOPE, QUALITY_RULE_TASK_SCOPE, QUALITY_GOVERN_OBJECT_SCOPE, and QUALITY_WATCH_SCOPE. The default value is the same as the value on the page. A rule scope may include other issues.
        self.rectify_scope = rectify_scope
        # The ID of the user who performs the rectification. Default value: the current user. This parameter is ignored when you associate with an existing process.
        self.rectify_user = rectify_user
        # The ID of the user who performs the verification. Default value: the current user. This parameter is ignored when you associate with an existing process.
        self.verify_user = verify_user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_to_rectify is not None:
            result['BindToRectify'] = self.bind_to_rectify

        if self.bind_to_rectify_id is not None:
            result['BindToRectifyId'] = self.bind_to_rectify_id

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.govern_item_type is not None:
            result['GovernItemType'] = self.govern_item_type

        if self.govern_object_ids is not None:
            result['GovernObjectIds'] = self.govern_object_ids

        if self.rectify_name is not None:
            result['RectifyName'] = self.rectify_name

        if self.rectify_priority is not None:
            result['RectifyPriority'] = self.rectify_priority

        if self.rectify_scope is not None:
            result['RectifyScope'] = self.rectify_scope

        if self.rectify_user is not None:
            result['RectifyUser'] = self.rectify_user

        if self.verify_user is not None:
            result['VerifyUser'] = self.verify_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindToRectify') is not None:
            self.bind_to_rectify = m.get('BindToRectify')

        if m.get('BindToRectifyId') is not None:
            self.bind_to_rectify_id = m.get('BindToRectifyId')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('GovernItemType') is not None:
            self.govern_item_type = m.get('GovernItemType')

        if m.get('GovernObjectIds') is not None:
            self.govern_object_ids = m.get('GovernObjectIds')

        if m.get('RectifyName') is not None:
            self.rectify_name = m.get('RectifyName')

        if m.get('RectifyPriority') is not None:
            self.rectify_priority = m.get('RectifyPriority')

        if m.get('RectifyScope') is not None:
            self.rectify_scope = m.get('RectifyScope')

        if m.get('RectifyUser') is not None:
            self.rectify_user = m.get('RectifyUser')

        if m.get('VerifyUser') is not None:
            self.verify_user = m.get('VerifyUser')

        return self

