# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetSecurityLevelResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        security_level_info: main_models.GetSecurityLevelResponseBodySecurityLevelInfo = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.security_level_info = security_level_info
        self.success = success

    def validate(self):
        if self.security_level_info:
            self.security_level_info.validate()

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

        if self.security_level_info is not None:
            result['SecurityLevelInfo'] = self.security_level_info.to_map()

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

        if m.get('SecurityLevelInfo') is not None:
            temp_model = main_models.GetSecurityLevelResponseBodySecurityLevelInfo()
            self.security_level_info = temp_model.from_map(m.get('SecurityLevelInfo'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSecurityLevelResponseBodySecurityLevelInfo(DaraModel):
    def __init__(
        self,
        abbreviation: str = None,
        description: str = None,
        index: int = None,
        name: str = None,
        related_classify_id_list: List[int] = None,
    ):
        self.abbreviation = abbreviation
        self.description = description
        self.index = index
        self.name = name
        self.related_classify_id_list = related_classify_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abbreviation is not None:
            result['Abbreviation'] = self.abbreviation

        if self.description is not None:
            result['Description'] = self.description

        if self.index is not None:
            result['Index'] = self.index

        if self.name is not None:
            result['Name'] = self.name

        if self.related_classify_id_list is not None:
            result['RelatedClassifyIdList'] = self.related_classify_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Abbreviation') is not None:
            self.abbreviation = m.get('Abbreviation')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RelatedClassifyIdList') is not None:
            self.related_classify_id_list = m.get('RelatedClassifyIdList')

        return self

