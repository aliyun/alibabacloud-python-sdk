# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetTransferInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTransferInfoResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.GetTransferInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTransferInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        creator: main_models.GetTransferInfoResponseBodyDataCreator = None,
        flow_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        last_modifier: main_models.GetTransferInfoResponseBodyDataLastModifier = None,
        new_owner: main_models.GetTransferInfoResponseBodyDataNewOwner = None,
        old_owner: main_models.GetTransferInfoResponseBodyDataOldOwner = None,
        privilege_transfer_mode: str = None,
        privilege_transfer_result_entries: List[main_models.GetTransferInfoResponseBodyDataPrivilegeTransferResultEntries] = None,
        proposal_id: int = None,
        title: str = None,
        transfer_comment: str = None,
        transfer_status: str = None,
    ):
        self.creator = creator
        self.flow_id = flow_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.last_modifier = last_modifier
        self.new_owner = new_owner
        self.old_owner = old_owner
        self.privilege_transfer_mode = privilege_transfer_mode
        self.privilege_transfer_result_entries = privilege_transfer_result_entries
        self.proposal_id = proposal_id
        self.title = title
        self.transfer_comment = transfer_comment
        self.transfer_status = transfer_status

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.last_modifier:
            self.last_modifier.validate()
        if self.new_owner:
            self.new_owner.validate()
        if self.old_owner:
            self.old_owner.validate()
        if self.privilege_transfer_result_entries:
            for v1 in self.privilege_transfer_result_entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier.to_map()

        if self.new_owner is not None:
            result['NewOwner'] = self.new_owner.to_map()

        if self.old_owner is not None:
            result['OldOwner'] = self.old_owner.to_map()

        if self.privilege_transfer_mode is not None:
            result['PrivilegeTransferMode'] = self.privilege_transfer_mode

        result['PrivilegeTransferResultEntries'] = []
        if self.privilege_transfer_result_entries is not None:
            for k1 in self.privilege_transfer_result_entries:
                result['PrivilegeTransferResultEntries'].append(k1.to_map() if k1 else None)

        if self.proposal_id is not None:
            result['ProposalId'] = self.proposal_id

        if self.title is not None:
            result['Title'] = self.title

        if self.transfer_comment is not None:
            result['TransferComment'] = self.transfer_comment

        if self.transfer_status is not None:
            result['TransferStatus'] = self.transfer_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            temp_model = main_models.GetTransferInfoResponseBodyDataCreator()
            self.creator = temp_model.from_map(m.get('Creator'))

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('LastModifier') is not None:
            temp_model = main_models.GetTransferInfoResponseBodyDataLastModifier()
            self.last_modifier = temp_model.from_map(m.get('LastModifier'))

        if m.get('NewOwner') is not None:
            temp_model = main_models.GetTransferInfoResponseBodyDataNewOwner()
            self.new_owner = temp_model.from_map(m.get('NewOwner'))

        if m.get('OldOwner') is not None:
            temp_model = main_models.GetTransferInfoResponseBodyDataOldOwner()
            self.old_owner = temp_model.from_map(m.get('OldOwner'))

        if m.get('PrivilegeTransferMode') is not None:
            self.privilege_transfer_mode = m.get('PrivilegeTransferMode')

        self.privilege_transfer_result_entries = []
        if m.get('PrivilegeTransferResultEntries') is not None:
            for k1 in m.get('PrivilegeTransferResultEntries'):
                temp_model = main_models.GetTransferInfoResponseBodyDataPrivilegeTransferResultEntries()
                self.privilege_transfer_result_entries.append(temp_model.from_map(k1))

        if m.get('ProposalId') is not None:
            self.proposal_id = m.get('ProposalId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('TransferComment') is not None:
            self.transfer_comment = m.get('TransferComment')

        if m.get('TransferStatus') is not None:
            self.transfer_status = m.get('TransferStatus')

        return self

class GetTransferInfoResponseBodyDataPrivilegeTransferResultEntries(DaraModel):
    def __init__(
        self,
        err_msg: str = None,
        privilege_display_name: str = None,
        status: str = None,
    ):
        self.err_msg = err_msg
        self.privilege_display_name = privilege_display_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.privilege_display_name is not None:
            result['PrivilegeDisplayName'] = self.privilege_display_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('PrivilegeDisplayName') is not None:
            self.privilege_display_name = m.get('PrivilegeDisplayName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetTransferInfoResponseBodyDataOldOwner(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        user_id: str = None,
    ):
        self.display_name = display_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetTransferInfoResponseBodyDataNewOwner(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        user_id: str = None,
    ):
        self.display_name = display_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetTransferInfoResponseBodyDataLastModifier(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        user_id: str = None,
    ):
        self.display_name = display_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class GetTransferInfoResponseBodyDataCreator(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        user_id: str = None,
    ):
        self.display_name = display_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

