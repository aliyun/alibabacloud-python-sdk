# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListSipTrunksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        list: List[main_models.ListSipTrunksResponseBodyList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The list of SIP trunks.
        self.list = list
        # The message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

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

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListSipTrunksResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSipTrunksResponseBodyList(DaraModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        ips: List[main_models.ListSipTrunksResponseBodyListIps] = None,
        trunk_id: str = None,
        trunk_name: str = None,
    ):
        # The description of the SIP trunk.
        self.description = description
        # The creation timestamp, in milliseconds.
        self.gmt_create = gmt_create
        # The list of IP addresses of the SIP trunk.
        self.ips = ips
        # The unique identifier of the SIP trunk.
        self.trunk_id = trunk_id
        # The name of the SIP trunk.
        self.trunk_name = trunk_name

    def validate(self):
        if self.ips:
            for v1 in self.ips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        result['Ips'] = []
        if self.ips is not None:
            for k1 in self.ips:
                result['Ips'].append(k1.to_map() if k1 else None)

        if self.trunk_id is not None:
            result['TrunkId'] = self.trunk_id

        if self.trunk_name is not None:
            result['TrunkName'] = self.trunk_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        self.ips = []
        if m.get('Ips') is not None:
            for k1 in m.get('Ips'):
                temp_model = main_models.ListSipTrunksResponseBodyListIps()
                self.ips.append(temp_model.from_map(k1))

        if m.get('TrunkId') is not None:
            self.trunk_id = m.get('TrunkId')

        if m.get('TrunkName') is not None:
            self.trunk_name = m.get('TrunkName')

        return self

class ListSipTrunksResponseBodyListIps(DaraModel):
    def __init__(
        self,
        ip: str = None,
    ):
        # The IP address of the SIP trunk.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        return self

