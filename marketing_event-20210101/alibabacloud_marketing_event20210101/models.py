# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class FindGuestCredentialsRecordRequest(TeaModel):
    def __init__(
        self,
        activity_id: str = None,
        date_time_string: str = None,
    ):
        self.activity_id = activity_id
        self.date_time_string = date_time_string

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.date_time_string is not None:
            result['DateTimeString'] = self.date_time_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('DateTimeString') is not None:
            self.date_time_string = m.get('DateTimeString')
        return self


class FindGuestCredentialsRecordResponseBodyDataChannelLevelInfoLevelOneOwner(TeaModel):
    def __init__(
        self,
        owner_emp_id_or_telephone: str = None,
        owner_name: str = None,
        owner_nick_name: str = None,
    ):
        self.owner_emp_id_or_telephone = owner_emp_id_or_telephone
        self.owner_name = owner_name
        self.owner_nick_name = owner_nick_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_emp_id_or_telephone is not None:
            result['OwnerEmpIdOrTelephone'] = self.owner_emp_id_or_telephone
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_nick_name is not None:
            result['OwnerNickName'] = self.owner_nick_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerEmpIdOrTelephone') is not None:
            self.owner_emp_id_or_telephone = m.get('OwnerEmpIdOrTelephone')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerNickName') is not None:
            self.owner_nick_name = m.get('OwnerNickName')
        return self


class FindGuestCredentialsRecordResponseBodyDataChannelLevelInfoLevelThreeOwner(TeaModel):
    def __init__(
        self,
        owner_emp_id_or_telephone: str = None,
        owner_name: str = None,
        owner_nick_name: str = None,
    ):
        self.owner_emp_id_or_telephone = owner_emp_id_or_telephone
        self.owner_name = owner_name
        self.owner_nick_name = owner_nick_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_emp_id_or_telephone is not None:
            result['OwnerEmpIdOrTelephone'] = self.owner_emp_id_or_telephone
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_nick_name is not None:
            result['OwnerNickName'] = self.owner_nick_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerEmpIdOrTelephone') is not None:
            self.owner_emp_id_or_telephone = m.get('OwnerEmpIdOrTelephone')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerNickName') is not None:
            self.owner_nick_name = m.get('OwnerNickName')
        return self


class FindGuestCredentialsRecordResponseBodyDataChannelLevelInfoLevelTwoOwner(TeaModel):
    def __init__(
        self,
        owner_emp_id_or_telephone: str = None,
        owner_name: str = None,
        owner_nick_name: str = None,
    ):
        self.owner_emp_id_or_telephone = owner_emp_id_or_telephone
        self.owner_name = owner_name
        self.owner_nick_name = owner_nick_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_emp_id_or_telephone is not None:
            result['OwnerEmpIdOrTelephone'] = self.owner_emp_id_or_telephone
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_nick_name is not None:
            result['OwnerNickName'] = self.owner_nick_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerEmpIdOrTelephone') is not None:
            self.owner_emp_id_or_telephone = m.get('OwnerEmpIdOrTelephone')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerNickName') is not None:
            self.owner_nick_name = m.get('OwnerNickName')
        return self


class FindGuestCredentialsRecordResponseBodyDataChannelLevelInfo(TeaModel):
    def __init__(
        self,
        channel_id: int = None,
        channel_name: str = None,
        level_one_channel_name: str = None,
        level_one_owner: List[FindGuestCredentialsRecordResponseBodyDataChannelLevelInfoLevelOneOwner] = None,
        level_three_channel_name: str = None,
        level_three_owner: List[FindGuestCredentialsRecordResponseBodyDataChannelLevelInfoLevelThreeOwner] = None,
        level_two_channel_name: str = None,
        level_two_owner: List[FindGuestCredentialsRecordResponseBodyDataChannelLevelInfoLevelTwoOwner] = None,
    ):
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.level_one_channel_name = level_one_channel_name
        self.level_one_owner = level_one_owner
        self.level_three_channel_name = level_three_channel_name
        self.level_three_owner = level_three_owner
        self.level_two_channel_name = level_two_channel_name
        self.level_two_owner = level_two_owner

    def validate(self):
        if self.level_one_owner:
            for k in self.level_one_owner:
                if k:
                    k.validate()
        if self.level_three_owner:
            for k in self.level_three_owner:
                if k:
                    k.validate()
        if self.level_two_owner:
            for k in self.level_two_owner:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.level_one_channel_name is not None:
            result['LevelOneChannelName'] = self.level_one_channel_name
        result['LevelOneOwner'] = []
        if self.level_one_owner is not None:
            for k in self.level_one_owner:
                result['LevelOneOwner'].append(k.to_map() if k else None)
        if self.level_three_channel_name is not None:
            result['LevelThreeChannelName'] = self.level_three_channel_name
        result['LevelThreeOwner'] = []
        if self.level_three_owner is not None:
            for k in self.level_three_owner:
                result['LevelThreeOwner'].append(k.to_map() if k else None)
        if self.level_two_channel_name is not None:
            result['LevelTwoChannelName'] = self.level_two_channel_name
        result['LevelTwoOwner'] = []
        if self.level_two_owner is not None:
            for k in self.level_two_owner:
                result['LevelTwoOwner'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('LevelOneChannelName') is not None:
            self.level_one_channel_name = m.get('LevelOneChannelName')
        self.level_one_owner = []
        if m.get('LevelOneOwner') is not None:
            for k in m.get('LevelOneOwner'):
                temp_model = FindGuestCredentialsRecordResponseBodyDataChannelLevelInfoLevelOneOwner()
                self.level_one_owner.append(temp_model.from_map(k))
        if m.get('LevelThreeChannelName') is not None:
            self.level_three_channel_name = m.get('LevelThreeChannelName')
        self.level_three_owner = []
        if m.get('LevelThreeOwner') is not None:
            for k in m.get('LevelThreeOwner'):
                temp_model = FindGuestCredentialsRecordResponseBodyDataChannelLevelInfoLevelThreeOwner()
                self.level_three_owner.append(temp_model.from_map(k))
        if m.get('LevelTwoChannelName') is not None:
            self.level_two_channel_name = m.get('LevelTwoChannelName')
        self.level_two_owner = []
        if m.get('LevelTwoOwner') is not None:
            for k in m.get('LevelTwoOwner'):
                temp_model = FindGuestCredentialsRecordResponseBodyDataChannelLevelInfoLevelTwoOwner()
                self.level_two_owner.append(temp_model.from_map(k))
        return self


class FindGuestCredentialsRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        admin: Dict[str, Any] = None,
        channel_id: int = None,
        channel_level_info: FindGuestCredentialsRecordResponseBodyDataChannelLevelInfo = None,
        company_name: str = None,
        credentials_code: str = None,
        credentials_name: str = None,
        id_number: str = None,
        id_type: str = None,
        name: str = None,
        status: int = None,
    ):
        self.admin = admin
        self.channel_id = channel_id
        self.channel_level_info = channel_level_info
        self.company_name = company_name
        self.credentials_code = credentials_code
        self.credentials_name = credentials_name
        self.id_number = id_number
        self.id_type = id_type
        self.name = name
        self.status = status

    def validate(self):
        if self.channel_level_info:
            self.channel_level_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin is not None:
            result['Admin'] = self.admin
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.channel_level_info is not None:
            result['ChannelLevelInfo'] = self.channel_level_info.to_map()
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.credentials_code is not None:
            result['CredentialsCode'] = self.credentials_code
        if self.credentials_name is not None:
            result['CredentialsName'] = self.credentials_name
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Admin') is not None:
            self.admin = m.get('Admin')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ChannelLevelInfo') is not None:
            temp_model = FindGuestCredentialsRecordResponseBodyDataChannelLevelInfo()
            self.channel_level_info = temp_model.from_map(m['ChannelLevelInfo'])
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('CredentialsCode') is not None:
            self.credentials_code = m.get('CredentialsCode')
        if m.get('CredentialsName') is not None:
            self.credentials_name = m.get('CredentialsName')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class FindGuestCredentialsRecordResponseBody(TeaModel):
    def __init__(
        self,
        data: List[FindGuestCredentialsRecordResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = FindGuestCredentialsRecordResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FindGuestCredentialsRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FindGuestCredentialsRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FindGuestCredentialsRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindGuestTicketRecordRequest(TeaModel):
    def __init__(
        self,
        activity_id: str = None,
        date_time_string: str = None,
    ):
        self.activity_id = activity_id
        self.date_time_string = date_time_string

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.date_time_string is not None:
            result['DateTimeString'] = self.date_time_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('DateTimeString') is not None:
            self.date_time_string = m.get('DateTimeString')
        return self


class FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelOneOwner(TeaModel):
    def __init__(
        self,
        owner_emp_id_or_telephone: str = None,
        owner_name: str = None,
        owner_nick_name: str = None,
    ):
        self.owner_emp_id_or_telephone = owner_emp_id_or_telephone
        self.owner_name = owner_name
        self.owner_nick_name = owner_nick_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_emp_id_or_telephone is not None:
            result['OwnerEmpIdOrTelephone'] = self.owner_emp_id_or_telephone
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_nick_name is not None:
            result['OwnerNickName'] = self.owner_nick_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerEmpIdOrTelephone') is not None:
            self.owner_emp_id_or_telephone = m.get('OwnerEmpIdOrTelephone')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerNickName') is not None:
            self.owner_nick_name = m.get('OwnerNickName')
        return self


class FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelThreeOwner(TeaModel):
    def __init__(
        self,
        owner_emp_id_or_telephone: str = None,
        owner_name: str = None,
        owner_nick_name: str = None,
    ):
        self.owner_emp_id_or_telephone = owner_emp_id_or_telephone
        self.owner_name = owner_name
        self.owner_nick_name = owner_nick_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_emp_id_or_telephone is not None:
            result['OwnerEmpIdOrTelephone'] = self.owner_emp_id_or_telephone
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_nick_name is not None:
            result['OwnerNickName'] = self.owner_nick_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerEmpIdOrTelephone') is not None:
            self.owner_emp_id_or_telephone = m.get('OwnerEmpIdOrTelephone')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerNickName') is not None:
            self.owner_nick_name = m.get('OwnerNickName')
        return self


class FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelTwoOwner(TeaModel):
    def __init__(
        self,
        owner_emp_id_or_telephone: str = None,
        owner_name: str = None,
        owner_nick_name: str = None,
    ):
        self.owner_emp_id_or_telephone = owner_emp_id_or_telephone
        self.owner_name = owner_name
        self.owner_nick_name = owner_nick_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_emp_id_or_telephone is not None:
            result['OwnerEmpIdOrTelephone'] = self.owner_emp_id_or_telephone
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_nick_name is not None:
            result['OwnerNickName'] = self.owner_nick_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerEmpIdOrTelephone') is not None:
            self.owner_emp_id_or_telephone = m.get('OwnerEmpIdOrTelephone')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerNickName') is not None:
            self.owner_nick_name = m.get('OwnerNickName')
        return self


class FindGuestTicketRecordResponseBodyDataChannelLevelInfo(TeaModel):
    def __init__(
        self,
        channel_id: int = None,
        channel_name: str = None,
        level_one_channel_name: str = None,
        level_one_owner: List[FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelOneOwner] = None,
        level_three_channel_name: str = None,
        level_three_owner: List[FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelThreeOwner] = None,
        level_two_channel_name: str = None,
        level_two_owner: List[FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelTwoOwner] = None,
    ):
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.level_one_channel_name = level_one_channel_name
        self.level_one_owner = level_one_owner
        self.level_three_channel_name = level_three_channel_name
        self.level_three_owner = level_three_owner
        self.level_two_channel_name = level_two_channel_name
        self.level_two_owner = level_two_owner

    def validate(self):
        if self.level_one_owner:
            for k in self.level_one_owner:
                if k:
                    k.validate()
        if self.level_three_owner:
            for k in self.level_three_owner:
                if k:
                    k.validate()
        if self.level_two_owner:
            for k in self.level_two_owner:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.level_one_channel_name is not None:
            result['LevelOneChannelName'] = self.level_one_channel_name
        result['LevelOneOwner'] = []
        if self.level_one_owner is not None:
            for k in self.level_one_owner:
                result['LevelOneOwner'].append(k.to_map() if k else None)
        if self.level_three_channel_name is not None:
            result['LevelThreeChannelName'] = self.level_three_channel_name
        result['LevelThreeOwner'] = []
        if self.level_three_owner is not None:
            for k in self.level_three_owner:
                result['LevelThreeOwner'].append(k.to_map() if k else None)
        if self.level_two_channel_name is not None:
            result['LevelTwoChannelName'] = self.level_two_channel_name
        result['LevelTwoOwner'] = []
        if self.level_two_owner is not None:
            for k in self.level_two_owner:
                result['LevelTwoOwner'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('LevelOneChannelName') is not None:
            self.level_one_channel_name = m.get('LevelOneChannelName')
        self.level_one_owner = []
        if m.get('LevelOneOwner') is not None:
            for k in m.get('LevelOneOwner'):
                temp_model = FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelOneOwner()
                self.level_one_owner.append(temp_model.from_map(k))
        if m.get('LevelThreeChannelName') is not None:
            self.level_three_channel_name = m.get('LevelThreeChannelName')
        self.level_three_owner = []
        if m.get('LevelThreeOwner') is not None:
            for k in m.get('LevelThreeOwner'):
                temp_model = FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelThreeOwner()
                self.level_three_owner.append(temp_model.from_map(k))
        if m.get('LevelTwoChannelName') is not None:
            self.level_two_channel_name = m.get('LevelTwoChannelName')
        self.level_two_owner = []
        if m.get('LevelTwoOwner') is not None:
            for k in m.get('LevelTwoOwner'):
                temp_model = FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelTwoOwner()
                self.level_two_owner.append(temp_model.from_map(k))
        return self


class FindGuestTicketRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        channel_level_info: FindGuestTicketRecordResponseBodyDataChannelLevelInfo = None,
        company_name: str = None,
        equity_dates: str = None,
        health_commitment_status: int = None,
        id_number: str = None,
        id_type: str = None,
        name: str = None,
        status: int = None,
        ticket_code: str = None,
        ticket_name: str = None,
        ticket_type: str = None,
    ):
        self.channel_level_info = channel_level_info
        self.company_name = company_name
        self.equity_dates = equity_dates
        self.health_commitment_status = health_commitment_status
        self.id_number = id_number
        self.id_type = id_type
        self.name = name
        self.status = status
        self.ticket_code = ticket_code
        self.ticket_name = ticket_name
        self.ticket_type = ticket_type

    def validate(self):
        if self.channel_level_info:
            self.channel_level_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_level_info is not None:
            result['ChannelLevelInfo'] = self.channel_level_info.to_map()
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.equity_dates is not None:
            result['EquityDates'] = self.equity_dates
        if self.health_commitment_status is not None:
            result['HealthCommitmentStatus'] = self.health_commitment_status
        if self.id_number is not None:
            result['IdNumber'] = self.id_number
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.ticket_code is not None:
            result['TicketCode'] = self.ticket_code
        if self.ticket_name is not None:
            result['TicketName'] = self.ticket_name
        if self.ticket_type is not None:
            result['TicketType'] = self.ticket_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelLevelInfo') is not None:
            temp_model = FindGuestTicketRecordResponseBodyDataChannelLevelInfo()
            self.channel_level_info = temp_model.from_map(m['ChannelLevelInfo'])
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('EquityDates') is not None:
            self.equity_dates = m.get('EquityDates')
        if m.get('HealthCommitmentStatus') is not None:
            self.health_commitment_status = m.get('HealthCommitmentStatus')
        if m.get('IdNumber') is not None:
            self.id_number = m.get('IdNumber')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TicketCode') is not None:
            self.ticket_code = m.get('TicketCode')
        if m.get('TicketName') is not None:
            self.ticket_name = m.get('TicketName')
        if m.get('TicketType') is not None:
            self.ticket_type = m.get('TicketType')
        return self


class FindGuestTicketRecordResponseBody(TeaModel):
    def __init__(
        self,
        data: List[FindGuestTicketRecordResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = FindGuestTicketRecordResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FindGuestTicketRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FindGuestTicketRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FindGuestTicketRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAllActivityInfoRequest(TeaModel):
    def __init__(
        self,
        activity_id: str = None,
    ):
        # This parameter is required.
        self.activity_id = activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        return self


class QueryAllActivityInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        activity_id: int = None,
        channel_name: str = None,
        company_name: str = None,
        customer_name: str = None,
        email: str = None,
        id: int = None,
        is_vip_customer: str = None,
        mobile: str = None,
        qrcode: str = None,
        report_fields: str = None,
    ):
        self.activity_id = activity_id
        self.channel_name = channel_name
        self.company_name = company_name
        self.customer_name = customer_name
        self.email = email
        self.id = id
        self.is_vip_customer = is_vip_customer
        self.mobile = mobile
        self.qrcode = qrcode
        self.report_fields = report_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name
        if self.email is not None:
            result['Email'] = self.email
        if self.id is not None:
            result['Id'] = self.id
        if self.is_vip_customer is not None:
            result['IsVipCustomer'] = self.is_vip_customer
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.qrcode is not None:
            result['QRCode'] = self.qrcode
        if self.report_fields is not None:
            result['ReportFields'] = self.report_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsVipCustomer') is not None:
            self.is_vip_customer = m.get('IsVipCustomer')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('QRCode') is not None:
            self.qrcode = m.get('QRCode')
        if m.get('ReportFields') is not None:
            self.report_fields = m.get('ReportFields')
        return self


class QueryAllActivityInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryAllActivityInfoResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryAllActivityInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAllActivityInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAllActivityInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryAllActivityInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySingleActivityInfoRequest(TeaModel):
    def __init__(
        self,
        activity_id: str = None,
        company_name: str = None,
        customer_name: str = None,
        mobile: str = None,
        qrcode: str = None,
    ):
        # This parameter is required.
        self.activity_id = activity_id
        self.company_name = company_name
        self.customer_name = customer_name
        self.mobile = mobile
        self.qrcode = qrcode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.qrcode is not None:
            result['QRCode'] = self.qrcode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('QRCode') is not None:
            self.qrcode = m.get('QRCode')
        return self


class QuerySingleActivityInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        activity_id: int = None,
        channel_name: str = None,
        company_name: str = None,
        customer_name: str = None,
        email: str = None,
        id: int = None,
        is_vip_customer: str = None,
        mobile: str = None,
        qrcode: str = None,
        report_fields: str = None,
    ):
        self.activity_id = activity_id
        self.channel_name = channel_name
        self.company_name = company_name
        self.customer_name = customer_name
        self.email = email
        self.id = id
        self.is_vip_customer = is_vip_customer
        self.mobile = mobile
        self.qrcode = qrcode
        self.report_fields = report_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name
        if self.email is not None:
            result['Email'] = self.email
        if self.id is not None:
            result['Id'] = self.id
        if self.is_vip_customer is not None:
            result['IsVipCustomer'] = self.is_vip_customer
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.qrcode is not None:
            result['QRCode'] = self.qrcode
        if self.report_fields is not None:
            result['ReportFields'] = self.report_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsVipCustomer') is not None:
            self.is_vip_customer = m.get('IsVipCustomer')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('QRCode') is not None:
            self.qrcode = m.get('QRCode')
        if m.get('ReportFields') is not None:
            self.report_fields = m.get('ReportFields')
        return self


class QuerySingleActivityInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QuerySingleActivityInfoResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QuerySingleActivityInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySingleActivityInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySingleActivityInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QuerySingleActivityInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncSignInInfoRequest(TeaModel):
    def __init__(
        self,
        activity_id: str = None,
        qrcode: str = None,
    ):
        # This parameter is required.
        self.activity_id = activity_id
        # This parameter is required.
        self.qrcode = qrcode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.qrcode is not None:
            result['QRCode'] = self.qrcode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('QRCode') is not None:
            self.qrcode = m.get('QRCode')
        return self


class SyncSignInInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SyncSignInInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncSignInInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SyncSignInInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


