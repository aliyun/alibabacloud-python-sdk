# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hitsdb20200615 import models as main_models
from darabonba.model import DaraModel

class GetInstanceIpWhiteListResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        group_list: List[main_models.GetInstanceIpWhiteListResponseBodyGroupList] = None,
        instance_id: str = None,
        ip_list: List[str] = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The details about the IP address whitelists.
        self.group_list = group_list
        # The ID of the Lindorm instance.
        self.instance_id = instance_id
        # The list of IP addresses in the whitelist of the instance.
        self.ip_list = ip_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.group_list:
            for v1 in self.group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['GroupList'] = []
        if self.group_list is not None:
            for k1 in self.group_list:
                result['GroupList'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip_list is not None:
            result['IpList'] = self.ip_list

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.group_list = []
        if m.get('GroupList') is not None:
            for k1 in m.get('GroupList'):
                temp_model = main_models.GetInstanceIpWhiteListResponseBodyGroupList()
                self.group_list.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceIpWhiteListResponseBodyGroupList(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        security_ip_list: str = None,
    ):
        # The name of the IP address whitelist.
        self.group_name = group_name
        # The IP addresses in the whitelist.
        self.security_ip_list = security_ip_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.security_ip_list is not None:
            result['SecurityIpList'] = self.security_ip_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('SecurityIpList') is not None:
            self.security_ip_list = m.get('SecurityIpList')

        return self

