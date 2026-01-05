# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListCrawlerTypesResponseBody(DaraModel):
    def __init__(
        self,
        crawler_types: List[main_models.CrawlerType] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The list of metadata crawler types.
        self.crawler_types = crawler_types
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.crawler_types:
            for v1 in self.crawler_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CrawlerTypes'] = []
        if self.crawler_types is not None:
            for k1 in self.crawler_types:
                result['CrawlerTypes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.crawler_types = []
        if m.get('CrawlerTypes') is not None:
            for k1 in m.get('CrawlerTypes'):
                temp_model = main_models.CrawlerType()
                self.crawler_types.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

