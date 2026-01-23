# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class GetInviteStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetInviteStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status Code. Error Code:
        # 
        # - 3057 InviteId is empty
        self.code = code
        # The returned data.
        self.data = data
        # The message returned.
        self.message = message
        # Request ID, Alibaba Cloud will track errors with this.
        self.request_id = request_id
        # Candidate Value: True/False, which indicates whether the current API call itself is successful. It does not guarantee the success of subsequent business operations.
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
            temp_model = main_models.GetInviteStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetInviteStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        invite_status: List[main_models.GetInviteStatusResponseBodyDataInviteStatus] = None,
    ):
        self.invite_status = invite_status

    def validate(self):
        if self.invite_status:
            for v1 in self.invite_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InviteStatus'] = []
        if self.invite_status is not None:
            for k1 in self.invite_status:
                result['InviteStatus'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invite_status = []
        if m.get('InviteStatus') is not None:
            for k1 in m.get('InviteStatus'):
                temp_model = main_models.GetInviteStatusResponseBodyDataInviteStatus()
                self.invite_status.append(temp_model.from_map(k1))

        return self

class GetInviteStatusResponseBodyDataInviteStatus(DaraModel):
    def __init__(
        self,
        code: str = None,
        invite_status_list: main_models.GetInviteStatusResponseBodyDataInviteStatusInviteStatusList = None,
        message: str = None,
        success: bool = None,
    ):
        # Result Code. Value Range:
        # *   200 OK
        # *   1109 system error
        self.code = code
        # List of Invitation Status result
        self.invite_status_list = invite_status_list
        # The message returned.
        self.message = message
        # Candidate Value: True/False, which indicates whether the current API call itself is successful. It does not guarantee the success of subsequent business operations.
        self.success = success

    def validate(self):
        if self.invite_status_list:
            self.invite_status_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.invite_status_list is not None:
            result['InviteStatusList'] = self.invite_status_list.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('InviteStatusList') is not None:
            temp_model = main_models.GetInviteStatusResponseBodyDataInviteStatusInviteStatusList()
            self.invite_status_list = temp_model.from_map(m.get('InviteStatusList'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetInviteStatusResponseBodyDataInviteStatusInviteStatusList(DaraModel):
    def __init__(
        self,
        association_success_time: str = None,
        cid: int = None,
        gmt_create: str = None,
        parent_id: str = None,
        status: int = None,
        sub_account_type: str = None,
        uid: int = None,
    ):
        # The time that Distribution Customer successfully associated with Distributor.</br>
        # This value will be empty if there is no existing association.
        self.association_success_time = association_success_time
        # Distribution Customer\\"s CID
        self.cid = cid
        # The time of email been sent out.
        self.gmt_create = gmt_create
        # The parent organization ID.
        self.parent_id = parent_id
        # Invitation Status:
        # * 0 No visit on registration URL
        # * 1 Successful Registration
        # * 2 Unsuccessful Registration
        # * 3 Registration URL have been visited, but no submitted sheet/ticket.
        self.status = status
        # Account Type:
        # - 1 Agency\\"s End User
        # - 2 Reseller\\"s End User
        # - 5 T2 Reseller Partner
        self.sub_account_type = sub_account_type
        # Distribution Customer\\"s UID
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.association_success_time is not None:
            result['AssociationSuccessTime'] = self.association_success_time

        if self.cid is not None:
            result['Cid'] = self.cid

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_account_type is not None:
            result['SubAccountType'] = self.sub_account_type

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationSuccessTime') is not None:
            self.association_success_time = m.get('AssociationSuccessTime')

        if m.get('Cid') is not None:
            self.cid = m.get('Cid')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubAccountType') is not None:
            self.sub_account_type = m.get('SubAccountType')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

