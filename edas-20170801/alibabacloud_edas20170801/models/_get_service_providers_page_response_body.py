# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetServiceProvidersPageResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetServiceProvidersPageResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The data structure.
        self.data = data
        # The message returned for the request.
        self.message = message
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetServiceProvidersPageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetServiceProvidersPageResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.GetServiceProvidersPageResponseBodyDataContent] = None,
        size: int = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        # The data array returned.
        self.content = content
        # The number of entries returned per page.
        self.size = size
        # The total number of returned entries.
        self.total_elements = total_elements
        # The total number of returned pages.
        self.total_pages = total_pages

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.size is not None:
            result['Size'] = self.size

        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.GetServiceProvidersPageResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class GetServiceProvidersPageResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        iannotations: str = None,
        ip: str = None,
        port: str = None,
        serialize_type: str = None,
        timeout: str = None,
    ):
        # The remarks of the service provider.
        self.iannotations = iannotations
        # The IP address of the service provider.
        self.ip = ip
        # The port number of the service provider.
        self.port = port
        # The serialization type.
        self.serialize_type = serialize_type
        # The service timeout period.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iannotations is not None:
            result['Iannotations'] = self.iannotations

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.port is not None:
            result['Port'] = self.port

        if self.serialize_type is not None:
            result['SerializeType'] = self.serialize_type

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iannotations') is not None:
            self.iannotations = m.get('Iannotations')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('SerializeType') is not None:
            self.serialize_type = m.get('SerializeType')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

