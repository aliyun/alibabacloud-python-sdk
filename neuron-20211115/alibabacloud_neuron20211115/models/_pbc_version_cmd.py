# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PbcVersionCmd(DaraModel):
    def __init__(
        self,
        api_schema: str = None,
        company_id: int = None,
        developer_id: int = None,
        document: str = None,
        market_id: int = None,
        name: str = None,
        schema: str = None,
        version: str = None,
    ):
        self.api_schema = api_schema
        self.company_id = company_id
        self.developer_id = developer_id
        self.document = document
        self.market_id = market_id
        self.name = name
        self.schema = schema
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_schema is not None:
            result['apiSchema'] = self.api_schema

        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.developer_id is not None:
            result['developerId'] = self.developer_id

        if self.document is not None:
            result['document'] = self.document

        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.name is not None:
            result['name'] = self.name

        if self.schema is not None:
            result['schema'] = self.schema

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiSchema') is not None:
            self.api_schema = m.get('apiSchema')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('developerId') is not None:
            self.developer_id = m.get('developerId')

        if m.get('document') is not None:
            self.document = m.get('document')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('schema') is not None:
            self.schema = m.get('schema')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

