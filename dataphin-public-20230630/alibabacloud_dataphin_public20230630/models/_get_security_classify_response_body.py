# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetSecurityClassifyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        security_classify_info: main_models.GetSecurityClassifyResponseBodySecurityClassifyInfo = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.security_classify_info = security_classify_info
        self.success = success

    def validate(self):
        if self.security_classify_info:
            self.security_classify_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_classify_info is not None:
            result['SecurityClassifyInfo'] = self.security_classify_info.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityClassifyInfo') is not None:
            temp_model = main_models.GetSecurityClassifyResponseBodySecurityClassifyInfo()
            self.security_classify_info = temp_model.from_map(m.get('SecurityClassifyInfo'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSecurityClassifyResponseBodySecurityClassifyInfo(DaraModel):
    def __init__(
        self,
        abbreviation: str = None,
        id: int = None,
        level_abbreviation: str = None,
        level_index: int = None,
        level_name: str = None,
        name: str = None,
        path: str = None,
    ):
        self.abbreviation = abbreviation
        self.id = id
        self.level_abbreviation = level_abbreviation
        self.level_index = level_index
        self.level_name = level_name
        self.name = name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abbreviation is not None:
            result['Abbreviation'] = self.abbreviation

        if self.id is not None:
            result['Id'] = self.id

        if self.level_abbreviation is not None:
            result['LevelAbbreviation'] = self.level_abbreviation

        if self.level_index is not None:
            result['LevelIndex'] = self.level_index

        if self.level_name is not None:
            result['LevelName'] = self.level_name

        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Abbreviation') is not None:
            self.abbreviation = m.get('Abbreviation')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LevelAbbreviation') is not None:
            self.level_abbreviation = m.get('LevelAbbreviation')

        if m.get('LevelIndex') is not None:
            self.level_index = m.get('LevelIndex')

        if m.get('LevelName') is not None:
            self.level_name = m.get('LevelName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

