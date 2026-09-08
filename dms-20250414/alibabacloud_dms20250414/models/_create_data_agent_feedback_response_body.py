# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class CreateDataAgentFeedbackResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateDataAgentFeedbackResponseBodyData = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The response struct.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message returned if the request failed.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateDataAgentFeedbackResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateDataAgentFeedbackResponseBodyData(DaraModel):
    def __init__(
        self,
        feedback_content: str = None,
        feedback_type: str = None,
        like_value: int = None,
        region_id: str = None,
        session_id: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        # The feedback content.
        self.feedback_content = feedback_content
        # The feedback type.
        self.feedback_type = feedback_type
        # The like value.
        self.like_value = like_value
        # The region.
        self.region_id = region_id
        # The agent session ID.
        self.session_id = session_id
        # The feedback target ID.
        self.target_id = target_id
        # The feedback target.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feedback_content is not None:
            result['FeedbackContent'] = self.feedback_content

        if self.feedback_type is not None:
            result['FeedbackType'] = self.feedback_type

        if self.like_value is not None:
            result['LikeValue'] = self.like_value

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeedbackContent') is not None:
            self.feedback_content = m.get('FeedbackContent')

        if m.get('FeedbackType') is not None:
            self.feedback_type = m.get('FeedbackType')

        if m.get('LikeValue') is not None:
            self.like_value = m.get('LikeValue')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

