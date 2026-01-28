# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class GetIntlFixPriceDomainListUrlResponseBody(DaraModel):
    def __init__(
        self,
        module: main_models.GetIntlFixPriceDomainListUrlResponseBodyModule = None,
        request_id: str = None,
    ):
        # The returned data.
        self.module = module
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            temp_model = main_models.GetIntlFixPriceDomainListUrlResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetIntlFixPriceDomainListUrlResponseBodyModule(DaraModel):
    def __init__(
        self,
        download_url: str = None,
    ):
        # The URL for downloading the list that contains available fixed-price domain names at the international site (alibabacloud.com).
        self.download_url = download_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        return self

