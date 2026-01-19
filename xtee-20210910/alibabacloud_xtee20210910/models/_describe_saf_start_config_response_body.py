# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeSafStartConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeSafStartConfigResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returned object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeSafStartConfigResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeSafStartConfigResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        device_types: List[str] = None,
        event_codes: List[str] = None,
        languages: List[str] = None,
        server_regions: List[str] = None,
    ):
        # List of device types.
        self.device_types = device_types
        # Event codes.
        self.event_codes = event_codes
        # Configuration language details.
        self.languages = languages
        # Server region
        self.server_regions = server_regions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_types is not None:
            result['deviceTypes'] = self.device_types

        if self.event_codes is not None:
            result['eventCodes'] = self.event_codes

        if self.languages is not None:
            result['languages'] = self.languages

        if self.server_regions is not None:
            result['serverRegions'] = self.server_regions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceTypes') is not None:
            self.device_types = m.get('deviceTypes')

        if m.get('eventCodes') is not None:
            self.event_codes = m.get('eventCodes')

        if m.get('languages') is not None:
            self.languages = m.get('languages')

        if m.get('serverRegions') is not None:
            self.server_regions = m.get('serverRegions')

        return self

