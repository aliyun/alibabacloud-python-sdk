# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetObjectScanEventResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetObjectScanEventResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetObjectScanEventResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetObjectScanEventResponseBodyData(DaraModel):
    def __init__(
        self,
        details: List[main_models.GetObjectScanEventResponseBodyDataDetails] = None,
        event_name: str = None,
        file_name: str = None,
        md_5: str = None,
    ):
        # The details of the alert event.
        self.details = details
        # The name of the alert item.
        self.event_name = event_name
        # The name of the object.
        self.file_name = file_name
        # The MD5 hash value of the object.
        self.md_5 = md_5

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.GetObjectScanEventResponseBodyDataDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        return self

class GetObjectScanEventResponseBodyDataDetails(DaraModel):
    def __init__(
        self,
        info_type: str = None,
        name: str = None,
        name_display: str = None,
        type: str = None,
        value: str = None,
        value_display: str = None,
    ):
        # The type of the item.
        self.info_type = info_type
        # The name of the item.
        self.name = name
        # The display name of the item.
        self.name_display = name_display
        # The type of the item.
        self.type = type
        # The value of the item.
        self.value = value
        # The display value of the item.
        self.value_display = value_display

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info_type is not None:
            result['InfoType'] = self.info_type

        if self.name is not None:
            result['Name'] = self.name

        if self.name_display is not None:
            result['NameDisplay'] = self.name_display

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        if self.value_display is not None:
            result['ValueDisplay'] = self.value_display

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InfoType') is not None:
            self.info_type = m.get('InfoType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameDisplay') is not None:
            self.name_display = m.get('NameDisplay')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueDisplay') is not None:
            self.value_display = m.get('ValueDisplay')

        return self

