# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListChatGroupResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.ListChatGroupResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Details about the access denied error.
        self.access_denied_detail = access_denied_detail
        # The status code. Valid values:
        # 
        # - `OK`: The request succeeded.
        # 
        # - For other error codes, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The response message. This parameter is returned only when an error occurs.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request succeeded. Valid values:
        # 
        # - **true**: The request succeeded.
        # 
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListChatGroupResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListChatGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListChatGroupResponseBodyDataList] = None,
        total: int = None,
    ):
        # The group list.
        self.list = list
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListChatGroupResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListChatGroupResponseBodyDataList(DaraModel):
    def __init__(
        self,
        business_number: str = None,
        business_role: str = None,
        description: str = None,
        gmt_modifier: int = None,
        group_id: str = None,
        group_link: str = None,
        group_status: str = None,
        group_type: str = None,
        invite_link: str = None,
        profile_picture_file: str = None,
        subject: str = None,
        total_participant_count: int = None,
    ):
        # The business number.
        self.business_number = business_number
        # The role of the bot in the group.
        self.business_role = business_role
        # The group description.
        self.description = description
        # The time the group was last updated.
        self.gmt_modifier = gmt_modifier
        # The group ID.
        self.group_id = group_id
        # The group link.
        self.group_link = group_link
        # The group status.
        self.group_status = group_status
        # The group type.
        self.group_type = group_type
        # The group invitation link.
        self.invite_link = invite_link
        # The group\\"s profile picture.
        self.profile_picture_file = profile_picture_file
        # The group subject.
        self.subject = subject
        # The total number of group participants.
        self.total_participant_count = total_participant_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number

        if self.business_role is not None:
            result['BusinessRole'] = self.business_role

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_modifier is not None:
            result['GmtModifier'] = self.gmt_modifier

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_link is not None:
            result['GroupLink'] = self.group_link

        if self.group_status is not None:
            result['GroupStatus'] = self.group_status

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.invite_link is not None:
            result['InviteLink'] = self.invite_link

        if self.profile_picture_file is not None:
            result['ProfilePictureFile'] = self.profile_picture_file

        if self.subject is not None:
            result['Subject'] = self.subject

        if self.total_participant_count is not None:
            result['TotalParticipantCount'] = self.total_participant_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')

        if m.get('BusinessRole') is not None:
            self.business_role = m.get('BusinessRole')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtModifier') is not None:
            self.gmt_modifier = m.get('GmtModifier')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupLink') is not None:
            self.group_link = m.get('GroupLink')

        if m.get('GroupStatus') is not None:
            self.group_status = m.get('GroupStatus')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('InviteLink') is not None:
            self.invite_link = m.get('InviteLink')

        if m.get('ProfilePictureFile') is not None:
            self.profile_picture_file = m.get('ProfilePictureFile')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        if m.get('TotalParticipantCount') is not None:
            self.total_participant_count = m.get('TotalParticipantCount')

        return self

