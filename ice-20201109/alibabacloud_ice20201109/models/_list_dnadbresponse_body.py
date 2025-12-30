# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListDNADBResponseBody(DaraModel):
    def __init__(
        self,
        dblist: List[main_models.ListDNADBResponseBodyDBList] = None,
        request_id: str = None,
    ):
        # The queried media fingerprint libraries.
        self.dblist = dblist
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dblist:
            for v1 in self.dblist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBList'] = []
        if self.dblist is not None:
            for k1 in self.dblist:
                result['DBList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dblist = []
        if m.get('DBList') is not None:
            for k1 in m.get('DBList'):
                temp_model = main_models.ListDNADBResponseBodyDBList()
                self.dblist.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDNADBResponseBodyDBList(DaraModel):
    def __init__(
        self,
        dbid: str = None,
        description: str = None,
        model: str = None,
        name: str = None,
        status: str = None,
    ):
        # The ID of the media fingerprint library.
        self.dbid = dbid
        # The description of the media fingerprint library.
        self.description = description
        # The model of the media fingerprint library. Valid values:
        # 
        # *   **Video**
        # *   **Audio**
        # *   **Image**
        # *   **Text** (supported only in the China (Shanghai) region)
        self.model = model
        # The name of the media fingerprint library.
        self.name = name
        # The state of the media fingerprint library. Default value: **offline**. ****Valid values:
        # 
        # *   **offline**: The media fingerprint library is offline.
        # *   **active**: The media fingerprint library is online.
        # *   **deleted**: The media fingerprint library is deleted.
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

