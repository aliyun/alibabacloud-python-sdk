# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetAdvancedSearchFileResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_search: main_models.GetAdvancedSearchFileResponseBodyResourceSearch = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the resource file.
        self.resource_search = resource_search

    def validate(self):
        if self.resource_search:
            self.resource_search.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_search is not None:
            result['ResourceSearch'] = self.resource_search.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceSearch') is not None:
            temp_model = main_models.GetAdvancedSearchFileResponseBodyResourceSearch()
            self.resource_search = temp_model.from_map(m.get('ResourceSearch'))

        return self

class GetAdvancedSearchFileResponseBodyResourceSearch(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        resource_inventory_generate_time: int = None,
        status: str = None,
    ):
        # The download URL of the resource file.
        self.download_url = download_url
        # The time when the resource file was generated. The value is a timestamp. Unit: milliseconds.
        self.resource_inventory_generate_time = resource_inventory_generate_time
        # The generation status of the resource file. Valid values:
        # 
        # *   CREATING: The resource file is being generated.
        # *   COMPLETE: The resource file is generated.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.resource_inventory_generate_time is not None:
            result['ResourceInventoryGenerateTime'] = self.resource_inventory_generate_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ResourceInventoryGenerateTime') is not None:
            self.resource_inventory_generate_time = m.get('ResourceInventoryGenerateTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

