# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetSiteCustomLogResponseBody(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        is_exist: bool = None,
        log_custom_field: main_models.GetSiteCustomLogResponseBodyLogCustomField = None,
        request_id: str = None,
        site_id: int = None,
    ):
        # The ID of the custom log field configuration.
        self.config_id = config_id
        # Indicates whether the custom configuration exists.
        self.is_exist = is_exist
        # The custom fields.
        self.log_custom_field = log_custom_field
        # The request ID.
        self.request_id = request_id
        # The website ID.
        self.site_id = site_id

    def validate(self):
        if self.log_custom_field:
            self.log_custom_field.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.is_exist is not None:
            result['IsExist'] = self.is_exist

        if self.log_custom_field is not None:
            result['LogCustomField'] = self.log_custom_field.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('IsExist') is not None:
            self.is_exist = m.get('IsExist')

        if m.get('LogCustomField') is not None:
            temp_model = main_models.GetSiteCustomLogResponseBodyLogCustomField()
            self.log_custom_field = temp_model.from_map(m.get('LogCustomField'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

class GetSiteCustomLogResponseBodyLogCustomField(DaraModel):
    def __init__(
        self,
        cookies: List[str] = None,
        request_headers: List[str] = None,
        response_headers: List[str] = None,
    ):
        # The cookie fields.
        self.cookies = cookies
        # The request header fields.
        self.request_headers = request_headers
        # The response header fields.
        self.response_headers = response_headers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cookies is not None:
            result['Cookies'] = self.cookies

        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers

        if self.response_headers is not None:
            result['ResponseHeaders'] = self.response_headers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')

        if m.get('RequestHeaders') is not None:
            self.request_headers = m.get('RequestHeaders')

        if m.get('ResponseHeaders') is not None:
            self.response_headers = m.get('ResponseHeaders')

        return self

