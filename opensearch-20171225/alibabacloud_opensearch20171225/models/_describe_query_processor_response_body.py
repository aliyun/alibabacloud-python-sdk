# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class DescribeQueryProcessorResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DescribeQueryProcessorResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the query analysis rule.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.DescribeQueryProcessorResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class DescribeQueryProcessorResponseBodyResult(DaraModel):
    def __init__(
        self,
        active: bool = None,
        created: int = None,
        domain: str = None,
        indexes: List[str] = None,
        name: str = None,
        processors: List[Dict[str, Any]] = None,
        updated: int = None,
    ):
        # Indicates whether the query analysis rule is the default one.
        self.active = active
        # The time when the query analysis rule was created.
        self.created = created
        # The type of the industry. Valid values:
        # 
        # *   GENERAL
        # *   ECOMMERCE
        # *   IT_CONTENT
        self.domain = domain
        # The indexes to which the query analysis rule applies.
        self.indexes = indexes
        # The name of the query analysis rule.
        self.name = name
        # The features that are used in the query analysis rule.
        self.processors = processors
        # The time when the query analysis rule was last updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['active'] = self.active

        if self.created is not None:
            result['created'] = self.created

        if self.domain is not None:
            result['domain'] = self.domain

        if self.indexes is not None:
            result['indexes'] = self.indexes

        if self.name is not None:
            result['name'] = self.name

        if self.processors is not None:
            result['processors'] = self.processors

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('indexes') is not None:
            self.indexes = m.get('indexes')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('processors') is not None:
            self.processors = m.get('processors')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

