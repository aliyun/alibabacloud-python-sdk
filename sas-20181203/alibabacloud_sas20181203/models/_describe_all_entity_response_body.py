# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeAllEntityResponseBody(DaraModel):
    def __init__(
        self,
        entity_list: List[main_models.DescribeAllEntityResponseBodyEntityList] = None,
        request_id: str = None,
    ):
        # An array that consists of servers.
        self.entity_list = entity_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.entity_list:
            for v1 in self.entity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EntityList'] = []
        if self.entity_list is not None:
            for k1 in self.entity_list:
                result['EntityList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entity_list = []
        if m.get('EntityList') is not None:
            for k1 in m.get('EntityList'):
                temp_model = main_models.DescribeAllEntityResponseBodyEntityList()
                self.entity_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAllEntityResponseBodyEntityList(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        ip: str = None,
        os: str = None,
        uuid: str = None,
    ):
        # The ID of the asset group.
        self.group_id = group_id
        # The name of the server.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The IP address of the server.
        self.ip = ip
        # The operating system of the server. Valid values:
        # 
        # *   **linux**
        # *   **windows**
        self.os = os
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.os is not None:
            result['Os'] = self.os

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

