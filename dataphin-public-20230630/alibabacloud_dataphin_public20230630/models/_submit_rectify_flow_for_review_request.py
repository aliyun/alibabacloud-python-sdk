# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class SubmitRectifyFlowForReviewRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        op_user_id: str = None,
        submit_command: main_models.SubmitRectifyFlowForReviewRequestSubmitCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The operator user ID.
        self.op_user_id = op_user_id
        # The business request parameters.
        # 
        # This parameter is required.
        self.submit_command = submit_command

    def validate(self):
        if self.submit_command:
            self.submit_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.submit_command is not None:
            result['SubmitCommand'] = self.submit_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('SubmitCommand') is not None:
            temp_model = main_models.SubmitRectifyFlowForReviewRequestSubmitCommand()
            self.submit_command = temp_model.from_map(m.get('SubmitCommand'))

        return self

class SubmitRectifyFlowForReviewRequestSubmitCommand(DaraModel):
    def __init__(
        self,
        comment: str = None,
        rectify_id: int = None,
    ):
        # The description of the rectification result. This parameter is required and can be up to 128 characters in length.
        # 
        # This parameter is required.
        self.comment = comment
        # The ID of the rectification process. Submission is allowed only when the process is in the rectifying or re-rectifying state.
        # 
        # This parameter is required.
        self.rectify_id = rectify_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.rectify_id is not None:
            result['RectifyId'] = self.rectify_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('RectifyId') is not None:
            self.rectify_id = m.get('RectifyId')

        return self

