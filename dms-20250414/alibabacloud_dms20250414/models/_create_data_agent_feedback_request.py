# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataAgentFeedbackRequest(DaraModel):
    def __init__(
        self,
        dmsunit: str = None,
        feedback_content: str = None,
        feedback_type: str = None,
        like_value: int = None,
        session_id: str = None,
        target_id: str = None,
        target_type: str = None,
        workspace_id: str = None,
    ):
        # The current DMS unit.
        self.dmsunit = dmsunit
        # The feedback content. You can directly enter the feedback content, or pass a JSON string for the issue report scenario as shown in the example. The feedback_type field corresponds to the issue type, user_feedback corresponds to the issue description, email corresponds to the contact email address, and is_authorized indicates whether to authorize log access for troubleshooting.
        # 
        # feedback_type issue types. Valid values:
        # 
        # - **ANALYSIS_RESULT_INACCURATE**: Inaccurate analysis result.
        # - **RUNTIME_ERROR**: Runtime error.
        # - **REPORT_EXCEPTION**: Report exception.
        # - **SLOW_RESPONSE**: Slow response.
        # - **PRODUCT_SUGGESTION**: Product suggestion.
        # - **OTHER**: Other.
        self.feedback_content = feedback_content
        # The feedback type. Valid values:
        # 
        # - **ISSUE_REPORT**: issue report.
        # - **CANCEL_CHAT**: task cancellation.
        # - **LIKE**: like.
        # - **DISLIKE**: dislike.
        self.feedback_type = feedback_type
        # The like value. This parameter is used only for like and dislike scenarios. Do not pass this parameter for other scenarios. Valid values:
        # 
        # - **1**: like.
        # - **-1**: dislike.
        self.like_value = like_value
        # The agent session ID.
        self.session_id = session_id
        # The feedback target ID.
        # 
        # - For issue reports, use SessionId + underscore + random UUID.
        # - For other feedback types, pass the checkpoint of the current SSE message stream.
        self.target_id = target_id
        # The feedback target. Valid values:
        # 
        # - **SESSION**: session (used for issue reports).
        # - **CHAT**: chat (used for task cancellation).
        # - **REPORT**: report.
        # - **PLAN**: execution plan.
        self.target_type = target_type
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dmsunit is not None:
            result['DMSUnit'] = self.dmsunit

        if self.feedback_content is not None:
            result['FeedbackContent'] = self.feedback_content

        if self.feedback_type is not None:
            result['FeedbackType'] = self.feedback_type

        if self.like_value is not None:
            result['LikeValue'] = self.like_value

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DMSUnit') is not None:
            self.dmsunit = m.get('DMSUnit')

        if m.get('FeedbackContent') is not None:
            self.feedback_content = m.get('FeedbackContent')

        if m.get('FeedbackType') is not None:
            self.feedback_type = m.get('FeedbackType')

        if m.get('LikeValue') is not None:
            self.like_value = m.get('LikeValue')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

