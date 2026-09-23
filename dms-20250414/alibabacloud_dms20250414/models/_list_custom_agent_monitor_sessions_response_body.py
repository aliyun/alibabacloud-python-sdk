# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListCustomAgentMonitorSessionsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListCustomAgentMonitorSessionsResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response struct.
        self.data = data
        # The error code returned if the call fails.
        self.error_code = error_code
        # The error message returned if the call fails.
        self.error_message = error_message
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
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListCustomAgentMonitorSessionsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCustomAgentMonitorSessionsResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListCustomAgentMonitorSessionsResponseBodyDataContent] = None,
        page_number: int = None,
        page_size: int = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        # The session details list for the current page, sorted by creation time in descending order.
        self.content = content
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of sessions within the filter scope.
        self.total_elements = total_elements
        # The total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.ListCustomAgentMonitorSessionsResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class ListCustomAgentMonitorSessionsResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        creator_user_name: str = None,
        custom_agent_id: str = None,
        dislike_count: int = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        like_count: int = None,
        session_id: str = None,
        state: str = None,
        title: str = None,
        turn_count: int = None,
    ):
        # The Alibaba Cloud UID of the creator.
        self.aliyun_uid = aliyun_uid
        # The display name of the creator.
        self.creator_user_name = creator_user_name
        # The custom agent ID.
        self.custom_agent_id = custom_agent_id
        # The number of dislikes for the session.
        self.dislike_count = dislike_count
        # The creation time.
        self.gmt_created = gmt_created
        # The modification time.
        self.gmt_modified = gmt_modified
        # The number of likes for the session.
        self.like_count = like_count
        # The session ID.
        self.session_id = session_id
        # The session status. Valid values:
        # - init: The session is in the initial state.
        # - INITIALIZING: The session is being initialized.
        # - RUNNING: The session is running.
        # - IDLE: The session is idle.
        # - RECOVERABLE: The session is completed and can accept further questions.
        # - UNAVAILABLE: The session is completed and cannot accept further questions.
        self.state = state
        # The session name.
        self.title = title
        # The total number of turns in the session.
        self.turn_count = turn_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.creator_user_name is not None:
            result['CreatorUserName'] = self.creator_user_name

        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id

        if self.dislike_count is not None:
            result['DislikeCount'] = self.dislike_count

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.like_count is not None:
            result['LikeCount'] = self.like_count

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.state is not None:
            result['State'] = self.state

        if self.title is not None:
            result['Title'] = self.title

        if self.turn_count is not None:
            result['TurnCount'] = self.turn_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('CreatorUserName') is not None:
            self.creator_user_name = m.get('CreatorUserName')

        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')

        if m.get('DislikeCount') is not None:
            self.dislike_count = m.get('DislikeCount')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('LikeCount') is not None:
            self.like_count = m.get('LikeCount')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('TurnCount') is not None:
            self.turn_count = m.get('TurnCount')

        return self

