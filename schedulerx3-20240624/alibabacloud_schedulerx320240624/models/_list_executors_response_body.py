# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class ListExecutorsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListExecutorsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -
        self.data = data
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListExecutorsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListExecutorsResponseBodyData(DaraModel):
    def __init__(
        self,
        address: str = None,
        ip: str = None,
        is_designated: bool = None,
        label: str = None,
        online: bool = None,
        port: int = None,
        version: str = None,
        weight: int = None,
    ):
        self.address = address
        self.ip = ip
        self.is_designated = is_designated
        self.label = label
        self.online = online
        self.port = port
        self.version = version
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.is_designated is not None:
            result['IsDesignated'] = self.is_designated

        if self.label is not None:
            result['Label'] = self.label

        if self.online is not None:
            result['Online'] = self.online

        if self.port is not None:
            result['Port'] = self.port

        if self.version is not None:
            result['Version'] = self.version

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('IsDesignated') is not None:
            self.is_designated = m.get('IsDesignated')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

