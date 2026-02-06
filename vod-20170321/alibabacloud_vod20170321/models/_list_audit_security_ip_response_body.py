# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class ListAuditSecurityIpResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_ip_list: List[main_models.ListAuditSecurityIpResponseBodySecurityIpList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the review security group.
        self.security_ip_list = security_ip_list

    def validate(self):
        if self.security_ip_list:
            for v1 in self.security_ip_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SecurityIpList'] = []
        if self.security_ip_list is not None:
            for k1 in self.security_ip_list:
                result['SecurityIpList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.security_ip_list = []
        if m.get('SecurityIpList') is not None:
            for k1 in m.get('SecurityIpList'):
                temp_model = main_models.ListAuditSecurityIpResponseBodySecurityIpList()
                self.security_ip_list.append(temp_model.from_map(k1))

        return self

class ListAuditSecurityIpResponseBodySecurityIpList(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        ips: str = None,
        modification_time: str = None,
        security_group_name: str = None,
    ):
        # The time when the review security group was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The IP addresses in the review security group.
        self.ips = ips
        # The time when the review security group was last modified. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.modification_time = modification_time
        # The name of the review security group.
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.ips is not None:
            result['Ips'] = self.ips

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Ips') is not None:
            self.ips = m.get('Ips')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        return self

