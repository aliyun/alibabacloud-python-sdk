# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_dbaudit20180320 import models as main_models
from darabonba.model import DaraModel

class GetSessionListResponseBody(DaraModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        incomplete: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        results: List[main_models.GetSessionListResponseBodyResults] = None,
        total_count: int = None,
    ):
        self.begin_date = begin_date
        self.end_date = end_date
        self.incomplete = incomplete
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.results = results
        self.total_count = total_count

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.incomplete is not None:
            result['Incomplete'] = self.incomplete

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Incomplete') is not None:
            self.incomplete = m.get('Incomplete')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.GetSessionListResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetSessionListResponseBodyResults(DaraModel):
    def __init__(
        self,
        action: str = None,
        capture_time: str = None,
        client_ip: str = None,
        client_ip_alias: str = None,
        client_mac: str = None,
        client_os_user: str = None,
        client_port: int = None,
        client_program: str = None,
        db_id: int = None,
        db_user: str = None,
        login_code: int = None,
        login_message: str = None,
        server_ip: str = None,
        server_mac: str = None,
        server_port: int = None,
        session_id: str = None,
    ):
        self.action = action
        self.capture_time = capture_time
        self.client_ip = client_ip
        self.client_ip_alias = client_ip_alias
        self.client_mac = client_mac
        self.client_os_user = client_os_user
        self.client_port = client_port
        self.client_program = client_program
        self.db_id = db_id
        self.db_user = db_user
        self.login_code = login_code
        self.login_message = login_message
        self.server_ip = server_ip
        self.server_mac = server_mac
        self.server_port = server_port
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.client_ip_alias is not None:
            result['ClientIpAlias'] = self.client_ip_alias

        if self.client_mac is not None:
            result['ClientMac'] = self.client_mac

        if self.client_os_user is not None:
            result['ClientOsUser'] = self.client_os_user

        if self.client_port is not None:
            result['ClientPort'] = self.client_port

        if self.client_program is not None:
            result['ClientProgram'] = self.client_program

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_user is not None:
            result['DbUser'] = self.db_user

        if self.login_code is not None:
            result['LoginCode'] = self.login_code

        if self.login_message is not None:
            result['LoginMessage'] = self.login_message

        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip

        if self.server_mac is not None:
            result['ServerMac'] = self.server_mac

        if self.server_port is not None:
            result['ServerPort'] = self.server_port

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('ClientIpAlias') is not None:
            self.client_ip_alias = m.get('ClientIpAlias')

        if m.get('ClientMac') is not None:
            self.client_mac = m.get('ClientMac')

        if m.get('ClientOsUser') is not None:
            self.client_os_user = m.get('ClientOsUser')

        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')

        if m.get('ClientProgram') is not None:
            self.client_program = m.get('ClientProgram')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')

        if m.get('LoginCode') is not None:
            self.login_code = m.get('LoginCode')

        if m.get('LoginMessage') is not None:
            self.login_message = m.get('LoginMessage')

        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')

        if m.get('ServerMac') is not None:
            self.server_mac = m.get('ServerMac')

        if m.get('ServerPort') is not None:
            self.server_port = m.get('ServerPort')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

