# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddSumRecordFlowPopRequest(TeaModel):
    def __init__(
        self,
        activity_id: str = None,
        code: str = None,
        conference_name: str = None,
        device_id: str = None,
        entry_name: str = None,
        idcard: str = None,
        sign_time: str = None,
        type: int = None,
    ):
        # This parameter is required.
        self.activity_id = activity_id
        self.code = code
        # This parameter is required.
        self.conference_name = conference_name
        # This parameter is required.
        self.device_id = device_id
        # This parameter is required.
        self.entry_name = entry_name
        self.idcard = idcard
        # This parameter is required.
        self.sign_time = sign_time
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.code is not None:
            result['Code'] = self.code
        if self.conference_name is not None:
            result['ConferenceName'] = self.conference_name
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.entry_name is not None:
            result['EntryName'] = self.entry_name
        if self.idcard is not None:
            result['Idcard'] = self.idcard
        if self.sign_time is not None:
            result['SignTime'] = self.sign_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConferenceName') is not None:
            self.conference_name = m.get('ConferenceName')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('EntryName') is not None:
            self.entry_name = m.get('EntryName')
        if m.get('Idcard') is not None:
            self.idcard = m.get('Idcard')
        if m.get('SignTime') is not None:
            self.sign_time = m.get('SignTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddSumRecordFlowPopResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddSumRecordFlowPopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddSumRecordFlowPopResponseBody = None,
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
            temp_model = AddSumRecordFlowPopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindExhibitorRfidPopRequest(TeaModel):
    def __init__(
        self,
        activity_id: int = None,
        device_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        guest_ticket_record_id: int = None,
        id: int = None,
        rfid: str = None,
        ticket_code: str = None,
    ):
        # This parameter is required.
        self.activity_id = activity_id
        # This parameter is required.
        self.device_id = device_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.guest_ticket_record_id = guest_ticket_record_id
        self.id = id
        # This parameter is required.
        self.rfid = rfid
        # This parameter is required.
        self.ticket_code = ticket_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.guest_ticket_record_id is not None:
            result['GuestTicketRecordId'] = self.guest_ticket_record_id
        if self.id is not None:
            result['Id'] = self.id
        if self.rfid is not None:
            result['Rfid'] = self.rfid
        if self.ticket_code is not None:
            result['TicketCode'] = self.ticket_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GuestTicketRecordId') is not None:
            self.guest_ticket_record_id = m.get('GuestTicketRecordId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Rfid') is not None:
            self.rfid = m.get('Rfid')
        if m.get('TicketCode') is not None:
            self.ticket_code = m.get('TicketCode')
        return self


class BindExhibitorRfidPopResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindExhibitorRfidPopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindExhibitorRfidPopResponseBody = None,
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
            temp_model = BindExhibitorRfidPopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindGuestRfidPopRequest(TeaModel):
    def __init__(
        self,
        activity_id: int = None,
        device_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        guest_ticket_record_id: int = None,
        id: int = None,
        rfid: str = None,
        ticket_code: str = None,
    ):
        # This parameter is required.
        self.activity_id = activity_id
        # This parameter is required.
        self.device_id = device_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.guest_ticket_record_id = guest_ticket_record_id
        self.id = id
        # This parameter is required.
        self.rfid = rfid
        # This parameter is required.
        self.ticket_code = ticket_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.guest_ticket_record_id is not None:
            result['GuestTicketRecordId'] = self.guest_ticket_record_id
        if self.id is not None:
            result['Id'] = self.id
        if self.rfid is not None:
            result['Rfid'] = self.rfid
        if self.ticket_code is not None:
            result['TicketCode'] = self.ticket_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GuestTicketRecordId') is not None:
            self.guest_ticket_record_id = m.get('GuestTicketRecordId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Rfid') is not None:
            self.rfid = m.get('Rfid')
        if m.get('TicketCode') is not None:
            self.ticket_code = m.get('TicketCode')
        return self


class BindGuestRfidPopResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindGuestRfidPopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindGuestRfidPopResponseBody = None,
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
            temp_model = BindGuestRfidPopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckNFCBindPopRequest(TeaModel):
    def __init__(
        self,
        activity_id: int = None,
        nfc_id: str = None,
    ):
        # This parameter is required.
        self.activity_id = activity_id
        # This parameter is required.
        self.nfc_id = nfc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.nfc_id is not None:
            result['NfcId'] = self.nfc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('NfcId') is not None:
            self.nfc_id = m.get('NfcId')
        return self


class CheckNFCBindPopResponseBodyData(TeaModel):
    def __init__(
        self,
        is_global: int = None,
        is_sign: bool = None,
    ):
        self.is_global = is_global
        self.is_sign = is_sign

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_global is not None:
            result['IsGlobal'] = self.is_global
        if self.is_sign is not None:
            result['IsSign'] = self.is_sign
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsGlobal') is not None:
            self.is_global = m.get('IsGlobal')
        if m.get('IsSign') is not None:
            self.is_sign = m.get('IsSign')
        return self


class CheckNFCBindPopResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: CheckNFCBindPopResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            temp_model = CheckNFCBindPopResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckNFCBindPopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckNFCBindPopResponseBody = None,
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
            temp_model = CheckNFCBindPopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindGuestCredentialsRecordRequest(TeaModel):
    def __init__(
        self,
        activity_id: str = None,
        date_time_string: str = None,
        end_date_time: str = None,
        start_date_time: str = None,
    ):
        self.activity_id = activity_id
        self.date_time_string = date_time_string
        self.end_date_time = end_date_time
        self.start_date_time = start_date_time

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
        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time
        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('DateTimeString') is not None:
            self.date_time_string = m.get('DateTimeString')
        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')
        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')
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
        end_date_time: str = None,
        start_date_time: str = None,
    ):
        self.activity_id = activity_id
        self.date_time_string = date_time_string
        self.end_date_time = end_date_time
        self.start_date_time = start_date_time

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
        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time
        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('DateTimeString') is not None:
            self.date_time_string = m.get('DateTimeString')
        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')
        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')
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
        if self.ticket_receive_dates is not None:
            result['TicketReceiveDates'] = self.ticket_receive_dates
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
        if m.get('TicketReceiveDates') is not None:
            self.ticket_receive_dates = m.get('TicketReceiveDates')
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
        access_denied_detail: str = None,
        code: str = None,
        data: List[QueryAllActivityInfoResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryAllActivityInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
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


class QueryOrderSessionListPopRequest(TeaModel):
    def __init__(
        self,
        activity_id: int = None,
        nfc_id: str = None,
    ):
        # This parameter is required.
        self.activity_id = activity_id
        # This parameter is required.
        self.nfc_id = nfc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.nfc_id is not None:
            result['NfcId'] = self.nfc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('NfcId') is not None:
            self.nfc_id = m.get('NfcId')
        return self


class QueryOrderSessionListPopResponseBodyData(TeaModel):
    def __init__(
        self,
        session_id: int = None,
        sign_in_date: str = None,
    ):
        self.session_id = session_id
        self.sign_in_date = sign_in_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sign_in_date is not None:
            result['SignInDate'] = self.sign_in_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SignInDate') is not None:
            self.sign_in_date = m.get('SignInDate')
        return self


class QueryOrderSessionListPopResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[QueryOrderSessionListPopResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryOrderSessionListPopResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryOrderSessionListPopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryOrderSessionListPopResponseBody = None,
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
            temp_model = QueryOrderSessionListPopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySessionByActivityIdPopRequest(TeaModel):
    def __init__(
        self,
        activity_id: int = None,
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


class QuerySessionByActivityIdPopResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        description_en: str = None,
        end_date_time: str = None,
        id: int = None,
        location: str = None,
        name: str = None,
        name_en: str = None,
        start_date_time: str = None,
    ):
        self.description = description
        self.description_en = description_en
        self.end_date_time = end_date_time
        self.id = id
        self.location = location
        self.name = name
        self.name_en = name_en
        self.start_date_time = start_date_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.description_en is not None:
            result['DescriptionEn'] = self.description_en
        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time
        if self.id is not None:
            result['Id'] = self.id
        if self.location is not None:
            result['Location'] = self.location
        if self.name is not None:
            result['Name'] = self.name
        if self.name_en is not None:
            result['NameEn'] = self.name_en
        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DescriptionEn') is not None:
            self.description_en = m.get('DescriptionEn')
        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameEn') is not None:
            self.name_en = m.get('NameEn')
        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')
        return self


class QuerySessionByActivityIdPopResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[QuerySessionByActivityIdPopResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QuerySessionByActivityIdPopResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySessionByActivityIdPopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySessionByActivityIdPopResponseBody = None,
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
            temp_model = QuerySessionByActivityIdPopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySessionListPopRequest(TeaModel):
    def __init__(
        self,
        activity_id: int = None,
        nfc_id: str = None,
    ):
        # This parameter is required.
        self.activity_id = activity_id
        # This parameter is required.
        self.nfc_id = nfc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.nfc_id is not None:
            result['NfcId'] = self.nfc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('NfcId') is not None:
            self.nfc_id = m.get('NfcId')
        return self


class QuerySessionListPopResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        end_time: str = None,
        id: int = None,
        location: str = None,
        name: str = None,
        start_time: str = None,
    ):
        # code
        self.code = code
        self.end_time = end_time
        # id
        self.id = id
        # location
        self.location = location
        # name
        self.name = name
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.location is not None:
            result['Location'] = self.location
        if self.name is not None:
            result['Name'] = self.name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QuerySessionListPopResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[QuerySessionListPopResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QuerySessionListPopResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySessionListPopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySessionListPopResponseBody = None,
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
            temp_model = QuerySessionListPopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySignInRecordPopRequest(TeaModel):
    def __init__(
        self,
        activity_id: int = None,
        end_time: str = None,
        page_num: int = None,
        page_size: int = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.activity_id = activity_id
        self.end_time = end_time
        self.page_num = page_num
        self.page_size = page_size
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QuerySignInRecordPopResponseBodyData(TeaModel):
    def __init__(
        self,
        event: str = None,
        rfid: str = None,
        session_id: int = None,
        time: str = None,
    ):
        self.event = event
        # nfcid
        self.rfid = rfid
        # sessionId
        self.session_id = session_id
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event is not None:
            result['Event'] = self.event
        if self.rfid is not None:
            result['Rfid'] = self.rfid
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('Rfid') is not None:
            self.rfid = m.get('Rfid')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class QuerySignInRecordPopResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[QuerySignInRecordPopResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QuerySignInRecordPopResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySignInRecordPopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySignInRecordPopResponseBody = None,
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
            temp_model = QuerySignInRecordPopResponseBody()
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
        access_denied_detail: str = None,
        code: str = None,
        data: List[QuerySingleActivityInfoResponseBodyData] = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QuerySingleActivityInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
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
        access_denied_detail: str = None,
        code: str = None,
        data: int = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
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


class TicketOrCredentialsSignInPopRequest(TeaModel):
    def __init__(
        self,
        activity_id: str = None,
        code: str = None,
        conference_name: str = None,
        device_id: str = None,
        entry_name: str = None,
        idcard: str = None,
        sign_time: str = None,
        type: int = None,
    ):
        # This parameter is required.
        self.activity_id = activity_id
        self.code = code
        # This parameter is required.
        self.conference_name = conference_name
        # This parameter is required.
        self.device_id = device_id
        # This parameter is required.
        self.entry_name = entry_name
        self.idcard = idcard
        # This parameter is required.
        self.sign_time = sign_time
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.code is not None:
            result['Code'] = self.code
        if self.conference_name is not None:
            result['ConferenceName'] = self.conference_name
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.entry_name is not None:
            result['EntryName'] = self.entry_name
        if self.idcard is not None:
            result['Idcard'] = self.idcard
        if self.sign_time is not None:
            result['SignTime'] = self.sign_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConferenceName') is not None:
            self.conference_name = m.get('ConferenceName')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('EntryName') is not None:
            self.entry_name = m.get('EntryName')
        if m.get('Idcard') is not None:
            self.idcard = m.get('Idcard')
        if m.get('SignTime') is not None:
            self.sign_time = m.get('SignTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class TicketOrCredentialsSignInPopResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: Any = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TicketOrCredentialsSignInPopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TicketOrCredentialsSignInPopResponseBody = None,
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
            temp_model = TicketOrCredentialsSignInPopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCredentialsStatusPopRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        proxy_recipient_name: str = None,
        proxy_recipient_phone_number: str = None,
        receipt_location: str = None,
        time: str = None,
    ):
        self.code = code
        self.proxy_recipient_name = proxy_recipient_name
        self.proxy_recipient_phone_number = proxy_recipient_phone_number
        self.receipt_location = receipt_location
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.proxy_recipient_name is not None:
            result['ProxyRecipientName'] = self.proxy_recipient_name
        if self.proxy_recipient_phone_number is not None:
            result['ProxyRecipientPhoneNumber'] = self.proxy_recipient_phone_number
        if self.receipt_location is not None:
            result['ReceiptLocation'] = self.receipt_location
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ProxyRecipientName') is not None:
            self.proxy_recipient_name = m.get('ProxyRecipientName')
        if m.get('ProxyRecipientPhoneNumber') is not None:
            self.proxy_recipient_phone_number = m.get('ProxyRecipientPhoneNumber')
        if m.get('ReceiptLocation') is not None:
            self.receipt_location = m.get('ReceiptLocation')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class UpdateCredentialsStatusPopResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateCredentialsStatusPopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCredentialsStatusPopResponseBody = None,
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
            temp_model = UpdateCredentialsStatusPopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTicketRecordByticketCodePopRequest(TeaModel):
    def __init__(
        self,
        agenda_id: str = None,
        code: str = None,
        event: str = None,
        scene_id: str = None,
        time: str = None,
    ):
        self.agenda_id = agenda_id
        self.code = code
        self.event = event
        self.scene_id = scene_id
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agenda_id is not None:
            result['AgendaId'] = self.agenda_id
        if self.code is not None:
            result['Code'] = self.code
        if self.event is not None:
            result['Event'] = self.event
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgendaId') is not None:
            self.agenda_id = m.get('AgendaId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class UpdateTicketRecordByticketCodePopResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTicketRecordByticketCodePopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTicketRecordByticketCodePopResponseBody = None,
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
            temp_model = UpdateTicketRecordByticketCodePopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


