# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ReviewRectifyFlowRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        op_user_id: str = None,
        review_command: main_models.ReviewRectifyFlowRequestReviewCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator user.
        self.op_user_id = op_user_id
        # The business request parameters.
        # 
        # This parameter is required.
        self.review_command = review_command

    def validate(self):
        if self.review_command:
            self.review_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.review_command is not None:
            result['ReviewCommand'] = self.review_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('ReviewCommand') is not None:
            temp_model = main_models.ReviewRectifyFlowRequestReviewCommand()
            self.review_command = temp_model.from_map(m.get('ReviewCommand'))

        return self

class ReviewRectifyFlowRequestReviewCommand(DaraModel):
    def __init__(
        self,
        comment: str = None,
        rectify_id: int = None,
        review_result: str = None,
    ):
        # The acceptance description. This parameter is optional and can contain up to 128 characters.
        self.comment = comment
        # The ID of the rectification process. This operation is allowed only when the process is pending acceptance.
        # 
        # This parameter is required.
        self.rectify_id = rectify_id
        # The acceptance result. Valid values: PASSED and REJECTED.
        # 
        # This parameter is required.
        self.review_result = review_result

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

        if self.review_result is not None:
            result['ReviewResult'] = self.review_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('RectifyId') is not None:
            self.rectify_id = m.get('RectifyId')

        if m.get('ReviewResult') is not None:
            self.review_result = m.get('ReviewResult')

        return self

