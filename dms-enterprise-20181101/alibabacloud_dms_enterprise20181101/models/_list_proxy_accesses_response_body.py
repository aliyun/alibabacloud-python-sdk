# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListProxyAccessesResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        proxy_access_list: List[main_models.ListProxyAccessesResponseBodyProxyAccessList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The information about the users that are authorized to access the database instance by using the secure access proxy feature.
        self.proxy_access_list = proxy_access_list
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.proxy_access_list:
            for v1 in self.proxy_access_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        result['ProxyAccessList'] = []
        if self.proxy_access_list is not None:
            for k1 in self.proxy_access_list:
                result['ProxyAccessList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        self.proxy_access_list = []
        if m.get('ProxyAccessList') is not None:
            for k1 in m.get('ProxyAccessList'):
                temp_model = main_models.ListProxyAccessesResponseBodyProxyAccessList()
                self.proxy_access_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListProxyAccessesResponseBodyProxyAccessList(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        gmt_create: str = None,
        indep_account: str = None,
        instance_id: int = None,
        origin_info: str = None,
        proxy_access_id: int = None,
        proxy_id: int = None,
        user_id: int = None,
        user_name: str = None,
        user_uid: str = None,
    ):
        # The username of the database account that is authorized to access the database instance by using the secure access proxy feature.
        self.access_id = access_id
        # The time when the user is authorized to access the database instance by using the secure access proxy feature.
        self.gmt_create = gmt_create
        # The username of the independent database account.
        self.indep_account = indep_account
        # The ID of the database instance.
        self.instance_id = instance_id
        # The method that is used to authorize the user to access the database instance by using the secure access proxy feature. Valid values: 
        # 
        # - **Authorization by the Alibaba Cloud Account ()**: The information in the parentheses () indicates the user ID (UID) of the Alibaba Cloud account.
        # - **Authorization by submitting the ticket ()**:The information in the parentheses () indicates the number of the ticket that the user submits to apply for permissions.
        self.origin_info = origin_info
        # The ID that DMS generates after the user is authorized to access the database instance by using the secure access proxy feature. The ID is unique in DMS.
        self.proxy_access_id = proxy_access_id
        # The ID of the secure access proxy.
        self.proxy_id = proxy_id
        # The ID of the user.
        self.user_id = user_id
        # The nickname of the user.
        self.user_name = user_name
        # The UID of the Alibaba Cloud account.
        self.user_uid = user_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.indep_account is not None:
            result['IndepAccount'] = self.indep_account

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.origin_info is not None:
            result['OriginInfo'] = self.origin_info

        if self.proxy_access_id is not None:
            result['ProxyAccessId'] = self.proxy_access_id

        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.user_uid is not None:
            result['UserUid'] = self.user_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('IndepAccount') is not None:
            self.indep_account = m.get('IndepAccount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OriginInfo') is not None:
            self.origin_info = m.get('OriginInfo')

        if m.get('ProxyAccessId') is not None:
            self.proxy_access_id = m.get('ProxyAccessId')

        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('UserUid') is not None:
            self.user_uid = m.get('UserUid')

        return self

