# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribePropertyUserDetailResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribePropertyUserDetailResponseBodyPageInfo = None,
        propertys: List[main_models.DescribePropertyUserDetailResponseBodyPropertys] = None,
        request_id: str = None,
    ):
        # The pagination information of the query result.
        self.page_info = page_info
        # The details of the account asset fingerprint entries returned.
        self.propertys = propertys
        # The ID of the request. Alibaba Cloud generates a unique identifier for the request. You can use the ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.propertys:
            for v1 in self.propertys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['Propertys'] = []
        if self.propertys is not None:
            for k1 in self.propertys:
                result['Propertys'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribePropertyUserDetailResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.propertys = []
        if m.get('Propertys') is not None:
            for k1 in m.get('Propertys'):
                temp_model = main_models.DescribePropertyUserDetailResponseBodyPropertys()
                self.propertys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePropertyUserDetailResponseBodyPropertys(DaraModel):
    def __init__(
        self,
        accounts_expiration_date: str = None,
        create_timestamp: int = None,
        group_names: List[str] = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        ip: str = None,
        is_could_login: int = None,
        is_passwd_expired: int = None,
        is_passwd_locked: int = None,
        is_root: str = None,
        is_sudoer: int = None,
        is_user_expired: int = None,
        last_login_ip: str = None,
        last_login_time: str = None,
        last_login_time_dt: int = None,
        last_login_timestamp: int = None,
        password_expiration_date: str = None,
        status: str = None,
        user: str = None,
        uuid: str = None,
    ):
        # The expiration time of the account.
        self.accounts_expiration_date = accounts_expiration_date
        # The timestamp of the latest Asset Fingerprints scan. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # The details of the user groups to which the account belongs.
        self.group_names = group_names
        # The instance ID of the server.
        self.instance_id = instance_id
        # The name of the server instance.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The list of IP addresses of the server.
        self.ip = ip
        # Indicates whether the account is an interactive logon account. Valid values:
        # 
        # - **0**: No.
        # - **1**: Yes.
        self.is_could_login = is_could_login
        # Indicates whether the password has expired. Valid values:
        # 
        # - **0**: Expired.
        # - **1**: Not expired.
        self.is_passwd_expired = is_passwd_expired
        # Indicates whether the password is locked. Valid values:
        # 
        # - **0**: Locked.
        # - **1**: Not locked.
        self.is_passwd_locked = is_passwd_locked
        # Indicates whether the account has ROOT permissions. Valid values:
        # 
        # - **0**: No.
        # - **1**: Yes.
        self.is_root = is_root
        # Indicates whether the account is a sudo account. Valid values:
        # 
        # - **0**: No.
        # - **1**: Yes.
        self.is_sudoer = is_sudoer
        # Indicates whether the user has expired. Valid values:
        # 
        # - **0**: Expired.
        # - **1**: Not expired.
        self.is_user_expired = is_user_expired
        # The source IP address of the last logon of the account.
        self.last_login_ip = last_login_ip
        # The time of the last logon of the account.
        self.last_login_time = last_login_time
        # The timestamp of the last logon of the account. Unit: milliseconds.
        self.last_login_time_dt = last_login_time_dt
        # The timestamp of the last logon of the account. Unit: milliseconds.
        self.last_login_timestamp = last_login_timestamp
        # The expiration time of the account password.
        self.password_expiration_date = password_expiration_date
        # This parameter is deprecated and can be ignored.
        self.status = status
        # The name of the account.
        self.user = user
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accounts_expiration_date is not None:
            result['AccountsExpirationDate'] = self.accounts_expiration_date

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.group_names is not None:
            result['GroupNames'] = self.group_names

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.is_could_login is not None:
            result['IsCouldLogin'] = self.is_could_login

        if self.is_passwd_expired is not None:
            result['IsPasswdExpired'] = self.is_passwd_expired

        if self.is_passwd_locked is not None:
            result['IsPasswdLocked'] = self.is_passwd_locked

        if self.is_root is not None:
            result['IsRoot'] = self.is_root

        if self.is_sudoer is not None:
            result['IsSudoer'] = self.is_sudoer

        if self.is_user_expired is not None:
            result['IsUserExpired'] = self.is_user_expired

        if self.last_login_ip is not None:
            result['LastLoginIp'] = self.last_login_ip

        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time

        if self.last_login_time_dt is not None:
            result['LastLoginTimeDt'] = self.last_login_time_dt

        if self.last_login_timestamp is not None:
            result['LastLoginTimestamp'] = self.last_login_timestamp

        if self.password_expiration_date is not None:
            result['PasswordExpirationDate'] = self.password_expiration_date

        if self.status is not None:
            result['Status'] = self.status

        if self.user is not None:
            result['User'] = self.user

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountsExpirationDate') is not None:
            self.accounts_expiration_date = m.get('AccountsExpirationDate')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('GroupNames') is not None:
            self.group_names = m.get('GroupNames')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('IsCouldLogin') is not None:
            self.is_could_login = m.get('IsCouldLogin')

        if m.get('IsPasswdExpired') is not None:
            self.is_passwd_expired = m.get('IsPasswdExpired')

        if m.get('IsPasswdLocked') is not None:
            self.is_passwd_locked = m.get('IsPasswdLocked')

        if m.get('IsRoot') is not None:
            self.is_root = m.get('IsRoot')

        if m.get('IsSudoer') is not None:
            self.is_sudoer = m.get('IsSudoer')

        if m.get('IsUserExpired') is not None:
            self.is_user_expired = m.get('IsUserExpired')

        if m.get('LastLoginIp') is not None:
            self.last_login_ip = m.get('LastLoginIp')

        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')

        if m.get('LastLoginTimeDt') is not None:
            self.last_login_time_dt = m.get('LastLoginTimeDt')

        if m.get('LastLoginTimestamp') is not None:
            self.last_login_timestamp = m.get('LastLoginTimestamp')

        if m.get('PasswordExpirationDate') is not None:
            self.password_expiration_date = m.get('PasswordExpirationDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('User') is not None:
            self.user = m.get('User')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribePropertyUserDetailResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        next_token: str = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of account asset fingerprint entries on the current page.
        self.count = count
        # The page number of the current page in a paging query.
        self.current_page = current_page
        # The NextToken value returned when the NextToken method is used.
        self.next_token = next_token
        # The number of account asset fingerprint entries per page in a paging query. Default value: **10**, which indicates 10 account asset fingerprint entries per page.
        self.page_size = page_size
        # The total number of account asset fingerprint entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

