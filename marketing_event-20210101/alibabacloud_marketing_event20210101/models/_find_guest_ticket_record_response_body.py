# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_marketing_event20210101 import models as main_models
from darabonba.model import DaraModel

class FindGuestTicketRecordResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.FindGuestTicketRecordResponseBodyData] = None,
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
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('Data'):
                temp_model = main_models.FindGuestTicketRecordResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class FindGuestTicketRecordResponseBodyData(DaraModel):
    def __init__(
        self,
        channel_level_info: main_models.FindGuestTicketRecordResponseBodyDataChannelLevelInfo = None,
        company_name: str = None,
        equity_dates: str = None,
        health_commitment_status: int = None,
        id_number: str = None,
        id_type: str = None,
        name: str = None,
        status: int = None,
        ticket_code: str = None,
        ticket_name: str = None,
        ticket_receive_dates: str = None,
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
        self.ticket_receive_dates = ticket_receive_dates
        self.ticket_type = ticket_type

    def validate(self):
        if self.channel_level_info:
            self.channel_level_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.ticket_receive_dates is not None:
            result['TicketReceiveDates'] = self.ticket_receive_dates

        if self.ticket_type is not None:
            result['TicketType'] = self.ticket_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelLevelInfo') is not None:
            temp_model = main_models.FindGuestTicketRecordResponseBodyDataChannelLevelInfo()
            self.channel_level_info = temp_model.from_map(m.get('ChannelLevelInfo'))

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

        if m.get('TicketReceiveDates') is not None:
            self.ticket_receive_dates = m.get('TicketReceiveDates')

        if m.get('TicketType') is not None:
            self.ticket_type = m.get('TicketType')

        return self

class FindGuestTicketRecordResponseBodyDataChannelLevelInfo(DaraModel):
    def __init__(
        self,
        channel_id: int = None,
        channel_name: str = None,
        level_one_channel_name: str = None,
        level_one_owner: List[main_models.FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelOneOwner] = None,
        level_three_channel_name: str = None,
        level_three_owner: List[main_models.FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelThreeOwner] = None,
        level_two_channel_name: str = None,
        level_two_owner: List[main_models.FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelTwoOwner] = None,
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
            for v1 in self.level_one_owner:
                 if v1:
                    v1.validate()
        if self.level_three_owner:
            for v1 in self.level_three_owner:
                 if v1:
                    v1.validate()
        if self.level_two_owner:
            for v1 in self.level_two_owner:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.level_one_channel_name is not None:
            result['LevelOneChannelName'] = self.level_one_channel_name

        result['LevelOneOwner'] = []
        if self.level_one_owner is not None:
            for k1 in self.level_one_owner:
                result['LevelOneOwner'].append(k1.to_map() if k1 else None)

        if self.level_three_channel_name is not None:
            result['LevelThreeChannelName'] = self.level_three_channel_name

        result['LevelThreeOwner'] = []
        if self.level_three_owner is not None:
            for k1 in self.level_three_owner:
                result['LevelThreeOwner'].append(k1.to_map() if k1 else None)

        if self.level_two_channel_name is not None:
            result['LevelTwoChannelName'] = self.level_two_channel_name

        result['LevelTwoOwner'] = []
        if self.level_two_owner is not None:
            for k1 in self.level_two_owner:
                result['LevelTwoOwner'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('LevelOneOwner'):
                temp_model = main_models.FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelOneOwner()
                self.level_one_owner.append(temp_model.from_map(k1))

        if m.get('LevelThreeChannelName') is not None:
            self.level_three_channel_name = m.get('LevelThreeChannelName')

        self.level_three_owner = []
        if m.get('LevelThreeOwner') is not None:
            for k1 in m.get('LevelThreeOwner'):
                temp_model = main_models.FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelThreeOwner()
                self.level_three_owner.append(temp_model.from_map(k1))

        if m.get('LevelTwoChannelName') is not None:
            self.level_two_channel_name = m.get('LevelTwoChannelName')

        self.level_two_owner = []
        if m.get('LevelTwoOwner') is not None:
            for k1 in m.get('LevelTwoOwner'):
                temp_model = main_models.FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelTwoOwner()
                self.level_two_owner.append(temp_model.from_map(k1))

        return self

class FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelTwoOwner(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelThreeOwner(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class FindGuestTicketRecordResponseBodyDataChannelLevelInfoLevelOneOwner(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

