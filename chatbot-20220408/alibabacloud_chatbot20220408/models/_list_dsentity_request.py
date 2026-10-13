# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDSEntityRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_type: str = None,
        instance_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The business space key. If this parameter is not specified, the default business space is accessed. You can obtain the key value on the business management page of the primary account.
        self.agent_key = agent_key
        # If left empty, all custom entities are returned (default).
        self.entity_type = entity_type
        # The chatbot ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The filter keyword. Uses contains matching. Scope: entity name (future expansion: entity members, synonyms).
        self.keyword = keyword
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

