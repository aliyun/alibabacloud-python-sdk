# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class GetAccountRelationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAccountRelationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # data
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful.
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
            temp_model = main_models.GetAccountRelationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAccountRelationResponseBodyData(DaraModel):
    def __init__(
        self,
        child_user_id: int = None,
        end_time: int = None,
        gmt_modified: int = None,
        id: int = None,
        parent_user_id: int = None,
        start_time: int = None,
        status: str = None,
        type: str = None,
    ):
        # The ID of the Alibaba Cloud account that is used as a member.
        self.child_user_id = child_user_id
        # The time when the financial relationship between the management account and the member was terminated.
        self.end_time = end_time
        # The time when the financial relationship between the management account and the member was modified.
        self.gmt_modified = gmt_modified
        # The ID of the financial relationship.
        self.id = id
        # The ID of the Alibaba Cloud account that is used as the management account.
        self.parent_user_id = parent_user_id
        # The time when the financial relationship between the management account and the member was established.
        self.start_time = start_time
        # The status of the financial relationship between the management account and the member.
        # 
        # - RELATED [Association established]
        # - CONFIRMING [To be confirmed by the other party]
        # - REJECTED [Refused by the other party]
        # - CONNECTION_CANCELED [Financial sub-account cancel request]
        # - CONNECTION_MASTER_CANCEL [Financial master account cancel invitation]
        # - CHANGE_CONFIRMING [Relationship change to be confirmed]
        # - INITIAL [Initial new relationship status]
        self.status = status
        # The type of the financial relationship.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.child_user_id is not None:
            result['ChildUserId'] = self.child_user_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.parent_user_id is not None:
            result['ParentUserId'] = self.parent_user_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildUserId') is not None:
            self.child_user_id = m.get('ChildUserId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ParentUserId') is not None:
            self.parent_user_id = m.get('ParentUserId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

