# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class DescribeBootRequest(TeaModel):
    def __init__(
        self,
        property_uuid: str = None,
    ):
        self.property_uuid = property_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_uuid is not None:
            result['PropertyUuid'] = self.property_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyUuid') is not None:
            self.property_uuid = m.get('PropertyUuid')
        return self


class DescribeBootResponseBody(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        request_id: str = None,
        white_list_affiliation: int = None,
        white_list_detail: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.request_id = request_id
        self.white_list_affiliation = white_list_affiliation
        self.white_list_detail = white_list_detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.white_list_affiliation is not None:
            result['WhiteListAffiliation'] = self.white_list_affiliation
        if self.white_list_detail is not None:
            result['WhiteListDetail'] = self.white_list_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WhiteListAffiliation') is not None:
            self.white_list_affiliation = m.get('WhiteListAffiliation')
        if m.get('WhiteListDetail') is not None:
            self.white_list_detail = m.get('WhiteListDetail')
        return self


class DescribeBootResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBootResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeBootResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventsRequest(TeaModel):
    def __init__(
        self,
        create_end_date: int = None,
        create_start_date: int = None,
        current_page: int = None,
        event_affiliation: int = None,
        event_level: int = None,
        event_status: int = None,
        event_type: int = None,
        handle_end_date: int = None,
        handle_start_date: int = None,
        handle_type: int = None,
        page_size: int = None,
        property_name: str = None,
        property_private_ip: str = None,
        property_public_ip: str = None,
        property_uuid: str = None,
        suspect: str = None,
        suspect_sig: str = None,
    ):
        self.create_end_date = create_end_date
        self.create_start_date = create_start_date
        self.current_page = current_page
        self.event_affiliation = event_affiliation
        self.event_level = event_level
        self.event_status = event_status
        self.event_type = event_type
        self.handle_end_date = handle_end_date
        self.handle_start_date = handle_start_date
        self.handle_type = handle_type
        self.page_size = page_size
        self.property_name = property_name
        self.property_private_ip = property_private_ip
        self.property_public_ip = property_public_ip
        self.property_uuid = property_uuid
        self.suspect = suspect
        self.suspect_sig = suspect_sig

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_end_date is not None:
            result['CreateEndDate'] = self.create_end_date
        if self.create_start_date is not None:
            result['CreateStartDate'] = self.create_start_date
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.event_affiliation is not None:
            result['EventAffiliation'] = self.event_affiliation
        if self.event_level is not None:
            result['EventLevel'] = self.event_level
        if self.event_status is not None:
            result['EventStatus'] = self.event_status
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.handle_end_date is not None:
            result['HandleEndDate'] = self.handle_end_date
        if self.handle_start_date is not None:
            result['HandleStartDate'] = self.handle_start_date
        if self.handle_type is not None:
            result['HandleType'] = self.handle_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.property_private_ip is not None:
            result['PropertyPrivateIp'] = self.property_private_ip
        if self.property_public_ip is not None:
            result['PropertyPublicIp'] = self.property_public_ip
        if self.property_uuid is not None:
            result['PropertyUuid'] = self.property_uuid
        if self.suspect is not None:
            result['Suspect'] = self.suspect
        if self.suspect_sig is not None:
            result['SuspectSig'] = self.suspect_sig
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateEndDate') is not None:
            self.create_end_date = m.get('CreateEndDate')
        if m.get('CreateStartDate') is not None:
            self.create_start_date = m.get('CreateStartDate')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EventAffiliation') is not None:
            self.event_affiliation = m.get('EventAffiliation')
        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')
        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('HandleEndDate') is not None:
            self.handle_end_date = m.get('HandleEndDate')
        if m.get('HandleStartDate') is not None:
            self.handle_start_date = m.get('HandleStartDate')
        if m.get('HandleType') is not None:
            self.handle_type = m.get('HandleType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('PropertyPrivateIp') is not None:
            self.property_private_ip = m.get('PropertyPrivateIp')
        if m.get('PropertyPublicIp') is not None:
            self.property_public_ip = m.get('PropertyPublicIp')
        if m.get('PropertyUuid') is not None:
            self.property_uuid = m.get('PropertyUuid')
        if m.get('Suspect') is not None:
            self.suspect = m.get('Suspect')
        if m.get('SuspectSig') is not None:
            self.suspect_sig = m.get('SuspectSig')
        return self


class DescribeEventsResponseBodyItems(TeaModel):
    def __init__(
        self,
        accumulation: str = None,
        event_affiliation: str = None,
        event_level: str = None,
        event_status: str = None,
        event_type: str = None,
        event_uuid: str = None,
        gmt_create: int = None,
        gmt_handle: int = None,
        gmt_modified: int = None,
        handle_type: str = None,
        property_name: str = None,
        property_private_ip: str = None,
        property_public_ip: str = None,
        property_uuid: str = None,
        suspect: str = None,
        suspect_sig: str = None,
        suspect_white_list: str = None,
    ):
        self.accumulation = accumulation
        self.event_affiliation = event_affiliation
        self.event_level = event_level
        self.event_status = event_status
        self.event_type = event_type
        self.event_uuid = event_uuid
        self.gmt_create = gmt_create
        self.gmt_handle = gmt_handle
        self.gmt_modified = gmt_modified
        self.handle_type = handle_type
        self.property_name = property_name
        self.property_private_ip = property_private_ip
        self.property_public_ip = property_public_ip
        self.property_uuid = property_uuid
        self.suspect = suspect
        self.suspect_sig = suspect_sig
        self.suspect_white_list = suspect_white_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accumulation is not None:
            result['Accumulation'] = self.accumulation
        if self.event_affiliation is not None:
            result['EventAffiliation'] = self.event_affiliation
        if self.event_level is not None:
            result['EventLevel'] = self.event_level
        if self.event_status is not None:
            result['EventStatus'] = self.event_status
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.event_uuid is not None:
            result['EventUuid'] = self.event_uuid
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_handle is not None:
            result['GmtHandle'] = self.gmt_handle
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.handle_type is not None:
            result['HandleType'] = self.handle_type
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.property_private_ip is not None:
            result['PropertyPrivateIp'] = self.property_private_ip
        if self.property_public_ip is not None:
            result['PropertyPublicIp'] = self.property_public_ip
        if self.property_uuid is not None:
            result['PropertyUuid'] = self.property_uuid
        if self.suspect is not None:
            result['Suspect'] = self.suspect
        if self.suspect_sig is not None:
            result['SuspectSig'] = self.suspect_sig
        if self.suspect_white_list is not None:
            result['SuspectWhiteList'] = self.suspect_white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accumulation') is not None:
            self.accumulation = m.get('Accumulation')
        if m.get('EventAffiliation') is not None:
            self.event_affiliation = m.get('EventAffiliation')
        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')
        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('EventUuid') is not None:
            self.event_uuid = m.get('EventUuid')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtHandle') is not None:
            self.gmt_handle = m.get('GmtHandle')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HandleType') is not None:
            self.handle_type = m.get('HandleType')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('PropertyPrivateIp') is not None:
            self.property_private_ip = m.get('PropertyPrivateIp')
        if m.get('PropertyPublicIp') is not None:
            self.property_public_ip = m.get('PropertyPublicIp')
        if m.get('PropertyUuid') is not None:
            self.property_uuid = m.get('PropertyUuid')
        if m.get('Suspect') is not None:
            self.suspect = m.get('Suspect')
        if m.get('SuspectSig') is not None:
            self.suspect_sig = m.get('SuspectSig')
        if m.get('SuspectWhiteList') is not None:
            self.suspect_white_list = m.get('SuspectWhiteList')
        return self


class DescribeEventsResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[DescribeEventsResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeEventsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(
        self,
        property_uuid: str = None,
    ):
        self.property_uuid = property_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_uuid is not None:
            result['PropertyUuid'] = self.property_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyUuid') is not None:
            self.property_uuid = m.get('PropertyUuid')
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        extensions: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        gmt_recent_report: int = None,
        online_status: int = None,
        program_exception_num: int = None,
        program_trust_detail: str = None,
        program_trust_status: int = None,
        program_white_list_id: int = None,
        program_white_list_name: str = None,
        property_affiliation: int = None,
        property_name: str = None,
        property_private_ip: str = None,
        property_public_ip: str = None,
        property_uuid: str = None,
        request_id: str = None,
        system_exception_num: int = None,
        system_trust_detail: str = None,
        system_trust_status: int = None,
        system_white_list_id: int = None,
    ):
        self.extensions = extensions
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.gmt_recent_report = gmt_recent_report
        self.online_status = online_status
        self.program_exception_num = program_exception_num
        self.program_trust_detail = program_trust_detail
        self.program_trust_status = program_trust_status
        self.program_white_list_id = program_white_list_id
        self.program_white_list_name = program_white_list_name
        self.property_affiliation = property_affiliation
        self.property_name = property_name
        self.property_private_ip = property_private_ip
        self.property_public_ip = property_public_ip
        self.property_uuid = property_uuid
        self.request_id = request_id
        self.system_exception_num = system_exception_num
        self.system_trust_detail = system_trust_detail
        self.system_trust_status = system_trust_status
        self.system_white_list_id = system_white_list_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.gmt_recent_report is not None:
            result['GmtRecentReport'] = self.gmt_recent_report
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        if self.program_exception_num is not None:
            result['ProgramExceptionNum'] = self.program_exception_num
        if self.program_trust_detail is not None:
            result['ProgramTrustDetail'] = self.program_trust_detail
        if self.program_trust_status is not None:
            result['ProgramTrustStatus'] = self.program_trust_status
        if self.program_white_list_id is not None:
            result['ProgramWhiteListId'] = self.program_white_list_id
        if self.program_white_list_name is not None:
            result['ProgramWhiteListName'] = self.program_white_list_name
        if self.property_affiliation is not None:
            result['PropertyAffiliation'] = self.property_affiliation
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.property_private_ip is not None:
            result['PropertyPrivateIp'] = self.property_private_ip
        if self.property_public_ip is not None:
            result['PropertyPublicIp'] = self.property_public_ip
        if self.property_uuid is not None:
            result['PropertyUuid'] = self.property_uuid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.system_exception_num is not None:
            result['SystemExceptionNum'] = self.system_exception_num
        if self.system_trust_detail is not None:
            result['SystemTrustDetail'] = self.system_trust_detail
        if self.system_trust_status is not None:
            result['SystemTrustStatus'] = self.system_trust_status
        if self.system_white_list_id is not None:
            result['SystemWhiteListId'] = self.system_white_list_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GmtRecentReport') is not None:
            self.gmt_recent_report = m.get('GmtRecentReport')
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        if m.get('ProgramExceptionNum') is not None:
            self.program_exception_num = m.get('ProgramExceptionNum')
        if m.get('ProgramTrustDetail') is not None:
            self.program_trust_detail = m.get('ProgramTrustDetail')
        if m.get('ProgramTrustStatus') is not None:
            self.program_trust_status = m.get('ProgramTrustStatus')
        if m.get('ProgramWhiteListId') is not None:
            self.program_white_list_id = m.get('ProgramWhiteListId')
        if m.get('ProgramWhiteListName') is not None:
            self.program_white_list_name = m.get('ProgramWhiteListName')
        if m.get('PropertyAffiliation') is not None:
            self.property_affiliation = m.get('PropertyAffiliation')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('PropertyPrivateIp') is not None:
            self.property_private_ip = m.get('PropertyPrivateIp')
        if m.get('PropertyPublicIp') is not None:
            self.property_public_ip = m.get('PropertyPublicIp')
        if m.get('PropertyUuid') is not None:
            self.property_uuid = m.get('PropertyUuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SystemExceptionNum') is not None:
            self.system_exception_num = m.get('SystemExceptionNum')
        if m.get('SystemTrustDetail') is not None:
            self.system_trust_detail = m.get('SystemTrustDetail')
        if m.get('SystemTrustStatus') is not None:
            self.system_trust_status = m.get('SystemTrustStatus')
        if m.get('SystemWhiteListId') is not None:
            self.system_white_list_id = m.get('SystemWhiteListId')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateAikcertRequest(TeaModel):
    def __init__(
        self,
        aik_name: str = None,
        aik_pub: str = None,
        ek_cert: str = None,
        ek_pub: str = None,
        nonce_digest: str = None,
        property_uuid: str = None,
    ):
        self.aik_name = aik_name
        self.aik_pub = aik_pub
        self.ek_cert = ek_cert
        self.ek_pub = ek_pub
        self.nonce_digest = nonce_digest
        self.property_uuid = property_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aik_name is not None:
            result['AikName'] = self.aik_name
        if self.aik_pub is not None:
            result['AikPub'] = self.aik_pub
        if self.ek_cert is not None:
            result['EkCert'] = self.ek_cert
        if self.ek_pub is not None:
            result['EkPub'] = self.ek_pub
        if self.nonce_digest is not None:
            result['NonceDigest'] = self.nonce_digest
        if self.property_uuid is not None:
            result['PropertyUuid'] = self.property_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AikName') is not None:
            self.aik_name = m.get('AikName')
        if m.get('AikPub') is not None:
            self.aik_pub = m.get('AikPub')
        if m.get('EkCert') is not None:
            self.ek_cert = m.get('EkCert')
        if m.get('EkPub') is not None:
            self.ek_pub = m.get('EkPub')
        if m.get('NonceDigest') is not None:
            self.nonce_digest = m.get('NonceDigest')
        if m.get('PropertyUuid') is not None:
            self.property_uuid = m.get('PropertyUuid')
        return self


class GenerateAikcertResponseBodyData(TeaModel):
    def __init__(
        self,
        data_credential_blob: str = None,
        key_credential_blob: str = None,
    ):
        self.data_credential_blob = data_credential_blob
        self.key_credential_blob = key_credential_blob

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_credential_blob is not None:
            result['dataCredentialBlob'] = self.data_credential_blob
        if self.key_credential_blob is not None:
            result['keyCredentialBlob'] = self.key_credential_blob
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataCredentialBlob') is not None:
            self.data_credential_blob = m.get('dataCredentialBlob')
        if m.get('keyCredentialBlob') is not None:
            self.key_credential_blob = m.get('keyCredentialBlob')
        return self


class GenerateAikcertResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GenerateAikcertResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = GenerateAikcertResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class GenerateAikcertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateAikcertResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GenerateAikcertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateNonceRequest(TeaModel):
    def __init__(
        self,
        aik_name: str = None,
        ek_cert: str = None,
        ek_pub: str = None,
        property_uuid: str = None,
    ):
        self.aik_name = aik_name
        self.ek_cert = ek_cert
        self.ek_pub = ek_pub
        self.property_uuid = property_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aik_name is not None:
            result['AikName'] = self.aik_name
        if self.ek_cert is not None:
            result['EkCert'] = self.ek_cert
        if self.ek_pub is not None:
            result['EkPub'] = self.ek_pub
        if self.property_uuid is not None:
            result['PropertyUuid'] = self.property_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AikName') is not None:
            self.aik_name = m.get('AikName')
        if m.get('EkCert') is not None:
            self.ek_cert = m.get('EkCert')
        if m.get('EkPub') is not None:
            self.ek_pub = m.get('EkPub')
        if m.get('PropertyUuid') is not None:
            self.property_uuid = m.get('PropertyUuid')
        return self


class GenerateNonceResponseBodyData(TeaModel):
    def __init__(
        self,
        credential_blob: str = None,
    ):
        self.credential_blob = credential_blob

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_blob is not None:
            result['CredentialBlob'] = self.credential_blob
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialBlob') is not None:
            self.credential_blob = m.get('CredentialBlob')
        return self


class GenerateNonceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GenerateNonceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = GenerateNonceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class GenerateNonceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateNonceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GenerateNonceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IgnoreEventsRequest(TeaModel):
    def __init__(
        self,
        event_uuids: str = None,
        handle_style: int = None,
    ):
        self.event_uuids = event_uuids
        self.handle_style = handle_style

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_uuids is not None:
            result['EventUuids'] = self.event_uuids
        if self.handle_style is not None:
            result['HandleStyle'] = self.handle_style
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventUuids') is not None:
            self.event_uuids = m.get('EventUuids')
        if m.get('HandleStyle') is not None:
            self.handle_style = m.get('HandleStyle')
        return self


class IgnoreEventsResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IgnoreEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IgnoreEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = IgnoreEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProduceAikcertRequest(TeaModel):
    def __init__(
        self,
        aik_name: str = None,
        cert_request: str = None,
        ek_cert: str = None,
        ek_pub_key: str = None,
        include_cert_chain: bool = None,
    ):
        self.aik_name = aik_name
        self.cert_request = cert_request
        self.ek_cert = ek_cert
        self.ek_pub_key = ek_pub_key
        self.include_cert_chain = include_cert_chain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aik_name is not None:
            result['AikName'] = self.aik_name
        if self.cert_request is not None:
            result['CertRequest'] = self.cert_request
        if self.ek_cert is not None:
            result['EkCert'] = self.ek_cert
        if self.ek_pub_key is not None:
            result['EkPubKey'] = self.ek_pub_key
        if self.include_cert_chain is not None:
            result['IncludeCertChain'] = self.include_cert_chain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AikName') is not None:
            self.aik_name = m.get('AikName')
        if m.get('CertRequest') is not None:
            self.cert_request = m.get('CertRequest')
        if m.get('EkCert') is not None:
            self.ek_cert = m.get('EkCert')
        if m.get('EkPubKey') is not None:
            self.ek_pub_key = m.get('EkPubKey')
        if m.get('IncludeCertChain') is not None:
            self.include_cert_chain = m.get('IncludeCertChain')
        return self


class ProduceAikcertResponseBodyData(TeaModel):
    def __init__(
        self,
        data_credential_blob: str = None,
        key_credential_blob: str = None,
    ):
        self.data_credential_blob = data_credential_blob
        self.key_credential_blob = key_credential_blob

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_credential_blob is not None:
            result['DataCredentialBlob'] = self.data_credential_blob
        if self.key_credential_blob is not None:
            result['KeyCredentialBlob'] = self.key_credential_blob
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCredentialBlob') is not None:
            self.data_credential_blob = m.get('DataCredentialBlob')
        if m.get('KeyCredentialBlob') is not None:
            self.key_credential_blob = m.get('KeyCredentialBlob')
        return self


class ProduceAikcertResponseBody(TeaModel):
    def __init__(
        self,
        data: ProduceAikcertResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ProduceAikcertResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ProduceAikcertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ProduceAikcertResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ProduceAikcertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutMessageRequest(TeaModel):
    def __init__(
        self,
        file_data: str = None,
        property_uuid: str = None,
    ):
        self.file_data = file_data
        self.property_uuid = property_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_data is not None:
            result['FileData'] = self.file_data
        if self.property_uuid is not None:
            result['PropertyUuid'] = self.property_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileData') is not None:
            self.file_data = m.get('FileData')
        if m.get('PropertyUuid') is not None:
            self.property_uuid = m.get('PropertyUuid')
        return self


class PutMessageResponseBodyDataKmoduleVerificationResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        status: int = None,
    ):
        self.code = code
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class PutMessageResponseBodyDataPolicyProcResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        proc_data: str = None,
    ):
        self.code = code
        self.proc_data = proc_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.proc_data is not None:
            result['procData'] = self.proc_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('procData') is not None:
            self.proc_data = m.get('procData')
        return self


class PutMessageResponseBodyDataProgramVerificationResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        status: int = None,
    ):
        self.code = code
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class PutMessageResponseBodyDataSystemVerificationResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        status: int = None,
    ):
        self.code = code
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class PutMessageResponseBodyData(TeaModel):
    def __init__(
        self,
        kmodule_verification_result: PutMessageResponseBodyDataKmoduleVerificationResult = None,
        next_client_imaindex: int = None,
        policy_proc_result: PutMessageResponseBodyDataPolicyProcResult = None,
        program_verification_result: PutMessageResponseBodyDataProgramVerificationResult = None,
        system_verification_result: PutMessageResponseBodyDataSystemVerificationResult = None,
    ):
        self.kmodule_verification_result = kmodule_verification_result
        self.next_client_imaindex = next_client_imaindex
        self.policy_proc_result = policy_proc_result
        self.program_verification_result = program_verification_result
        self.system_verification_result = system_verification_result

    def validate(self):
        if self.kmodule_verification_result:
            self.kmodule_verification_result.validate()
        if self.policy_proc_result:
            self.policy_proc_result.validate()
        if self.program_verification_result:
            self.program_verification_result.validate()
        if self.system_verification_result:
            self.system_verification_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kmodule_verification_result is not None:
            result['kmoduleVerificationResult'] = self.kmodule_verification_result.to_map()
        if self.next_client_imaindex is not None:
            result['nextClientIMAIndex'] = self.next_client_imaindex
        if self.policy_proc_result is not None:
            result['policyProcResult'] = self.policy_proc_result.to_map()
        if self.program_verification_result is not None:
            result['programVerificationResult'] = self.program_verification_result.to_map()
        if self.system_verification_result is not None:
            result['systemVerificationResult'] = self.system_verification_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kmoduleVerificationResult') is not None:
            temp_model = PutMessageResponseBodyDataKmoduleVerificationResult()
            self.kmodule_verification_result = temp_model.from_map(m['kmoduleVerificationResult'])
        if m.get('nextClientIMAIndex') is not None:
            self.next_client_imaindex = m.get('nextClientIMAIndex')
        if m.get('policyProcResult') is not None:
            temp_model = PutMessageResponseBodyDataPolicyProcResult()
            self.policy_proc_result = temp_model.from_map(m['policyProcResult'])
        if m.get('programVerificationResult') is not None:
            temp_model = PutMessageResponseBodyDataProgramVerificationResult()
            self.program_verification_result = temp_model.from_map(m['programVerificationResult'])
        if m.get('systemVerificationResult') is not None:
            temp_model = PutMessageResponseBodyDataSystemVerificationResult()
            self.system_verification_result = temp_model.from_map(m['systemVerificationResult'])
        return self


class PutMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: PutMessageResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            temp_model = PutMessageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class PutMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = PutMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterMessageRequest(TeaModel):
    def __init__(
        self,
        extensions: str = None,
        instance_id: str = None,
        instance_type: str = None,
        property_affiliation: int = None,
        property_name: str = None,
        property_private_ip: str = None,
        property_public_ip: str = None,
        property_uuid: str = None,
    ):
        self.extensions = extensions
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.property_affiliation = property_affiliation
        self.property_name = property_name
        self.property_private_ip = property_private_ip
        self.property_public_ip = property_public_ip
        self.property_uuid = property_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.property_affiliation is not None:
            result['PropertyAffiliation'] = self.property_affiliation
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.property_private_ip is not None:
            result['PropertyPrivateIp'] = self.property_private_ip
        if self.property_public_ip is not None:
            result['PropertyPublicIp'] = self.property_public_ip
        if self.property_uuid is not None:
            result['PropertyUuid'] = self.property_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PropertyAffiliation') is not None:
            self.property_affiliation = m.get('PropertyAffiliation')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('PropertyPrivateIp') is not None:
            self.property_private_ip = m.get('PropertyPrivateIp')
        if m.get('PropertyPublicIp') is not None:
            self.property_public_ip = m.get('PropertyPublicIp')
        if m.get('PropertyUuid') is not None:
            self.property_uuid = m.get('PropertyUuid')
        return self


class RegisterMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RegisterMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TrustEventsRequest(TeaModel):
    def __init__(
        self,
        event_uuids: str = None,
        handle_style: int = None,
    ):
        self.event_uuids = event_uuids
        self.handle_style = handle_style

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_uuids is not None:
            result['EventUuids'] = self.event_uuids
        if self.handle_style is not None:
            result['HandleStyle'] = self.handle_style
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventUuids') is not None:
            self.event_uuids = m.get('EventUuids')
        if m.get('HandleStyle') is not None:
            self.handle_style = m.get('HandleStyle')
        return self


class TrustEventsResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TrustEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TrustEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = TrustEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnregisterMessageRequest(TeaModel):
    def __init__(
        self,
        properties: str = None,
    ):
        self.properties = properties

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['Properties'] = self.properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        return self


class UnregisterMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnregisterMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnregisterMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UnregisterMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyMessageRequest(TeaModel):
    def __init__(
        self,
        file_data: str = None,
    ):
        self.file_data = file_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_data is not None:
            result['FileData'] = self.file_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileData') is not None:
            self.file_data = m.get('FileData')
        return self


class VerifyMessageResponseBodyDataImaVerificationResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        status: int = None,
        tcb_obsolete: List[str] = None,
        untrusted: List[str] = None,
    ):
        self.code = code
        self.status = status
        self.tcb_obsolete = tcb_obsolete
        self.untrusted = untrusted

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.status is not None:
            result['Status'] = self.status
        if self.tcb_obsolete is not None:
            result['TcbObsolete'] = self.tcb_obsolete
        if self.untrusted is not None:
            result['Untrusted'] = self.untrusted
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TcbObsolete') is not None:
            self.tcb_obsolete = m.get('TcbObsolete')
        if m.get('Untrusted') is not None:
            self.untrusted = m.get('Untrusted')
        return self


class VerifyMessageResponseBodyDataPcrVerificationResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        status: int = None,
        tcb_obsolete: List[str] = None,
        untrusted: List[str] = None,
    ):
        self.code = code
        self.status = status
        self.tcb_obsolete = tcb_obsolete
        self.untrusted = untrusted

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.status is not None:
            result['Status'] = self.status
        if self.tcb_obsolete is not None:
            result['TcbObsolete'] = self.tcb_obsolete
        if self.untrusted is not None:
            result['Untrusted'] = self.untrusted
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TcbObsolete') is not None:
            self.tcb_obsolete = m.get('TcbObsolete')
        if m.get('Untrusted') is not None:
            self.untrusted = m.get('Untrusted')
        return self


class VerifyMessageResponseBodyData(TeaModel):
    def __init__(
        self,
        ima_verification_result: VerifyMessageResponseBodyDataImaVerificationResult = None,
        pcr_verification_result: VerifyMessageResponseBodyDataPcrVerificationResult = None,
    ):
        self.ima_verification_result = ima_verification_result
        self.pcr_verification_result = pcr_verification_result

    def validate(self):
        if self.ima_verification_result:
            self.ima_verification_result.validate()
        if self.pcr_verification_result:
            self.pcr_verification_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ima_verification_result is not None:
            result['ImaVerificationResult'] = self.ima_verification_result.to_map()
        if self.pcr_verification_result is not None:
            result['PcrVerificationResult'] = self.pcr_verification_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImaVerificationResult') is not None:
            temp_model = VerifyMessageResponseBodyDataImaVerificationResult()
            self.ima_verification_result = temp_model.from_map(m['ImaVerificationResult'])
        if m.get('PcrVerificationResult') is not None:
            temp_model = VerifyMessageResponseBodyDataPcrVerificationResult()
            self.pcr_verification_result = temp_model.from_map(m['PcrVerificationResult'])
        return self


class VerifyMessageResponseBody(TeaModel):
    def __init__(
        self,
        data: VerifyMessageResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = VerifyMessageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = VerifyMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


