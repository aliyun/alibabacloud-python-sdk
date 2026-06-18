# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListKeylessServersResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        result: List[main_models.ListKeylessServersResponseBodyResult] = None,
        site_id: int = None,
        site_name: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # A list of keyless server configurations.
        self.result = result
        # The site ID.
        self.site_id = site_id
        # The site name.
        self.site_name = site_name
        # The total count.
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListKeylessServersResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListKeylessServersResponseBodyResult(DaraModel):
    def __init__(
        self,
        ca_certificate: str = None,
        client_certificate: str = None,
        client_private_key: str = None,
        create_time: str = None,
        host: str = None,
        id: str = None,
        name: str = None,
        port: int = None,
        update_time: str = None,
        verify: bool = None,
    ):
        # The CA certificate used to verify the server certificate of the keyless server. This parameter applies only when `Verify` is set to `true`.
        self.ca_certificate = ca_certificate
        # The client certificate. This parameter must be provided with `ClientPrivateKey`.
        self.client_certificate = client_certificate
        # The client private key. This parameter must be provided with `ClientCertificate`.
        self.client_private_key = client_private_key
        # The creation time.
        self.create_time = create_time
        # The keyless server host name.
        self.host = host
        # The keyless server ID.
        self.id = id
        # The keyless server name.
        self.name = name
        # The keyless server port. Valid values: 1 to 65535.
        self.port = port
        # The update time.
        self.update_time = update_time
        # Specifies whether to verify the server certificate of the keyless server. Defaults to false.
        self.verify = verify

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_certificate is not None:
            result['CaCertificate'] = self.ca_certificate

        if self.client_certificate is not None:
            result['ClientCertificate'] = self.client_certificate

        if self.client_private_key is not None:
            result['ClientPrivateKey'] = self.client_private_key

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.host is not None:
            result['Host'] = self.host

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.port is not None:
            result['Port'] = self.port

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.verify is not None:
            result['Verify'] = self.verify

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCertificate') is not None:
            self.ca_certificate = m.get('CaCertificate')

        if m.get('ClientCertificate') is not None:
            self.client_certificate = m.get('ClientCertificate')

        if m.get('ClientPrivateKey') is not None:
            self.client_private_key = m.get('ClientPrivateKey')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Verify') is not None:
            self.verify = m.get('Verify')

        return self

