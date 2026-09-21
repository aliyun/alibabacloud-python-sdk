# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class TraceSiteRequest(DaraModel):
    def __init__(
        self,
        body: main_models.TraceSiteRequestBody = None,
        context: main_models.TraceSiteRequestContext = None,
        cookies: List[main_models.TraceSiteRequestCookies] = None,
        headers: List[main_models.TraceSiteRequestHeaders] = None,
        method: str = None,
        protocol: str = None,
        url: str = None,
    ):
        # The HTTP request body.
        self.body = body
        # The environment context. This parameter is optional.
        self.context = context
        # The cookie parameters.
        self.cookies = cookies
        # The request headers.
        self.headers = headers
        # The HTTP method.
        self.method = method
        # The HTTP protocol.
        self.protocol = protocol
        # The URL of the request.
        # 
        # This parameter is required.
        self.url = url

    def validate(self):
        if self.body:
            self.body.validate()
        if self.context:
            self.context.validate()
        if self.cookies:
            for v1 in self.cookies:
                 if v1:
                    v1.validate()
        if self.headers:
            for v1 in self.headers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body.to_map()

        if self.context is not None:
            result['Context'] = self.context.to_map()

        result['Cookies'] = []
        if self.cookies is not None:
            for k1 in self.cookies:
                result['Cookies'].append(k1.to_map() if k1 else None)

        result['Headers'] = []
        if self.headers is not None:
            for k1 in self.headers:
                result['Headers'].append(k1.to_map() if k1 else None)

        if self.method is not None:
            result['Method'] = self.method

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.TraceSiteRequestBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('Context') is not None:
            temp_model = main_models.TraceSiteRequestContext()
            self.context = temp_model.from_map(m.get('Context'))

        self.cookies = []
        if m.get('Cookies') is not None:
            for k1 in m.get('Cookies'):
                temp_model = main_models.TraceSiteRequestCookies()
                self.cookies.append(temp_model.from_map(k1))

        self.headers = []
        if m.get('Headers') is not None:
            for k1 in m.get('Headers'):
                temp_model = main_models.TraceSiteRequestHeaders()
                self.headers.append(temp_model.from_map(k1))

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class TraceSiteRequestHeaders(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The HTTP request header name.
        self.name = name
        # The HTTP request header value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class TraceSiteRequestCookies(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The cookie name.
        self.name = name
        # The cookie value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class TraceSiteRequestContext(DaraModel):
    def __init__(
        self,
        geo_location: main_models.TraceSiteRequestContextGeoLocation = None,
        skip_challenge: bool = None,
    ):
        # The simulated geolocation information.
        self.geo_location = geo_location
        # Specifies whether to skip the security challenge test.
        self.skip_challenge = skip_challenge

    def validate(self):
        if self.geo_location:
            self.geo_location.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.geo_location is not None:
            result['GeoLocation'] = self.geo_location.to_map()

        if self.skip_challenge is not None:
            result['SkipChallenge'] = self.skip_challenge

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GeoLocation') is not None:
            temp_model = main_models.TraceSiteRequestContextGeoLocation()
            self.geo_location = temp_model.from_map(m.get('GeoLocation'))

        if m.get('SkipChallenge') is not None:
            self.skip_challenge = m.get('SkipChallenge')

        return self

class TraceSiteRequestContextGeoLocation(DaraModel):
    def __init__(
        self,
        country_code: str = None,
        isp_code: str = None,
        region_code: str = None,
    ):
        # The country/region code.
        self.country_code = country_code
        # The Internet service provider (ISP) code. This parameter is valid only when the country or region is the Chinese mainland.
        self.isp_code = isp_code
        # The region or province code. This parameter is valid only when the country or region is the Chinese mainland.
        self.region_code = region_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.country_code is not None:
            result['CountryCode'] = self.country_code

        if self.isp_code is not None:
            result['IspCode'] = self.isp_code

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')

        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        return self

class TraceSiteRequestBody(DaraModel):
    def __init__(
        self,
        json: Any = None,
        plain_text: str = None,
    ):
        # The content in JSON format. If both JSON format content and plain text content are specified, the JSON format content takes precedence.
        self.json = json
        # The plain text content.
        self.plain_text = plain_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.json is not None:
            result['Json'] = self.json

        if self.plain_text is not None:
            result['PlainText'] = self.plain_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Json') is not None:
            self.json = m.get('Json')

        if m.get('PlainText') is not None:
            self.plain_text = m.get('PlainText')

        return self

