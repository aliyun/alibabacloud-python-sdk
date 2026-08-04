# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ListUserMessageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        result: List[main_models.ListUserMessageResponseBodyResult] = None,
    ):
        # Status code returned by the service. SUCCESS indicates success; otherwise, it indicates failure.
        self.code = code
        # error message
        self.message = message
        # List of user message query results
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListUserMessageResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListUserMessageResponseBodyResult(DaraModel):
    def __init__(
        self,
        content: str = None,
        device_name: str = None,
        gmt_create: str = None,
        id: str = None,
        pic: str = None,
        source: str = None,
        source_uuid: str = None,
        status: int = None,
        type: str = None,
        url: str = None,
    ):
        # Message text
        self.content = content
        # Device name
        self.device_name = device_name
        # Time when the message was sent
        self.gmt_create = gmt_create
        # Message ID
        self.id = id
        # Device Image
        self.pic = pic
        # Message source: app or box
        self.source = source
        # Source Device ID
        self.source_uuid = source_uuid
        # Message status: 0 indicates unread, and 1 indicates read.
        self.status = status
        # Currently only audio is supported.
        self.type = type
        # Audio message link
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.id is not None:
            result['Id'] = self.id

        if self.pic is not None:
            result['Pic'] = self.pic

        if self.source is not None:
            result['Source'] = self.source

        if self.source_uuid is not None:
            result['SourceUuid'] = self.source_uuid

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Pic') is not None:
            self.pic = m.get('Pic')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceUuid') is not None:
            self.source_uuid = m.get('SourceUuid')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

