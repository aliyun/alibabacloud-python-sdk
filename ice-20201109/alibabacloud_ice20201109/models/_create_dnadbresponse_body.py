# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class CreateDNADBResponseBody(DaraModel):
    def __init__(
        self,
        dbinfo: main_models.CreateDNADBResponseBodyDBInfo = None,
        request_id: str = None,
    ):
        # The details of the media fingerprint library.
        self.dbinfo = dbinfo
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dbinfo:
            self.dbinfo.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinfo is not None:
            result['DBInfo'] = self.dbinfo.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInfo') is not None:
            temp_model = main_models.CreateDNADBResponseBodyDBInfo()
            self.dbinfo = temp_model.from_map(m.get('DBInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateDNADBResponseBodyDBInfo(DaraModel):
    def __init__(
        self,
        dbid: str = None,
        description: str = None,
        model: str = None,
        name: str = None,
        status: str = None,
    ):
        # The ID of the media fingerprint library. We recommend that you save this ID for subsequent calls of other operations.
        self.dbid = dbid
        # The description of the media fingerprint library.
        self.description = description
        # The model of the media fingerprint library.
        self.model = model
        # The name of the media fingerprint library.
        self.name = name
        # The state of the media fingerprint library. After a media fingerprint library is created, it enters the offline state. After the media fingerprint library is processed at the backend, it enters the active state.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbid is not None:
            result['DBId'] = self.dbid

        if self.description is not None:
            result['Description'] = self.description

        if self.model is not None:
            result['Model'] = self.model

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBId') is not None:
            self.dbid = m.get('DBId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

